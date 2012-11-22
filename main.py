import sys
sys.path.append("/usr/lib/gobject-introspection")
from giscanner.girparser import GIRParser
from giscanner import ast
from generator import Generator
from collections import namedtuple
import os

Param = namedtuple('Param', ['name', 'c_type', 'go_type'])

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

    self.functions = []
    self.enum_symbols = []
    self.const_symbols = []
    self.typedefs = {}

  def parse(self):
    for node in self.namespace.itervalues():
      if isinstance(node, ast.Function):
        info = self.handleFunction(node)
        self.functions.append(info)
      elif isinstance(node, ast.Enum):
        self.handleEnum(node)
      elif isinstance(node, ast.Constant):
        self.handleConstant(node)
      elif isinstance(node, ast.Record):
        #self.handleRecord(node)
        pass
      elif isinstance(node, ast.Callback):
        pass
      elif isinstance(node, ast.Union):
        pass
      elif isinstance(node, ast.Alias):
        pass
      elif isinstance(node, ast.Bitfield):
        pass
      elif isinstance(node, ast.Class):
        pass
      elif isinstance(node, ast.Interface):
        pass
      else:
        print 'not handle:', type(node)

  def handleFunction(self, node):
    info = Dict()
    info.has_varargs = has_varargs = False
    info.has_va_list = has_va_list = False
    info.has_long_double = has_long_double = False
    info.name = name = node.name
    info.c_name = c_name = node.symbol
    info.deprecated = False
    if not node.deprecated is None:
      info.deprecated = True
      return info
    info.skip = False
    if c_name in self.skip_symbols:
      info.skip = True
      return info
    info.go_name = go_name = convertFuncName(name)
    info.parameters = parameters = []
    for i, param in enumerate(node.parameters):
      arg_name = param.argname
      if arg_name == 'type':
        arg_name = '_type'
      elif arg_name == 'func':
        arg_name = '_func'
      elif arg_name == 'len':
        arg_name = '_len'

      arg_c_type = param.type.ctype
      if arg_c_type == '<varargs>':
        has_varargs = True
      elif arg_c_type == 'va_list':
        has_va_list = True
      elif 'long double' in arg_c_type:
        has_long_double = True
      else:
        if arg_name is None:
          arg_name = 'arg_%d' % i
        arg_go_type = self.convert_to_go_type(param.type.ctype)
        parameters.append(Param(arg_name, arg_c_type, arg_go_type))
    if node.throws:
      parameters.append(Param('err', '_pp_GError', 'C._pp_GError'))
      self.typedefs['GError**'] = '_pp_GError'
    info.has_varargs = has_varargs
    info.has_va_list = has_va_list
    info.has_long_double = has_long_double

    no_return = False
    return_c_type = node.retval.type.ctype
    return_go_type = None
    if return_c_type == 'void':
      no_return = True
    else:
      return_go_type = self.convert_to_go_type(return_c_type)
    info.no_return = no_return
    info.return_c_type = return_c_type
    info.return_go_type = return_go_type

    return info

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
    name = node.name
    c_type = node.ctype
    print name, c_type
    get_type_func = node.get_type
    for constructor in node.constructors:
      c_function_name = constructor.symbol
      name = constructor.name
      ret_type = constructor.retval.type #TODO convert to c type
      print '\t', ret_type
      for param in constructor.parameters:
        arg_name = param.argname
        arg_type = param.type #TODO convert to c type
        print arg_type
    for function in node.static_methods:
      print '\t', function #TODO
      pass
    for method in node.methods:
      print '\t', method #TODO
      pass
    for field in node.fields:
      field_name = field.name
      print 'field name', field_name
      field_is_private = field.private
      print 'private', field_is_private
      field_is_readable = field.readable
      print 'readable', field_is_readable
      field_is_writable = field.writable
      print 'writable', field_is_writable
      field_is_anonymous = field.anonymous_node
      print 'callback', field_is_anonymous
      if not field_is_anonymous:
        field_c_type = field.type.ctype
        print 'type', field_c_type

  def convert_to_go_type(self, t):
    if t == 'long double':
      return 'longdouble'
    t = t.replace('volatile ', '') 
    orig_t = t
    need_typedef = False
    pre = ''
    if t.startswith('const '):
      need_typedef = True
      pre += '_const'
      t = t.replace('const ', '')
    if t.endswith('*'):
      need_typedef = True
      pre += '_'
      while t.endswith('*'):
        pre += 'p'
        t = t[:-1]
    if need_typedef:
      t = pre + '_' + t
      self.typedefs[orig_t] = t
    t = 'C.' + t
    return t

def convertFuncName(s):
  words = s.split('_')
  words = [w.capitalize() for w in words]
  return ''.join(words)

class Dict(dict):
  __getattr__ = dict.__getitem__
  __setattr__ = dict.__setattr__

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
