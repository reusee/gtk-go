#!/usr/bin/env python2

import sys
sys.path.append("/usr/lib/gobject-introspection")
from giscanner.girparser import GIRParser
from giscanner import ast
from generator import Generator
import os
from common import *
from convert import *

class Parser:
  def __init__(self, filename):
    parser = GIRParser(False)
    parser.parse(filename)

    self.skip_symbols = set()
    skip_symbol_file = os.path.join(os.path.dirname(os.path.abspath(filename)), 'skip_symbols')
    if os.path.exists(skip_symbol_file):
      self.skip_symbols = set([line.strip() 
        for line in open(skip_symbol_file, 'r').xreadlines()
        if not line.startswith('//')
        ])
      self.skip_symbols = set([l for l in self.skip_symbols if l])

    self.namespace = parser.get_namespace()
    self.package_name = self.namespace.name.lower()
    self.pkgconfig_packages = list(parser.get_pkgconfig_packages())
    self.includes = list(parser.get_c_includes())
    self.prefixes = self.namespace.symbol_prefixes

    self.functions = []
    self.functions_need_helper = []
    self.enum_symbols = []
    self.const_symbols = []
    self.construct_records = set()
    self.type_mappings = Dict()

    self.exported_functions = set()

    self._cur_nodeA = None
    self._cur_nodeB = None
    self._cur_nodeC = None
    self._kinds = set()
    self._kind_example = {}

  def parse(self):
    for node in self.namespace.itervalues():
      handlerName = 'handle' + type(node).__name__
      if hasattr(self, handlerName):
        getattr(self, handlerName)(node)
      #else:
      #  print type(node).__name__, 'not handle'
      #  stop

    #print (' %d kinds ' % len(self._kinds)).center(50, '=')
    #for kind in self._kinds:
    #  print kind
    #  print '\n'.join(str(x) for x in self._kind_example[kind][:10])
    #  print

  def handleFunction(self, node, cls = '', is_method = False, c_class = ''):
    self._cur_nodeA = node
    info = Dict()
    info.name = node.name
    info.c_name = node.symbol
    info.is_method = is_method
    info.c_class = c_class
    if info.c_name in self.exported_functions:
      return
    self.exported_functions.add(info.c_name)

    info.skip = False
    if not node.deprecated is None or info.c_name in self.skip_symbols:
      info.skip = True

    if is_method:
      if info.name == "":
        info.go_name = 'New' + cls
      else:
        info.go_name = self.convert_func_name(info.name)
    else:
      info.go_name = cls + self.convert_func_name(info.name)
    info.cls = cls
    info.parameters, info.not_implement, info.need_helper = self.convert_parameters(node.parameters)
    info.need_helper = info.need_helper and not info.skip

    if is_method:
      info.parameters.insert(0, Dict({
        'name': 'self',
        'transfer': False,
        'type': Dict({
          'need_helper': False,
          'go_type': '*%s' % cls,
          'c_type': '%s*' % c_class,
          'c_param_type': '%s*' % c_class,
          'c_original_type': '%s*' % c_class,
        }),
      }))

    if node.throws:
      info.parameters.append(Dict({
        'name': 'err',
        'transfer': False,
        'type': Dict({
          'need_helper': False,
          'go_type': 'unsafe.Pointer',
          'c_param_type': 'void*',
          'c_type': 'GError**',
          'c_original_type': 'GError**',
        }),
      }))
      info.need_helper = True

    info.return_type = self.get_type_info(node.retval)
    info.no_return = False
    if info.return_type.c_type == 'void':
      info.no_return = True

    self.functions.append(info)
    if info.need_helper and not info.not_implement:
      self.functions_need_helper.append(info)

  def handleEnum(self, node):
    for mem in node.members:
      if mem.symbol in self.skip_symbols:
        continue
      self.enum_symbols.append(mem.symbol)

  def handleConstant(self, node):
    #self.const_symbols.append((node.ctype, node.value, node.value_type.resolved))
    if node.ctype in self.skip_symbols:
      return
    self.const_symbols.append(node.ctype)

  def handleRecord(self, node):
    # name
    name = node.name
    c_type = node.ctype
    if c_type in self.skip_symbols:
      return
    self.construct_records.add((name, c_type))
    self.map_record_type(name, c_type)
    # constructors
    for constructor in node.constructors:
      self._cur_nodeA = constructor
      self.handleFunction(constructor, name)
    # static methods
    for function in node.static_methods:
      self._cur_nodeA = function
      self.handleFunction(function, name)
    # methods
    for method in node.methods:
      self._cur_nodeA = method
      self.handleFunction(method, name, True, c_type)

  def map_record_type(self, name, c_type):
    self.type_mappings['*C.' + c_type] = Dict({
      'mapped_type': '*' + name,
      'mapped_name_func': lambda param: '_cp_%s_' % param.name,
      'mapping_code_func': lambda param: '\t_cp_%s_ := (*C.%s)(%s)\n' % (
        param.name, c_type, param.name),
      'return_code_func': lambda exp: '''\
\t_c_return_ := %s
\t_go_return_ := (*%s)(_c_return_)
\truntime.SetFinalizer(&_go_return_, func (x **%s) {
\t\tC.g_object_unref(C.gpointer(_c_return_))
\t})
\treturn _go_return_
''' % (exp, name, name,),
    })

  def convert_func_name(self, s):
    words = s.split('_')
    words = [w.capitalize() for w in words]
    return ''.join(words)

  def convert_parameters(self, parameters):
    not_implement = False
    need_helper = False
    params = []
    for i, param in enumerate(parameters):
      name = param.argname
      param_info = Dict({
        'transfer': param.transfer != 'none',
        'type': self.get_type_info(param),
        'direction': param.direction,
      })
      not_implement = param_info.type.not_implement or not_implement
      if is_go_word(name):
        name += '_'
      if name is None:
        name = 'arg_%d' % i
      if param_info.type.need_helper:
        need_helper = True
      param_info.name = name
      params.append(param_info)

    return params, not_implement, need_helper

  def get_type_info(self, param):
    t = param.type
    # go_type and c_param_type are the same, or strictlly compatible
    c_original_type = c_type = c_param_type = go_type = t.ctype
    not_implement = False
    need_helper = False

    if isinstance(t, ast.Array) and isinstance(param, ast.Parameter):
      not_implement = True
      #self.collect_array_type_info(param)
    if c_type in [
        '<varargs>',
        'va_list',
        ]:
      not_implement = True

    c_type = c_type.replace('volatile ', '')
    if c_type.startswith('const '):
      need_helper = True
      c_type = c_type.replace('const ', '')
    c_param_type = c_type
    go_type = c_type
    if c_type.endswith('**'):
      need_helper = True
      go_type = 'unsafe.Pointer'
      c_param_type = 'void*'
    if go_type == 'long double': #BUG will lose precision
      need_helper = True
      go_type = 'double'
      c_param_type = 'double'

    if go_type != 'unsafe.Pointer':
      go_type = 'C.' + go_type
    if go_type.endswith('*'):
      go_type = '*' + go_type[:-1]

    return Dict({
      'need_helper': need_helper,
      'not_implement': not_implement,
      'c_type': c_type,
      'go_type': go_type,
      'c_param_type': c_param_type,
      'c_original_type': c_original_type,
    })

  def collect_array_type_info(self, param):
    print (' %s ' % self._cur_nodeA.symbol).center(50, '-')
    ary = param.type
    elem = param.type.element_type
    print 'name:', param.argname
    print 'caller_allocates:', param.caller_allocates
    print 'direction:', param.direction
    print 'transfer:', param.transfer
    print 
    print 'array type:', ary.array_type
    print 'array ctype:', ary.ctype
    print 'array zeroterm:', ary.zeroterminated
    print 'array length param:', ary.length_param_name
    print
    print 'elem resolved:', elem.resolved
    print 'elem ctype:', elem.ctype

    kind = (
      param.caller_allocates,
      param.direction,
      param.transfer,
      ary.array_type,
      ary.ctype,
      ary.zeroterminated,
      ary.length_param_name != None,
      elem.resolved,
      elem.ctype,
      )
    self._kinds.add(kind)
    self._kind_example.setdefault(kind, [])
    self._kind_example[kind].append((self._cur_nodeA.symbol, param.argname))

def main():
  if len(sys.argv) < 2:
    print "usage: %s <gir file>" % sys.argv[0]
    sys.exit()
  parser = Parser(sys.argv[1])
  parser.parse()
  generator = Generator(parser)
  generator.generate()
  generator.write("%s/%s.go" % (parser.package_name, parser.package_name))

if __name__ == '__main__':
  main()
