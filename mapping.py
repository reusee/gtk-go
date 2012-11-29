class Mapping:
  def __init__(self):
    self.cgo_type = None
    self.go_type = None

    self.param_mapping_code = None
    self.return_mapping_code = None

PARAM_MAPPINGS = {}

m = Mapping()
m.cgo_type = '*C.gchar'
m.go_type = 'string'
m.param_mapping_code = lambda param: '''\
\t%s := (*C.gchar)(unsafe.Pointer(C.CString(%s)))
''' % (param.mapped_cgo_name, param.name)
PARAM_MAPPINGS[m.cgo_type] = m

RETURN_MAPPINGS = {}

m = Mapping()
m.cgo_type = 'C.gboolean'
m.go_type = 'bool'
m.param_mapping_code = lambda param: '\tvar _cgo_of_%s_ C.gboolean\n' % param.name
m.return_mapping_code = lambda param: '\t%s = %s == C.glibtrue()\n' % (param.name, param.mapped_cgo_name)
RETURN_MAPPINGS[m.cgo_type] = m

def make_numeric_return_mapping(cgo_type, go_type):
  m = Mapping()
  m.cgo_type = cgo_type
  m.go_type = go_type
  m.param_mapping_code = lambda param: '\tvar _cgo_of_%s_ %s\n' % (param.name, param.go_type[1:])
  m.return_mapping_code = lambda param: '\t%s = %s(%s)\n' % (param.name, go_type, param.mapped_cgo_name)
  RETURN_MAPPINGS[m.cgo_type] = m

make_numeric_return_mapping('C.gchar', 'int8')
make_numeric_return_mapping('C.guchar', 'byte')

make_numeric_return_mapping('C.gint', 'int')
make_numeric_return_mapping('C.guint', 'uint')
make_numeric_return_mapping('C.gshort', 'int')
make_numeric_return_mapping('C.gushort', 'uint')
make_numeric_return_mapping('C.glong', 'int64')
make_numeric_return_mapping('C.gulong', 'uint64')
make_numeric_return_mapping('C.gint8', 'int8')
make_numeric_return_mapping('C.guint8', 'uint8')
make_numeric_return_mapping('C.gint16', 'int16')
make_numeric_return_mapping('C.guint16', 'uint16')
make_numeric_return_mapping('C.gint32', 'int32')
make_numeric_return_mapping('C.guint32', 'uint32')
make_numeric_return_mapping('C.gint64', 'int64')
make_numeric_return_mapping('C.guint64', 'uint64')

make_numeric_return_mapping('C.gfloat', 'float64')
make_numeric_return_mapping('C.gdouble', 'float64')
make_numeric_return_mapping('C.gsize', 'uint64')
make_numeric_return_mapping('C.gssize', 'int64')
make_numeric_return_mapping('C.goffset', 'int64')

make_numeric_return_mapping('C.gintptr', 'int64')
make_numeric_return_mapping('C.guintptr', 'uint64')
