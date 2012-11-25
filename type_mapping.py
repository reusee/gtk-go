from common import *

mappings = Dict()

mappings['unsafe.Pointer'] = Dict({
  'mapped_type': 'unsafe.Pointer',
  'mapped_name_func': lambda param: param.name,
  'mapping_code_func': lambda param: '',
  'to_go_type_code_head': 'unsafe.Pointer(',
  'to_go_type_code_tail': ')',
})
mappings['*C.void'] = mappings['unsafe.Pointer']

# glib basic types

def map_bool(param):
  return '''\
\t%s := C._false()
\tif %s { %s = C._true() }
''' % (
    '_gbool_' + param.name,
    param.name,
    '_gbool_' + param.name,
    )
mappings['C.gboolean'] = Dict({
  'mapped_type': 'bool',
  'mapped_name_func': lambda param: '_gbool_' + param.name,
  'mapping_code_func': map_bool,
  'to_go_type_func': 'gboolean2bool',
  'to_go_type_func_code': '''\
func gboolean2bool(b C.gboolean) bool {
  return b == C._true()
}''',
})

mappings['C.gpointer'] = Dict({
  'mapped_type': 'unsafe.Pointer',
  'mapped_name_func': lambda param: '_gpointer_' + param.name,
  'mapping_code_func': lambda param: '\t%s := (C.gpointer)(%s)\n' % (
    '_gpointer_' + param.name, param.name),
  'to_go_type_code_head': 'unsafe.Pointer(',
  'to_go_type_code_tail': ')',
})

mappings['C.gconstpointer'] = Dict({
  'mapped_type': 'unsafe.Pointer',
  'mapped_name_func': lambda param: '_gpointer_' + param.name,
  'mapping_code_func': lambda param: '\t%s := (C.gconstpointer)(%s)\n' % (
    '_gpointer_' + param.name, param.name),
  'to_go_type_code_head': 'unsafe.Pointer(',
  'to_go_type_code_tail': ')',
})

def map_gcharp(param):
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
  'mapping_code_func': map_gcharp,
  'to_go_type_func': 'gcharp2string',
  'to_go_type_func_code': '''\
func gcharp2string(str *C.gchar) string {
  return C.GoString((*C.char)(str))
}''',
})

def map_gucharp(param):
  code = []
  mapped_cstr_name = '_custr_' + param.name
  mapped_gstr_name = '_gustr_' + param.name
  code.append('\t%s := unsafe.Pointer(C.CString(string(%s)))\n' % (mapped_cstr_name, param.name))
  if not param.transfer: # free it
    code.append('\tdefer C.free(%s)\n' % mapped_cstr_name)
  code.append('\t%s := (*C.guchar)(unsafe.Pointer(%s))\n' % (mapped_gstr_name, mapped_cstr_name))
  return ''.join(code)
mappings['*C.guchar'] = Dict({
  'mapped_type': '[]byte',
  'mapped_name_func': lambda param: '_gustr_' + param.name,
  'mapping_code_func': map_gucharp,
  'to_go_type_func': 'gucharp2byteslice',
  'to_go_type_func_code': '''\
func gucharp2byteslice(str *C.guchar) []byte {
  return C.GoBytes(unsafe.Pointer(str), C.int(C.strlen((*C.char)(unsafe.Pointer(str)))))
}''',
})

def make_numeric_mapping(c_type, go_type):
  return Dict({
    'mapped_type': go_type,
    'mapped_name_func': lambda param: ('_%s_' % c_type) + param.name,
    'mapping_code_func': lambda param: '\t%s := C.%s(%s)\n' % (
      ('_%s_' % c_type) + param.name,
      c_type,
      param.name),
    'to_go_type_func': '%s2%s' % (
      c_type, go_type),
    'to_go_type_func_code': '''\
func %s2%s(i C.%s) %s {
  return %s(i)
}''' % (
  c_type, go_type,
  c_type, go_type,
  go_type,
  ),
  })

mappings['C.gchar'] = make_numeric_mapping('gchar', 'int8')
mappings['C.guchar'] = make_numeric_mapping('guchar', 'byte')

mappings['C.gint'] = make_numeric_mapping('gint', 'int')
mappings['C.guint'] = make_numeric_mapping('guint', 'uint')
mappings['C.gshort'] = make_numeric_mapping('gshort', 'int')
mappings['C.gushort'] = make_numeric_mapping('gushort', 'uint')
mappings['C.glong'] = make_numeric_mapping('glong', 'int64')
mappings['C.gulong'] = make_numeric_mapping('gulong', 'uint64')
mappings['C.gint8'] = make_numeric_mapping('gint8', 'int8')
mappings['C.guint8'] = make_numeric_mapping('guint8', 'uint8')
mappings['C.gint16'] = make_numeric_mapping('gint16', 'int16')
mappings['C.guint16'] = make_numeric_mapping('guint16', 'uint16')
mappings['C.gint32'] = make_numeric_mapping('gint32', 'int32')
mappings['C.guint32'] = make_numeric_mapping('guint32', 'uint32')
mappings['C.gint64'] = make_numeric_mapping('gint64', 'int64')
mappings['C.guint64'] = make_numeric_mapping('guint64', 'uint64')

mappings['C.gfloat'] = make_numeric_mapping('gfloat', 'float64')
mappings['C.gdouble'] = make_numeric_mapping('gdouble', 'float64')
mappings['C.gsize'] = make_numeric_mapping('gsize', 'uint64')
mappings['C.gssize'] = make_numeric_mapping('gssize', 'int64')
mappings['C.goffset'] = make_numeric_mapping('goffset', 'int64')

mappings['C.gintptr'] = make_numeric_mapping('gintptr', 'int64')
mappings['C.guintptr'] = make_numeric_mapping('guintptr', 'uint64')

def make_numeric_p_mapping(c_type, go_type):
  return Dict({
    'mapped_type': '*' + go_type,
    'mapped_name_func': lambda param: ('_cp_%s_' % c_type) + param.name,
    'mapping_code_func': lambda param: '''\
\t%s := C.%s(*%s)
\t%s := (*C.%s)(&%s)
''' % (
      ('_c_%s_' % c_type) + param.name,
      c_type,
      param.name,
      ('_cp_%s_' % c_type) + param.name,
      c_type,
      ('_c_%s_' % c_type) + param.name,
      ),
    'to_go_type_func': '%sp2%sp' % (
      c_type, go_type),
    'to_go_type_func_code': '''\
func %sp2%sp(p *C.%s) *%s {
  i := %s(*p)
  return &i
}''' % (
  c_type, go_type,
  c_type, go_type,
  go_type,
  ),
  })

mappings['*C.gint'] = make_numeric_p_mapping('gint', 'int')
mappings['*C.guint'] = make_numeric_p_mapping('guint', 'uint')
mappings['*C.gshort'] = make_numeric_p_mapping('gshort', 'int')
mappings['*C.gushort'] = make_numeric_p_mapping('gushort', 'uint')
mappings['*C.glong'] = make_numeric_p_mapping('glong', 'int64')
mappings['*C.gulong'] = make_numeric_p_mapping('gulong', 'uint64')
mappings['*C.gint8'] = make_numeric_p_mapping('gint8', 'int8')
mappings['*C.guint8'] = make_numeric_p_mapping('guint8', 'uint8')
mappings['*C.gint16'] = make_numeric_p_mapping('gint16', 'int16')
mappings['*C.guint16'] = make_numeric_p_mapping('guint16', 'uint16')
mappings['*C.gint32'] = make_numeric_p_mapping('gint32', 'int32')
mappings['*C.guint32'] = make_numeric_p_mapping('guint32', 'uint32')
mappings['*C.gint64'] = make_numeric_p_mapping('gint64', 'int64')
mappings['*C.guint64'] = make_numeric_p_mapping('guint64', 'uint64')

mappings['*C.gfloat'] = make_numeric_p_mapping('gfloat', 'float64')
mappings['*C.gdouble'] = make_numeric_p_mapping('gdouble', 'float64')
mappings['*C.gsize'] = make_numeric_p_mapping('gsize', 'uint64')
mappings['*C.gssize'] = make_numeric_p_mapping('gssize', 'int64')
mappings['*C.goffset'] = make_numeric_p_mapping('goffset', 'int64')

mappings['*C.gintptr'] = make_numeric_p_mapping('gintptr', 'int64')
mappings['*C.guintptr'] = make_numeric_p_mapping('guintptr', 'uint64')

# c types

mappings['C.double'] = make_numeric_mapping('double', 'float64')

#mappings['C.va_list'] = Dict({
#  'help_code': '''\
#typedef struct va_list_wrap {
#  va_list v;
#} va_list_wrap;
#''',
#  'mapped_type': 'C.va_list',
#  'mapped_name_func': lambda param: '_wrapped_' + param.name,
#  'mapping_code_func': lambda param: '''\
#\tvar _wrapped_%s C.va_list_wrap
#\t_wrapped_%s.v = %s
#''' % (
#    param.name, param.name, param.name,
#  ),
#})
