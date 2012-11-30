class Value:
  def __init__(self):
    self.gir_param_info = None

    self.c_return_type = None

    self.c_parameter_name = None
    self.c_parameter_type = None
    self.c_argument = None

    self.go_parameter_type = None
    self.go_parameter_name = None

    self.go_return_name = None
    self.go_return_type = None

    self.receiver_name = '_self_'
    self.receiver_type = None

class FunctionGenerator:
  def __init__(self):
    self.data = {}
    self.skip = False

    self.has_receiver = False
    self.receiver = None

    self.go_func_name = None
    self.go_parameters = []
    self.go_returns = []

    self.statements_before_cgo_call = []

    self.cgo_has_return = False
    self.cgo_return_lvalue = None
    self.cgo_func_name = None
    self.cgo_arguments = []

    self.statements_after_cgo_call = []

    self.has_c_func = False
    self.c_return_value = None
    self.c_func_name = None
    self.c_parameters = []
    self.lib_func_spec = None

    self.c_has_return = False
    self.lib_func_name = None
    self.c_arguments = []

  def generate_go_func(self):
    return '''\
func {receiver_expression}{go_func_name}({parameters}) ({returns}) {{
{statements_before_cgo_call}\t{cgo_return_lvalue}{cgo_func_name}({cgo_arguments})
{statements_after_cgo_call}\treturn
}}
'''.format(
    receiver_expression = ('(%s %s) ' % (
      self.receiver.receiver_name, self.receiver.receiver_type)) if self.has_receiver else '',
    go_func_name = self.go_func_name,
    parameters = ', '.join('%s %s' % (param.go_parameter_name, param.go_parameter_type)
      for param in self.go_parameters),
    returns = ', '.join('%s %s' % (ret.go_return_name, ret.go_return_type)
      for ret in self.go_returns),
    statements_before_cgo_call = ''.join('\t%s\n' % statement
      for statement in self.statements_before_cgo_call),
    cgo_return_lvalue = ('%s = ' % self.cgo_return_lvalue) if self.cgo_has_return else '',
    cgo_func_name = self.cgo_func_name,
    cgo_arguments = ', '.join(x.cgo_argument
      for x in self.cgo_arguments),
    statements_after_cgo_call = ''.join('\t%s\n' % statement
      for statement in self.statements_after_cgo_call),
    )

  def generate_c_func(self):
    return '''\
{return_type} {function_name}({parameters}) {{
\t{return_or_not}({return_type}){lib_func_name}({arguments});
}}'''.format(
    return_type = self.c_return_value.c_return_type,
    function_name = self.c_func_name,
    parameters = ', '.join('%s %s' % (param.c_parameter_type, param.c_parameter_name)
      for param in self.c_parameters),
    return_or_not = 'return ' if self.c_has_return else '',
    lib_func_name = self.lib_func_name,
    arguments = ', '.join(argument.c_argument
      for argument in self.c_arguments),
    )
