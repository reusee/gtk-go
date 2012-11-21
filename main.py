import sys
sys.path.append("/usr/lib/gobject-introspection")
from giscanner.girparser import GIRParser
from giscanner import ast
import StringIO

class Generator:
  def __init__(self, filename):
    parser = GIRParser(False)
    parser.parse(filename)

    self.out = StringIO.StringIO()

    print '=> namespace'
    namespace = parser.get_namespace()
    print namespace.name, namespace.version
    self.namespace = namespace
    package_name = namespace.name.lower()
    print >>self.out, "package %s\n" % package_name

    print '=> pkgconfig packages'
    pkgs = []
    for pkg in parser.get_pkgconfig_packages():
      pkgs.append(pkg)
      print pkg
    print >>self.out, "// #cgo pkg-config: %s" % ' '.join(pkgs)

    print '=> includes'
    for include in parser.get_c_includes():
      print include
      print >>self.out, "// #include <%s>" % include

    print >>self.out, 'import "C"\n'

  def write(self, f):
    output_file = open(f, 'w')
    output_file.write(self.out.getvalue())
    output_file.close()

  def start(self):
    print '=> nodes'
    for node in self.namespace.itervalues():
      if isinstance(node, ast.Function):
        self.handleFunction(node)
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
    print '-- Function', node

    c_function_name = node.symbol
    function_name = node.name
    go_func_name = convertFuncName(function_name)
    out = []
    out.append('func %s(' % go_func_name)

    params_str = []
    args = []
    for param in node.parameters:
      arg_name = param.argname
      if arg_name == 'type':
        arg_name = '_type'
      elif arg_name == 'func':
        arg_name = '_func'
      arg_type = param.type.ctype
      if arg_type == '<varargs>': 
        self.out.write("// %s not support\n\n" % c_function_name)
        return 
      elif arg_type.endswith('**'):
        self.out.write("// %s not support\n\n" % c_function_name)
        return 
      elif arg_type == 'va_list':
        self.out.write("// %s not support\n\n" % c_function_name)
        return 
      else:
        arg_type = convertTypeName(param.type.ctype)
        params_str.append('%s %s' % (arg_name, arg_type))
        args.append(arg_name)
    out.append(', '.join(params_str))
    out.append(') ')

    no_return = False
    return_type = node.retval.type.ctype
    if return_type == 'void':
      out.append('{\n')
      no_return = True
    else:
      return_type = convertTypeName(return_type)
      out.append('%s {\n' % return_type)

    if no_return:
      out.append('\tC.%s(%s)\n' % (c_function_name, ', '.join(args)))
    else:
      out.append('\treturn C.%s(%s)\n' % (c_function_name, ', '.join(args)))
    out.append('}\n\n')
    self.out.write(''.join(out))

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
    #print dir(node)
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
  print "type =>", s
  s = s.replace('const ', '') #TODO need wrapper
  s = s.replace('volatile ', '') #TODO need wrapper
  s = 'C.' + s
  while s.endswith('*'):
    s = '*' + s[:-1]
  return s

def main():
  if len(sys.argv) < 2:
    print "usage: %s [gir file]" % sys.argv[0]
    sys.exit()
  generator = Generator(sys.argv[1])
  generator.start()
  generator.write("out.go")

if __name__ == '__main__':
  main()
