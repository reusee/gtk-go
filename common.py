class Dict(dict):
  __getattr__ = dict.__getitem__
  __setattr__ = dict.__setattr__
