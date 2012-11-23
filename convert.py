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
    name = param.argname
    if is_go_word(name):
      name += '_'
    transfer = param.transfer != 'none'
    c_type = param.type.ctype
    if c_type == '<varargs>':
      not_implement = True
    elif c_type == 'va_list':
      not_implement = True
    elif 'long double' in c_type:
      not_implement = True
    else:
      if name is None:
        name = 'arg_%d' % i
      go_type, need_cast = convert_to_go_type(param.type.ctype)
      if need_cast:
        need_wrapper = True
      ret.append(Param(name, c_type, go_type, need_cast, transfer))
  return ret, not_implement, need_wrapper

def convert_func_name(s):
  words = s.split('_')
  words = [w.capitalize() for w in words]
  return ''.join(words)

def convert_to_go_type(s):
  s = s.replace('volatile ', '') 
  need_cast = False
  if s.startswith('const '):
    need_cast = True
    s = s.replace('const ', '')
  if s == 'long double':
    s = 'longdouble'
  if s.endswith('**'):
    need_cast = True
    s = 'unsafe.Pointer'
  else:
    s = 'C.' + s
  if s.endswith('*'):
    s = '*' + s[:-1]
  return s, need_cast
