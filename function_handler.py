from giscanner import ast
from function_generator import *
from common import *

def handleFunction(parser, function, klass = None):
  generator = FunctionGenerator()

  processors = [
      debug,

      # basic
      check_skip,
      collect_c_func_info,
      collect_go_func_info,

      # tunning
      dereference_basic_type_out_param,
      make_constructor_return_go_type,
      map_glib_numeric_parameters_to_go_type,
      map_glib_numeric_returns_to_go_type,
      map_string_parameters,
      map_string_returns,
  ]

  for processor in processors:
    processor(parser, generator, function, klass)
    if generator.skip:
      return None

  return generator

def debug(parser, generator, function, klass):
  pass

def check_skip(parser, generator, function, klass):
  if function.symbol in parser.skip_symbols:
    generator.skip = True
  if function.symbol in parser.exported_functions:
    generator.skip = True
  if function.deprecated is not None:
    generator.skip = True
  for param in function.parameters:
    if param.type.resolved == '<varargs>':
      generator.skip = True
    if param.type.resolved == 'va_list':
      generator.skip = True
    if param.type.resolved == '<array>':
      generator.skip = True
    if param.direction == 'inout':
      generator.skip = True

def convert_to_cgo_capatible_type(t):
  if '*const' in t:
    t = t.replace('*const ', '*')
  if 'const' in t:
    t = t.replace('const', '')
  if '**' in t:
    t = 'void *'
  if 'long double' in t:
    t = 'double'
  t = t.strip()
  return t

def collect_c_func_info(parser, generator, function, klass):
  c_func_name = function.symbol
  lib_func_spec = parser.func_spec[c_func_name]
  generator.lib_func_spec = lib_func_spec
  c_return_value = Value()
  generator.c_return_value = c_return_value
  c_return_value.c_return_type = convert_to_cgo_capatible_type(lib_func_spec.return_type)
  if generator.c_return_value.c_return_type != lib_func_spec.return_type:
    generator.has_c_func = True

  # has_c_func, c_parameters, c_arguments
  for i, param in enumerate(lib_func_spec.parameters):
    value = Value()
    if function.is_method and i == 0: # use class type instead of spec type
      value.c_parameter_type = klass.ctype + ' *'
      value.c_parameter_name = '_self_'
    else:
      value.c_parameter_type = convert_to_cgo_capatible_type(param.type)
      value.c_parameter_name = param.name
    if value.c_parameter_type != param.type:
      generator.has_c_func = True
    if value.c_parameter_type != param.type:
      value.c_argument = '(%s)(%s)' % (param.type, value.c_parameter_name)
    else:
      value.c_argument = value.c_parameter_name
    generator.c_parameters.append(value)
    generator.c_arguments.append(value)

  # c_func_name
  if generator.has_c_func:
    generator.c_func_name = '_' + c_func_name
  else:
    generator.c_func_name = c_func_name

  generator.c_has_return = lib_func_spec.return_type != 'void'
  generator.lib_func_name = c_func_name

def collect_go_func_info(parser, generator, function, klass):
  # receiver
  if function.is_method:
    generator.has_receiver = True
    value = generator.c_parameters[0]
    value.receiver_name = '_self_'
    value.receiver_type = '*' + klass.gi_name.split('.')[-1]
    generator.receiver = value

  # go func name
  generator.go_func_name = ''.join(x.capitalize() 
      for x in function.name.split('_'))
  if function.is_constructor:
    generator.go_func_name = klass.gi_name.split('.')[-1] + generator.go_func_name
  elif klass and not function.is_constructor and not function.is_method: # class or record static function
    generator.go_func_name = klass.gi_name.split('.')[-1] + generator.go_func_name

  # go return
  generator.cgo_has_return = generator.c_has_return
  if generator.cgo_has_return:
    value = generator.c_return_value
    value.go_return_name = '_return_'
    value.go_return_type = convert_to_cgo_type(value.c_return_type)
    value.gir_info = function.retval
    generator.go_returns.append(value)

  # go parameter names and types and cgo arguments
  values = generator.c_parameters
  if function.is_method: # because function.parameters does not contain _self_ param
    values = values[1:]
  for i, param in enumerate(function.parameters):
    value = values[i]
    value.gir_info = param
    name = value.c_parameter_name
    if is_go_word(name):
      name += '_'
    if param.direction == 'in':
      value.go_parameter_name = name
      value.go_parameter_type = convert_to_cgo_type(value.c_parameter_type)
      generator.go_parameters.append(value)
    elif param.direction == 'out':
      value.go_return_name = name
      value.go_return_type = convert_to_cgo_type(value.c_parameter_type)
      generator.go_returns.append(value)
    value.cgo_argument = name
    generator.cgo_arguments.append(value)

  if function.throws:
    value = values[-1]
    value.go_return_name = '_error_'
    value.go_return_type = 'unsafe.Pointer'
    value.cgo_argument = value.go_return_name
    generator.go_returns.append(value)
    generator.cgo_arguments.append(value)

  if function.is_method:
    value = generator.c_parameters[0]
    value.cgo_argument = '(%s)(%s)' % (
        convert_to_cgo_type(value.c_parameter_type),
        generator.receiver.receiver_name)
    generator.cgo_arguments.insert(0, value)

  # cgo call
  generator.cgo_return_lvalue = '_return_'
  generator.cgo_func_name = 'C.' + generator.c_func_name

def convert_to_cgo_type(c_type):
  c_type = c_type.replace('volatile', '')
  if c_type == 'void *':
    return 'unsafe.Pointer'
  cgo_type = 'C.' + c_type
  if c_type.endswith('*'):
    cgo_type = '*' + cgo_type[:-1]
  return cgo_type.strip()

def dereference_basic_type_out_param(parser, generator, function, klass):
  for ret in generator.go_returns:
    if ret.gir_info and ret.gir_info.type.is_equiv(ast.BASIC_GIR_TYPES):
      if ret.go_return_type[0] != '*': continue
      if not isinstance(ret.gir_info, ast.Parameter): continue
      ret.go_return_type = ret.go_return_type[1:]
      ret.cgo_argument = '&' + ret.cgo_argument

def make_constructor_return_go_type(parser, generator, function, klass):
  if function.is_constructor:
    generator.statements_before_cgo_call.append('var _cgo_return_ %s' 
        % generator.c_return_value.go_return_type)
    generator.c_return_value.go_return_type = '*' + klass.gi_name.split('.')[-1]
    generator.cgo_return_lvalue = '_cgo_return_'
    generator.statements_after_cgo_call.append('_return_ = (%s)(unsafe.Pointer(_cgo_return_))'
        % generator.c_return_value.go_return_type)

numeric_mapping = {
  'C.gchar': 'int8',
  'C.guchar': 'byte',

  'C.gint': 'int',
  'C.guint': 'uint',
  'C.gshort': 'int',
  'C.gushort': 'uint',
  'C.glong': 'int64',
  'C.gulong': 'uint64',
  'C.gint8': 'int8',
  'C.guint8': 'uint8',
  'C.gint16': 'int16',
  'C.guint16': 'uint16',
  'C.gint32': 'int32',
  'C.guint32': 'uint32',
  'C.gint64': 'int64',
  'C.guint64': 'uint64',

  'C.gfloat': 'float64',
  'C.gdouble': 'float64',
  'C.gsize': 'uint64',
  'C.gssize': 'int64',
  'C.goffset': 'int64',

  'C.gintptr': 'int64',
  'C.guintptr': 'uint64',
}

def map_glib_numeric_parameters_to_go_type(parser, generator, function, klass):
  for param in generator.go_parameters:
    if param.go_parameter_type in numeric_mapping:
      generator.statements_before_cgo_call.append('_cgo_%s_ := (%s)(%s)' % (
        param.go_parameter_name, param.go_parameter_type, param.go_parameter_name))
      param.go_parameter_type = numeric_mapping[param.go_parameter_type]
      param.cgo_argument = '_cgo_%s_' % param.go_parameter_name

def map_glib_numeric_returns_to_go_type(parser, generator, function, klass):
  for ret in generator.go_returns:
    if ret.go_return_type in numeric_mapping:
      generator.statements_before_cgo_call.append('var %s %s' % (
        ret.go_return_name, ret.go_return_type))
      generator.statements_after_cgo_call.append('_go_%s_ = (%s)(%s)' % (
        ret.go_return_name,
        numeric_mapping[ret.go_return_type],
        ret.go_return_name))
      ret.go_return_name = '_go_%s_' % ret.go_return_name
      ret.go_return_type = numeric_mapping[ret.go_return_type]

def map_string_parameters(parser, generator, function, klass):
  for param in generator.go_parameters:
    if param.gir_info.type.resolved in ['filename', 'utf8']:
      generator.statements_before_cgo_call.extend([
        '_cstring_%s_ := C.CString(%s)' % (param.go_parameter_name, param.go_parameter_name),
        '_cgo_%s_ := (%s)(unsafe.Pointer(_cstring_%s_))' % (
          param.go_parameter_name, param.go_parameter_type, param.go_parameter_name),
        ])
      if param.gir_info.transfer == 'none':
        generator.statements_before_cgo_call.append(
            'defer C.free(unsafe.Pointer(_cstring_%s_))' % param.go_parameter_name)
      param.cgo_argument = '_cgo_%s_' % param.go_parameter_name
      param.go_parameter_type = 'string'

def map_string_returns(parser, generator, function, klass):
  for ret in generator.go_returns:
    if ret.gir_info is None: continue
    if ret.gir_info.type.resolved in ['filename', 'utf8']:
      if ret.go_return_type == 'unsafe.Pointer': continue 
      print ret.go_return_type, function.name
      generator.statements_before_cgo_call.append('var %s %s' % (
        ret.go_return_name, ret.go_return_type))
      generator.statements_after_cgo_call.append('_go_%s_ = C.GoString((*C.char)(unsafe.Pointer(%s)))'
          % (ret.go_return_name, ret.go_return_name))
      ret.go_return_name = '_go_%s_' % ret.go_return_name
      ret.go_return_type = 'string'
