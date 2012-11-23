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

    self.functions = []
    self.functions_need_wrapper = []
    self.enum_symbols = []
    self.const_symbols = []

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
    info.name = name = node.name
    info.c_name = c_name = node.symbol
    info.need_wrapper = False

    info.skip = False
    if not node.deprecated is None or c_name in self.skip_symbols:
      info.skip = True
      return info

    info.go_name = go_name = convert_func_name(name)
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
    # name
    name = node.name
    c_type = node.ctype
    # constructors
    for constructor in node.constructors:
      c_function_name = constructor.symbol
      function_name = constructor.name
      return_c_type = constructor.retval.type.ctype
      for param in constructor.parameters:
        arg_name = param.argname
        arg_type = param.type.ctype
      #TODO deal with parameter and return types, etc.
    # static methods
    for function in node.static_methods:
      pass #TODO
    # methods
    for method in node.methods:
      pass #TODO

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
