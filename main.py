import sys
sys.path.append("/usr/lib/gobject-introspection")
from giscanner.girparser import GIRParser
from giscanner import ast
from generator import Generator
from collections import namedtuple

Param = namedtuple('Param', ['name', 'type', 'is_const'])

class Parser:
  def __init__(self, filename):
    parser = GIRParser(False)
    parser.parse(filename)

    self.namespace = parser.get_namespace()
    self.package_name = self.namespace.name.lower()
    self.pkgconfig_packages = list(parser.get_pkgconfig_packages())
    self.includes = list(parser.get_c_includes())
    deprecated_functions_file = '%s_deprecated_functions' % self.package_name
    self.deprecated_functions = [l.strip() for l in open(deprecated_functions_file, 'r').xreadlines()]
    skip_functions_file = '%s_skip_functions' % self.package_name
    self.skip_functions = [l.strip() for l in open(skip_functions_file, 'r').xreadlines()]

    self.functions = {}

  def parse(self):
    for node in self.namespace.itervalues():
      if isinstance(node, ast.Function):
        info = self.handleFunction(node)
        self.functions[info.name] = info
      elif isinstance(node, ast.Enum):
        self.handleEnum(node)
      elif isinstance(node, ast.Constant):
        self.handleConstant(node)
      elif isinstance(node, ast.Record):
        self.handleRecord(node)
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
    info.name = name = node.name
    info.c_name = c_name = node.symbol
    info.deprecated = False
    if not node.deprecated is None or c_name in self.deprecated_functions:
      info.deprecated = True
      return info
    info.skip = False
    if c_name in self.skip_functions:
      info.skip = True
      return info
    info.go_name = go_name = convertFuncName(name)
    info.parameters = parameters = []
    has_varargs = False
    has_pointer_of_pointer = False
    has_va_list = False
    has_long_double = False
    for i, param in enumerate(node.parameters):
      arg_name = param.argname
      if arg_name == 'type':
        arg_name = '_type'
      elif arg_name == 'func':
        arg_name = '_func'
      elif arg_name == 'len':
        arg_name = '_len'

      arg_type = param.type.ctype
      if arg_type == '<varargs>':
        has_varargs = True
      elif arg_type.endswith('**'):
        has_pointer_of_pointer = True
      elif arg_type == 'va_list':
        has_va_list = True
      elif 'long double' in arg_type:
        has_long_double = True
      else:
        if arg_name is None:
          arg_name = 'arg_%d' % i
        arg_type, is_const = convertTypeName(param.type.ctype)
        parameters.append(Param(arg_name, arg_type, is_const))
    info.has_varargs = has_varargs
    info.has_pointer_of_pointer = has_pointer_of_pointer
    info.has_va_list = has_va_list
    info.has_long_double = has_long_double

    no_return = False
    return_type = node.retval.type.ctype
    if return_type == 'void':
      no_return = True
    else:
      return_type, _ = convertTypeName(return_type)
    info.no_return = no_return
    info.return_type = return_type

    return info

  def handleEnum(self, node):
    c_enum_name = node.ctype
    #print c_enum_name
    for mem in node.members:
      member_value = mem.value
      member_symbol = mem.symbol
      #print member_symbol, member_value

  def handleConstant(self, node):
    value = node.value
    name = node.ctype
    c_type = node.value_type
    #print name, c_type, value

  def handleRecord(self, node):
    type_name = node.ctype
    get_type_func = node.get_type
    for constructor in node.constructors:
      c_function_name = constructor.symbol
      name = constructor.name
      ret_type = constructor.retval.type #TODO convert to c type
      #print ret_type
      for param in constructor.parameters:
        arg_name = param.argname
        arg_type = param.type #TODO convert to c type
        #print arg_type
    for function in node.static_methods:
      #print function #TODO
      pass
    for method in node.methods:
      #print method #TODO
      pass

def convertFuncName(s):
  words = s.split('_')
  words = [w.capitalize() for w in words]
  return ''.join(words)

def convertTypeName(s):
  s = s.replace('volatile ', '')
  is_const = False
  if s.startswith('const '):
    is_const = True
    s = s.replace('const ', '')
  if s == 'long double':
    s = 'longdouble'
  s = 'C.' + s
  while s.endswith('*'):
    s = '*' + s[:-1]
  return s, is_const

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
  generator.write("%s.go" % parser.package_name)

if __name__ == '__main__':
  main()
