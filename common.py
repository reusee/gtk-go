from collections import namedtuple

class Dict(dict):
  __getattr__ = dict.__getitem__
  __setattr__ = dict.__setattr__

Param = namedtuple('Param', ['name', 'c_type', 'go_type', 'cast_c_type', 'cast_go_type', 'transfer'])
