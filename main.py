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
    self.functions_need_wrapper = []
    self.enum_symbols = []
    self.const_symbols = []
    self.construct_records = set()
    self.type_mappings = Dict()

    self.exported_functions = set()

  def parse(self):
    for node in self.namespace.itervalues():
      handlerName = 'handle' + type(node).__name__
      if hasattr(self, handlerName):
        getattr(self, handlerName)(node)
      #else:
      #  print type(node).__name__, 'not handle'
      #  stop

  def handleFunction(self, node, cls = ''):
    info = Dict()
    info.name = node.name
    info.c_name = node.symbol
    if info.c_name in self.exported_functions:
      return
    self.exported_functions.add(info.c_name)

    info.skip = False
    if not node.deprecated is None or info.c_name in self.skip_symbols:
      info.skip = True

    info.go_name = cls + convert_func_name(info.name)
    info.cls = cls
    info.parameters, info.not_implement, info.need_wrapper = convert_parameters(node.parameters)
    info.need_wrapper = info.need_wrapper and not info.not_implement

    if node.throws:
      info.parameters.append(Param('err', 'GError**', 'unsafe.Pointer', True, False))
      info.need_wrapper = True

    info.no_return = False
    info.return_c_type = node.retval.type.ctype
    info.return_go_type = None
    if info.return_c_type == 'void':
      info.no_return = True
    else:
      info.return_go_type, _ = convert_to_go_type(info.return_c_type)

    self.functions.append(info)
    if info.need_wrapper:
      self.functions_need_wrapper.append(info)

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
    self.construct_records.add((name, c_type))
    self.map_record_type(name, c_type)
    # constructors
    for constructor in node.constructors:
      self.handleFunction(constructor, name)
    # static methods
    for function in node.static_methods:
      self.handleFunction(function, name)
    # methods
    for method in node.methods:
      #self.handleFunction(method, name)
      pass #TODO

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

def main():
  if len(sys.argv) < 2:
    print "usage: %s [gir file]" % sys.argv[0]
    sys.exit()
  parser = Parser(sys.argv[1])
  parser.parse()
  generator = Generator(parser)
  generator.generate()
  generator.write("example-%s/%s.go" % (parser.package_name, parser.package_name))

if __name__ == '__main__':
  main()
