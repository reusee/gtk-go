class FunctionGenerator:
  def __init__(self):
    self.data = {}
    self.skip = False

    # receiver info
    self.has_receiver = False
    self.receiver_name = '_self_'
    self.receiver_type = None

    self.go_func_name = None
    self.go_parameter_names = []
    self.go_parameter_types = []
    self.go_return_names = []
    self.go_return_types = []

    self.statements_before_cgo_call = []

    self.cgo_has_return = False
    self.cgo_return_lvalue = None
    self.cgo_func_name = None
    self.cgo_arguments = []

    self.statements_after_cgo_call = []

    # c func info
    self.has_c_func = False
    self.c_func_return_type = None
    self.c_func_name = None
    self.c_parameter_names = []
    self.c_parameter_types = []
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
    receiver_expression = ('(%s %s) ' % (self.receiver_name, self.receiver_type)) if self.has_receiver else '',
    go_func_name = self.go_func_name,
    parameters = ', '.join('%s %s' % (param[0], param[1])
      for param in zip(self.go_parameter_names, self.go_parameter_types)),
    returns = ', '.join('%s %s' % (ret[0], ret[1])
      for ret in zip(self.go_return_names, self.go_return_types)),
    statements_before_cgo_call = ''.join('\t%s\n' % statement
      for statement in self.statements_before_cgo_call),
    cgo_return_lvalue = ('%s = ' % self.cgo_return_lvalue) if self.cgo_has_return else '',
    cgo_func_name = self.cgo_func_name,
    cgo_arguments = ', '.join(self.cgo_arguments),
    statements_after_cgo_call = ''.join('\t%s\n' % statement
      for statement in self.statements_after_cgo_call),
    )

  def generate_c_func(self):
    return '''\
{return_type} {function_name}({parameters}) {{
\t{return_or_not}({return_type}){lib_func_name}({arguments});
}}'''.format(
    return_type = self.c_func_return_type,
    function_name = self.c_func_name,
    parameters = ', '.join('%s %s' % (param[0], param[1])
      for param in zip(self.c_parameter_types, self.c_parameter_names)),
    return_or_not = 'return ' if self.c_has_return else '',
    lib_func_name = self.lib_func_name,
    arguments = ', '.join(argument
      for argument in self.c_arguments),
    )
