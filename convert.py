from common import *

def is_go_word(w): # neither c keyword
  return w in set([
  # keywords
  'func', 'interface', 'select', 'defer',
  'go', 'map', 'chan', 'package', 'fallthrough',
  'range', 'type', 'import', 'var',
  # builtins
  'append', 'close', 'delete', 'panic',
  'recover', 'bool', 'byte', 'complex128',
  'complex64', 'error', 'float32', 'float64',
  'int', 'int16', 'int32', 'int64', 'int8',
  'rune', 'string', 'uint', 'uint16', 'uint32',
  'uint64', 'uint8', 'uintptr',
  'cap', 'copy', 'len',
    ])

def convert_parameters(parameters):
  not_implement = False
  need_wrapper = False
  ret = []
  for i, param in enumerate(parameters):
    param_info = Dict()
    name = param.argname
    if is_go_word(name):
      name += '_'
    transfer = param.transfer != 'none'
    c_type = param.type.ctype
    if c_type == '<varargs>':
      not_implement = True
    else:
      if name is None:
        name = 'arg_%d' % i
      convert_to_go_type(c_type, param_info)
      if param_info.cast_c_type:
        need_wrapper = True
      param_info.name = name
      param_info.transfer = transfer
      param_info.c_type = c_type
      ret.append(param_info)
  return ret, not_implement, need_wrapper

def convert_func_name(s):
  words = s.split('_')
  words = [w.capitalize() for w in words]
  return ''.join(words)

def convert_to_go_type(s, param_info):
  s = s.replace('volatile ', '') 
  cast_c_type = None
  cast_go_type = None
  if s.startswith('const '):
    cast_c_type = 'void*'
    cast_go_type = 'unsafe.Pointer'
    s = s.replace('const ', '')
  if s.endswith('**'):
    cast_c_type = 'void*'
    cast_go_type = 'unsafe.Pointer'
    s = 'void*'
  if s == 'long double':
    cast_c_type = 'double' #BUG will lose precision
    cast_go_type = 'C.double'
    s = 'double'
  elif s == 'va_list':
    cast_c_type = 'va_list_wrap'
    param_info.c_value_func = lambda param: '%s.v' % param.name
  s = 'C.' + s
  if s.endswith('*'):
    s = '*' + s[:-1]
  param_info.go_type = s
  param_info.cast_c_type = cast_c_type
  param_info.cast_go_type = cast_go_type
