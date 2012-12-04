#!/usr/bin/env python2

import sys
sys.path.append("/usr/lib/gobject-introspection")
from giscanner.girparser import GIRParser
from generator import Generator
import os
from common import *
from function_handler import handleFunction
import imp

class Translator:
  def __init__(self):
    self.class_parents = {}
    self.parsers = []
    self.names = set()
    self.namespaces = set()

  def add(self, filename):
    parser = Parser(filename, self)
    self.parsers.append(parser)

  def preprocess(self):
    # prepare
    for parser in self.parsers:
      parser.prepare()
    # collect inheritance info
    for parser in self.parsers:
      for node in parser.nodes_of_class:
        name = parser.convert_gi_name_to_go_name(node.gi_name)
        if self.class_parents.has_key(name):
          print 'type name conflict', name
          assert False
        if '_' in name: return
        if not node.parent:
          self.class_parents[name] = True
        else:
          parent_name = parser.convert_gi_name_to_go_name(node.parent.resolved)
          self.class_parents[name] = parent_name

  def parse(self):
    for parser in self.parsers:
      parser.parse()

  def generate(self):
    for parser in self.parsers:
      generator = Generator(parser)
      generator.generate()

class Parser:
  def __init__(self, filename, translator):
    self.translator = translator
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
    self.translator.namespaces.add(self.namespace.name)
    self.pkgconfig_packages = list(parser.get_pkgconfig_packages())
    self.includes = list(parser.get_c_includes())
    self.prefixes = self.namespace.symbol_prefixes

    self.functions = []
    self.const_symbols = set()

    self.class_types = {}
    self.record_types = {}

    self.exported_functions = set()
    self.functions_to_handle = []

  def prepare(self):
    for node in self.namespace.itervalues():
      node_type = type(node).__name__.lower()
      container = 'nodes_of_' + node_type
      if not hasattr(self, container):
        setattr(self, container, [])
      container = getattr(self, container)
      container.append(node)

  def parse(self):
    order = [
      'nodes_of_class',
      'nodes_of_record',
      'nodes_of_alias',
      'nodes_of_bitfield',
      'nodes_of_callback',
      'nodes_of_constant',
      'nodes_of_enum',
      'nodes_of_interface',

      'nodes_of_function',
    ]
    for container in order:
      if not hasattr(self, container): continue
      container = getattr(self, container)
      for node in container:
        handler = 'handle' + type(node).__name__
        handler = getattr(self, handler)
        handler(node)

    for args in self.functions_to_handle:
      self.handleFunction(*args)

  def handleFunction(self, *args):
    generator = handleFunction(self, *args)
    if generator:
      self.functions.append(generator)
      self.exported_functions.add(generator.lib_func_name)

  def handleEnum(self, node):
    for mem in node.members:
      if mem.symbol in self.skip_symbols:
        continue
      self.const_symbols.add(mem.symbol)

  def handleConstant(self, node):
    if node.ctype in self.skip_symbols: return
    self.const_symbols.add(node.ctype)

  def _handleCompositeType(self, node):
    # constructors
    for constructor in node.constructors:
      self.functions_to_handle.append((constructor, node))
    # static methods
    for function in node.static_methods:
      self.functions_to_handle.append((function, node))
    # methods
    for method in node.methods:
      self.functions_to_handle.append((method, node))

  def handleRecord(self, node):
    name = self.convert_gi_name_to_go_name(node.gi_name)
    if '_' in name: return
    c_type = node.ctype
    if c_type in self.skip_symbols: return
    if name in self.translator.names:
      print 'type name conflict', name
      assert False
    self.record_types[name] = c_type
    self.translator.names.add(name)
    self._handleCompositeType(node)

  def handleClass(self, node):
    name = self.convert_gi_name_to_go_name(node.gi_name)
    if '_' in name: return
    c_type = node.ctype
    if c_type in self.skip_symbols: return
    if not node.parent:
      self.class_types[name] = 'unsafe.Pointer'
    else:
      parent_name = self.convert_gi_name_to_go_name(node.parent.resolved)
      self.class_types[name] = parent_name
    self.translator.names.add(name)
    self._handleCompositeType(node)

  def handleAlias(self, alias):
    pass

  def handleBitfield(self, bitfield):
    for member in bitfield.members:
      self.const_symbols.add(member.symbol)

  def handleCallback(self, callback):
    pass #TODO

  def handleInterface(self, interface):
    pass #TODO

  def handleUnion(self, union):
    pass #TODO

  def get_family_tree(self, t):
    ret = [t]
    t = self.translator.class_parents[t]
    while t != True:
      ret.append(t)
      t = self.translator.class_parents[t]
    return ret

  def convert_gi_name_to_go_name(self, gi_name):
    namespace, name = gi_name.split('.')
    if namespace not in self.translator.namespaces:
      name = gi_name.replace('.', '')
    if name in self.conflict_type_names:
      name = gi_name.replace('.', '')
    return name

def main():
  if len(sys.argv) < 2:
    print "usage: %s <gir files path>" % sys.argv[0]
    sys.exit()
  import glob
  gir_files = glob.glob(os.path.join(os.path.abspath(sys.argv[1]), '*.gir'))
  translator = Translator()
  for f in gir_files:
    print os.path.basename(f)
    translator.add(f)
  translator.preprocess()
  translator.parse()
  translator.generate()

if __name__ == '__main__':
  main()
