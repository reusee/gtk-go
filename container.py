from giscanner import ast
from common import *

class Function:
  def __init__(self):
    self.name = None
    self.c_name = None
    self.go_name = None

    self.is_method = False
    self.c_class = None

    self.skip = False

    self.return_value = None
    self.parameters = None
    self.c_parameters = None
    self.extra_returns = None

    self.need_helper = False

class Value:
  def __init__(self, gi_container = None):
    self.need_helper = False
    self.not_implement = False
    self.mapping = None
    self.is_basic_out_param = False
    self.caller_allocates = False

    if gi_container is None: return

    self.transfer = gi_container.transfer != 'none'
    self.direction = gi_container.direction

    if isinstance(gi_container, ast.Parameter):
      self.caller_allocates = gi_container.caller_allocates
      self.name = gi_container.argname
      if is_go_word(self.name):
        self.name += '_'
      if self.name is None:
        self.name = self.GiveName()
    elif isinstance(gi_container, ast.Return):
      self.name = '_return_'

    self.ParseTypeInfo(gi_container)

  def ParseTypeInfo(self, gi_container):
    self.c_type = gi_container.type.ctype

    if 'out' in gi_container.direction and isinstance(gi_container, ast.Parameter):
      self.is_basic_out_param = gi_container.type.is_equiv(ast.BASIC_GIR_TYPES)

    if isinstance(gi_container.type, ast.Array) and isinstance(gi_container, ast.Parameter):
      self.not_implement = True
    if self.c_type in ['<varargs>', 'va_list']:
      self.not_implement = True

    self.c_type = self.c_type.replace('volatile ', '')
    self.go_type = self.c_type

    if self.c_type.startswith('const '): # cgo has no const types
      self.need_helper = True
      self.c_type = self.c_type.replace('const ', '')
      self.go_type = self.c_type

    if '**' in self.c_type: # cgo has no pointer of pointer type
      self.need_helper = True
      self.c_type = 'void*'
      self.go_type = 'unsafe.Pointer'

    if self.c_type == 'long double': # go has no long double type, use double instead, buf will lose precision
      self.need_helper = True
      self.c_type = 'double'
      self.go_type = self.c_type

    if self.go_type != 'unsafe.Pointer':
      self.go_type = 'C.' + self.go_type
    if self.go_type.endswith('*'):
      self.go_type = '*' + self.go_type[:-1]

    self.out_go_type = self.go_type # used in out param
    if self.out_go_type.startswith('*'):
      self.out_go_type = self.out_go_type[1:]

  @property
  def mapped_go_type(self):
    if self.mapping:
      return self.mapping.go_type
    return self.go_type

  @property
  def mapped_out_go_type(self):
    if self.mapping:
      return self.out_go_type
    return self.go_type

  @property
  def mapped_cgo_name(self):
    if self.mapping:
      return '_cgo_of_%s_' % self.name
    return self.name

  _name_serial_ = 0
  @classmethod
  def GiveName(cls):
    cls._name_serial_ += 1
    return 'arg_%d' % cls._name_serial_

  @classmethod
  def selfValue(cls, c_class):
    value = Value()
    value.need_helper = True
    value.transfer = False
    value.direction = 'in'
    value.name = '_self_'
    value.c_type = c_class + '*'
    value.go_type = '*C.' + c_class
    value.out_go_type = 'C.' + c_class
    return value

  @classmethod
  def errValue(cls):
    value = Value()
    value.need_helper = True
    value.transfer = False
    value.direction = 'out'
    value.name = '_error_'
    value.c_type = 'void*'
    value.go_type = 'unsafe.Pointer'
    value.out_go_type = 'unsafe.Pointer'
    return value
