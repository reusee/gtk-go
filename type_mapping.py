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
  'to_go_type_func': 'gcharp2string',
  'to_go_type_func_code': '''\
func gcharp2string(str *C.gchar) string {
  return C.GoString((*C.char)(str))
}''',
})

mappings['unsafe.Pointer'] = Dict({
  'mapped_type': 'unsafe.Pointer',
  'mapped_name_func': lambda param: param.name,
  'mapping_code_func': lambda param: '',
  'to_go_type_code_head': 'unsafe.Pointer(',
  'to_go_type_code_tail': ')',
})
