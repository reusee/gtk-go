from common import *
from giscanner import ast

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
  need_helper = False
  ret = []
  for i, param in enumerate(parameters):
    name = param.argname
    print '>>', name
    param_info = Dict({
      'transfer': param.transfer != 'none',
      'type': get_type_info(param),
    })
    if is_go_word(name):
      name += '_'
    if param_info.type.c_type == '<varargs>':
      not_implement = True
    else:
      if name is None:
        name = 'arg_%d' % i
      if param_info.type.need_helper:
        need_helper = True
      param_info.name = name
      ret.append(param_info)

  return ret, not_implement, need_helper

def convert_func_name(s):
  words = s.split('_')
  words = [w.capitalize() for w in words]
  return ''.join(words)

def get_type_info(param):
  t = param.type
  suffix = ''
  if isinstance(param, ast.Parameter) and param.direction in (
      ast.PARAM_DIRECTION_OUT, ast.PARAM_DIRECTION_INOUT):
    suffix = '*'
  c_type = t.ctype
  print suffix
  if t.is_equiv((ast.TYPE_STRING, ast.TYPE_FILENAME)) and param.transfer == ast.PARAM_TRANSFER_NONE:
    print '>'
    c_type = 'const gchar*' + suffix

  ret = Dict()
  need_helper = False

  c_original_type = None

  if isinstance(t, ast.Array) and isinstance(param, ast.Parameter):
    if t.array_type == ast.Array.C:
      if t.element_type.is_equiv((ast.TYPE_STRING, ast.TYPE_FILENAME)):
        print '>>'
        c_original_type = 'const gchar**'
      elif t.element_type.is_equiv((
        ast.TYPE_BOOLEAN,
        ast.TYPE_DOUBLE,
        ast.TYPE_INT,
        )):
        c_type = c_type + '*'
        c_original_type = c_type
    print '=' * 20, 'ARRAY', t.ctype, c_type, t.element_type, t.resolved

  go_type = None # use in go function parameter
  cgo_cast_type = None # use in cgo function call
  c_helper_param_type = c_type # use in c helper function parameter

  go_type = c_type
  go_type = go_type.replace('volatile ', '')
  if go_type.startswith('const '): # use helper
    need_helper = True
    go_type = go_type.replace('const ', '')
    cgo_cast_type = 'unsafe.Pointer'
    c_helper_param_type = 'void*'
  if go_type.endswith('**'):
    need_helper = True
    go_type = 'unsafe.Pointer'
    c_helper_param_type = 'void*'
  if go_type == 'long double': #BUG will lose precision
    need_helper = True
    go_type = 'double'
    c_helper_param_type = 'double'
  if go_type == 'va_list':
    need_helper = True
    c_helper_param_type = 'va_list_wrap'
    ret.c_helper_value_func = lambda param: '%s.v' % param.name
    #TODO convert va_list to va_list_wrap
  go_type = 'C' + go_type
  if go_type.endswith('*'):
    go_type = '*' + go_type[:-1]

  ret.need_helper = need_helper
  ret.go_type = go_type
  ret.cgo_cast_type = cgo_cast_type
  ret.c_helper_param_type = c_helper_param_type
  ret.c_original_type = c_original_type
  ret.c_type = c_type
  return ret
