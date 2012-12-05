Strip_prefix_from_const = True

Compile_error_c_symbols = [
  'GIConv',
  'GTestLogBuffer',
  'GTestLogMsg',

  'g_atomic_int_add',
  'g_atomic_int_and',
  'g_atomic_int_compare_and_exchange',
  'g_atomic_int_dec_and_test',
  'g_atomic_int_get',
  'g_atomic_int_inc',
  'g_atomic_int_or',
  'g_atomic_int_set',
  'g_atomic_int_xor',
  'g_atomic_pointer_add',
  'g_atomic_pointer_and',
  'g_atomic_pointer_compare_and_exchange',
  'g_atomic_pointer_get',
  'g_atomic_pointer_or',
  'g_atomic_pointer_set',
  'g_atomic_pointer_xor',
  'g_clear_pointer',
  'g_once_init_enter',
  'g_once_init_leave',
  'g_pointer_bit_lock',
  'g_pointer_bit_trylock',
  'g_pointer_bit_unlock',

  'g_date_to_struct_tm',

  'g_main_context_query',

  'g_variant_type_checked_',
]

Not_exported_c_macros = [
  'G_WIN32_MSG_HANDLE',

  'G_SQRT2',
  'G_PI_4',
  'G_PI_2',
  'G_PI',
  'G_LOG_DOMAIN',
  'G_LOG_2_BASE_10',
  'G_LN2',
  'G_LN10',
  'G_E',
]

Deprecated_c_symbols = [
  'g_slice_get_config_state',
  'g_slice_get_config',
  'g_slice_set_config',
  'g_assert_warning',
  'g_variant_get_gtype',
]
