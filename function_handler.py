from function_generator import *
from common import *

def handleFunction(parser, function, klass = None):
  generator = FunctionGenerator()

  processors = [
      debug,
      check_skip,
      collect_c_func_info,
      collect_go_func_info,
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
  generator.c_func_return_type = convert_to_cgo_capatible_type(lib_func_spec.return_type)
  if generator.c_func_return_type != lib_func_spec.return_type:
    generator.has_c_func = True

  # has_c_func, c_parameter_types
  for i, arg_type in enumerate(lib_func_spec.arg_types):
    if function.is_method and i == 0: # use class type instead of spec type
      t = klass.ctype + ' *'
    else:
      t = convert_to_cgo_capatible_type(arg_type)
    if t != arg_type:
      generator.has_c_func = True
    generator.c_parameter_types.append(t)

  # c_parameter_names
  if klass and function.is_method: # method_function
    generator.c_parameter_names.append(generator.receiver_name)
  for i, param in enumerate(function.parameters): # function.parameters does not have _self_ and error 
    generator.c_parameter_names.append(param.argname)
  if function.throws:
    generator.c_parameter_names.append('_error_')

  # c_arguments
  assert len(generator.c_parameter_names) == len(generator.c_parameter_types)
  for i, name in enumerate(generator.c_parameter_names):
    if generator.c_parameter_types[i] != lib_func_spec.arg_types[i]:
      generator.c_arguments.append('(%s)(%s)' % (lib_func_spec.arg_types[i], name))
    else:
      generator.c_arguments.append(name)

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
    generator.receiver_type = '*' + klass.gi_name.split('.')[-1]

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
    generator.go_return_names.append('_return_')
    generator.go_return_types.append(convert_to_cgo_type(generator.c_func_return_type))

  # go parameter names and types
  types = generator.c_parameter_types
  if function.is_method:
    types = types[1:] # skip the _self_
  for i, param in enumerate(function.parameters):
    name = param.argname
    if is_go_word(name):
      name += '_'
    if param.direction == 'in':
      generator.go_parameter_names.append(name)
      generator.go_parameter_types.append(convert_to_cgo_type(types[i]))
    elif param.direction == 'out':
      generator.go_return_names.append(name)
      generator.go_return_types.append(convert_to_cgo_type(types[i]))
    generator.cgo_arguments.append(name)
  if function.throws:
    generator.go_return_names.append('_error_')
    generator.go_return_types.append('unsafe.Pointer')

  # cgo call
  generator.cgo_return_lvalue = '_return_'
  generator.cgo_func_name = 'C.' + generator.c_func_name
  if function.is_method:
    generator.cgo_arguments.insert(0, '(%s)(%s)' % (
      convert_to_cgo_type(generator.c_parameter_types[0]),
      generator.receiver_name))
  if function.throws:
    generator.cgo_arguments.append('_error_')

def convert_to_cgo_type(c_type):
  c_type = c_type.replace('volatile', '')
  if c_type == 'void *':
    return 'unsafe.Pointer'
  cgo_type = 'C.' + c_type
  if c_type.endswith('*'):
    cgo_type = '*' + cgo_type[:-1]
  return cgo_type.strip()
