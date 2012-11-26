class Dict(dict):
  def __getattr__(self, k):
    return dict.get(self, k, None)
  def __getitem__(self, k):
    return dict.get(self, k, None)
  def __setattr__(self, k, v):
    dict.__setitem__(self, k, v)
    dict.__setattr__(self, k, v)
  def __setitem__(self, k, v):
    dict.__setitem__(self, k, v)
    dict.__setattr__(self, k, v)

def test_dict():
  d = Dict()
  d.foo = 'foo'
  assert d['foo'] == 'foo'
  assert d.foo == 'foo'
  d['bar'] = 'bar'
  assert d.bar == 'bar'
  assert d['bar'] == 'bar'
  assert d.Foo == None
  assert d['Bar'] == None
  d = Dict({
    'foo': 'foo',
    'bar': 'bar',
  })
  assert d.foo == 'foo'
  assert d['foo'] == 'foo'
  assert d.bar == 'bar'
  assert d['bar'] == 'bar'
  assert d.get('FOO', '') == ''

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

if __name__ == '__main__':
  test_dict()
