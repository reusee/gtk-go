import StringIO
import platform

class Generator:
  def __init__(self, parser):
    self.parser = parser
    self.out = StringIO.StringIO()

  def generate(self):
    # package name
    print >>self.out, "package %s\n" % self.parser.package_name
    # pkg-config packages
    if 'gobject-2.0' not in self.parser.pkgconfig_packages:
      self.parser.pkgconfig_packages.append('gobject-2.0')
    print >>self.out, "// #cgo pkg-config: %s" % ' '.join(self.parser.pkgconfig_packages)
    # basic includes
    print >>self.out, "// #include <glib-object.h>"
    print >>self.out, "// #include <glib/gstdio.h>"
    # platform specific includes
    system = platform.system()
    if system == 'Linux':
      print >>self.out, "// #include <glib-unix.h>"
    # includes
    for include in self.parser.includes:
      print >>self.out, "// #include <%s>" % include
    # typedefs
    print >>self.out, "/*"
    print >>self.out, "typedef long double longdouble;"
    for orig, t in self.parser.typedefs.iteritems():
      print >>self.out, "typedef %s %s;" % (orig, t)
    print >>self.out, "*/"
    # cgo
    print >>self.out, 'import "C"\n'

    for func in self.parser.functions:
      self.generate_function(func)

    self.generate_enum_symbols()

    self.generate_const_symbols()

  def generate_function(self, func):
    # not support yet or has problem
    if func.deprecated:
      self.out.write('//Deprecated %s\n\n' % func.c_name)
      return
    elif func.skip:
      self.out.write('//Skipped %s\n\n' % func.c_name)
      return
    elif func.has_varargs:
      self.out.write('//TODO varargs %s\n\n' % func.c_name)
      return
    elif func.has_va_list:
      self.out.write('//TODO va_list %s\n\n' % func.c_name)
      return
    elif func.has_long_double:
      self.out.write('//TODO long double %s\n\n' % func.c_name)
      return

    out = []
    # signature
    out.append('func %s(%s) %s{\n' % (
      func.go_name,
      ', '.join('%s %s' % (param.name, param.go_type) for param in func.parameters),
      '' if func.no_return else (func.return_go_type + ' ')
      ))
    # body
    out.append('\t')
    if not func.no_return:
      out.append('return ')
    out.append('C.%s(%s)\n}\n\n' % (func.c_name, ', '.join(param.name for param in func.parameters)))

    self.out.write(''.join(out))

  def generate_enum_symbols(self):
    print >>self.out, "const ("
    for symbol in self.parser.enum_symbols:
      go_name = symbol
      for prefix in self.parser.namespace.symbol_prefixes:
        if symbol.startswith((prefix + '_').upper()):
          go_name = symbol[len(prefix) + 1:]
      print >>self.out, "\t%s = C.%s" % (go_name, symbol)
    print >>self.out, ")"

  def generate_const_symbols(self):
    print >>self.out, "const ("
    for symbol in self.parser.const_symbols:
      go_name = symbol
      for prefix in self.parser.namespace.symbol_prefixes:
        if symbol.startswith((prefix + '_').upper()):
          go_name = symbol[len(prefix) + 1:]
      print >>self.out, "\t%s = C.%s" % (go_name, symbol)
    print >>self.out, ")"

  def write(self, f):
    output_file = open(f, 'w')
    output_file.write(self.out.getvalue())
    output_file.close()
