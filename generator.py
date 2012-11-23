import StringIO
import platform
from type_mapping import mappings
import time

class Generator:
  def __init__(self, parser):
    self.parser = parser
    self.out = StringIO.StringIO()
    mappings.update(self.parser.type_mappings)

    self.to_go_type_funcs = set()

  def generate(self):
    # package name
    print >>self.out, "// this file is auto-generated by go-gi\n"
    print >>self.out, "package %s\n" % self.parser.package_name
    # pkg-config packages
    if 'gobject-2.0' not in self.parser.pkgconfig_packages:
      self.parser.pkgconfig_packages.append('gobject-2.0')
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
    # typedefs
    print >>self.out, "typedef long double longdouble;"
    # helper functions
    self.generate_macro_helpers()
    # wrappers
    for func in self.parser.functions_need_wrapper:
      self.generate_wrapper(func)
    print >>self.out, "*/"
    # cgo
    print >>self.out, 'import "C"'
    # imports
    print >>self.out, 'import ('
    print >>self.out, '\t"unsafe"'
    print >>self.out, '\t"runtime"'
    print >>self.out, ')\n'

    for func in self.parser.functions:
      self.generate_function(func)

    self.generate_enum_symbols()

    self.generate_const_symbols()

    self.generate_to_go_type_func_codes()

    self.generate_record_types()

  def write(self, f):
    output_file = open(f, 'w')
    output_file.write(self.out.getvalue())
    output_file.close()

  def generate_function(self, func):
    # not support yet or has problem
    if func.skip:
      self.out.write('//Skipped %s\n\n' % func.c_name)
      return
    elif func.not_implement:
      self.out.write('//TODO %s\n\n' % func.c_name)
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
    return_type_mapping = None
    if mappings.has_key(mapped_return_type):
      return_type_mapping = mappings[mapped_return_type]
      mapped_return_type = return_type_mapping.mapped_type
    out.append('%s{\n' % (
      '' if func.no_return else (mapped_return_type + ' '),
      ))
    out.extend(mapping_code)

    # return expression
    return_expression = []
    if return_type_mapping != None:
      if return_type_mapping.has_key('to_go_type_func'):
        return_expression.append('%s(' % mappings[func.return_go_type].to_go_type_func)
        self.to_go_type_funcs.add(func.return_go_type)
      elif return_type_mapping.has_key('to_go_type_code_head'):
        return_expression.append(return_type_mapping.to_go_type_code_head)
    if func.need_wrapper:
      return_expression.append('C._%s(' % func.c_name)
      sep = None
      for param in func.parameters:
        if sep != None:
          return_expression.append(sep)
        sep = ', '
        if param.need_cast:
          return_expression.append('unsafe.Pointer(%s)' % mapped_param_name.get(param.name, param.name))
        else:
          return_expression.append(mapped_param_name.get(param.name, param.name))
      return_expression.append(')')
    else:
      return_expression.append('C.%s(%s)' % (func.c_name, ', '.join(mapped_param_name.get(param.name, param.name)
        for param in func.parameters)))
    if return_type_mapping != None:
      if return_type_mapping.has_key('to_go_type_func'):
        return_expression.append(')')
      elif return_type_mapping.has_key('to_go_type_code_tail'):
        return_expression.append(return_type_mapping.to_go_type_code_tail)
    return_expression = ''.join(return_expression)

    if return_type_mapping != None and return_type_mapping.has_key('return_code_func'):
      out.append(return_type_mapping.return_code_func(return_expression))
    else:
      out.append('\t')
      if not func.no_return:
        out.append('return ')
      out.append(return_expression)
      out.append('\n')
    out.append('}\n\n')

    self.out.write(''.join(out))

  def generate_to_go_type_func_codes(self):
    for t in self.to_go_type_funcs:
      self.out.write(mappings[t].to_go_type_func_code)
      self.out.write('\n')

  def generate_wrapper(self, func):
    if func.skip:
      return
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
      for prefix in self.parser.prefixes:
        if symbol.startswith(prefix.upper()):
          go_name = symbol[len(prefix) + 1:]
      print >>self.out, "const %s = C.%s" % (go_name, symbol)

  def generate_const_symbols(self):
    for symbol in self.parser.const_symbols:
      go_name = symbol
      for prefix in self.parser.prefixes:
        if symbol.startswith(prefix.upper()):
          go_name = symbol[len(prefix) + 1:]
      print >>self.out, "const %s = C.%s" % (go_name, symbol)

  def generate_macro_helpers(self):
    print >>self.out, "gboolean _true() { return TRUE; }"
    print >>self.out, "gboolean _false() { return FALSE; }"

  def generate_record_types(self):
    for name, c_type in self.parser.construct_records:
      if c_type in self.parser.skip_symbols:
        continue
      print >>self.out, "type %s C.%s" % (name, c_type)
