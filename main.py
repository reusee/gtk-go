import sys
sys.path.append("/usr/lib/gobject-introspection")
from giscanner.girparser import GIRParser
from giscanner import ast
from generator import Generator
from collections import namedtuple
import os

Param = namedtuple('Param', ['name', 'c_type', 'go_type', 'need_cast'])

class Parser:
  def __init__(self, filename):
    parser = GIRParser(False)
    parser.parse(filename)

    self.namespace = parser.get_namespace()
    self.package_name = self.namespace.name.lower()
    self.pkgconfig_packages = list(parser.get_pkgconfig_packages())
    self.includes = list(parser.get_c_includes())
    deprecated_functions_file = '%s_deprecated_functions' % self.package_name
    self.deprecated_functions = []
    if os.path.exists(deprecated_functions_file):
      self.deprecated_functions = [l.strip() for l in open(deprecated_functions_file, 'r').xreadlines()]
    skip_functions_file = '%s_skip_functions' % self.package_name
    self.skip_functions = []
    if os.path.exists(skip_functions_file):
      self.skip_functions = [l.strip() for l in open(skip_functions_file, 'r').xreadlines()]

    self.functions = []
    self.functions_need_wrapper = []
    self.enum_symbols = []

  def parse(self):
    for node in self.namespace.itervalues():
      if isinstance(node, ast.Function):
        info = self.handleFunction(node)
        self.functions.append(info)
        if info.need_wrapper:
          self.functions_need_wrapper.append(info)
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
    info.need_wrapper = need_wrapper = False
    info.has_varargs = has_varargs = False
    info.has_va_list = has_va_list = False
    info.has_long_double = has_long_double = False
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
        arg_go_type, need_cast = convert_to_go_type(param.type.ctype)
        if need_cast:
          need_wrapper = True
        parameters.append(Param(arg_name, arg_c_type, arg_go_type, need_cast))
    if node.throws:
      parameters.append(Param('err', 'GError**', 'unsafe.Pointer', True))
      need_wrapper = True
    info.has_varargs = has_varargs
    info.has_va_list = has_va_list
    info.has_long_double = has_long_double
    info.need_wrapper = need_wrapper and not has_varargs and not has_va_list and not has_long_double

    no_return = False
    return_c_type = node.retval.type.ctype
    return_go_type = None
    if return_c_type == 'void':
      no_return = True
    else:
      return_go_type, _ = convert_to_go_type(return_c_type)
    info.no_return = no_return
    info.return_c_type = return_c_type
    info.return_go_type = return_go_type

    return info

  def handleEnum(self, node):
    c_enum_name = node.ctype
    for mem in node.members:
      member_value = mem.value
      member_symbol = mem.symbol
      self.enum_symbols.append(member_symbol)

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

def convert_to_go_type(s):
  s = s.replace('volatile ', '') 
  need_cast = False
  if s.startswith('const '):
    need_cast = True
    s = s.replace('const ', '')
  if s == 'long double':
    s = 'longdouble'
  if s.endswith('**'):
    need_cast = True
    s = 'unsafe.Pointer'
  else:
    s = 'C.' + s
  if s.endswith('*'):
    s = '*' + s[:-1]
  return s, need_cast

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
