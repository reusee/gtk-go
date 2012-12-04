import StringIO
import platform
import time
import os

class Generator:
  def __init__(self, parser):
    self.parser = parser
    self.out = StringIO.StringIO()

    self.to_go_type_funcs = set()

  def generate(self):
    # package name
    print >>self.out, "// this file is auto-generated by gtk-go\n"
    print >>self.out, "package %s\n" % self.parser.package
    # pkg-config packages
    if 'gobject-2.0' not in self.parser.pkgconfig_packages:
      self.parser.pkgconfig_packages.append('gobject-2.0')
    if 'gtk+-3.0' not in self.parser.pkgconfig_packages:
      self.parser.pkgconfig_packages.append('gtk+-3.0')
    print >>self.out, "// #cgo pkg-config: %s" % ' '.join(self.parser.pkgconfig_packages)
    # basic includes
    print >>self.out, "// #include <string.h>"
    print >>self.out, "// #include <glib-object.h>"
    print >>self.out, "// #include <glib/gstdio.h>"
    # platform specific includes
    system = platform.system()
    if system == 'Linux':
      print >>self.out, "// #include <glib-unix.h>"
    # includes
    for include in self.parser.includes:
      print >>self.out, "// #include <%s>" % include
    print >>self.out, "/*"
    # c functions
    for generator in self.parser.functions:
      if generator.has_c_func:
        print >>self.out, generator.generate_c_func()
    print >>self.out, "*/"
    # cgo
    print >>self.out, 'import "C"'
    # imports
    print >>self.out, 'import ('
    print >>self.out, '\t"unsafe"'
    #print >>self.out, '\t"runtime"'
    print >>self.out, ')\n'

    self.generate_types()
    for generator in self.parser.functions:
      print >>self.out, generator.generate_go_func()
    self.generate_const_symbols()

    self.write()

  def write(self):
    f = os.path.join(self.parser.path, '%s.go' % self.parser.module_name)
    output_file = open(f, 'w')
    output_file.write(self.out.getvalue())
    output_file.close()

  def generate_const_symbols(self):
    for symbol in self.parser.const_symbols:
      if self.parser.is_skip(symbol): continue
      go_name = symbol
      for prefix in self.parser.prefixes:
        if symbol.startswith(prefix.upper()):
          go_name = symbol[len(prefix) + 1:]
      if hasattr(self.parser, 'conflict_const_names') and go_name in self.parser.conflict_const_names:
        go_name = symbol
      print >>self.out, "const %s = C.%s" % (go_name, symbol)

  def generate_types(self):
    for name, c_type in self.parser.record_types.iteritems():
      print >>self.out, "type %s C.%s" % (name, c_type)

    for name, field in self.parser.class_types.iteritems():
      if field != 'unsafe.Pointer':
        print >>self.out, 'type %s struct { %s }' % (name, field)
      else:
        print >>self.out, 'type %s struct { _value_ unsafe.Pointer }' % name
      family_tree = self.parser.get_family_tree(name)
      print >>self.out, '''\
type {klass}Kind interface {{
  _Is{klass}()
  GetGObject() unsafe.Pointer
}}
func (self {klass}) _Is{klass} () {{}}
func (self {klass}) GetGObject() unsafe.Pointer {{ return self._value_ }}
func To{klass}(value unsafe.Pointer) {klass} {{ return {types}value{braces} }}\
'''.format(
    klass = name,
    types = ''.join('%s{' % t for t in family_tree),
    braces = '}' * len(family_tree),
    )
