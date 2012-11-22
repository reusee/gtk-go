import StringIO
import platform
from type_mapping import mappings

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
    print >>self.out, ')\n'

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
    out.append('func %s(' % func.go_name)
    mapping_code = []
    mapped_param_name = {}
    sep = None
    for param in func.parameters:
      if sep != None: out.append(sep)
      sep = ', '
      mapped_type = param.go_type
      if mappings.has_key(mapped_type): # map parameter type
        m = mappings[mapped_type]
        mapped_type = m.mapped_type
        mapping_code.append(m.mapping_code_func(param))
        mapped_param_name[param.name] = m.mapped_name_func(param)
      out.append('%s %s' % (param.name, mapped_type))
    out.append(') ')

    mapped_return_type = func.return_go_type
    if mappings.has_key(mapped_return_type): # map return type
      mapped_return_type = mappings[mapped_return_type].mapped_type
    out.append('%s {\n' % (
      '' if func.no_return else mapped_return_type,
      ))
    out.extend(mapping_code)

    # body
    out.append('\t')
    if not func.no_return:
      out.append('return ')
    if mappings.has_key(func.return_go_type): # mapped return type wrap head
      out.append(mappings[func.return_go_type].return_wrap_head)
    if func.need_wrapper:
      out.append('C._%s(' % func.c_name)
      sep = None
      for param in func.parameters:
        if sep != None:
          out.append(sep)
        sep = ', '
        if param.need_cast:
          out.append('unsafe.Pointer(%s)' % mapped_param_name.get(param.name, param.name))
        else:
          out.append(mapped_param_name.get(param.name, param.name))
      out.append(')')
    else:
      out.append('C.%s(%s)' % (func.c_name, ', '.join(mapped_param_name.get(param.name, param.name)
        for param in func.parameters)))
    if mappings.has_key(func.return_go_type): # mapped return type wrap tail
      out.append(mappings[func.return_go_type].return_wrap_tail)
    out.append('\n}\n\n')

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

  def generate_enum_symbols(self):
    for symbol in self.parser.enum_symbols:
      go_name = symbol
      if symbol.startswith('GTK_'):
        go_name = symbol[4:]
      print >>self.out, "const %s = C.%s" % (go_name, symbol)

  def generate_const_symbols(self):
    for symbol in self.parser.const_symbols:
      go_name = symbol
      if symbol.startswith('GTK_'):
        go_name = symbol[4:]
      print >>self.out, "const %s = C.%s" % (go_name, symbol)

  def write(self, f):
    output_file = open(f, 'w')
    output_file.write(self.out.getvalue())
    output_file.close()
