from common import *

mappings = Dict()

def map_gchar(param):
  code = []
  mapped_cstr_name = '_cstr_' + param.name
  mapped_gstr_name = '_gstr_' + param.name
  code.append('\t%s := unsafe.Pointer(C.CString(%s))\n' % (mapped_cstr_name, param.name))
  if not param.transfer: # free it
    code.append('\tdefer C.free(%s)\n' % mapped_cstr_name)
  code.append('\t%s := (*C.gchar)(unsafe.Pointer(%s))\n' % (mapped_gstr_name, mapped_cstr_name))
  return ''.join(code)
mappings['*C.gchar'] = Dict({
  'mapped_type': 'string',
  'mapped_name_func': lambda param: '_gstr_' + param.name,
  'mapping_code_func': map_gchar,
  'return_wrap_head': 'C.GoString((*C.char)(',
  'return_wrap_tail': '))',
})

mappings['unsafe.Pointer'] = Dict({
  'mapped_type': 'unsafe.Pointer',
  'mapped_name_func': lambda param: param.name,
  'mapping_code_func': lambda param: '',
  'return_wrap_head': 'unsafe.Pointer(',
  'return_wrap_tail': ')',
})
