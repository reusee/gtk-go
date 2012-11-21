import sys
sys.path.append("/usr/lib/gobject-introspection")
from giscanner.girparser import GIRParser
from giscanner import ast

class Generator:
  def __init__(self, filename):
    parser = GIRParser(False)
    parser.parse(filename)

    print '=> includes'
    for include in parser.get_includes():
      print include

    print '=> namespace'
    namespace = parser.get_namespace()
    print namespace.name, namespace.version
    self.namespace = namespace

    print '=> pkgconfig packages'
    for pkg in parser.get_pkgconfig_packages():
      print pkg

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
      else:
        print type(node)

  def handleFunction(self, node):
    #print '-- Function', node

    c_function_name = node.symbol
    #print 'c function name:', c_function_name

    return_type = node.retval.type
    #print 'return type:', return_type

    for param in node.parameters:
      arg_name = param.argname
      arg_type = param.type
      #print 'parameter:', arg_name, arg_type

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
    print dir(node)
    type_name = node.ctype
    get_type_func = node.get_type
    for constructor in node.constructors:
      c_function_name = constructor.symbol
      name = constructor.name
      ret_type = constructor.retval.type #TODO convert to c type
      print ret_type
      for param in constructor.parameters:
        arg_name = param.argname
        arg_type = param.type #TODO convert to c type
        print arg_type
    for function in node.static_methods:
      print function #TODO
    for method in node.methods:
      print method #TODO

def main():
  if len(sys.argv) < 2:
    print "usage: %s [gir file]" % sys.argv[0]
    sys.exit()
  generator = Generator(sys.argv[1])
  generator.start()

if __name__ == '__main__':
  main()
