#!/usr/bin/env python2

import sys
sys.path.append("/usr/lib/gobject-introspection")
from giscanner.girparser import GIRParser
from generator import Generator
import os
from common import *
from container import *

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
    func_spec_file = os.path.join(os.path.dirname(os.path.abspath(filename)), 'func_spec')
    for line in open(func_spec_file, 'r').xreadlines():
      fields = line.strip().split('|')
      func_name, return_type = fields[:2]
      arg_types = fields[2:]
      for i, t in enumerate(arg_types):
        arg_types[i] = t.replace('[]', '*')
      self.func_spec[func_name] = Dict({
        'return_type': return_type,
        'arg_types': arg_types,
      })

    self.namespace = parser.get_namespace()
    self.package_name = self.namespace.name.lower()
    self.pkgconfig_packages = list(parser.get_pkgconfig_packages())
    self.includes = list(parser.get_c_includes())
    self.prefixes = self.namespace.symbol_prefixes

    self.functions = []
    self.enum_symbols = []
    self.const_symbols = []
    self.construct_records = set()

    self.exported_functions = set()

  def parse(self):
    for node in self.namespace.itervalues():
      handlerName = 'handle' + type(node).__name__
      if hasattr(self, handlerName):
        getattr(self, handlerName)(node)
      else:
        print type(node).__name__, 'not handle'
        stop

  def handleFunction(self, node, gi_class = '', is_method = False, c_class = ''):
    func = Function()
    # name
    func.c_name = node.symbol
    if func.c_name in self.exported_functions:
      return
    self.exported_functions.add(func.c_name)
    func.name = self.convert_func_name(node.name)
    if is_method:
      if func.name == "":
        func.name = 'New' + gi_class
    else:
      func.name = gi_class + func.name

    # class
    func.is_method = is_method
    func.c_class = c_class
    func.gi_class = gi_class

    # ins and outs
    func.return_value = Value(node.retval)
    func.parameters = []
    func.c_parameters = []
    if is_method:
      value = Value.selfValue(c_class)
      func.c_parameters.append(value)
    func.extra_returns = []
    for i, param in enumerate(node.parameters):
      value = Value(param)
      if 'in' in param.direction:
        func.parameters.append(value)
      if 'out' in param.direction:
        func.extra_returns.append(value)
      func.c_parameters.append(value)
    if node.throws:
      value = Value.errValue()
      func.extra_returns.append(value)
      func.c_parameters.append(value)

    func.need_helper = False
    if func.is_method:
      func.need_helper = True
    func.need_helper |= any(value.need_helper for value in func.parameters)
    func.need_helper |= any(value.need_helper for value in func.extra_returns)

    func.skip = node.deprecated is not None or func.c_name in self.skip_symbols
    func.skip |= any(value.not_implement for value in func.parameters)
    func.skip |= any(value.not_implement for value in func.extra_returns)

    self.functions.append(func)

  def convert_func_name(self, s):
    words = s.split('_')
    words = [w.capitalize() for w in words]
    return ''.join(words)

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
    if c_type in self.skip_symbols:
      return
    self.construct_records.add((name, c_type))
    # constructors
    for constructor in node.constructors:
      self.handleFunction(constructor, name)
    # static methods
    for function in node.static_methods:
      self.handleFunction(function, name)
    # methods
    for method in node.methods:
      self.handleFunction(method, name, True, c_type)

  def handleAlias(self, alias):
    pass

  def handleClass(self, cls):
    self.handleRecord(cls)
    #print cls #TODO
    #for k in dir(cls):
    #  if k.startswith('_'): continue
    #  print k.ljust(20, ' '), getattr(cls, k)
    #print '=' * 30

  def handleBitfield(self, bitfield):
    for member in bitfield.members:
      self.enum_symbols.append(member.symbol)

  def handleCallback(self, callback):
    pass #TODO

  def handleInterface(self, interface):
    pass #TODO

  def handleUnion(self, union):
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
