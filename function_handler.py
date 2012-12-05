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
      map_record_and_class_parameters,
      map_record_and_class_returns,
      map_glib_numeric_parameters,
      map_glib_numeric_returns,
      map_string_parameters,
      map_string_returns,
      map_boolean_parameters,
      map_boolean_returns,
      map_byte_array_parameters,
      map_byte_array_returns,
      map_enum_parameters,
  ]

  for processor in processors:
    processor(parser, generator, function, klass)
    if generator.skip:
      return None

  return generator

def debug(parser, generator, function, klass):
  pass

handled_param_array_types = [
  ('guint8*', 'guint8'),
]

def check_skip(parser, generator, function, klass):
  if parser.is_skip(function.symbol):
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
      key = (param.type.ctype, param.type.element_type.ctype)
      if key not in handled_param_array_types:
        generator.skip = True
    if param.direction == 'inout':
      generator.skip = True
    if parser.is_skip(param.type.ctype):
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
  if t == 'unsigned long':
    t = 'gulong'
  if t == 'unsigned int':
    t = 'guint'
  if t == 'unsigned char':
    t = 'guchar'
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
      if klass.ctype is None:
        value.c_parameter_type = klass.c_name + ' *'
      else:
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
    value.receiver_type = '*' + parser.convert_gi_name_to_go_name(klass.gi_name)
    generator.receiver = value

  # go func name
  generator.go_func_name = ''.join(x.capitalize() 
      for x in function.name.split('_'))
  if generator.go_func_name == '':
    generator.go_func_name = 'New'
  if function.is_constructor:
    generator.go_func_name = klass.gi_name.split('.')[-1] + generator.go_func_name
  elif klass and not function.is_constructor and not function.is_method: # class or record static function
    generator.go_func_name = klass.gi_name.split('.')[-1] + generator.go_func_name
  if not function.is_method: # method function will not cause name conflict
    if generator.go_func_name in parser.translator.names:
      generator.go_func_name = parser.module_name.capitalize() + generator.go_func_name
    if hasattr(parser, 'conflict_function_names') and generator.go_func_name in parser.conflict_function_names:
      generator.go_func_name = parser.module_name.capitalize() + generator.go_func_name
    parser.translator.names.add(generator.go_func_name)

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
    assert value.cgo_argument != None
    generator.cgo_arguments.append(value)

  if function.throws:
    value = values[-1]
    value.go_return_name = '_error_'
    value.go_return_type = 'error'
    generator.statements_before_cgo_call.append('var _cgo_error_ *C.GError')
    value.cgo_argument = 'unsafe.Pointer(&_cgo_error_)'
    generator.statements_after_cgo_call.extend([
      'if _cgo_error_ != nil {',
      '\t_error_ = &GoError{C.GoString((*C.char)(unsafe.Pointer(_cgo_error_.message)))}',
      '\tdefer C.g_error_free(_cgo_error_)',
      '}',
    ])
    assert value.cgo_argument != None
    generator.go_returns.append(value)
    generator.cgo_arguments.append(value)

  if function.is_method: # _self_ param
    value = generator.c_parameters[0]
    klass_name = parser.convert_gi_name_to_go_name(klass.gi_name)
    if klass_name in parser.class_types:
      value.cgo_argument = '(%s)(%s._value_)' % (
          convert_to_cgo_type(value.c_parameter_type),
          generator.receiver.receiver_name)
    elif klass_name in parser.record_types:
      value.cgo_argument = '(%s)(%s)' % (
          convert_to_cgo_type(value.c_parameter_type),
          generator.receiver.receiver_name)
    else: 
      assert False
    assert value.cgo_argument != None
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
    if not ret.gir_info: continue
    if not ret.gir_info.type.is_equiv(ast.BASIC_GIR_TYPES): continue
    if ret.go_return_type[0] != '*': continue
    if not isinstance(ret.gir_info, ast.Parameter): continue
    ret.go_return_type = ret.go_return_type[1:]
    ret.cgo_argument = '&' + ret.cgo_argument

def map_record_and_class_parameters(parser, generator, function, klass):
  for param in generator.go_parameters:
    if param.gir_info.type.target_giname is None: continue
    gi_type = parser.convert_gi_name_to_go_name(param.gir_info.type.target_giname)
    if (gi_type not in parser.record_types) and (gi_type not in parser.class_types): continue

    if gi_type in parser.record_types:
      generator.statements_before_cgo_call.append('_cgo_%s_ := (%s)(unsafe.Pointer(%s))' % (
        param.go_parameter_name, param.go_parameter_type, param.go_parameter_name))
      param.go_parameter_type = '*' + gi_type
    elif gi_type in parser.class_types:
      generator.statements_before_cgo_call.append('_cgo_%s_ := (%s)(%s.GetGObject())' % (
        param.go_parameter_name,
        convert_to_cgo_type(param.c_parameter_type),
        param.go_parameter_name))
      param.go_parameter_type = gi_type + 'Kind'
    param.cgo_argument = '_cgo_%s_' % param.go_parameter_name

def map_record_and_class_returns(parser, generator, function, klass):
  for ret in generator.go_returns:
    if ret.gir_info is None: continue
    if ret.gir_info.type.target_giname is None: continue
    gi_type = parser.convert_gi_name_to_go_name(ret.gir_info.type.target_giname)
    if (gi_type not in parser.record_types) and (gi_type not in parser.class_types): continue

    if isinstance(ret.gir_info, ast.Parameter) and ret.gir_info.caller_allocates:
      assert(gi_type not in parser.class_types)
      generator.statements_before_cgo_call.append('var _allocated_%s_ %s' % (
        ret.go_return_name, ret.go_return_type[1:]))
      generator.statements_after_cgo_call.append('%s = (%s)(unsafe.Pointer(%s))' % (
        ret.go_return_name,
        '*' + gi_type,
        '&_allocated_%s_' % ret.go_return_name))
      ret.go_return_type = '*' + gi_type
      ret.cgo_argument = '&_allocated_%s_' % ret.go_return_name

    elif isinstance(ret.gir_info, ast.Parameter) and not ret.gir_info.caller_allocates:
      assert ret.go_return_type == 'unsafe.Pointer'
      #assert(gi_type not in parser.class_types) #TODO
      generator.statements_before_cgo_call.append('var _allocated_%s_ %s' % (
        ret.go_return_name, convert_to_cgo_type(ret.gir_info.type.ctype[:-1])))
      generator.statements_after_cgo_call.append('%s = (%s)(unsafe.Pointer(%s))' % (
        ret.go_return_name,
        '*' + gi_type,
        '_allocated_%s_' % ret.go_return_name))
      ret.go_return_type = '*' + gi_type
      ret.cgo_argument = 'unsafe.Pointer(&_allocated_%s_)' % ret.go_return_name

    elif isinstance(ret.gir_info, ast.Return):
      if gi_type in parser.record_types:
        mapped_ret_type = '*' + gi_type
        generator.statements_before_cgo_call.append('var %s %s' % (
          ret.go_return_name, ret.go_return_type))
        generator.statements_after_cgo_call.append('_go_%s_ = (%s)(unsafe.Pointer(%s))' % (
          ret.go_return_name, mapped_ret_type, ret.go_return_name))
        ret.go_return_name = '_go_%s_' % ret.go_return_name
        ret.go_return_type = mapped_ret_type
      elif gi_type in parser.class_types:
        generator.statements_before_cgo_call.append('var %s %s' % (
          ret.go_return_name,
          convert_to_cgo_type(ret.c_return_type)))
        if function.is_constructor:
          ret.go_return_type = parser.convert_gi_name_to_go_name(klass.gi_name)
        elif klass and not function.is_constructor and not function.is_method and 'new' in function.symbol: # constructive static method
          ret.go_return_type = parser.convert_gi_name_to_go_name(klass.gi_name)
        else:
          ret.go_return_type = gi_type
        generator.statements_after_cgo_call.append('_go_%s_ = To%s(unsafe.Pointer(_return_))' % (
          ret.go_return_name, ret.go_return_type))
        ret.go_return_name = '_go_%s_' % ret.go_return_name
      else: assert False

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

def map_glib_numeric_parameters(parser, generator, function, klass):
  for param in generator.go_parameters:
    if param.go_parameter_type not in numeric_mapping: continue
    generator.statements_before_cgo_call.append('_cgo_%s_ := (%s)(%s)' % (
      param.go_parameter_name, param.go_parameter_type, param.go_parameter_name))
    param.go_parameter_type = numeric_mapping[param.go_parameter_type]
    param.cgo_argument = '_cgo_%s_' % param.go_parameter_name

def map_glib_numeric_returns(parser, generator, function, klass):
  for ret in generator.go_returns:
    if ret.go_return_type not in numeric_mapping: continue
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
    if param.gir_info.type.resolved not in ['filename', 'utf8']: continue
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
    if ret.gir_info.type.resolved not in ['filename', 'utf8']: continue
    if ret.go_return_type == 'unsafe.Pointer': continue 
    generator.statements_before_cgo_call.append('var %s %s' % (
      ret.go_return_name, ret.go_return_type))
    generator.statements_after_cgo_call.append('_go_%s_ = C.GoString((*C.char)(unsafe.Pointer(%s)))'
        % (ret.go_return_name, ret.go_return_name))
    ret.go_return_name = '_go_%s_' % ret.go_return_name
    ret.go_return_type = 'string'

def map_boolean_parameters(parser, generator, function, klass):
  for param in generator.go_parameters:
    if param.go_parameter_type != 'C.gboolean': continue
    generator.statements_before_cgo_call.extend([
      '_cgo_%s_ := (C.gboolean)(C.FALSE)' % param.go_parameter_name,
      'if %s { _cgo_%s_ = (C.gboolean)(C.TRUE) }' % (param.go_parameter_name, param.go_parameter_name),
      ])
    param.cgo_argument = '_cgo_%s_' % param.go_parameter_name
    param.go_parameter_type = 'bool'

def map_boolean_returns(parser, generator, function, klass):
  for ret in generator.go_returns:
    if ret.go_return_type != 'C.gboolean': continue
    generator.statements_before_cgo_call.append('var %s C.gboolean' % ret.go_return_name)
    generator.statements_after_cgo_call.append('_go_%s_ = %s == (C.gboolean)(C.TRUE)' 
        % (ret.go_return_name, ret.go_return_name))
    ret.go_return_name = '_go_%s_' % ret.go_return_name
    ret.go_return_type = 'bool'

def map_byte_array_parameters(parser, generator, function, klass):
  for param in generator.go_parameters:
    if param.gir_info.type.resolved != '<array>': continue
    if param.gir_info.type.ctype != 'guint8*': continue
    if param.gir_info.type.element_type.ctype != 'guint8': continue
    generator.statements_before_cgo_call.extend([
      '_cstring_%s_ := C.CString(string(%s))' % (param.go_parameter_name, param.go_parameter_name),
      'defer C.free(unsafe.Pointer(_cstring_%s_))' % (param.go_parameter_name),
      '_cgo_%s_ := (*C.guint8)(unsafe.Pointer(_cstring_%s_))' % (param.go_parameter_name, param.go_parameter_name),
    ])
    param.go_parameter_type = '[]byte'
    param.cgo_argument = '_cgo_%s_' % param.go_parameter_name

def map_byte_array_returns(parser, generator, function, klass):
  for ret in generator.go_returns:
    if not ret.gir_info: continue
    if ret.gir_info.type.resolved != '<array>': continue
    if ret.gir_info.type.ctype != 'guchar*': continue
    if ret.gir_info.type.element_type.ctype != 'guchar': continue
    generator.statements_before_cgo_call.append(
      'var %s *C.guchar' % ret.go_return_name)
    generator.statements_after_cgo_call.append(
      '_go_%s_ = C.GoBytes(unsafe.Pointer(%s), C.int(C.strlen((*C.char)(unsafe.Pointer(%s)))))' % (
        ret.go_return_name,
        ret.go_return_name,
        ret.go_return_name,
        ))
    ret.go_return_name = '_go_%s_' % ret.go_return_name
    ret.go_return_type = '[]byte'

def map_enum_parameters(parser, generator, function, klass):
  for param in generator.go_parameters:
    if param.gir_info.type.ctype in parser.translator.enum_types:
      generator.statements_before_cgo_call.append(
        '_cgo_%s_ := (%s)(%s)' % (
          param.go_parameter_name,
          param.go_parameter_type,
          param.go_parameter_name,
          ))
      param.go_parameter_type = 'int'
      param.cgo_argument = '_cgo_%s_' % param.go_parameter_name
