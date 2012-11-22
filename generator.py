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
    print >>self.out, "/*"
    # typedefs
    print >>self.out, "typedef long double longdouble;"
    # wrappers
    for func in self.parser.functions_need_wrapper:
      self.generate_wrapper(func)
    print >>self.out, "*/"
    # cgo
    print >>self.out, 'import "C"'
    # imports
    print >>self.out, 'import ('
    print >>self.out, '\t"unsafe"'
    print >>self.out, ')'

    for func in self.parser.functions:
      self.generate_function(func)

  def generate_function(self, func):
    # not support yet or has problem
    if func.deprecated:
      self.out.write('\n//Deprecated %s\n' % func.c_name)
      return
    elif func.skip:
      self.out.write('\n//Skipped %s\n' % func.c_name)
      return
    elif func.has_varargs:
      self.out.write('\n//TODO varargs %s\n' % func.c_name)
      return
    elif func.has_va_list:
      self.out.write('\n//TODO va_list %s\n' % func.c_name)
      return
    elif func.has_long_double:
      self.out.write('\n//TODO long double %s\n' % func.c_name)
      return

    out = []
    # signature
    out.append('\nfunc %s(%s) %s{\n' % (
      func.go_name,
      ', '.join('%s %s' % (param.name, param.go_type) for param in func.parameters),
      '' if func.no_return else (func.return_go_type + ' ')
      ))
    # body
    out.append('\t')
    if not func.no_return:
      out.append('return ')
    if func.need_wrapper:
      out.append('C._%s(' % func.c_name)
      sep = None
      for param in func.parameters:
        if sep != None:
          out.append(sep)
        sep = ', '
        if param.need_cast:
          out.append('unsafe.Pointer(%s)' % param.name)
        else:
          out.append(param.name)
      out.append(')\n}\n')
    else:
      out.append('C.%s(%s)\n}\n' % (func.c_name, ', '.join(param.name for param in func.parameters)))

    self.out.write(''.join(out))

  def generate_wrapper(self, func):
    out = []
    out.append('%s %s(' % (
      func.return_c_type,
      '_' + func.c_name,
      ))
    sep = None
    for param in func.parameters:
      if sep != None:
        out.append(sep)
      sep = ', '
      if param.need_cast:
        out.append('void*')
      else:
        out.append(param.c_type)
      out.append(' ' + param.name)
    out.append(') {\n\t')
    if not func.no_return:
      out.append('return ')
    out.append('%s(' % func.c_name)
    sep = None
    for param in func.parameters:
      if sep != None:
        out.append(sep)
      sep = ', '
      if param.need_cast:
        out.append('(%s)(%s)' % (param.c_type, param.name))
      else:
        out.append(param.name)
    out.append(');\n}\n')
    self.out.write(''.join(out))

  def write(self, f):
    output_file = open(f, 'w')
    output_file.write(self.out.getvalue())
    output_file.close()
