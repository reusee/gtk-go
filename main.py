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

    self.path = os.path.dirname(os.path.abspath(filename))
    self.package = os.path.basename(self.path)

    self.skip_symbols = set()
    skip_symbol_file = os.path.join(self.path, 'skip_symbols')
    if os.path.exists(skip_symbol_file):
      self.skip_symbols = set([line.strip() 
        for line in open(skip_symbol_file, 'r').xreadlines()
        if not line.startswith('//')
        ])
      self.skip_symbols = set([l for l in self.skip_symbols if l])

    self.func_spec = {}
    func_spec_file = os.path.join(self.path, 'func_spec.py')
    func_spec_module = imp.load_source('func_spec', func_spec_file)
    self.func_spec = func_spec_module.func_specs

    config_file = os.path.join(self.path, 'config.py')
    config_module = imp.load_source('config', config_file)
    for name in dir(config_module):
      if name.startswith('_'): continue
      if name[0].islower(): continue
      setattr(self, name.lower(), getattr(config_module, name))

    self.namespace = parser.get_namespace()
    self.module_name = self.namespace.name.lower()
    self.pkgconfig_packages = list(parser.get_pkgconfig_packages())
    self.includes = list(parser.get_c_includes())
    self.prefixes = self.namespace.symbol_prefixes

    self.functions = []
    self.enum_symbols = []
    self.const_symbols = []

    self.record_types = {}
    self.class_types = {}
    self.class_parents = {}

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
    for mem in node.members:
      if mem.symbol in self.skip_symbols:
        continue
      self.enum_symbols.append(mem.symbol)

  def handleConstant(self, node):
    #self.const_symbols.append((node.ctype, node.value, node.value_type.resolved))
    if node.ctype in self.skip_symbols:
      return
    self.const_symbols.append(node.ctype)

  def _handleCompositeType(self, node):
    # constructors
    for constructor in node.constructors:
      self.handleFunction(constructor, node)
    # static methods
    for function in node.static_methods:
      self.handleFunction(function, node)
    # methods
    for method in node.methods:
      self.handleFunction(method, node)

  def handleRecord(self, node):
    name = node.gi_name.replace('.', '')
    if '_' in name: return
    c_type = node.ctype
    if c_type in self.skip_symbols: return
    self.record_types[name] = c_type
    self._handleCompositeType(node)

  def handleClass(self, node):
    name = node.gi_name.replace('.', '')
    if '_' in name: return
    c_type = node.ctype
    if c_type in self.skip_symbols: return
    if not node.parent:
      self.class_types[name] = 'unsafe.Pointer'
      self.class_parents[name] = True
    else:
      parent_name = node.parent.resolved.replace('.', '')
      self.class_types[name] = parent_name
      self.class_parents[name] = parent_name
    self._handleCompositeType(node)

  def handleAlias(self, alias):
    pass

  def handleBitfield(self, bitfield):
    for member in bitfield.members:
      self.enum_symbols.append(member.symbol)

  def handleCallback(self, callback):
    pass #TODO

  def handleInterface(self, interface):
    pass #TODO

  def handleUnion(self, union):
    pass #TODO

  def get_family_tree(self, t):
    ret = [t]
    if not self.class_parents.has_key(t): return ret
    t = self.class_parents[t]
    while t != True:
      ret.append(t)
      if not self.class_parents.has_key(t): break
      t = self.class_parents[t]
    return ret

def main():
  if len(sys.argv) < 2:
    print "usage: %s <gir files path>" % sys.argv[0]
    sys.exit()
  import glob
  gir_files = glob.glob(os.path.join(os.path.abspath(sys.argv[1]), '*.gir'))
  for f in gir_files:
    print os.path.basename(f)
    parser = Parser(f)
    parser.parse()
    generator = Generator(parser)
    generator.generate()

if __name__ == '__main__':
  main()
