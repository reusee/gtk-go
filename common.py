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
