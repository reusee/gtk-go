#!/usr/bin/env python2

import sys
sys.path.append("/usr/lib/gobject-introspection")
from giscanner.girparser import GIRParser
from generator import Generator
import os
from common import *
from function_handler import handleFunction
import imp

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

    self.func_spec = {}
    func_spec_file = os.path.join(os.path.dirname(os.path.abspath(filename)), 'func_spec.py')
    func_spec_module = imp.load_source('func_spec', func_spec_file)
    self.func_spec = func_spec_module.func_specs

    self.namespace = parser.get_namespace()
    self.package_name = self.namespace.name.lower()
    self.pkgconfig_packages = list(parser.get_pkgconfig_packages())
    self.includes = list(parser.get_c_includes())
    self.prefixes = self.namespace.symbol_prefixes

    self.functions = []
    self.enum_symbols = []
    self.const_symbols = []

    self.gi_types = set()
    self.gi_value_types = set()
    self.gi_reference_types = set()

    self.exported_functions = set()

    self.functions_to_handle = []

  def parse(self):
    for node in self.namespace.itervalues():
      handlerName = 'handle' + type(node).__name__
      if hasattr(self, handlerName):
        getattr(self, handlerName)(node)
      else:
        print type(node).__name__, 'not handle'
        stop
    for args in self.functions_to_handle:
      self._handleFunction(*args)

  def handleFunction(self, *args):
    self.functions_to_handle.append(args)

  def _handleFunction(self, *args):
    generator = handleFunction(self, *args)
    if generator:
      self.functions.append(generator)
      self.exported_functions.add(generator.lib_func_name)

  def handleEnum(self, node):
    self.gi_types.add((node.name, node.ctype))
    self.gi_value_types.add(node.name)
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
    self.gi_types.add((name, c_type))
    self.gi_reference_types.add(name)
    # constructors
    for constructor in node.constructors:
      self.handleFunction(constructor, node)
    # static methods
    for function in node.static_methods:
      self.handleFunction(function, node)
    # methods
    for method in node.methods:
      self.handleFunction(method, node)

  def handleAlias(self, alias):
    self.gi_types.add((alias.name, alias.ctype))
    self.gi_value_types.add(alias.name)

  def handleClass(self, cls):
    self.handleRecord(cls)
    #TODO

  def handleBitfield(self, bitfield):
    self.gi_types.add((bitfield.name, bitfield.ctype))
    self.gi_value_types.add(bitfield.name)
    for member in bitfield.members:
      self.enum_symbols.append(member.symbol)

  def handleCallback(self, callback):
    self.gi_types.add((callback.name, callback.ctype))
    self.gi_value_types.add(callback.name)
    pass #TODO

  def handleInterface(self, interface):
    pass #TODO

  def handleUnion(self, union):
    self.gi_types.add((union.name, union.ctype))
    self.gi_value_types.add(union.name)
    pass #TODO

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
