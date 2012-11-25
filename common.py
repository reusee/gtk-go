class _Dict(dict):
  __getattr__ = dict.__getitem__
  __setattr__ = dict.__setitem__
  def __setitem__(self, k, v):
    dict.__setitem__(self, k, v)
    self.__setattr__(k, v)

def Dict(d = None):
  if d is None:
    return _Dict()
  else:
    ret = _Dict()
    ret.update(d)
    return ret

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
