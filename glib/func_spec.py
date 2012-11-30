from collections import namedtuple
Spec = namedtuple('Spec', ['return_type', 'parameters'])
Param = namedtuple('Param', ['name', 'type'])
func_specs = {
  '__builtin_bswap32': Spec(
    return_type = 'uint32_t',
    parameters = [
      Param(
        type = 'uint32_t',
        name = 'x',
      ),
    ],
  ),
  '__builtin_bswap64': Spec(
    return_type = 'uint64_t',
    parameters = [
      Param(
        type = 'uint64_t',
        name = 'x',
      ),
    ],
  ),
  'clock': Spec(
    return_type = 'clock_t',
    parameters = [
    ],
  ),
  'time': Spec(
    return_type = 'time_t',
    parameters = [
      Param(
        type = 'time_t *',
        name = '__timer',
      ),
    ],
  ),
  'difftime': Spec(
    return_type = 'double',
    parameters = [
      Param(
        type = 'time_t',
        name = '__time1',
      ),
      Param(
        type = 'time_t',
        name = '__time0',
      ),
    ],
  ),
  'mktime': Spec(
    return_type = 'time_t',
    parameters = [
      Param(
        type = 'struct tm *',
        name = '__tp',
      ),
    ],
  ),
  'strftime': Spec(
    return_type = 'size_t',
    parameters = [
      Param(
        type = 'char *restrict',
        name = '__s',
      ),
      Param(
        type = 'size_t',
        name = '__maxsize',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
      Param(
        type = 'const struct tm *restrict',
        name = '__tp',
      ),
    ],
  ),
  'strftime_l': Spec(
    return_type = 'size_t',
    parameters = [
      Param(
        type = 'char *restrict',
        name = '__s',
      ),
      Param(
        type = 'size_t',
        name = '__maxsize',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
      Param(
        type = 'const struct tm *restrict',
        name = '__tp',
      ),
      Param(
        type = '__locale_t',
        name = '__loc',
      ),
    ],
  ),
  'gmtime': Spec(
    return_type = 'struct tm *',
    parameters = [
      Param(
        type = 'const time_t *',
        name = '__timer',
      ),
    ],
  ),
  'localtime': Spec(
    return_type = 'struct tm *',
    parameters = [
      Param(
        type = 'const time_t *',
        name = '__timer',
      ),
    ],
  ),
  'gmtime_r': Spec(
    return_type = 'struct tm *',
    parameters = [
      Param(
        type = 'const time_t *restrict',
        name = '__timer',
      ),
      Param(
        type = 'struct tm *restrict',
        name = '__tp',
      ),
    ],
  ),
  'localtime_r': Spec(
    return_type = 'struct tm *',
    parameters = [
      Param(
        type = 'const time_t *restrict',
        name = '__timer',
      ),
      Param(
        type = 'struct tm *restrict',
        name = '__tp',
      ),
    ],
  ),
  'asctime': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'const struct tm *',
        name = '__tp',
      ),
    ],
  ),
  'ctime': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'const time_t *',
        name = '__timer',
      ),
    ],
  ),
  'asctime_r': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'const struct tm *restrict',
        name = '__tp',
      ),
      Param(
        type = 'char *restrict',
        name = '__buf',
      ),
    ],
  ),
  'ctime_r': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'const time_t *restrict',
        name = '__timer',
      ),
      Param(
        type = 'char *restrict',
        name = '__buf',
      ),
    ],
  ),
  'tzset': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'stime': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const time_t *',
        name = '__when',
      ),
    ],
  ),
  'timegm': Spec(
    return_type = 'time_t',
    parameters = [
      Param(
        type = 'struct tm *',
        name = '__tp',
      ),
    ],
  ),
  'timelocal': Spec(
    return_type = 'time_t',
    parameters = [
      Param(
        type = 'struct tm *',
        name = '__tp',
      ),
    ],
  ),
  'dysize': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__year',
      ),
    ],
  ),
  'nanosleep': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const struct timespec *',
        name = '__requested_time',
      ),
      Param(
        type = 'struct timespec *',
        name = '__remaining',
      ),
    ],
  ),
  'clock_getres': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'clockid_t',
        name = '__clock_id',
      ),
      Param(
        type = 'struct timespec *',
        name = '__res',
      ),
    ],
  ),
  'clock_gettime': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'clockid_t',
        name = '__clock_id',
      ),
      Param(
        type = 'struct timespec *',
        name = '__tp',
      ),
    ],
  ),
  'clock_settime': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'clockid_t',
        name = '__clock_id',
      ),
      Param(
        type = 'const struct timespec *',
        name = '__tp',
      ),
    ],
  ),
  'clock_nanosleep': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'clockid_t',
        name = '__clock_id',
      ),
      Param(
        type = 'int',
        name = '__flags',
      ),
      Param(
        type = 'const struct timespec *',
        name = '__req',
      ),
      Param(
        type = 'struct timespec *',
        name = '__rem',
      ),
    ],
  ),
  'clock_getcpuclockid': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pid_t',
        name = '__pid',
      ),
      Param(
        type = 'clockid_t *',
        name = '__clock_id',
      ),
    ],
  ),
  'timer_create': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'clockid_t',
        name = '__clock_id',
      ),
      Param(
        type = 'struct sigevent *restrict',
        name = '__evp',
      ),
      Param(
        type = 'timer_t *restrict',
        name = '__timerid',
      ),
    ],
  ),
  'timer_delete': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'timer_t',
        name = '__timerid',
      ),
    ],
  ),
  'timer_settime': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'timer_t',
        name = '__timerid',
      ),
      Param(
        type = 'int',
        name = '__flags',
      ),
      Param(
        type = 'const struct itimerspec *restrict',
        name = '__value',
      ),
      Param(
        type = 'struct itimerspec *restrict',
        name = '__ovalue',
      ),
    ],
  ),
  'timer_gettime': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'timer_t',
        name = '__timerid',
      ),
      Param(
        type = 'struct itimerspec *',
        name = '__value',
      ),
    ],
  ),
  'timer_getoverrun': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'timer_t',
        name = '__timerid',
      ),
    ],
  ),
  'g_array_new': Spec(
    return_type = 'GArray *',
    parameters = [
      Param(
        type = 'gboolean',
        name = 'zero_terminated',
      ),
      Param(
        type = 'gboolean',
        name = 'clear_',
      ),
      Param(
        type = 'guint',
        name = 'element_size',
      ),
    ],
  ),
  'g_array_sized_new': Spec(
    return_type = 'GArray *',
    parameters = [
      Param(
        type = 'gboolean',
        name = 'zero_terminated',
      ),
      Param(
        type = 'gboolean',
        name = 'clear_',
      ),
      Param(
        type = 'guint',
        name = 'element_size',
      ),
      Param(
        type = 'guint',
        name = 'reserved_size',
      ),
    ],
  ),
  'g_array_free': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GArray *',
        name = 'array',
      ),
      Param(
        type = 'gboolean',
        name = 'free_segment',
      ),
    ],
  ),
  'g_array_ref': Spec(
    return_type = 'GArray *',
    parameters = [
      Param(
        type = 'GArray *',
        name = 'array',
      ),
    ],
  ),
  'g_array_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GArray *',
        name = 'array',
      ),
    ],
  ),
  'g_array_get_element_size': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GArray *',
        name = 'array',
      ),
    ],
  ),
  'g_array_append_vals': Spec(
    return_type = 'GArray *',
    parameters = [
      Param(
        type = 'GArray *',
        name = 'array',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
      Param(
        type = 'guint',
        name = 'len',
      ),
    ],
  ),
  'g_array_prepend_vals': Spec(
    return_type = 'GArray *',
    parameters = [
      Param(
        type = 'GArray *',
        name = 'array',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
      Param(
        type = 'guint',
        name = 'len',
      ),
    ],
  ),
  'g_array_insert_vals': Spec(
    return_type = 'GArray *',
    parameters = [
      Param(
        type = 'GArray *',
        name = 'array',
      ),
      Param(
        type = 'guint',
        name = 'index_',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
      Param(
        type = 'guint',
        name = 'len',
      ),
    ],
  ),
  'g_array_set_size': Spec(
    return_type = 'GArray *',
    parameters = [
      Param(
        type = 'GArray *',
        name = 'array',
      ),
      Param(
        type = 'guint',
        name = 'length',
      ),
    ],
  ),
  'g_array_remove_index': Spec(
    return_type = 'GArray *',
    parameters = [
      Param(
        type = 'GArray *',
        name = 'array',
      ),
      Param(
        type = 'guint',
        name = 'index_',
      ),
    ],
  ),
  'g_array_remove_index_fast': Spec(
    return_type = 'GArray *',
    parameters = [
      Param(
        type = 'GArray *',
        name = 'array',
      ),
      Param(
        type = 'guint',
        name = 'index_',
      ),
    ],
  ),
  'g_array_remove_range': Spec(
    return_type = 'GArray *',
    parameters = [
      Param(
        type = 'GArray *',
        name = 'array',
      ),
      Param(
        type = 'guint',
        name = 'index_',
      ),
      Param(
        type = 'guint',
        name = 'length',
      ),
    ],
  ),
  'g_array_sort': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GArray *',
        name = 'array',
      ),
      Param(
        type = 'GCompareFunc',
        name = 'compare_func',
      ),
    ],
  ),
  'g_array_sort_with_data': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GArray *',
        name = 'array',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'compare_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_array_set_clear_func': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GArray *',
        name = 'array',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'clear_func',
      ),
    ],
  ),
  'g_ptr_array_new': Spec(
    return_type = 'GPtrArray *',
    parameters = [
    ],
  ),
  'g_ptr_array_new_with_free_func': Spec(
    return_type = 'GPtrArray *',
    parameters = [
      Param(
        type = 'GDestroyNotify',
        name = 'element_free_func',
      ),
    ],
  ),
  'g_ptr_array_sized_new': Spec(
    return_type = 'GPtrArray *',
    parameters = [
      Param(
        type = 'guint',
        name = 'reserved_size',
      ),
    ],
  ),
  'g_ptr_array_new_full': Spec(
    return_type = 'GPtrArray *',
    parameters = [
      Param(
        type = 'guint',
        name = 'reserved_size',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'element_free_func',
      ),
    ],
  ),
  'g_ptr_array_free': Spec(
    return_type = 'gpointer *',
    parameters = [
      Param(
        type = 'GPtrArray *',
        name = 'array',
      ),
      Param(
        type = 'gboolean',
        name = 'free_seg',
      ),
    ],
  ),
  'g_ptr_array_ref': Spec(
    return_type = 'GPtrArray *',
    parameters = [
      Param(
        type = 'GPtrArray *',
        name = 'array',
      ),
    ],
  ),
  'g_ptr_array_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GPtrArray *',
        name = 'array',
      ),
    ],
  ),
  'g_ptr_array_set_free_func': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GPtrArray *',
        name = 'array',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'element_free_func',
      ),
    ],
  ),
  'g_ptr_array_set_size': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GPtrArray *',
        name = 'array',
      ),
      Param(
        type = 'gint',
        name = 'length',
      ),
    ],
  ),
  'g_ptr_array_remove_index': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GPtrArray *',
        name = 'array',
      ),
      Param(
        type = 'guint',
        name = 'index_',
      ),
    ],
  ),
  'g_ptr_array_remove_index_fast': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GPtrArray *',
        name = 'array',
      ),
      Param(
        type = 'guint',
        name = 'index_',
      ),
    ],
  ),
  'g_ptr_array_remove': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GPtrArray *',
        name = 'array',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_ptr_array_remove_fast': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GPtrArray *',
        name = 'array',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_ptr_array_remove_range': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GPtrArray *',
        name = 'array',
      ),
      Param(
        type = 'guint',
        name = 'index_',
      ),
      Param(
        type = 'guint',
        name = 'length',
      ),
    ],
  ),
  'g_ptr_array_add': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GPtrArray *',
        name = 'array',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_ptr_array_sort': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GPtrArray *',
        name = 'array',
      ),
      Param(
        type = 'GCompareFunc',
        name = 'compare_func',
      ),
    ],
  ),
  'g_ptr_array_sort_with_data': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GPtrArray *',
        name = 'array',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'compare_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_ptr_array_foreach': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GPtrArray *',
        name = 'array',
      ),
      Param(
        type = 'GFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_byte_array_new': Spec(
    return_type = 'GByteArray *',
    parameters = [
    ],
  ),
  'g_byte_array_new_take': Spec(
    return_type = 'GByteArray *',
    parameters = [
      Param(
        type = 'guint8 *',
        name = 'data',
      ),
      Param(
        type = 'gsize',
        name = 'len',
      ),
    ],
  ),
  'g_byte_array_sized_new': Spec(
    return_type = 'GByteArray *',
    parameters = [
      Param(
        type = 'guint',
        name = 'reserved_size',
      ),
    ],
  ),
  'g_byte_array_free': Spec(
    return_type = 'guint8 *',
    parameters = [
      Param(
        type = 'GByteArray *',
        name = 'array',
      ),
      Param(
        type = 'gboolean',
        name = 'free_segment',
      ),
    ],
  ),
  'g_byte_array_free_to_bytes': Spec(
    return_type = 'GBytes *',
    parameters = [
      Param(
        type = 'GByteArray *',
        name = 'array',
      ),
    ],
  ),
  'g_byte_array_ref': Spec(
    return_type = 'GByteArray *',
    parameters = [
      Param(
        type = 'GByteArray *',
        name = 'array',
      ),
    ],
  ),
  'g_byte_array_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GByteArray *',
        name = 'array',
      ),
    ],
  ),
  'g_byte_array_append': Spec(
    return_type = 'GByteArray *',
    parameters = [
      Param(
        type = 'GByteArray *',
        name = 'array',
      ),
      Param(
        type = 'const guint8 *',
        name = 'data',
      ),
      Param(
        type = 'guint',
        name = 'len',
      ),
    ],
  ),
  'g_byte_array_prepend': Spec(
    return_type = 'GByteArray *',
    parameters = [
      Param(
        type = 'GByteArray *',
        name = 'array',
      ),
      Param(
        type = 'const guint8 *',
        name = 'data',
      ),
      Param(
        type = 'guint',
        name = 'len',
      ),
    ],
  ),
  'g_byte_array_set_size': Spec(
    return_type = 'GByteArray *',
    parameters = [
      Param(
        type = 'GByteArray *',
        name = 'array',
      ),
      Param(
        type = 'guint',
        name = 'length',
      ),
    ],
  ),
  'g_byte_array_remove_index': Spec(
    return_type = 'GByteArray *',
    parameters = [
      Param(
        type = 'GByteArray *',
        name = 'array',
      ),
      Param(
        type = 'guint',
        name = 'index_',
      ),
    ],
  ),
  'g_byte_array_remove_index_fast': Spec(
    return_type = 'GByteArray *',
    parameters = [
      Param(
        type = 'GByteArray *',
        name = 'array',
      ),
      Param(
        type = 'guint',
        name = 'index_',
      ),
    ],
  ),
  'g_byte_array_remove_range': Spec(
    return_type = 'GByteArray *',
    parameters = [
      Param(
        type = 'GByteArray *',
        name = 'array',
      ),
      Param(
        type = 'guint',
        name = 'index_',
      ),
      Param(
        type = 'guint',
        name = 'length',
      ),
    ],
  ),
  'g_byte_array_sort': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GByteArray *',
        name = 'array',
      ),
      Param(
        type = 'GCompareFunc',
        name = 'compare_func',
      ),
    ],
  ),
  'g_byte_array_sort_with_data': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GByteArray *',
        name = 'array',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'compare_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_atomic_int_get': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'volatile gint *',
        name = 'atomic',
      ),
    ],
  ),
  'g_atomic_int_set': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'volatile gint *',
        name = 'atomic',
      ),
      Param(
        type = 'gint',
        name = 'newval',
      ),
    ],
  ),
  'g_atomic_int_inc': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'volatile gint *',
        name = 'atomic',
      ),
    ],
  ),
  'g_atomic_int_dec_and_test': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'volatile gint *',
        name = 'atomic',
      ),
    ],
  ),
  'g_atomic_int_compare_and_exchange': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'volatile gint *',
        name = 'atomic',
      ),
      Param(
        type = 'gint',
        name = 'oldval',
      ),
      Param(
        type = 'gint',
        name = 'newval',
      ),
    ],
  ),
  'g_atomic_int_add': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'volatile gint *',
        name = 'atomic',
      ),
      Param(
        type = 'gint',
        name = 'val',
      ),
    ],
  ),
  'g_atomic_int_and': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'volatile guint *',
        name = 'atomic',
      ),
      Param(
        type = 'guint',
        name = 'val',
      ),
    ],
  ),
  'g_atomic_int_or': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'volatile guint *',
        name = 'atomic',
      ),
      Param(
        type = 'guint',
        name = 'val',
      ),
    ],
  ),
  'g_atomic_int_xor': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'volatile guint *',
        name = 'atomic',
      ),
      Param(
        type = 'guint',
        name = 'val',
      ),
    ],
  ),
  'g_atomic_pointer_get': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'volatile void *',
        name = 'atomic',
      ),
    ],
  ),
  'g_atomic_pointer_set': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'volatile void *',
        name = 'atomic',
      ),
      Param(
        type = 'gpointer',
        name = 'newval',
      ),
    ],
  ),
  'g_atomic_pointer_compare_and_exchange': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'volatile void *',
        name = 'atomic',
      ),
      Param(
        type = 'gpointer',
        name = 'oldval',
      ),
      Param(
        type = 'gpointer',
        name = 'newval',
      ),
    ],
  ),
  'g_atomic_pointer_add': Spec(
    return_type = 'gssize',
    parameters = [
      Param(
        type = 'volatile void *',
        name = 'atomic',
      ),
      Param(
        type = 'gssize',
        name = 'val',
      ),
    ],
  ),
  'g_atomic_pointer_and': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'volatile void *',
        name = 'atomic',
      ),
      Param(
        type = 'gsize',
        name = 'val',
      ),
    ],
  ),
  'g_atomic_pointer_or': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'volatile void *',
        name = 'atomic',
      ),
      Param(
        type = 'gsize',
        name = 'val',
      ),
    ],
  ),
  'g_atomic_pointer_xor': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'volatile void *',
        name = 'atomic',
      ),
      Param(
        type = 'gsize',
        name = 'val',
      ),
    ],
  ),
  'g_atomic_int_exchange_and_add': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'volatile gint *',
        name = 'atomic',
      ),
      Param(
        type = 'gint',
        name = 'val',
      ),
    ],
  ),
  'g_quark_try_string': Spec(
    return_type = 'GQuark',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_quark_from_static_string': Spec(
    return_type = 'GQuark',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_quark_from_string': Spec(
    return_type = 'GQuark',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_quark_to_string': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GQuark',
        name = 'quark',
      ),
    ],
  ),
  'g_intern_string': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_intern_static_string': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_error_new': Spec(
    return_type = 'GError *',
    parameters = [
      Param(
        type = 'GQuark',
        name = 'domain',
      ),
      Param(
        type = 'gint',
        name = 'code',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_error_new_literal': Spec(
    return_type = 'GError *',
    parameters = [
      Param(
        type = 'GQuark',
        name = 'domain',
      ),
      Param(
        type = 'gint',
        name = 'code',
      ),
      Param(
        type = 'const gchar *',
        name = 'message',
      ),
    ],
  ),
  'g_error_new_valist': Spec(
    return_type = 'GError *',
    parameters = [
      Param(
        type = 'GQuark',
        name = 'domain',
      ),
      Param(
        type = 'gint',
        name = 'code',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
    ],
  ),
  'g_error_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GError *',
        name = 'error',
      ),
    ],
  ),
  'g_error_copy': Spec(
    return_type = 'GError *',
    parameters = [
      Param(
        type = 'const GError *',
        name = 'error',
      ),
    ],
  ),
  'g_error_matches': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GError *',
        name = 'error',
      ),
      Param(
        type = 'GQuark',
        name = 'domain',
      ),
      Param(
        type = 'gint',
        name = 'code',
      ),
    ],
  ),
  'g_set_error': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GError **',
        name = 'err',
      ),
      Param(
        type = 'GQuark',
        name = 'domain',
      ),
      Param(
        type = 'gint',
        name = 'code',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_set_error_literal': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GError **',
        name = 'err',
      ),
      Param(
        type = 'GQuark',
        name = 'domain',
      ),
      Param(
        type = 'gint',
        name = 'code',
      ),
      Param(
        type = 'const gchar *',
        name = 'message',
      ),
    ],
  ),
  'g_propagate_error': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GError **',
        name = 'dest',
      ),
      Param(
        type = 'GError *',
        name = 'src',
      ),
    ],
  ),
  'g_clear_error': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GError **',
        name = 'err',
      ),
    ],
  ),
  'g_prefix_error': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GError **',
        name = 'err',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_propagate_prefixed_error': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GError **',
        name = 'dest',
      ),
      Param(
        type = 'GError *',
        name = 'src',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_thread_error_quark': Spec(
    return_type = 'GQuark',
    parameters = [
    ],
  ),
  'g_thread_ref': Spec(
    return_type = 'GThread *',
    parameters = [
      Param(
        type = 'GThread *',
        name = 'thread',
      ),
    ],
  ),
  'g_thread_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GThread *',
        name = 'thread',
      ),
    ],
  ),
  'g_thread_new': Spec(
    return_type = 'GThread *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'GThreadFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_thread_try_new': Spec(
    return_type = 'GThread *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'GThreadFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_thread_self': Spec(
    return_type = 'GThread *',
    parameters = [
    ],
  ),
  'g_thread_exit': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'retval',
      ),
    ],
  ),
  'g_thread_join': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GThread *',
        name = 'thread',
      ),
    ],
  ),
  'g_thread_yield': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'g_mutex_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_mutex_clear': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_mutex_lock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_mutex_trylock': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_mutex_unlock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_rw_lock_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRWLock *',
        name = 'rw_lock',
      ),
    ],
  ),
  'g_rw_lock_clear': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRWLock *',
        name = 'rw_lock',
      ),
    ],
  ),
  'g_rw_lock_writer_lock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRWLock *',
        name = 'rw_lock',
      ),
    ],
  ),
  'g_rw_lock_writer_trylock': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GRWLock *',
        name = 'rw_lock',
      ),
    ],
  ),
  'g_rw_lock_writer_unlock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRWLock *',
        name = 'rw_lock',
      ),
    ],
  ),
  'g_rw_lock_reader_lock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRWLock *',
        name = 'rw_lock',
      ),
    ],
  ),
  'g_rw_lock_reader_trylock': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GRWLock *',
        name = 'rw_lock',
      ),
    ],
  ),
  'g_rw_lock_reader_unlock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRWLock *',
        name = 'rw_lock',
      ),
    ],
  ),
  'g_rec_mutex_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRecMutex *',
        name = 'rec_mutex',
      ),
    ],
  ),
  'g_rec_mutex_clear': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRecMutex *',
        name = 'rec_mutex',
      ),
    ],
  ),
  'g_rec_mutex_lock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRecMutex *',
        name = 'rec_mutex',
      ),
    ],
  ),
  'g_rec_mutex_trylock': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GRecMutex *',
        name = 'rec_mutex',
      ),
    ],
  ),
  'g_rec_mutex_unlock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRecMutex *',
        name = 'rec_mutex',
      ),
    ],
  ),
  'g_cond_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCond *',
        name = 'cond',
      ),
    ],
  ),
  'g_cond_clear': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCond *',
        name = 'cond',
      ),
    ],
  ),
  'g_cond_wait': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCond *',
        name = 'cond',
      ),
      Param(
        type = 'GMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_cond_signal': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCond *',
        name = 'cond',
      ),
    ],
  ),
  'g_cond_broadcast': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCond *',
        name = 'cond',
      ),
    ],
  ),
  'g_cond_wait_until': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GCond *',
        name = 'cond',
      ),
      Param(
        type = 'GMutex *',
        name = 'mutex',
      ),
      Param(
        type = 'gint64',
        name = 'end_time',
      ),
    ],
  ),
  'g_private_get': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GPrivate *',
        name = 'key',
      ),
    ],
  ),
  'g_private_set': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GPrivate *',
        name = 'key',
      ),
      Param(
        type = 'gpointer',
        name = 'value',
      ),
    ],
  ),
  'g_private_replace': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GPrivate *',
        name = 'key',
      ),
      Param(
        type = 'gpointer',
        name = 'value',
      ),
    ],
  ),
  'g_once_impl': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GOnce *',
        name = 'once',
      ),
      Param(
        type = 'GThreadFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'arg',
      ),
    ],
  ),
  'g_once_init_enter': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'volatile void *',
        name = 'location',
      ),
    ],
  ),
  'g_once_init_leave': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'volatile void *',
        name = 'location',
      ),
      Param(
        type = 'gsize',
        name = 'result',
      ),
    ],
  ),
  'g_async_queue_new': Spec(
    return_type = 'GAsyncQueue *',
    parameters = [
    ],
  ),
  'g_async_queue_new_full': Spec(
    return_type = 'GAsyncQueue *',
    parameters = [
      Param(
        type = 'GDestroyNotify',
        name = 'item_free_func',
      ),
    ],
  ),
  'g_async_queue_lock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_async_queue_unlock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_async_queue_ref': Spec(
    return_type = 'GAsyncQueue *',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_async_queue_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_async_queue_ref_unlocked': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_async_queue_unref_and_unlock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_async_queue_push': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_async_queue_push_unlocked': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_async_queue_push_sorted': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_async_queue_push_sorted_unlocked': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_async_queue_pop': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_async_queue_pop_unlocked': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_async_queue_try_pop': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_async_queue_try_pop_unlocked': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_async_queue_timeout_pop': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
      Param(
        type = 'guint64',
        name = 'timeout',
      ),
    ],
  ),
  'g_async_queue_timeout_pop_unlocked': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
      Param(
        type = 'guint64',
        name = 'timeout',
      ),
    ],
  ),
  'g_async_queue_length': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_async_queue_length_unlocked': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_async_queue_sort': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_async_queue_sort_unlocked': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_async_queue_timed_pop': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
      Param(
        type = 'GTimeVal *',
        name = 'end_time',
      ),
    ],
  ),
  'g_async_queue_timed_pop_unlocked': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GAsyncQueue *',
        name = 'queue',
      ),
      Param(
        type = 'GTimeVal *',
        name = 'end_time',
      ),
    ],
  ),
  '__sigismember': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const __sigset_t *',
        name = '',
      ),
      Param(
        type = 'int',
        name = '',
      ),
    ],
  ),
  '__sigaddset': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__sigset_t *',
        name = '',
      ),
      Param(
        type = 'int',
        name = '',
      ),
    ],
  ),
  '__sigdelset': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__sigset_t *',
        name = '',
      ),
      Param(
        type = 'int',
        name = '',
      ),
    ],
  ),
  '__sysv_signal': Spec(
    return_type = '__sighandler_t',
    parameters = [
      Param(
        type = 'int',
        name = '__sig',
      ),
      Param(
        type = '__sighandler_t',
        name = '__handler',
      ),
    ],
  ),
  'signal': Spec(
    return_type = '__sighandler_t',
    parameters = [
      Param(
        type = 'int',
        name = '__sig',
      ),
      Param(
        type = '__sighandler_t',
        name = '__handler',
      ),
    ],
  ),
  'kill': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__pid_t',
        name = '__pid',
      ),
      Param(
        type = 'int',
        name = '__sig',
      ),
    ],
  ),
  'killpg': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__pid_t',
        name = '__pgrp',
      ),
      Param(
        type = 'int',
        name = '__sig',
      ),
    ],
  ),
  'raise': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__sig',
      ),
    ],
  ),
  'ssignal': Spec(
    return_type = '__sighandler_t',
    parameters = [
      Param(
        type = 'int',
        name = '__sig',
      ),
      Param(
        type = '__sighandler_t',
        name = '__handler',
      ),
    ],
  ),
  'gsignal': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__sig',
      ),
    ],
  ),
  'psignal': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'int',
        name = '__sig',
      ),
      Param(
        type = 'const char *',
        name = '__s',
      ),
    ],
  ),
  'psiginfo': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const siginfo_t *',
        name = '__pinfo',
      ),
      Param(
        type = 'const char *',
        name = '__s',
      ),
    ],
  ),
  '__sigpause': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__sig_or_mask',
      ),
      Param(
        type = 'int',
        name = '__is_sig',
      ),
    ],
  ),
  'sigblock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__mask',
      ),
    ],
  ),
  'sigsetmask': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__mask',
      ),
    ],
  ),
  'siggetmask': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  'sigemptyset': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'sigset_t *',
        name = '__set',
      ),
    ],
  ),
  'sigfillset': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'sigset_t *',
        name = '__set',
      ),
    ],
  ),
  'sigaddset': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'sigset_t *',
        name = '__set',
      ),
      Param(
        type = 'int',
        name = '__signo',
      ),
    ],
  ),
  'sigdelset': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'sigset_t *',
        name = '__set',
      ),
      Param(
        type = 'int',
        name = '__signo',
      ),
    ],
  ),
  'sigismember': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const sigset_t *',
        name = '__set',
      ),
      Param(
        type = 'int',
        name = '__signo',
      ),
    ],
  ),
  'sigprocmask': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__how',
      ),
      Param(
        type = 'const sigset_t *restrict',
        name = '__set',
      ),
      Param(
        type = 'sigset_t *restrict',
        name = '__oset',
      ),
    ],
  ),
  'sigsuspend': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const sigset_t *',
        name = '__set',
      ),
    ],
  ),
  'sigaction': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__sig',
      ),
      Param(
        type = 'const struct sigaction *restrict',
        name = '__act',
      ),
      Param(
        type = 'struct sigaction *restrict',
        name = '__oact',
      ),
    ],
  ),
  'sigpending': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'sigset_t *',
        name = '__set',
      ),
    ],
  ),
  'sigwait': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const sigset_t *restrict',
        name = '__set',
      ),
      Param(
        type = 'int *restrict',
        name = '__sig',
      ),
    ],
  ),
  'sigwaitinfo': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const sigset_t *restrict',
        name = '__set',
      ),
      Param(
        type = 'siginfo_t *restrict',
        name = '__info',
      ),
    ],
  ),
  'sigtimedwait': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const sigset_t *restrict',
        name = '__set',
      ),
      Param(
        type = 'siginfo_t *restrict',
        name = '__info',
      ),
      Param(
        type = 'const struct timespec *restrict',
        name = '__timeout',
      ),
    ],
  ),
  'sigqueue': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__pid_t',
        name = '__pid',
      ),
      Param(
        type = 'int',
        name = '__sig',
      ),
      Param(
        type = 'const union sigval',
        name = '__val',
      ),
    ],
  ),
  'sigvec': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__sig',
      ),
      Param(
        type = 'const struct sigvec *',
        name = '__vec',
      ),
      Param(
        type = 'struct sigvec *',
        name = '__ovec',
      ),
    ],
  ),
  'sigreturn': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'struct sigcontext *',
        name = '__scp',
      ),
    ],
  ),
  'siginterrupt': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__sig',
      ),
      Param(
        type = 'int',
        name = '__interrupt',
      ),
    ],
  ),
  'sigstack': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'struct sigstack *',
        name = '__ss',
      ),
      Param(
        type = 'struct sigstack *',
        name = '__oss',
      ),
    ],
  ),
  'sigaltstack': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const struct sigaltstack *restrict',
        name = '__ss',
      ),
      Param(
        type = 'struct sigaltstack *restrict',
        name = '__oss',
      ),
    ],
  ),
  'pthread_sigmask': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__how',
      ),
      Param(
        type = 'const __sigset_t *restrict',
        name = '__newmask',
      ),
      Param(
        type = '__sigset_t *restrict',
        name = '__oldmask',
      ),
    ],
  ),
  'pthread_kill': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_t',
        name = '__threadid',
      ),
      Param(
        type = 'int',
        name = '__signo',
      ),
    ],
  ),
  '__libc_current_sigrtmin': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  '__libc_current_sigrtmax': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  'g_on_error_query': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'prg_name',
      ),
    ],
  ),
  'g_on_error_stack_trace': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'prg_name',
      ),
    ],
  ),
  'g_base64_encode_step': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'const guchar *',
        name = 'in',
      ),
      Param(
        type = 'gsize',
        name = 'len',
      ),
      Param(
        type = 'gboolean',
        name = 'break_lines',
      ),
      Param(
        type = 'gchar *',
        name = 'out',
      ),
      Param(
        type = 'gint *',
        name = 'state',
      ),
      Param(
        type = 'gint *',
        name = 'save',
      ),
    ],
  ),
  'g_base64_encode_close': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'gboolean',
        name = 'break_lines',
      ),
      Param(
        type = 'gchar *',
        name = 'out',
      ),
      Param(
        type = 'gint *',
        name = 'state',
      ),
      Param(
        type = 'gint *',
        name = 'save',
      ),
    ],
  ),
  'g_base64_encode': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const guchar *',
        name = 'data',
      ),
      Param(
        type = 'gsize',
        name = 'len',
      ),
    ],
  ),
  'g_base64_decode_step': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'in',
      ),
      Param(
        type = 'gsize',
        name = 'len',
      ),
      Param(
        type = 'guchar *',
        name = 'out',
      ),
      Param(
        type = 'gint *',
        name = 'state',
      ),
      Param(
        type = 'guint *',
        name = 'save',
      ),
    ],
  ),
  'g_base64_decode': Spec(
    return_type = 'guchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'text',
      ),
      Param(
        type = 'gsize *',
        name = 'out_len',
      ),
    ],
  ),
  'g_base64_decode_inplace': Spec(
    return_type = 'guchar *',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'text',
      ),
      Param(
        type = 'gsize *',
        name = 'out_len',
      ),
    ],
  ),
  'g_bit_lock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'volatile gint *',
        name = 'address',
      ),
      Param(
        type = 'gint',
        name = 'lock_bit',
      ),
    ],
  ),
  'g_bit_trylock': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'volatile gint *',
        name = 'address',
      ),
      Param(
        type = 'gint',
        name = 'lock_bit',
      ),
    ],
  ),
  'g_bit_unlock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'volatile gint *',
        name = 'address',
      ),
      Param(
        type = 'gint',
        name = 'lock_bit',
      ),
    ],
  ),
  'g_pointer_bit_lock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'volatile void *',
        name = 'address',
      ),
      Param(
        type = 'gint',
        name = 'lock_bit',
      ),
    ],
  ),
  'g_pointer_bit_trylock': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'volatile void *',
        name = 'address',
      ),
      Param(
        type = 'gint',
        name = 'lock_bit',
      ),
    ],
  ),
  'g_pointer_bit_unlock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'volatile void *',
        name = 'address',
      ),
      Param(
        type = 'gint',
        name = 'lock_bit',
      ),
    ],
  ),
  'g_bookmark_file_error_quark': Spec(
    return_type = 'GQuark',
    parameters = [
    ],
  ),
  'g_bookmark_file_new': Spec(
    return_type = 'GBookmarkFile *',
    parameters = [
    ],
  ),
  'g_bookmark_file_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
    ],
  ),
  'g_bookmark_file_load_from_file': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'filename',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_load_from_data': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'data',
      ),
      Param(
        type = 'gsize',
        name = 'length',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_load_from_data_dirs': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'file',
      ),
      Param(
        type = 'gchar **',
        name = 'full_path',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_to_data': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_to_file': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'filename',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_set_title': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'const gchar *',
        name = 'title',
      ),
    ],
  ),
  'g_bookmark_file_get_title': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_set_description': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'const gchar *',
        name = 'description',
      ),
    ],
  ),
  'g_bookmark_file_get_description': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_set_mime_type': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'const gchar *',
        name = 'mime_type',
      ),
    ],
  ),
  'g_bookmark_file_get_mime_type': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_set_groups': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'const gchar **',
        name = 'groups',
      ),
      Param(
        type = 'gsize',
        name = 'length',
      ),
    ],
  ),
  'g_bookmark_file_add_group': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'const gchar *',
        name = 'group',
      ),
    ],
  ),
  'g_bookmark_file_has_group': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'const gchar *',
        name = 'group',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_get_groups': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_add_application': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'exec',
      ),
    ],
  ),
  'g_bookmark_file_has_application': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_get_applications': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_set_app_info': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'exec',
      ),
      Param(
        type = 'gint',
        name = 'count',
      ),
      Param(
        type = 'time_t',
        name = 'stamp',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_get_app_info': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'gchar **',
        name = 'exec',
      ),
      Param(
        type = 'guint *',
        name = 'count',
      ),
      Param(
        type = 'time_t *',
        name = 'stamp',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_set_is_private': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'gboolean',
        name = 'is_private',
      ),
    ],
  ),
  'g_bookmark_file_get_is_private': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_set_icon': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'const gchar *',
        name = 'href',
      ),
      Param(
        type = 'const gchar *',
        name = 'mime_type',
      ),
    ],
  ),
  'g_bookmark_file_get_icon': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'gchar **',
        name = 'href',
      ),
      Param(
        type = 'gchar **',
        name = 'mime_type',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_set_added': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'time_t',
        name = 'added',
      ),
    ],
  ),
  'g_bookmark_file_get_added': Spec(
    return_type = 'time_t',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_set_modified': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'time_t',
        name = 'modified',
      ),
    ],
  ),
  'g_bookmark_file_get_modified': Spec(
    return_type = 'time_t',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_set_visited': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'time_t',
        name = 'visited',
      ),
    ],
  ),
  'g_bookmark_file_get_visited': Spec(
    return_type = 'time_t',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_has_item': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
    ],
  ),
  'g_bookmark_file_get_size': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
    ],
  ),
  'g_bookmark_file_get_uris': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
    ],
  ),
  'g_bookmark_file_remove_group': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'const gchar *',
        name = 'group',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_remove_application': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_remove_item': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bookmark_file_move_item': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GBookmarkFile *',
        name = 'bookmark',
      ),
      Param(
        type = 'const gchar *',
        name = 'old_uri',
      ),
      Param(
        type = 'const gchar *',
        name = 'new_uri',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_bytes_new': Spec(
    return_type = 'GBytes *',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
      Param(
        type = 'gsize',
        name = 'size',
      ),
    ],
  ),
  'g_bytes_new_take': Spec(
    return_type = 'GBytes *',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'gsize',
        name = 'size',
      ),
    ],
  ),
  'g_bytes_new_static': Spec(
    return_type = 'GBytes *',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
      Param(
        type = 'gsize',
        name = 'size',
      ),
    ],
  ),
  'g_bytes_new_with_free_func': Spec(
    return_type = 'GBytes *',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
      Param(
        type = 'gsize',
        name = 'size',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'free_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_bytes_new_from_bytes': Spec(
    return_type = 'GBytes *',
    parameters = [
      Param(
        type = 'GBytes *',
        name = 'bytes',
      ),
      Param(
        type = 'gsize',
        name = 'offset',
      ),
      Param(
        type = 'gsize',
        name = 'length',
      ),
    ],
  ),
  'g_bytes_get_data': Spec(
    return_type = 'gconstpointer',
    parameters = [
      Param(
        type = 'GBytes *',
        name = 'bytes',
      ),
      Param(
        type = 'gsize *',
        name = 'size',
      ),
    ],
  ),
  'g_bytes_get_size': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'GBytes *',
        name = 'bytes',
      ),
    ],
  ),
  'g_bytes_ref': Spec(
    return_type = 'GBytes *',
    parameters = [
      Param(
        type = 'GBytes *',
        name = 'bytes',
      ),
    ],
  ),
  'g_bytes_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GBytes *',
        name = 'bytes',
      ),
    ],
  ),
  'g_bytes_unref_to_data': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GBytes *',
        name = 'bytes',
      ),
      Param(
        type = 'gsize *',
        name = 'size',
      ),
    ],
  ),
  'g_bytes_unref_to_array': Spec(
    return_type = 'GByteArray *',
    parameters = [
      Param(
        type = 'GBytes *',
        name = 'bytes',
      ),
    ],
  ),
  'g_bytes_hash': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'bytes',
      ),
    ],
  ),
  'g_bytes_equal': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'bytes1',
      ),
      Param(
        type = 'gconstpointer',
        name = 'bytes2',
      ),
    ],
  ),
  'g_bytes_compare': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'bytes1',
      ),
      Param(
        type = 'gconstpointer',
        name = 'bytes2',
      ),
    ],
  ),
  'g_get_charset': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const char **',
        name = 'charset',
      ),
    ],
  ),
  'g_get_codeset': Spec(
    return_type = 'gchar *',
    parameters = [
    ],
  ),
  'g_get_language_names': Spec(
    return_type = 'const gchar *const *',
    parameters = [
    ],
  ),
  'g_get_locale_variants': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'locale',
      ),
    ],
  ),
  'g_checksum_type_get_length': Spec(
    return_type = 'gssize',
    parameters = [
      Param(
        type = 'GChecksumType',
        name = 'checksum_type',
      ),
    ],
  ),
  'g_checksum_new': Spec(
    return_type = 'GChecksum *',
    parameters = [
      Param(
        type = 'GChecksumType',
        name = 'checksum_type',
      ),
    ],
  ),
  'g_checksum_reset': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GChecksum *',
        name = 'checksum',
      ),
    ],
  ),
  'g_checksum_copy': Spec(
    return_type = 'GChecksum *',
    parameters = [
      Param(
        type = 'const GChecksum *',
        name = 'checksum',
      ),
    ],
  ),
  'g_checksum_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GChecksum *',
        name = 'checksum',
      ),
    ],
  ),
  'g_checksum_update': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GChecksum *',
        name = 'checksum',
      ),
      Param(
        type = 'const guchar *',
        name = 'data',
      ),
      Param(
        type = 'gssize',
        name = 'length',
      ),
    ],
  ),
  'g_checksum_get_string': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GChecksum *',
        name = 'checksum',
      ),
    ],
  ),
  'g_checksum_get_digest': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GChecksum *',
        name = 'checksum',
      ),
      Param(
        type = 'guint8 *',
        name = 'buffer',
      ),
      Param(
        type = 'gsize *',
        name = 'digest_len',
      ),
    ],
  ),
  'g_compute_checksum_for_data': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GChecksumType',
        name = 'checksum_type',
      ),
      Param(
        type = 'const guchar *',
        name = 'data',
      ),
      Param(
        type = 'gsize',
        name = 'length',
      ),
    ],
  ),
  'g_compute_checksum_for_string': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GChecksumType',
        name = 'checksum_type',
      ),
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'length',
      ),
    ],
  ),
  'g_compute_checksum_for_bytes': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GChecksumType',
        name = 'checksum_type',
      ),
      Param(
        type = 'GBytes *',
        name = 'data',
      ),
    ],
  ),
  'g_convert_error_quark': Spec(
    return_type = 'GQuark',
    parameters = [
    ],
  ),
  'g_iconv_open': Spec(
    return_type = 'GIConv',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'to_codeset',
      ),
      Param(
        type = 'const gchar *',
        name = 'from_codeset',
      ),
    ],
  ),
  'g_iconv': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'GIConv',
        name = 'converter',
      ),
      Param(
        type = 'gchar **',
        name = 'inbuf',
      ),
      Param(
        type = 'gsize *',
        name = 'inbytes_left',
      ),
      Param(
        type = 'gchar **',
        name = 'outbuf',
      ),
      Param(
        type = 'gsize *',
        name = 'outbytes_left',
      ),
    ],
  ),
  'g_iconv_close': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GIConv',
        name = 'converter',
      ),
    ],
  ),
  'g_convert': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
      Param(
        type = 'const gchar *',
        name = 'to_codeset',
      ),
      Param(
        type = 'const gchar *',
        name = 'from_codeset',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_read',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_written',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_convert_with_iconv': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
      Param(
        type = 'GIConv',
        name = 'converter',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_read',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_written',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_convert_with_fallback': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
      Param(
        type = 'const gchar *',
        name = 'to_codeset',
      ),
      Param(
        type = 'const gchar *',
        name = 'from_codeset',
      ),
      Param(
        type = 'const gchar *',
        name = 'fallback',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_read',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_written',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_locale_to_utf8': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'opsysstring',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_read',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_written',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_locale_from_utf8': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'utf8string',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_read',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_written',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_filename_to_utf8': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'opsysstring',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_read',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_written',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_filename_from_utf8': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'utf8string',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_read',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_written',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_filename_from_uri': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'uri',
      ),
      Param(
        type = 'gchar **',
        name = 'hostname',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_filename_to_uri': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'filename',
      ),
      Param(
        type = 'const gchar *',
        name = 'hostname',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_filename_display_name': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'filename',
      ),
    ],
  ),
  'g_get_filename_charsets': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar ***',
        name = 'charsets',
      ),
    ],
  ),
  'g_filename_display_basename': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'filename',
      ),
    ],
  ),
  'g_uri_list_extract_uris': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'uri_list',
      ),
    ],
  ),
  'g_datalist_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GData **',
        name = 'datalist',
      ),
    ],
  ),
  'g_datalist_clear': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GData **',
        name = 'datalist',
      ),
    ],
  ),
  'g_datalist_id_get_data': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GData **',
        name = 'datalist',
      ),
      Param(
        type = 'GQuark',
        name = 'key_id',
      ),
    ],
  ),
  'g_datalist_id_set_data_full': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GData **',
        name = 'datalist',
      ),
      Param(
        type = 'GQuark',
        name = 'key_id',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'destroy_func',
      ),
    ],
  ),
  'g_datalist_id_dup_data': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GData **',
        name = 'datalist',
      ),
      Param(
        type = 'GQuark',
        name = 'key_id',
      ),
      Param(
        type = 'GDuplicateFunc',
        name = 'dup_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_datalist_id_replace_data': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GData **',
        name = 'datalist',
      ),
      Param(
        type = 'GQuark',
        name = 'key_id',
      ),
      Param(
        type = 'gpointer',
        name = 'oldval',
      ),
      Param(
        type = 'gpointer',
        name = 'newval',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'destroy',
      ),
      Param(
        type = 'GDestroyNotify *',
        name = 'old_destroy',
      ),
    ],
  ),
  'g_datalist_id_remove_no_notify': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GData **',
        name = 'datalist',
      ),
      Param(
        type = 'GQuark',
        name = 'key_id',
      ),
    ],
  ),
  'g_datalist_foreach': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GData **',
        name = 'datalist',
      ),
      Param(
        type = 'GDataForeachFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_datalist_set_flags': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GData **',
        name = 'datalist',
      ),
      Param(
        type = 'guint',
        name = 'flags',
      ),
    ],
  ),
  'g_datalist_unset_flags': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GData **',
        name = 'datalist',
      ),
      Param(
        type = 'guint',
        name = 'flags',
      ),
    ],
  ),
  'g_datalist_get_flags': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GData **',
        name = 'datalist',
      ),
    ],
  ),
  'g_dataset_destroy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'dataset_location',
      ),
    ],
  ),
  'g_dataset_id_get_data': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'dataset_location',
      ),
      Param(
        type = 'GQuark',
        name = 'key_id',
      ),
    ],
  ),
  'g_datalist_get_data': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GData **',
        name = 'datalist',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
    ],
  ),
  'g_dataset_id_set_data_full': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'dataset_location',
      ),
      Param(
        type = 'GQuark',
        name = 'key_id',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'destroy_func',
      ),
    ],
  ),
  'g_dataset_id_remove_no_notify': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'dataset_location',
      ),
      Param(
        type = 'GQuark',
        name = 'key_id',
      ),
    ],
  ),
  'g_dataset_foreach': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'dataset_location',
      ),
      Param(
        type = 'GDataForeachFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_date_new': Spec(
    return_type = 'GDate *',
    parameters = [
    ],
  ),
  'g_date_new_dmy': Spec(
    return_type = 'GDate *',
    parameters = [
      Param(
        type = 'GDateDay',
        name = 'day',
      ),
      Param(
        type = 'GDateMonth',
        name = 'month',
      ),
      Param(
        type = 'GDateYear',
        name = 'year',
      ),
    ],
  ),
  'g_date_new_julian': Spec(
    return_type = 'GDate *',
    parameters = [
      Param(
        type = 'guint32',
        name = 'julian_day',
      ),
    ],
  ),
  'g_date_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
    ],
  ),
  'g_date_valid': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'date',
      ),
    ],
  ),
  'g_date_valid_day': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GDateDay',
        name = 'day',
      ),
    ],
  ),
  'g_date_valid_month': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GDateMonth',
        name = 'month',
      ),
    ],
  ),
  'g_date_valid_year': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GDateYear',
        name = 'year',
      ),
    ],
  ),
  'g_date_valid_weekday': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GDateWeekday',
        name = 'weekday',
      ),
    ],
  ),
  'g_date_valid_julian': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'guint32',
        name = 'julian_date',
      ),
    ],
  ),
  'g_date_valid_dmy': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GDateDay',
        name = 'day',
      ),
      Param(
        type = 'GDateMonth',
        name = 'month',
      ),
      Param(
        type = 'GDateYear',
        name = 'year',
      ),
    ],
  ),
  'g_date_get_weekday': Spec(
    return_type = 'GDateWeekday',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'date',
      ),
    ],
  ),
  'g_date_get_month': Spec(
    return_type = 'GDateMonth',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'date',
      ),
    ],
  ),
  'g_date_get_year': Spec(
    return_type = 'GDateYear',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'date',
      ),
    ],
  ),
  'g_date_get_day': Spec(
    return_type = 'GDateDay',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'date',
      ),
    ],
  ),
  'g_date_get_julian': Spec(
    return_type = 'guint32',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'date',
      ),
    ],
  ),
  'g_date_get_day_of_year': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'date',
      ),
    ],
  ),
  'g_date_get_monday_week_of_year': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'date',
      ),
    ],
  ),
  'g_date_get_sunday_week_of_year': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'date',
      ),
    ],
  ),
  'g_date_get_iso8601_week_of_year': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'date',
      ),
    ],
  ),
  'g_date_clear': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'guint',
        name = 'n_dates',
      ),
    ],
  ),
  'g_date_set_parse': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
    ],
  ),
  'g_date_set_time_t': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'time_t',
        name = 'timet',
      ),
    ],
  ),
  'g_date_set_time_val': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'GTimeVal *',
        name = 'timeval',
      ),
    ],
  ),
  'g_date_set_time': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'GTime',
        name = 'time_',
      ),
    ],
  ),
  'g_date_set_month': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'GDateMonth',
        name = 'month',
      ),
    ],
  ),
  'g_date_set_day': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'GDateDay',
        name = 'day',
      ),
    ],
  ),
  'g_date_set_year': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'GDateYear',
        name = 'year',
      ),
    ],
  ),
  'g_date_set_dmy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'GDateDay',
        name = 'day',
      ),
      Param(
        type = 'GDateMonth',
        name = 'month',
      ),
      Param(
        type = 'GDateYear',
        name = 'y',
      ),
    ],
  ),
  'g_date_set_julian': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'guint32',
        name = 'julian_date',
      ),
    ],
  ),
  'g_date_is_first_of_month': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'date',
      ),
    ],
  ),
  'g_date_is_last_of_month': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'date',
      ),
    ],
  ),
  'g_date_add_days': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'guint',
        name = 'n_days',
      ),
    ],
  ),
  'g_date_subtract_days': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'guint',
        name = 'n_days',
      ),
    ],
  ),
  'g_date_add_months': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'guint',
        name = 'n_months',
      ),
    ],
  ),
  'g_date_subtract_months': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'guint',
        name = 'n_months',
      ),
    ],
  ),
  'g_date_add_years': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'guint',
        name = 'n_years',
      ),
    ],
  ),
  'g_date_subtract_years': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'guint',
        name = 'n_years',
      ),
    ],
  ),
  'g_date_is_leap_year': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GDateYear',
        name = 'year',
      ),
    ],
  ),
  'g_date_get_days_in_month': Spec(
    return_type = 'guint8',
    parameters = [
      Param(
        type = 'GDateMonth',
        name = 'month',
      ),
      Param(
        type = 'GDateYear',
        name = 'year',
      ),
    ],
  ),
  'g_date_get_monday_weeks_in_year': Spec(
    return_type = 'guint8',
    parameters = [
      Param(
        type = 'GDateYear',
        name = 'year',
      ),
    ],
  ),
  'g_date_get_sunday_weeks_in_year': Spec(
    return_type = 'guint8',
    parameters = [
      Param(
        type = 'GDateYear',
        name = 'year',
      ),
    ],
  ),
  'g_date_days_between': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'date1',
      ),
      Param(
        type = 'const GDate *',
        name = 'date2',
      ),
    ],
  ),
  'g_date_compare': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'lhs',
      ),
      Param(
        type = 'const GDate *',
        name = 'rhs',
      ),
    ],
  ),
  'g_date_to_struct_tm': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const GDate *',
        name = 'date',
      ),
      Param(
        type = 'struct tm *',
        name = 'tm',
      ),
    ],
  ),
  'g_date_clamp': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date',
      ),
      Param(
        type = 'const GDate *',
        name = 'min_date',
      ),
      Param(
        type = 'const GDate *',
        name = 'max_date',
      ),
    ],
  ),
  'g_date_order': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDate *',
        name = 'date1',
      ),
      Param(
        type = 'GDate *',
        name = 'date2',
      ),
    ],
  ),
  'g_date_strftime': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'gchar *',
        name = 's',
      ),
      Param(
        type = 'gsize',
        name = 'slen',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
      Param(
        type = 'const GDate *',
        name = 'date',
      ),
    ],
  ),
  'g_time_zone_new': Spec(
    return_type = 'GTimeZone *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'identifier',
      ),
    ],
  ),
  'g_time_zone_new_utc': Spec(
    return_type = 'GTimeZone *',
    parameters = [
    ],
  ),
  'g_time_zone_new_local': Spec(
    return_type = 'GTimeZone *',
    parameters = [
    ],
  ),
  'g_time_zone_ref': Spec(
    return_type = 'GTimeZone *',
    parameters = [
      Param(
        type = 'GTimeZone *',
        name = 'tz',
      ),
    ],
  ),
  'g_time_zone_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTimeZone *',
        name = 'tz',
      ),
    ],
  ),
  'g_time_zone_find_interval': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GTimeZone *',
        name = 'tz',
      ),
      Param(
        type = 'GTimeType',
        name = 'type',
      ),
      Param(
        type = 'gint64',
        name = 'time_',
      ),
    ],
  ),
  'g_time_zone_adjust_time': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GTimeZone *',
        name = 'tz',
      ),
      Param(
        type = 'GTimeType',
        name = 'type',
      ),
      Param(
        type = 'gint64 *',
        name = 'time_',
      ),
    ],
  ),
  'g_time_zone_get_abbreviation': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GTimeZone *',
        name = 'tz',
      ),
      Param(
        type = 'gint',
        name = 'interval',
      ),
    ],
  ),
  'g_time_zone_get_offset': Spec(
    return_type = 'gint32',
    parameters = [
      Param(
        type = 'GTimeZone *',
        name = 'tz',
      ),
      Param(
        type = 'gint',
        name = 'interval',
      ),
    ],
  ),
  'g_time_zone_is_dst': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GTimeZone *',
        name = 'tz',
      ),
      Param(
        type = 'gint',
        name = 'interval',
      ),
    ],
  ),
  'g_date_time_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_ref': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_new_now': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GTimeZone *',
        name = 'tz',
      ),
    ],
  ),
  'g_date_time_new_now_local': Spec(
    return_type = 'GDateTime *',
    parameters = [
    ],
  ),
  'g_date_time_new_now_utc': Spec(
    return_type = 'GDateTime *',
    parameters = [
    ],
  ),
  'g_date_time_new_from_unix_local': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'gint64',
        name = 't',
      ),
    ],
  ),
  'g_date_time_new_from_unix_utc': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'gint64',
        name = 't',
      ),
    ],
  ),
  'g_date_time_new_from_timeval_local': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'const GTimeVal *',
        name = 'tv',
      ),
    ],
  ),
  'g_date_time_new_from_timeval_utc': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'const GTimeVal *',
        name = 'tv',
      ),
    ],
  ),
  'g_date_time_new': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GTimeZone *',
        name = 'tz',
      ),
      Param(
        type = 'gint',
        name = 'year',
      ),
      Param(
        type = 'gint',
        name = 'month',
      ),
      Param(
        type = 'gint',
        name = 'day',
      ),
      Param(
        type = 'gint',
        name = 'hour',
      ),
      Param(
        type = 'gint',
        name = 'minute',
      ),
      Param(
        type = 'gdouble',
        name = 'seconds',
      ),
    ],
  ),
  'g_date_time_new_local': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'gint',
        name = 'year',
      ),
      Param(
        type = 'gint',
        name = 'month',
      ),
      Param(
        type = 'gint',
        name = 'day',
      ),
      Param(
        type = 'gint',
        name = 'hour',
      ),
      Param(
        type = 'gint',
        name = 'minute',
      ),
      Param(
        type = 'gdouble',
        name = 'seconds',
      ),
    ],
  ),
  'g_date_time_new_utc': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'gint',
        name = 'year',
      ),
      Param(
        type = 'gint',
        name = 'month',
      ),
      Param(
        type = 'gint',
        name = 'day',
      ),
      Param(
        type = 'gint',
        name = 'hour',
      ),
      Param(
        type = 'gint',
        name = 'minute',
      ),
      Param(
        type = 'gdouble',
        name = 'seconds',
      ),
    ],
  ),
  'g_date_time_add': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
      Param(
        type = 'GTimeSpan',
        name = 'timespan',
      ),
    ],
  ),
  'g_date_time_add_years': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
      Param(
        type = 'gint',
        name = 'years',
      ),
    ],
  ),
  'g_date_time_add_months': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
      Param(
        type = 'gint',
        name = 'months',
      ),
    ],
  ),
  'g_date_time_add_weeks': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
      Param(
        type = 'gint',
        name = 'weeks',
      ),
    ],
  ),
  'g_date_time_add_days': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
      Param(
        type = 'gint',
        name = 'days',
      ),
    ],
  ),
  'g_date_time_add_hours': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
      Param(
        type = 'gint',
        name = 'hours',
      ),
    ],
  ),
  'g_date_time_add_minutes': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
      Param(
        type = 'gint',
        name = 'minutes',
      ),
    ],
  ),
  'g_date_time_add_seconds': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
      Param(
        type = 'gdouble',
        name = 'seconds',
      ),
    ],
  ),
  'g_date_time_add_full': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
      Param(
        type = 'gint',
        name = 'years',
      ),
      Param(
        type = 'gint',
        name = 'months',
      ),
      Param(
        type = 'gint',
        name = 'days',
      ),
      Param(
        type = 'gint',
        name = 'hours',
      ),
      Param(
        type = 'gint',
        name = 'minutes',
      ),
      Param(
        type = 'gdouble',
        name = 'seconds',
      ),
    ],
  ),
  'g_date_time_compare': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'dt1',
      ),
      Param(
        type = 'gconstpointer',
        name = 'dt2',
      ),
    ],
  ),
  'g_date_time_difference': Spec(
    return_type = 'GTimeSpan',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'end',
      ),
      Param(
        type = 'GDateTime *',
        name = 'begin',
      ),
    ],
  ),
  'g_date_time_hash': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_equal': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'dt1',
      ),
      Param(
        type = 'gconstpointer',
        name = 'dt2',
      ),
    ],
  ),
  'g_date_time_get_ymd': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
      Param(
        type = 'gint *',
        name = 'year',
      ),
      Param(
        type = 'gint *',
        name = 'month',
      ),
      Param(
        type = 'gint *',
        name = 'day',
      ),
    ],
  ),
  'g_date_time_get_year': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_get_month': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_get_day_of_month': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_get_week_numbering_year': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_get_week_of_year': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_get_day_of_week': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_get_day_of_year': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_get_hour': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_get_minute': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_get_second': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_get_microsecond': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_get_seconds': Spec(
    return_type = 'gdouble',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_to_unix': Spec(
    return_type = 'gint64',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_to_timeval': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
      Param(
        type = 'GTimeVal *',
        name = 'tv',
      ),
    ],
  ),
  'g_date_time_get_utc_offset': Spec(
    return_type = 'GTimeSpan',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_get_timezone_abbreviation': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_is_daylight_savings': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_to_timezone': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
      Param(
        type = 'GTimeZone *',
        name = 'tz',
      ),
    ],
  ),
  'g_date_time_to_local': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_to_utc': Spec(
    return_type = 'GDateTime *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
    ],
  ),
  'g_date_time_format': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GDateTime *',
        name = 'datetime',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_dir_open': Spec(
    return_type = 'GDir *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'path',
      ),
      Param(
        type = 'guint',
        name = 'flags',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_dir_read_name': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GDir *',
        name = 'dir',
      ),
    ],
  ),
  'g_dir_rewind': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDir *',
        name = 'dir',
      ),
    ],
  ),
  'g_dir_close': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDir *',
        name = 'dir',
      ),
    ],
  ),
  'g_getenv': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'variable',
      ),
    ],
  ),
  'g_setenv': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'variable',
      ),
      Param(
        type = 'const gchar *',
        name = 'value',
      ),
      Param(
        type = 'gboolean',
        name = 'overwrite',
      ),
    ],
  ),
  'g_unsetenv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'variable',
      ),
    ],
  ),
  'g_listenv': Spec(
    return_type = 'gchar **',
    parameters = [
    ],
  ),
  'g_get_environ': Spec(
    return_type = 'gchar **',
    parameters = [
    ],
  ),
  'g_environ_getenv': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'gchar **',
        name = 'envp',
      ),
      Param(
        type = 'const gchar *',
        name = 'variable',
      ),
    ],
  ),
  'g_environ_setenv': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'gchar **',
        name = 'envp',
      ),
      Param(
        type = 'const gchar *',
        name = 'variable',
      ),
      Param(
        type = 'const gchar *',
        name = 'value',
      ),
      Param(
        type = 'gboolean',
        name = 'overwrite',
      ),
    ],
  ),
  'g_environ_unsetenv': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'gchar **',
        name = 'envp',
      ),
      Param(
        type = 'const gchar *',
        name = 'variable',
      ),
    ],
  ),
  'g_file_error_quark': Spec(
    return_type = 'GQuark',
    parameters = [
    ],
  ),
  'g_file_error_from_errno': Spec(
    return_type = 'GFileError',
    parameters = [
      Param(
        type = 'gint',
        name = 'err_no',
      ),
    ],
  ),
  'g_file_test': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'filename',
      ),
      Param(
        type = 'GFileTest',
        name = 'test',
      ),
    ],
  ),
  'g_file_get_contents': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'filename',
      ),
      Param(
        type = 'gchar **',
        name = 'contents',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_file_set_contents': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'filename',
      ),
      Param(
        type = 'const gchar *',
        name = 'contents',
      ),
      Param(
        type = 'gssize',
        name = 'length',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_file_read_link': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'filename',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_mkdtemp': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'tmpl',
      ),
    ],
  ),
  'g_mkdtemp_full': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'tmpl',
      ),
      Param(
        type = 'gint',
        name = 'mode',
      ),
    ],
  ),
  'g_mkstemp': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'tmpl',
      ),
    ],
  ),
  'g_mkstemp_full': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'tmpl',
      ),
      Param(
        type = 'gint',
        name = 'flags',
      ),
      Param(
        type = 'gint',
        name = 'mode',
      ),
    ],
  ),
  'g_file_open_tmp': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'tmpl',
      ),
      Param(
        type = 'gchar **',
        name = 'name_used',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_dir_make_tmp': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'tmpl',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_build_path': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'separator',
      ),
      Param(
        type = 'const gchar *',
        name = 'first_element',
      ),
    ],
  ),
  'g_build_pathv': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'separator',
      ),
      Param(
        type = 'gchar **',
        name = 'args',
      ),
    ],
  ),
  'g_build_filename': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'first_element',
      ),
    ],
  ),
  'g_build_filenamev': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gchar **',
        name = 'args',
      ),
    ],
  ),
  'g_mkdir_with_parents': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'pathname',
      ),
      Param(
        type = 'gint',
        name = 'mode',
      ),
    ],
  ),
  'g_path_is_absolute': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'file_name',
      ),
    ],
  ),
  'g_path_skip_root': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'file_name',
      ),
    ],
  ),
  'g_basename': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'file_name',
      ),
    ],
  ),
  'g_get_current_dir': Spec(
    return_type = 'gchar *',
    parameters = [
    ],
  ),
  'g_path_get_basename': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'file_name',
      ),
    ],
  ),
  'g_path_get_dirname': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'file_name',
      ),
    ],
  ),
  'g_strip_context': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'msgid',
      ),
      Param(
        type = 'const gchar *',
        name = 'msgval',
      ),
    ],
  ),
  'g_dgettext': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'domain',
      ),
      Param(
        type = 'const gchar *',
        name = 'msgid',
      ),
    ],
  ),
  'g_dcgettext': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'domain',
      ),
      Param(
        type = 'const gchar *',
        name = 'msgid',
      ),
      Param(
        type = 'gint',
        name = 'category',
      ),
    ],
  ),
  'g_dngettext': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'domain',
      ),
      Param(
        type = 'const gchar *',
        name = 'msgid',
      ),
      Param(
        type = 'const gchar *',
        name = 'msgid_plural',
      ),
      Param(
        type = 'gulong',
        name = 'n',
      ),
    ],
  ),
  'g_dpgettext': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'domain',
      ),
      Param(
        type = 'const gchar *',
        name = 'msgctxtid',
      ),
      Param(
        type = 'gsize',
        name = 'msgidoffset',
      ),
    ],
  ),
  'g_dpgettext2': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'domain',
      ),
      Param(
        type = 'const gchar *',
        name = 'context',
      ),
      Param(
        type = 'const gchar *',
        name = 'msgid',
      ),
    ],
  ),
  'g_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'mem',
      ),
    ],
  ),
  'g_clear_pointer': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer *',
        name = 'pp',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'destroy',
      ),
    ],
  ),
  'g_malloc': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gsize',
        name = 'n_bytes',
      ),
    ],
  ),
  'g_malloc0': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gsize',
        name = 'n_bytes',
      ),
    ],
  ),
  'g_realloc': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'mem',
      ),
      Param(
        type = 'gsize',
        name = 'n_bytes',
      ),
    ],
  ),
  'g_try_malloc': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gsize',
        name = 'n_bytes',
      ),
    ],
  ),
  'g_try_malloc0': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gsize',
        name = 'n_bytes',
      ),
    ],
  ),
  'g_try_realloc': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'mem',
      ),
      Param(
        type = 'gsize',
        name = 'n_bytes',
      ),
    ],
  ),
  'g_malloc_n': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gsize',
        name = 'n_blocks',
      ),
      Param(
        type = 'gsize',
        name = 'n_block_bytes',
      ),
    ],
  ),
  'g_malloc0_n': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gsize',
        name = 'n_blocks',
      ),
      Param(
        type = 'gsize',
        name = 'n_block_bytes',
      ),
    ],
  ),
  'g_realloc_n': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'mem',
      ),
      Param(
        type = 'gsize',
        name = 'n_blocks',
      ),
      Param(
        type = 'gsize',
        name = 'n_block_bytes',
      ),
    ],
  ),
  'g_try_malloc_n': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gsize',
        name = 'n_blocks',
      ),
      Param(
        type = 'gsize',
        name = 'n_block_bytes',
      ),
    ],
  ),
  'g_try_malloc0_n': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gsize',
        name = 'n_blocks',
      ),
      Param(
        type = 'gsize',
        name = 'n_block_bytes',
      ),
    ],
  ),
  'g_try_realloc_n': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'mem',
      ),
      Param(
        type = 'gsize',
        name = 'n_blocks',
      ),
      Param(
        type = 'gsize',
        name = 'n_block_bytes',
      ),
    ],
  ),
  'g_mem_set_vtable': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMemVTable *',
        name = 'vtable',
      ),
    ],
  ),
  'g_mem_is_system_malloc': Spec(
    return_type = 'gboolean',
    parameters = [
    ],
  ),
  'g_mem_profile': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'g_node_new': Spec(
    return_type = 'GNode *',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_node_destroy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'root',
      ),
    ],
  ),
  'g_node_unlink': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
    ],
  ),
  'g_node_copy_deep': Spec(
    return_type = 'GNode *',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
      Param(
        type = 'GCopyFunc',
        name = 'copy_func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_node_copy': Spec(
    return_type = 'GNode *',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
    ],
  ),
  'g_node_insert': Spec(
    return_type = 'GNode *',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'parent',
      ),
      Param(
        type = 'gint',
        name = 'position',
      ),
      Param(
        type = 'GNode *',
        name = 'node',
      ),
    ],
  ),
  'g_node_insert_before': Spec(
    return_type = 'GNode *',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'parent',
      ),
      Param(
        type = 'GNode *',
        name = 'sibling',
      ),
      Param(
        type = 'GNode *',
        name = 'node',
      ),
    ],
  ),
  'g_node_insert_after': Spec(
    return_type = 'GNode *',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'parent',
      ),
      Param(
        type = 'GNode *',
        name = 'sibling',
      ),
      Param(
        type = 'GNode *',
        name = 'node',
      ),
    ],
  ),
  'g_node_prepend': Spec(
    return_type = 'GNode *',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'parent',
      ),
      Param(
        type = 'GNode *',
        name = 'node',
      ),
    ],
  ),
  'g_node_n_nodes': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'root',
      ),
      Param(
        type = 'GTraverseFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_node_get_root': Spec(
    return_type = 'GNode *',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
    ],
  ),
  'g_node_is_ancestor': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
      Param(
        type = 'GNode *',
        name = 'descendant',
      ),
    ],
  ),
  'g_node_depth': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
    ],
  ),
  'g_node_find': Spec(
    return_type = 'GNode *',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'root',
      ),
      Param(
        type = 'GTraverseType',
        name = 'order',
      ),
      Param(
        type = 'GTraverseFlags',
        name = 'flags',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_node_traverse': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'root',
      ),
      Param(
        type = 'GTraverseType',
        name = 'order',
      ),
      Param(
        type = 'GTraverseFlags',
        name = 'flags',
      ),
      Param(
        type = 'gint',
        name = 'max_depth',
      ),
      Param(
        type = 'GNodeTraverseFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_node_max_height': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'root',
      ),
    ],
  ),
  'g_node_children_foreach': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
      Param(
        type = 'GTraverseFlags',
        name = 'flags',
      ),
      Param(
        type = 'GNodeForeachFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_node_reverse_children': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
    ],
  ),
  'g_node_n_children': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
    ],
  ),
  'g_node_nth_child': Spec(
    return_type = 'GNode *',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
      Param(
        type = 'guint',
        name = 'n',
      ),
    ],
  ),
  'g_node_last_child': Spec(
    return_type = 'GNode *',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
    ],
  ),
  'g_node_find_child': Spec(
    return_type = 'GNode *',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
      Param(
        type = 'GTraverseFlags',
        name = 'flags',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_node_child_position': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
      Param(
        type = 'GNode *',
        name = 'child',
      ),
    ],
  ),
  'g_node_child_index': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_node_first_sibling': Spec(
    return_type = 'GNode *',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
    ],
  ),
  'g_node_last_sibling': Spec(
    return_type = 'GNode *',
    parameters = [
      Param(
        type = 'GNode *',
        name = 'node',
      ),
    ],
  ),
  'g_list_alloc': Spec(
    return_type = 'GList *',
    parameters = [
    ],
  ),
  'g_list_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
    ],
  ),
  'g_list_free_1': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
    ],
  ),
  'g_list_free_full': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'free_func',
      ),
    ],
  ),
  'g_list_append': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_list_prepend': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_list_insert': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'gint',
        name = 'position',
      ),
    ],
  ),
  'g_list_insert_sorted': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GCompareFunc',
        name = 'func',
      ),
    ],
  ),
  'g_list_insert_sorted_with_data': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_list_insert_before': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'GList *',
        name = 'sibling',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_list_concat': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list1',
      ),
      Param(
        type = 'GList *',
        name = 'list2',
      ),
    ],
  ),
  'g_list_remove': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
    ],
  ),
  'g_list_remove_all': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
    ],
  ),
  'g_list_remove_link': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'GList *',
        name = 'llink',
      ),
    ],
  ),
  'g_list_delete_link': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'GList *',
        name = 'link_',
      ),
    ],
  ),
  'g_list_reverse': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
    ],
  ),
  'g_list_copy': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
    ],
  ),
  'g_list_copy_deep': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'GCopyFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_list_nth': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'guint',
        name = 'n',
      ),
    ],
  ),
  'g_list_nth_prev': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'guint',
        name = 'n',
      ),
    ],
  ),
  'g_list_find': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
    ],
  ),
  'g_list_find_custom': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
      Param(
        type = 'GCompareFunc',
        name = 'func',
      ),
    ],
  ),
  'g_list_position': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'GList *',
        name = 'llink',
      ),
    ],
  ),
  'g_list_index': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
    ],
  ),
  'g_list_last': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
    ],
  ),
  'g_list_first': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
    ],
  ),
  'g_list_length': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
    ],
  ),
  'g_list_foreach': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'GFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_list_sort': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'GCompareFunc',
        name = 'compare_func',
      ),
    ],
  ),
  'g_list_sort_with_data': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'compare_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_list_nth_data': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GList *',
        name = 'list',
      ),
      Param(
        type = 'guint',
        name = 'n',
      ),
    ],
  ),
  'g_hash_table_new': Spec(
    return_type = 'GHashTable *',
    parameters = [
      Param(
        type = 'GHashFunc',
        name = 'hash_func',
      ),
      Param(
        type = 'GEqualFunc',
        name = 'key_equal_func',
      ),
    ],
  ),
  'g_hash_table_new_full': Spec(
    return_type = 'GHashTable *',
    parameters = [
      Param(
        type = 'GHashFunc',
        name = 'hash_func',
      ),
      Param(
        type = 'GEqualFunc',
        name = 'key_equal_func',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'key_destroy_func',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'value_destroy_func',
      ),
    ],
  ),
  'g_hash_table_destroy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
    ],
  ),
  'g_hash_table_insert': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
      Param(
        type = 'gpointer',
        name = 'key',
      ),
      Param(
        type = 'gpointer',
        name = 'value',
      ),
    ],
  ),
  'g_hash_table_replace': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
      Param(
        type = 'gpointer',
        name = 'key',
      ),
      Param(
        type = 'gpointer',
        name = 'value',
      ),
    ],
  ),
  'g_hash_table_add': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
      Param(
        type = 'gpointer',
        name = 'key',
      ),
    ],
  ),
  'g_hash_table_remove': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
      Param(
        type = 'gconstpointer',
        name = 'key',
      ),
    ],
  ),
  'g_hash_table_remove_all': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
    ],
  ),
  'g_hash_table_steal': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
      Param(
        type = 'gconstpointer',
        name = 'key',
      ),
    ],
  ),
  'g_hash_table_steal_all': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
    ],
  ),
  'g_hash_table_lookup': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
      Param(
        type = 'gconstpointer',
        name = 'key',
      ),
    ],
  ),
  'g_hash_table_contains': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
      Param(
        type = 'gconstpointer',
        name = 'key',
      ),
    ],
  ),
  'g_hash_table_lookup_extended': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
      Param(
        type = 'gconstpointer',
        name = 'lookup_key',
      ),
      Param(
        type = 'gpointer *',
        name = 'orig_key',
      ),
      Param(
        type = 'gpointer *',
        name = 'value',
      ),
    ],
  ),
  'g_hash_table_foreach': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
      Param(
        type = 'GHFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_hash_table_find': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
      Param(
        type = 'GHRFunc',
        name = 'predicate',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_hash_table_foreach_remove': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
      Param(
        type = 'GHRFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_hash_table_foreach_steal': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
      Param(
        type = 'GHRFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_hash_table_size': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
    ],
  ),
  'g_hash_table_get_keys': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
    ],
  ),
  'g_hash_table_get_values': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
    ],
  ),
  'g_hash_table_iter_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHashTableIter *',
        name = 'iter',
      ),
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
    ],
  ),
  'g_hash_table_iter_next': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GHashTableIter *',
        name = 'iter',
      ),
      Param(
        type = 'gpointer *',
        name = 'key',
      ),
      Param(
        type = 'gpointer *',
        name = 'value',
      ),
    ],
  ),
  'g_hash_table_iter_get_hash_table': Spec(
    return_type = 'GHashTable *',
    parameters = [
      Param(
        type = 'GHashTableIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_hash_table_iter_remove': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHashTableIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_hash_table_iter_replace': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHashTableIter *',
        name = 'iter',
      ),
      Param(
        type = 'gpointer',
        name = 'value',
      ),
    ],
  ),
  'g_hash_table_iter_steal': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHashTableIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_hash_table_ref': Spec(
    return_type = 'GHashTable *',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
    ],
  ),
  'g_hash_table_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHashTable *',
        name = 'hash_table',
      ),
    ],
  ),
  'g_str_equal': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'v1',
      ),
      Param(
        type = 'gconstpointer',
        name = 'v2',
      ),
    ],
  ),
  'g_str_hash': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'v',
      ),
    ],
  ),
  'g_int_equal': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'v1',
      ),
      Param(
        type = 'gconstpointer',
        name = 'v2',
      ),
    ],
  ),
  'g_int_hash': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'v',
      ),
    ],
  ),
  'g_int64_equal': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'v1',
      ),
      Param(
        type = 'gconstpointer',
        name = 'v2',
      ),
    ],
  ),
  'g_int64_hash': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'v',
      ),
    ],
  ),
  'g_double_equal': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'v1',
      ),
      Param(
        type = 'gconstpointer',
        name = 'v2',
      ),
    ],
  ),
  'g_double_hash': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'v',
      ),
    ],
  ),
  'g_direct_hash': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'v',
      ),
    ],
  ),
  'g_direct_equal': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'v1',
      ),
      Param(
        type = 'gconstpointer',
        name = 'v2',
      ),
    ],
  ),
  'g_hmac_new': Spec(
    return_type = 'GHmac *',
    parameters = [
      Param(
        type = 'GChecksumType',
        name = 'digest_type',
      ),
      Param(
        type = 'const guchar *',
        name = 'key',
      ),
      Param(
        type = 'gsize',
        name = 'key_len',
      ),
    ],
  ),
  'g_hmac_copy': Spec(
    return_type = 'GHmac *',
    parameters = [
      Param(
        type = 'const GHmac *',
        name = 'hmac',
      ),
    ],
  ),
  'g_hmac_ref': Spec(
    return_type = 'GHmac *',
    parameters = [
      Param(
        type = 'GHmac *',
        name = 'hmac',
      ),
    ],
  ),
  'g_hmac_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHmac *',
        name = 'hmac',
      ),
    ],
  ),
  'g_hmac_update': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHmac *',
        name = 'hmac',
      ),
      Param(
        type = 'const guchar *',
        name = 'data',
      ),
      Param(
        type = 'gssize',
        name = 'length',
      ),
    ],
  ),
  'g_hmac_get_string': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GHmac *',
        name = 'hmac',
      ),
    ],
  ),
  'g_hmac_get_digest': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHmac *',
        name = 'hmac',
      ),
      Param(
        type = 'guint8 *',
        name = 'buffer',
      ),
      Param(
        type = 'gsize *',
        name = 'digest_len',
      ),
    ],
  ),
  'g_compute_hmac_for_data': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GChecksumType',
        name = 'digest_type',
      ),
      Param(
        type = 'const guchar *',
        name = 'key',
      ),
      Param(
        type = 'gsize',
        name = 'key_len',
      ),
      Param(
        type = 'const guchar *',
        name = 'data',
      ),
      Param(
        type = 'gsize',
        name = 'length',
      ),
    ],
  ),
  'g_compute_hmac_for_string': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GChecksumType',
        name = 'digest_type',
      ),
      Param(
        type = 'const guchar *',
        name = 'key',
      ),
      Param(
        type = 'gsize',
        name = 'key_len',
      ),
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'length',
      ),
    ],
  ),
  'g_hook_list_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'guint',
        name = 'hook_size',
      ),
    ],
  ),
  'g_hook_list_clear': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
    ],
  ),
  'g_hook_alloc': Spec(
    return_type = 'GHook *',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
    ],
  ),
  'g_hook_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'GHook *',
        name = 'hook',
      ),
    ],
  ),
  'g_hook_ref': Spec(
    return_type = 'GHook *',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'GHook *',
        name = 'hook',
      ),
    ],
  ),
  'g_hook_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'GHook *',
        name = 'hook',
      ),
    ],
  ),
  'g_hook_destroy': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'gulong',
        name = 'hook_id',
      ),
    ],
  ),
  'g_hook_destroy_link': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'GHook *',
        name = 'hook',
      ),
    ],
  ),
  'g_hook_prepend': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'GHook *',
        name = 'hook',
      ),
    ],
  ),
  'g_hook_insert_before': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'GHook *',
        name = 'sibling',
      ),
      Param(
        type = 'GHook *',
        name = 'hook',
      ),
    ],
  ),
  'g_hook_insert_sorted': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'GHook *',
        name = 'hook',
      ),
      Param(
        type = 'GHookCompareFunc',
        name = 'func',
      ),
    ],
  ),
  'g_hook_get': Spec(
    return_type = 'GHook *',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'gulong',
        name = 'hook_id',
      ),
    ],
  ),
  'g_hook_find': Spec(
    return_type = 'GHook *',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'gboolean',
        name = 'need_valids',
      ),
      Param(
        type = 'GHookFindFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_hook_find_data': Spec(
    return_type = 'GHook *',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'gboolean',
        name = 'need_valids',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_hook_find_func': Spec(
    return_type = 'GHook *',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'gboolean',
        name = 'need_valids',
      ),
      Param(
        type = 'gpointer',
        name = 'func',
      ),
    ],
  ),
  'g_hook_find_func_data': Spec(
    return_type = 'GHook *',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'gboolean',
        name = 'need_valids',
      ),
      Param(
        type = 'gpointer',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_hook_first_valid': Spec(
    return_type = 'GHook *',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'gboolean',
        name = 'may_be_in_call',
      ),
    ],
  ),
  'g_hook_next_valid': Spec(
    return_type = 'GHook *',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'GHook *',
        name = 'hook',
      ),
      Param(
        type = 'gboolean',
        name = 'may_be_in_call',
      ),
    ],
  ),
  'g_hook_compare_ids': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GHook *',
        name = 'new_hook',
      ),
      Param(
        type = 'GHook *',
        name = 'sibling',
      ),
    ],
  ),
  'g_hook_list_invoke': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'gboolean',
        name = 'may_recurse',
      ),
    ],
  ),
  'g_hook_list_invoke_check': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'gboolean',
        name = 'may_recurse',
      ),
    ],
  ),
  'g_hook_list_marshal': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'gboolean',
        name = 'may_recurse',
      ),
      Param(
        type = 'GHookMarshaller',
        name = 'marshaller',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_hook_list_marshal_check': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GHookList *',
        name = 'hook_list',
      ),
      Param(
        type = 'gboolean',
        name = 'may_recurse',
      ),
      Param(
        type = 'GHookCheckMarshaller',
        name = 'marshaller',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_hostname_is_non_ascii': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'hostname',
      ),
    ],
  ),
  'g_hostname_is_ascii_encoded': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'hostname',
      ),
    ],
  ),
  'g_hostname_is_ip_address': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'hostname',
      ),
    ],
  ),
  'g_hostname_to_ascii': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'hostname',
      ),
    ],
  ),
  'g_hostname_to_unicode': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'hostname',
      ),
    ],
  ),
  'g_poll': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GPollFD *',
        name = 'fds',
      ),
      Param(
        type = 'guint',
        name = 'nfds',
      ),
      Param(
        type = 'gint',
        name = 'timeout',
      ),
    ],
  ),
  'g_slist_alloc': Spec(
    return_type = 'GSList *',
    parameters = [
    ],
  ),
  'g_slist_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
    ],
  ),
  'g_slist_free_1': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
    ],
  ),
  'g_slist_free_full': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'free_func',
      ),
    ],
  ),
  'g_slist_append': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_slist_prepend': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_slist_insert': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'gint',
        name = 'position',
      ),
    ],
  ),
  'g_slist_insert_sorted': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GCompareFunc',
        name = 'func',
      ),
    ],
  ),
  'g_slist_insert_sorted_with_data': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_slist_insert_before': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'slist',
      ),
      Param(
        type = 'GSList *',
        name = 'sibling',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_slist_concat': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list1',
      ),
      Param(
        type = 'GSList *',
        name = 'list2',
      ),
    ],
  ),
  'g_slist_remove': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
    ],
  ),
  'g_slist_remove_all': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
    ],
  ),
  'g_slist_remove_link': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'GSList *',
        name = 'link_',
      ),
    ],
  ),
  'g_slist_delete_link': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'GSList *',
        name = 'link_',
      ),
    ],
  ),
  'g_slist_reverse': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
    ],
  ),
  'g_slist_copy': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
    ],
  ),
  'g_slist_copy_deep': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'GCopyFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_slist_nth': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'guint',
        name = 'n',
      ),
    ],
  ),
  'g_slist_find': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
    ],
  ),
  'g_slist_find_custom': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
      Param(
        type = 'GCompareFunc',
        name = 'func',
      ),
    ],
  ),
  'g_slist_position': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'GSList *',
        name = 'llink',
      ),
    ],
  ),
  'g_slist_index': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
    ],
  ),
  'g_slist_last': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
    ],
  ),
  'g_slist_length': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
    ],
  ),
  'g_slist_foreach': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'GFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_slist_sort': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'GCompareFunc',
        name = 'compare_func',
      ),
    ],
  ),
  'g_slist_sort_with_data': Spec(
    return_type = 'GSList *',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'compare_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_slist_nth_data': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GSList *',
        name = 'list',
      ),
      Param(
        type = 'guint',
        name = 'n',
      ),
    ],
  ),
  'g_main_context_new': Spec(
    return_type = 'GMainContext *',
    parameters = [
    ],
  ),
  'g_main_context_ref': Spec(
    return_type = 'GMainContext *',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
    ],
  ),
  'g_main_context_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
    ],
  ),
  'g_main_context_default': Spec(
    return_type = 'GMainContext *',
    parameters = [
    ],
  ),
  'g_main_context_iteration': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
      Param(
        type = 'gboolean',
        name = 'may_block',
      ),
    ],
  ),
  'g_main_context_pending': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
    ],
  ),
  'g_main_context_find_source_by_id': Spec(
    return_type = 'GSource *',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
      Param(
        type = 'guint',
        name = 'source_id',
      ),
    ],
  ),
  'g_main_context_find_source_by_user_data': Spec(
    return_type = 'GSource *',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_main_context_find_source_by_funcs_user_data': Spec(
    return_type = 'GSource *',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
      Param(
        type = 'GSourceFuncs *',
        name = 'funcs',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_main_context_wakeup': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
    ],
  ),
  'g_main_context_acquire': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
    ],
  ),
  'g_main_context_release': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
    ],
  ),
  'g_main_context_is_owner': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
    ],
  ),
  'g_main_context_wait': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
      Param(
        type = 'GCond *',
        name = 'cond',
      ),
      Param(
        type = 'GMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_main_context_prepare': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
      Param(
        type = 'gint *',
        name = 'priority',
      ),
    ],
  ),
  'g_main_context_query': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
      Param(
        type = 'gint',
        name = 'max_priority',
      ),
      Param(
        type = 'gint *',
        name = 'timeout_',
      ),
      Param(
        type = 'GPollFD *',
        name = 'fds',
      ),
      Param(
        type = 'gint',
        name = 'n_fds',
      ),
    ],
  ),
  'g_main_context_check': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
      Param(
        type = 'gint',
        name = 'max_priority',
      ),
      Param(
        type = 'GPollFD *',
        name = 'fds',
      ),
      Param(
        type = 'gint',
        name = 'n_fds',
      ),
    ],
  ),
  'g_main_context_dispatch': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
    ],
  ),
  'g_main_context_set_poll_func': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
      Param(
        type = 'GPollFunc',
        name = 'func',
      ),
    ],
  ),
  'g_main_context_get_poll_func': Spec(
    return_type = 'GPollFunc',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
    ],
  ),
  'g_main_context_add_poll': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
      Param(
        type = 'GPollFD *',
        name = 'fd',
      ),
      Param(
        type = 'gint',
        name = 'priority',
      ),
    ],
  ),
  'g_main_context_remove_poll': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
      Param(
        type = 'GPollFD *',
        name = 'fd',
      ),
    ],
  ),
  'g_main_depth': Spec(
    return_type = 'gint',
    parameters = [
    ],
  ),
  'g_main_current_source': Spec(
    return_type = 'GSource *',
    parameters = [
    ],
  ),
  'g_main_context_push_thread_default': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
    ],
  ),
  'g_main_context_pop_thread_default': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
    ],
  ),
  'g_main_context_get_thread_default': Spec(
    return_type = 'GMainContext *',
    parameters = [
    ],
  ),
  'g_main_context_ref_thread_default': Spec(
    return_type = 'GMainContext *',
    parameters = [
    ],
  ),
  'g_main_loop_new': Spec(
    return_type = 'GMainLoop *',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
      Param(
        type = 'gboolean',
        name = 'is_running',
      ),
    ],
  ),
  'g_main_loop_run': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMainLoop *',
        name = 'loop',
      ),
    ],
  ),
  'g_main_loop_quit': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMainLoop *',
        name = 'loop',
      ),
    ],
  ),
  'g_main_loop_ref': Spec(
    return_type = 'GMainLoop *',
    parameters = [
      Param(
        type = 'GMainLoop *',
        name = 'loop',
      ),
    ],
  ),
  'g_main_loop_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMainLoop *',
        name = 'loop',
      ),
    ],
  ),
  'g_main_loop_is_running': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GMainLoop *',
        name = 'loop',
      ),
    ],
  ),
  'g_main_loop_get_context': Spec(
    return_type = 'GMainContext *',
    parameters = [
      Param(
        type = 'GMainLoop *',
        name = 'loop',
      ),
    ],
  ),
  'g_source_new': Spec(
    return_type = 'GSource *',
    parameters = [
      Param(
        type = 'GSourceFuncs *',
        name = 'source_funcs',
      ),
      Param(
        type = 'guint',
        name = 'struct_size',
      ),
    ],
  ),
  'g_source_ref': Spec(
    return_type = 'GSource *',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
    ],
  ),
  'g_source_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
    ],
  ),
  'g_source_attach': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
    ],
  ),
  'g_source_destroy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
    ],
  ),
  'g_source_set_priority': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
      Param(
        type = 'gint',
        name = 'priority',
      ),
    ],
  ),
  'g_source_get_priority': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
    ],
  ),
  'g_source_set_can_recurse': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
      Param(
        type = 'gboolean',
        name = 'can_recurse',
      ),
    ],
  ),
  'g_source_get_can_recurse': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
    ],
  ),
  'g_source_get_id': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
    ],
  ),
  'g_source_get_context': Spec(
    return_type = 'GMainContext *',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
    ],
  ),
  'g_source_set_callback': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
      Param(
        type = 'GSourceFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'notify',
      ),
    ],
  ),
  'g_source_set_funcs': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
      Param(
        type = 'GSourceFuncs *',
        name = 'funcs',
      ),
    ],
  ),
  'g_source_is_destroyed': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
    ],
  ),
  'g_source_set_name': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
      Param(
        type = 'const char *',
        name = 'name',
      ),
    ],
  ),
  'g_source_get_name': Spec(
    return_type = 'const char *',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
    ],
  ),
  'g_source_set_name_by_id': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'guint',
        name = 'tag',
      ),
      Param(
        type = 'const char *',
        name = 'name',
      ),
    ],
  ),
  'g_source_set_callback_indirect': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
      Param(
        type = 'gpointer',
        name = 'callback_data',
      ),
      Param(
        type = 'GSourceCallbackFuncs *',
        name = 'callback_funcs',
      ),
    ],
  ),
  'g_source_add_poll': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
      Param(
        type = 'GPollFD *',
        name = 'fd',
      ),
    ],
  ),
  'g_source_remove_poll': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
      Param(
        type = 'GPollFD *',
        name = 'fd',
      ),
    ],
  ),
  'g_source_add_child_source': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
      Param(
        type = 'GSource *',
        name = 'child_source',
      ),
    ],
  ),
  'g_source_remove_child_source': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
      Param(
        type = 'GSource *',
        name = 'child_source',
      ),
    ],
  ),
  'g_source_get_current_time': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
      Param(
        type = 'GTimeVal *',
        name = 'timeval',
      ),
    ],
  ),
  'g_source_get_time': Spec(
    return_type = 'gint64',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
    ],
  ),
  'g_idle_source_new': Spec(
    return_type = 'GSource *',
    parameters = [
    ],
  ),
  'g_child_watch_source_new': Spec(
    return_type = 'GSource *',
    parameters = [
      Param(
        type = 'GPid',
        name = 'pid',
      ),
    ],
  ),
  'g_timeout_source_new': Spec(
    return_type = 'GSource *',
    parameters = [
      Param(
        type = 'guint',
        name = 'interval',
      ),
    ],
  ),
  'g_timeout_source_new_seconds': Spec(
    return_type = 'GSource *',
    parameters = [
      Param(
        type = 'guint',
        name = 'interval',
      ),
    ],
  ),
  'g_get_current_time': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTimeVal *',
        name = 'result',
      ),
    ],
  ),
  'g_get_monotonic_time': Spec(
    return_type = 'gint64',
    parameters = [
    ],
  ),
  'g_get_real_time': Spec(
    return_type = 'gint64',
    parameters = [
    ],
  ),
  'g_source_remove': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'guint',
        name = 'tag',
      ),
    ],
  ),
  'g_source_remove_by_user_data': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_source_remove_by_funcs_user_data': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GSourceFuncs *',
        name = 'funcs',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_timeout_add_full': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gint',
        name = 'priority',
      ),
      Param(
        type = 'guint',
        name = 'interval',
      ),
      Param(
        type = 'GSourceFunc',
        name = 'function',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'notify',
      ),
    ],
  ),
  'g_timeout_add': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'guint',
        name = 'interval',
      ),
      Param(
        type = 'GSourceFunc',
        name = 'function',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_timeout_add_seconds_full': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gint',
        name = 'priority',
      ),
      Param(
        type = 'guint',
        name = 'interval',
      ),
      Param(
        type = 'GSourceFunc',
        name = 'function',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'notify',
      ),
    ],
  ),
  'g_timeout_add_seconds': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'guint',
        name = 'interval',
      ),
      Param(
        type = 'GSourceFunc',
        name = 'function',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_child_watch_add_full': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gint',
        name = 'priority',
      ),
      Param(
        type = 'GPid',
        name = 'pid',
      ),
      Param(
        type = 'GChildWatchFunc',
        name = 'function',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'notify',
      ),
    ],
  ),
  'g_child_watch_add': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GPid',
        name = 'pid',
      ),
      Param(
        type = 'GChildWatchFunc',
        name = 'function',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_idle_add': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GSourceFunc',
        name = 'function',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_idle_add_full': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gint',
        name = 'priority',
      ),
      Param(
        type = 'GSourceFunc',
        name = 'function',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'notify',
      ),
    ],
  ),
  'g_idle_remove_by_data': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_main_context_invoke_full': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
      Param(
        type = 'gint',
        name = 'priority',
      ),
      Param(
        type = 'GSourceFunc',
        name = 'function',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'notify',
      ),
    ],
  ),
  'g_main_context_invoke': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMainContext *',
        name = 'context',
      ),
      Param(
        type = 'GSourceFunc',
        name = 'function',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_unicode_script_to_iso15924': Spec(
    return_type = 'guint32',
    parameters = [
      Param(
        type = 'GUnicodeScript',
        name = 'script',
      ),
    ],
  ),
  'g_unicode_script_from_iso15924': Spec(
    return_type = 'GUnicodeScript',
    parameters = [
      Param(
        type = 'guint32',
        name = 'iso15924',
      ),
    ],
  ),
  'g_unichar_isalnum': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_isalpha': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_iscntrl': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_isdigit': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_isgraph': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_islower': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_isprint': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_ispunct': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_isspace': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_isupper': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_isxdigit': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_istitle': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_isdefined': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_iswide': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_iswide_cjk': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_iszerowidth': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_ismark': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_toupper': Spec(
    return_type = 'gunichar',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_tolower': Spec(
    return_type = 'gunichar',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_totitle': Spec(
    return_type = 'gunichar',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_digit_value': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_xdigit_value': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_type': Spec(
    return_type = 'GUnicodeType',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_break_type': Spec(
    return_type = 'GUnicodeBreakType',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_unichar_combining_class': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'uc',
      ),
    ],
  ),
  'g_unichar_get_mirror_char': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'ch',
      ),
      Param(
        type = 'gunichar *',
        name = 'mirrored_ch',
      ),
    ],
  ),
  'g_unichar_get_script': Spec(
    return_type = 'GUnicodeScript',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'ch',
      ),
    ],
  ),
  'g_unichar_validate': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'ch',
      ),
    ],
  ),
  'g_unichar_compose': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'a',
      ),
      Param(
        type = 'gunichar',
        name = 'b',
      ),
      Param(
        type = 'gunichar *',
        name = 'ch',
      ),
    ],
  ),
  'g_unichar_decompose': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'ch',
      ),
      Param(
        type = 'gunichar *',
        name = 'a',
      ),
      Param(
        type = 'gunichar *',
        name = 'b',
      ),
    ],
  ),
  'g_unichar_fully_decompose': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'ch',
      ),
      Param(
        type = 'gboolean',
        name = 'compat',
      ),
      Param(
        type = 'gunichar *',
        name = 'result',
      ),
      Param(
        type = 'gsize',
        name = 'result_len',
      ),
    ],
  ),
  'g_unicode_canonical_ordering': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gunichar *',
        name = 'string',
      ),
      Param(
        type = 'gsize',
        name = 'len',
      ),
    ],
  ),
  'g_unicode_canonical_decomposition': Spec(
    return_type = 'gunichar *',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'ch',
      ),
      Param(
        type = 'gsize *',
        name = 'result_len',
      ),
    ],
  ),
  'g_utf8_get_char': Spec(
    return_type = 'gunichar',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'p',
      ),
    ],
  ),
  'g_utf8_get_char_validated': Spec(
    return_type = 'gunichar',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'p',
      ),
      Param(
        type = 'gssize',
        name = 'max_len',
      ),
    ],
  ),
  'g_utf8_offset_to_pointer': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'glong',
        name = 'offset',
      ),
    ],
  ),
  'g_utf8_pointer_to_offset': Spec(
    return_type = 'glong',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'const gchar *',
        name = 'pos',
      ),
    ],
  ),
  'g_utf8_prev_char': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'p',
      ),
    ],
  ),
  'g_utf8_find_next_char': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'p',
      ),
      Param(
        type = 'const gchar *',
        name = 'end',
      ),
    ],
  ),
  'g_utf8_find_prev_char': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'const gchar *',
        name = 'p',
      ),
    ],
  ),
  'g_utf8_strlen': Spec(
    return_type = 'glong',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'p',
      ),
      Param(
        type = 'gssize',
        name = 'max',
      ),
    ],
  ),
  'g_utf8_substring': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'glong',
        name = 'start_pos',
      ),
      Param(
        type = 'glong',
        name = 'end_pos',
      ),
    ],
  ),
  'g_utf8_strncpy': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'dest',
      ),
      Param(
        type = 'const gchar *',
        name = 'src',
      ),
      Param(
        type = 'gsize',
        name = 'n',
      ),
    ],
  ),
  'g_utf8_strchr': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'p',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_utf8_strrchr': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'p',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
      Param(
        type = 'gunichar',
        name = 'c',
      ),
    ],
  ),
  'g_utf8_strreverse': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  'g_utf8_to_utf16': Spec(
    return_type = 'gunichar2 *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'glong',
        name = 'len',
      ),
      Param(
        type = 'glong *',
        name = 'items_read',
      ),
      Param(
        type = 'glong *',
        name = 'items_written',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_utf8_to_ucs4': Spec(
    return_type = 'gunichar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'glong',
        name = 'len',
      ),
      Param(
        type = 'glong *',
        name = 'items_read',
      ),
      Param(
        type = 'glong *',
        name = 'items_written',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_utf8_to_ucs4_fast': Spec(
    return_type = 'gunichar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'glong',
        name = 'len',
      ),
      Param(
        type = 'glong *',
        name = 'items_written',
      ),
    ],
  ),
  'g_utf16_to_ucs4': Spec(
    return_type = 'gunichar *',
    parameters = [
      Param(
        type = 'const gunichar2 *',
        name = 'str',
      ),
      Param(
        type = 'glong',
        name = 'len',
      ),
      Param(
        type = 'glong *',
        name = 'items_read',
      ),
      Param(
        type = 'glong *',
        name = 'items_written',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_utf16_to_utf8': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gunichar2 *',
        name = 'str',
      ),
      Param(
        type = 'glong',
        name = 'len',
      ),
      Param(
        type = 'glong *',
        name = 'items_read',
      ),
      Param(
        type = 'glong *',
        name = 'items_written',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_ucs4_to_utf16': Spec(
    return_type = 'gunichar2 *',
    parameters = [
      Param(
        type = 'const gunichar *',
        name = 'str',
      ),
      Param(
        type = 'glong',
        name = 'len',
      ),
      Param(
        type = 'glong *',
        name = 'items_read',
      ),
      Param(
        type = 'glong *',
        name = 'items_written',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_ucs4_to_utf8': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gunichar *',
        name = 'str',
      ),
      Param(
        type = 'glong',
        name = 'len',
      ),
      Param(
        type = 'glong *',
        name = 'items_read',
      ),
      Param(
        type = 'glong *',
        name = 'items_written',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_unichar_to_utf8': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gunichar',
        name = 'c',
      ),
      Param(
        type = 'gchar *',
        name = 'outbuf',
      ),
    ],
  ),
  'g_utf8_validate': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'max_len',
      ),
      Param(
        type = 'const gchar **',
        name = 'end',
      ),
    ],
  ),
  'g_utf8_strup': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  'g_utf8_strdown': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  'g_utf8_casefold': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  'g_utf8_normalize': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
      Param(
        type = 'GNormalizeMode',
        name = 'mode',
      ),
    ],
  ),
  'g_utf8_collate': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str1',
      ),
      Param(
        type = 'const gchar *',
        name = 'str2',
      ),
    ],
  ),
  'g_utf8_collate_key': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  'g_utf8_collate_key_for_filename': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  '_g_utf8_make_valid': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
    ],
  ),
  'g_get_user_name': Spec(
    return_type = 'const gchar *',
    parameters = [
    ],
  ),
  'g_get_real_name': Spec(
    return_type = 'const gchar *',
    parameters = [
    ],
  ),
  'g_get_home_dir': Spec(
    return_type = 'const gchar *',
    parameters = [
    ],
  ),
  'g_get_tmp_dir': Spec(
    return_type = 'const gchar *',
    parameters = [
    ],
  ),
  'g_get_host_name': Spec(
    return_type = 'const gchar *',
    parameters = [
    ],
  ),
  'g_get_prgname': Spec(
    return_type = 'gchar *',
    parameters = [
    ],
  ),
  'g_set_prgname': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'prgname',
      ),
    ],
  ),
  'g_get_application_name': Spec(
    return_type = 'const gchar *',
    parameters = [
    ],
  ),
  'g_set_application_name': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'application_name',
      ),
    ],
  ),
  'g_reload_user_special_dirs_cache': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'g_get_user_data_dir': Spec(
    return_type = 'const gchar *',
    parameters = [
    ],
  ),
  'g_get_user_config_dir': Spec(
    return_type = 'const gchar *',
    parameters = [
    ],
  ),
  'g_get_user_cache_dir': Spec(
    return_type = 'const gchar *',
    parameters = [
    ],
  ),
  'g_get_system_data_dirs': Spec(
    return_type = 'const gchar *const *',
    parameters = [
    ],
  ),
  'g_get_system_config_dirs': Spec(
    return_type = 'const gchar *const *',
    parameters = [
    ],
  ),
  'g_get_user_runtime_dir': Spec(
    return_type = 'const gchar *',
    parameters = [
    ],
  ),
  'g_get_user_special_dir': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GUserDirectory',
        name = 'directory',
      ),
    ],
  ),
  'g_parse_debug_string': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'const GDebugKey *',
        name = 'keys',
      ),
      Param(
        type = 'guint',
        name = 'nkeys',
      ),
    ],
  ),
  'g_snprintf': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'string',
      ),
      Param(
        type = 'gulong',
        name = 'n',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_vsnprintf': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'string',
      ),
      Param(
        type = 'gulong',
        name = 'n',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
    ],
  ),
  'g_nullify_pointer': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer *',
        name = 'nullify_location',
      ),
    ],
  ),
  'g_format_size_full': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'guint64',
        name = 'size',
      ),
      Param(
        type = 'GFormatSizeFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_format_size': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'guint64',
        name = 'size',
      ),
    ],
  ),
  'g_format_size_for_display': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'goffset',
        name = 'size',
      ),
    ],
  ),
  'g_atexit': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVoidFunc',
        name = 'func',
      ),
    ],
  ),
  'g_find_program_in_path': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'program',
      ),
    ],
  ),
  'g_bit_nth_lsf': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gulong',
        name = 'mask',
      ),
      Param(
        type = 'gint',
        name = 'nth_bit',
      ),
    ],
  ),
  'g_bit_nth_msf': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gulong',
        name = 'mask',
      ),
      Param(
        type = 'gint',
        name = 'nth_bit',
      ),
    ],
  ),
  'g_bit_storage': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gulong',
        name = 'number',
      ),
    ],
  ),
  'g_bit_nth_lsf': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gulong',
        name = 'mask',
      ),
      Param(
        type = 'gint',
        name = 'nth_bit',
      ),
    ],
  ),
  'g_bit_nth_msf': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gulong',
        name = 'mask',
      ),
      Param(
        type = 'gint',
        name = 'nth_bit',
      ),
    ],
  ),
  'g_bit_storage': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gulong',
        name = 'number',
      ),
    ],
  ),
  'g_string_new': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'init',
      ),
    ],
  ),
  'g_string_new_len': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'init',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  'g_string_sized_new': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'gsize',
        name = 'dfl_size',
      ),
    ],
  ),
  'g_string_free': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gboolean',
        name = 'free_segment',
      ),
    ],
  ),
  'g_string_free_to_bytes': Spec(
    return_type = 'GBytes *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
    ],
  ),
  'g_string_equal': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GString *',
        name = 'v',
      ),
      Param(
        type = 'const GString *',
        name = 'v2',
      ),
    ],
  ),
  'g_string_hash': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'const GString *',
        name = 'str',
      ),
    ],
  ),
  'g_string_assign': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'rval',
      ),
    ],
  ),
  'g_string_truncate': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gsize',
        name = 'len',
      ),
    ],
  ),
  'g_string_set_size': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gsize',
        name = 'len',
      ),
    ],
  ),
  'g_string_insert_len': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gssize',
        name = 'pos',
      ),
      Param(
        type = 'const gchar *',
        name = 'val',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  'g_string_append': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'val',
      ),
    ],
  ),
  'g_string_append_len': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'val',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  'g_string_append_c': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gchar',
        name = 'c',
      ),
    ],
  ),
  'g_string_append_unichar': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gunichar',
        name = 'wc',
      ),
    ],
  ),
  'g_string_prepend': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'val',
      ),
    ],
  ),
  'g_string_prepend_c': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gchar',
        name = 'c',
      ),
    ],
  ),
  'g_string_prepend_unichar': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gunichar',
        name = 'wc',
      ),
    ],
  ),
  'g_string_prepend_len': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'val',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  'g_string_insert': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gssize',
        name = 'pos',
      ),
      Param(
        type = 'const gchar *',
        name = 'val',
      ),
    ],
  ),
  'g_string_insert_c': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gssize',
        name = 'pos',
      ),
      Param(
        type = 'gchar',
        name = 'c',
      ),
    ],
  ),
  'g_string_insert_unichar': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gssize',
        name = 'pos',
      ),
      Param(
        type = 'gunichar',
        name = 'wc',
      ),
    ],
  ),
  'g_string_overwrite': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gsize',
        name = 'pos',
      ),
      Param(
        type = 'const gchar *',
        name = 'val',
      ),
    ],
  ),
  'g_string_overwrite_len': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gsize',
        name = 'pos',
      ),
      Param(
        type = 'const gchar *',
        name = 'val',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  'g_string_erase': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gssize',
        name = 'pos',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  'g_string_ascii_down': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
    ],
  ),
  'g_string_ascii_up': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
    ],
  ),
  'g_string_vprintf': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
    ],
  ),
  'g_string_printf': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_string_append_vprintf': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
    ],
  ),
  'g_string_append_printf': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_string_append_uri_escaped': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'unescaped',
      ),
      Param(
        type = 'const gchar *',
        name = 'reserved_chars_allowed',
      ),
      Param(
        type = 'gboolean',
        name = 'allow_utf8',
      ),
    ],
  ),
  'g_string_append_c_inline': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'gstring',
      ),
      Param(
        type = 'gchar',
        name = 'c',
      ),
    ],
  ),
  'g_string_down': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
    ],
  ),
  'g_string_up': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GString *',
        name = 'string',
      ),
    ],
  ),
  'g_io_channel_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
    ],
  ),
  'g_io_channel_ref': Spec(
    return_type = 'GIOChannel *',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
    ],
  ),
  'g_io_channel_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
    ],
  ),
  'g_io_channel_read': Spec(
    return_type = 'GIOError',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'gchar *',
        name = 'buf',
      ),
      Param(
        type = 'gsize',
        name = 'count',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_read',
      ),
    ],
  ),
  'g_io_channel_write': Spec(
    return_type = 'GIOError',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'const gchar *',
        name = 'buf',
      ),
      Param(
        type = 'gsize',
        name = 'count',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_written',
      ),
    ],
  ),
  'g_io_channel_seek': Spec(
    return_type = 'GIOError',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'gint64',
        name = 'offset',
      ),
      Param(
        type = 'GSeekType',
        name = 'type',
      ),
    ],
  ),
  'g_io_channel_close': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
    ],
  ),
  'g_io_channel_shutdown': Spec(
    return_type = 'GIOStatus',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'gboolean',
        name = 'flush',
      ),
      Param(
        type = 'GError **',
        name = 'err',
      ),
    ],
  ),
  'g_io_add_watch_full': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'gint',
        name = 'priority',
      ),
      Param(
        type = 'GIOCondition',
        name = 'condition',
      ),
      Param(
        type = 'GIOFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'notify',
      ),
    ],
  ),
  'g_io_create_watch': Spec(
    return_type = 'GSource *',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'GIOCondition',
        name = 'condition',
      ),
    ],
  ),
  'g_io_add_watch': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'GIOCondition',
        name = 'condition',
      ),
      Param(
        type = 'GIOFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_io_channel_set_buffer_size': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'gsize',
        name = 'size',
      ),
    ],
  ),
  'g_io_channel_get_buffer_size': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
    ],
  ),
  'g_io_channel_get_buffer_condition': Spec(
    return_type = 'GIOCondition',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
    ],
  ),
  'g_io_channel_set_flags': Spec(
    return_type = 'GIOStatus',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'GIOFlags',
        name = 'flags',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_io_channel_get_flags': Spec(
    return_type = 'GIOFlags',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
    ],
  ),
  'g_io_channel_set_line_term': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'const gchar *',
        name = 'line_term',
      ),
      Param(
        type = 'gint',
        name = 'length',
      ),
    ],
  ),
  'g_io_channel_get_line_term': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'gint *',
        name = 'length',
      ),
    ],
  ),
  'g_io_channel_set_buffered': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'gboolean',
        name = 'buffered',
      ),
    ],
  ),
  'g_io_channel_get_buffered': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
    ],
  ),
  'g_io_channel_set_encoding': Spec(
    return_type = 'GIOStatus',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'const gchar *',
        name = 'encoding',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_io_channel_get_encoding': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
    ],
  ),
  'g_io_channel_set_close_on_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'gboolean',
        name = 'do_close',
      ),
    ],
  ),
  'g_io_channel_get_close_on_unref': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
    ],
  ),
  'g_io_channel_flush': Spec(
    return_type = 'GIOStatus',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_io_channel_read_line': Spec(
    return_type = 'GIOStatus',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'gchar **',
        name = 'str_return',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
      Param(
        type = 'gsize *',
        name = 'terminator_pos',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_io_channel_read_line_string': Spec(
    return_type = 'GIOStatus',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'GString *',
        name = 'buffer',
      ),
      Param(
        type = 'gsize *',
        name = 'terminator_pos',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_io_channel_read_to_end': Spec(
    return_type = 'GIOStatus',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'gchar **',
        name = 'str_return',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_io_channel_read_chars': Spec(
    return_type = 'GIOStatus',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'gchar *',
        name = 'buf',
      ),
      Param(
        type = 'gsize',
        name = 'count',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_read',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_io_channel_read_unichar': Spec(
    return_type = 'GIOStatus',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'gunichar *',
        name = 'thechar',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_io_channel_write_chars': Spec(
    return_type = 'GIOStatus',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'const gchar *',
        name = 'buf',
      ),
      Param(
        type = 'gssize',
        name = 'count',
      ),
      Param(
        type = 'gsize *',
        name = 'bytes_written',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_io_channel_write_unichar': Spec(
    return_type = 'GIOStatus',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'gunichar',
        name = 'thechar',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_io_channel_seek_position': Spec(
    return_type = 'GIOStatus',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
      Param(
        type = 'gint64',
        name = 'offset',
      ),
      Param(
        type = 'GSeekType',
        name = 'type',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_io_channel_new_file': Spec(
    return_type = 'GIOChannel *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'filename',
      ),
      Param(
        type = 'const gchar *',
        name = 'mode',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_io_channel_error_quark': Spec(
    return_type = 'GQuark',
    parameters = [
    ],
  ),
  'g_io_channel_error_from_errno': Spec(
    return_type = 'GIOChannelError',
    parameters = [
      Param(
        type = 'gint',
        name = 'en',
      ),
    ],
  ),
  'g_io_channel_unix_new': Spec(
    return_type = 'GIOChannel *',
    parameters = [
      Param(
        type = 'int',
        name = 'fd',
      ),
    ],
  ),
  'g_io_channel_unix_get_fd': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GIOChannel *',
        name = 'channel',
      ),
    ],
  ),
  'g_key_file_error_quark': Spec(
    return_type = 'GQuark',
    parameters = [
    ],
  ),
  'g_key_file_new': Spec(
    return_type = 'GKeyFile *',
    parameters = [
    ],
  ),
  'g_key_file_ref': Spec(
    return_type = 'GKeyFile *',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
    ],
  ),
  'g_key_file_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
    ],
  ),
  'g_key_file_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
    ],
  ),
  'g_key_file_set_list_separator': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'gchar',
        name = 'separator',
      ),
    ],
  ),
  'g_key_file_load_from_file': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'file',
      ),
      Param(
        type = 'GKeyFileFlags',
        name = 'flags',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_load_from_data': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'data',
      ),
      Param(
        type = 'gsize',
        name = 'length',
      ),
      Param(
        type = 'GKeyFileFlags',
        name = 'flags',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_load_from_dirs': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'file',
      ),
      Param(
        type = 'const gchar **',
        name = 'search_dirs',
      ),
      Param(
        type = 'gchar **',
        name = 'full_path',
      ),
      Param(
        type = 'GKeyFileFlags',
        name = 'flags',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_load_from_data_dirs': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'file',
      ),
      Param(
        type = 'gchar **',
        name = 'full_path',
      ),
      Param(
        type = 'GKeyFileFlags',
        name = 'flags',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_to_data': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_get_start_group': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
    ],
  ),
  'g_key_file_get_groups': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
    ],
  ),
  'g_key_file_get_keys': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_has_group': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
    ],
  ),
  'g_key_file_has_key': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_get_value': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_set_value': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'const gchar *',
        name = 'value',
      ),
    ],
  ),
  'g_key_file_get_string': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_set_string': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_key_file_get_locale_string': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'const gchar *',
        name = 'locale',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_set_locale_string': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'const gchar *',
        name = 'locale',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_key_file_get_boolean': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_set_boolean': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'gboolean',
        name = 'value',
      ),
    ],
  ),
  'g_key_file_get_integer': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_set_integer': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'gint',
        name = 'value',
      ),
    ],
  ),
  'g_key_file_get_int64': Spec(
    return_type = 'gint64',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_set_int64': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'gint64',
        name = 'value',
      ),
    ],
  ),
  'g_key_file_get_uint64': Spec(
    return_type = 'guint64',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_set_uint64': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'guint64',
        name = 'value',
      ),
    ],
  ),
  'g_key_file_get_double': Spec(
    return_type = 'gdouble',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_set_double': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'gdouble',
        name = 'value',
      ),
    ],
  ),
  'g_key_file_get_string_list': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_set_string_list': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'const gchar *const []',
        name = 'list',
      ),
      Param(
        type = 'gsize',
        name = 'length',
      ),
    ],
  ),
  'g_key_file_get_locale_string_list': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'const gchar *',
        name = 'locale',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_set_locale_string_list': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'const gchar *',
        name = 'locale',
      ),
      Param(
        type = 'const gchar *const []',
        name = 'list',
      ),
      Param(
        type = 'gsize',
        name = 'length',
      ),
    ],
  ),
  'g_key_file_get_boolean_list': Spec(
    return_type = 'gboolean *',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_set_boolean_list': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'gboolean []',
        name = 'list',
      ),
      Param(
        type = 'gsize',
        name = 'length',
      ),
    ],
  ),
  'g_key_file_get_integer_list': Spec(
    return_type = 'gint *',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_set_double_list': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'gdouble []',
        name = 'list',
      ),
      Param(
        type = 'gsize',
        name = 'length',
      ),
    ],
  ),
  'g_key_file_get_double_list': Spec(
    return_type = 'gdouble *',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_set_integer_list': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'gint []',
        name = 'list',
      ),
      Param(
        type = 'gsize',
        name = 'length',
      ),
    ],
  ),
  'g_key_file_set_comment': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'const gchar *',
        name = 'comment',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_get_comment': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_remove_comment': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_remove_key': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_key_file_remove_group': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GKeyFile *',
        name = 'key_file',
      ),
      Param(
        type = 'const gchar *',
        name = 'group_name',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_mapped_file_new': Spec(
    return_type = 'GMappedFile *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'filename',
      ),
      Param(
        type = 'gboolean',
        name = 'writable',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_mapped_file_new_from_fd': Spec(
    return_type = 'GMappedFile *',
    parameters = [
      Param(
        type = 'gint',
        name = 'fd',
      ),
      Param(
        type = 'gboolean',
        name = 'writable',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_mapped_file_get_length': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'GMappedFile *',
        name = 'file',
      ),
    ],
  ),
  'g_mapped_file_get_contents': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GMappedFile *',
        name = 'file',
      ),
    ],
  ),
  'g_mapped_file_get_bytes': Spec(
    return_type = 'GBytes *',
    parameters = [
      Param(
        type = 'GMappedFile *',
        name = 'file',
      ),
    ],
  ),
  'g_mapped_file_ref': Spec(
    return_type = 'GMappedFile *',
    parameters = [
      Param(
        type = 'GMappedFile *',
        name = 'file',
      ),
    ],
  ),
  'g_mapped_file_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMappedFile *',
        name = 'file',
      ),
    ],
  ),
  'g_mapped_file_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMappedFile *',
        name = 'file',
      ),
    ],
  ),
  'g_markup_error_quark': Spec(
    return_type = 'GQuark',
    parameters = [
    ],
  ),
  'g_markup_parse_context_new': Spec(
    return_type = 'GMarkupParseContext *',
    parameters = [
      Param(
        type = 'const GMarkupParser *',
        name = 'parser',
      ),
      Param(
        type = 'GMarkupParseFlags',
        name = 'flags',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'user_data_dnotify',
      ),
    ],
  ),
  'g_markup_parse_context_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMarkupParseContext *',
        name = 'context',
      ),
    ],
  ),
  'g_markup_parse_context_parse': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GMarkupParseContext *',
        name = 'context',
      ),
      Param(
        type = 'const gchar *',
        name = 'text',
      ),
      Param(
        type = 'gssize',
        name = 'text_len',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_markup_parse_context_push': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMarkupParseContext *',
        name = 'context',
      ),
      Param(
        type = 'const GMarkupParser *',
        name = 'parser',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_markup_parse_context_pop': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GMarkupParseContext *',
        name = 'context',
      ),
    ],
  ),
  'g_markup_parse_context_end_parse': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GMarkupParseContext *',
        name = 'context',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_markup_parse_context_get_element': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GMarkupParseContext *',
        name = 'context',
      ),
    ],
  ),
  'g_markup_parse_context_get_element_stack': Spec(
    return_type = 'const GSList *',
    parameters = [
      Param(
        type = 'GMarkupParseContext *',
        name = 'context',
      ),
    ],
  ),
  'g_markup_parse_context_get_position': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMarkupParseContext *',
        name = 'context',
      ),
      Param(
        type = 'gint *',
        name = 'line_number',
      ),
      Param(
        type = 'gint *',
        name = 'char_number',
      ),
    ],
  ),
  'g_markup_parse_context_get_user_data': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GMarkupParseContext *',
        name = 'context',
      ),
    ],
  ),
  'g_markup_escape_text': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'text',
      ),
      Param(
        type = 'gssize',
        name = 'length',
      ),
    ],
  ),
  'g_markup_printf_escaped': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const char *',
        name = 'format',
      ),
    ],
  ),
  'g_markup_vprintf_escaped': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const char *',
        name = 'format',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
    ],
  ),
  'g_markup_collect_attributes': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'element_name',
      ),
      Param(
        type = 'const gchar **',
        name = 'attribute_names',
      ),
      Param(
        type = 'const gchar **',
        name = 'attribute_values',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
      Param(
        type = 'GMarkupCollectType',
        name = 'first_type',
      ),
      Param(
        type = 'const gchar *',
        name = 'first_attr',
      ),
    ],
  ),
  'g_printf_string_upper_bound': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
    ],
  ),
  'g_log_set_handler': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'log_domain',
      ),
      Param(
        type = 'GLogLevelFlags',
        name = 'log_levels',
      ),
      Param(
        type = 'GLogFunc',
        name = 'log_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_log_remove_handler': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'log_domain',
      ),
      Param(
        type = 'guint',
        name = 'handler_id',
      ),
    ],
  ),
  'g_log_default_handler': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'log_domain',
      ),
      Param(
        type = 'GLogLevelFlags',
        name = 'log_level',
      ),
      Param(
        type = 'const gchar *',
        name = 'message',
      ),
      Param(
        type = 'gpointer',
        name = 'unused_data',
      ),
    ],
  ),
  'g_log_set_default_handler': Spec(
    return_type = 'GLogFunc',
    parameters = [
      Param(
        type = 'GLogFunc',
        name = 'log_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_log': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'log_domain',
      ),
      Param(
        type = 'GLogLevelFlags',
        name = 'log_level',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_logv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'log_domain',
      ),
      Param(
        type = 'GLogLevelFlags',
        name = 'log_level',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
    ],
  ),
  'g_log_set_fatal_mask': Spec(
    return_type = 'GLogLevelFlags',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'log_domain',
      ),
      Param(
        type = 'GLogLevelFlags',
        name = 'fatal_mask',
      ),
    ],
  ),
  'g_log_set_always_fatal': Spec(
    return_type = 'GLogLevelFlags',
    parameters = [
      Param(
        type = 'GLogLevelFlags',
        name = 'fatal_mask',
      ),
    ],
  ),
  '_g_log_fallback_handler': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'log_domain',
      ),
      Param(
        type = 'GLogLevelFlags',
        name = 'log_level',
      ),
      Param(
        type = 'const gchar *',
        name = 'message',
      ),
      Param(
        type = 'gpointer',
        name = 'unused_data',
      ),
    ],
  ),
  'g_return_if_fail_warning': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'log_domain',
      ),
      Param(
        type = 'const char *',
        name = 'pretty_function',
      ),
      Param(
        type = 'const char *',
        name = 'expression',
      ),
    ],
  ),
  'g_warn_message': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'domain',
      ),
      Param(
        type = 'const char *',
        name = 'file',
      ),
      Param(
        type = 'int',
        name = 'line',
      ),
      Param(
        type = 'const char *',
        name = 'func',
      ),
      Param(
        type = 'const char *',
        name = 'warnexpr',
      ),
    ],
  ),
  'g_assert_warning': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'log_domain',
      ),
      Param(
        type = 'const char *',
        name = 'file',
      ),
      Param(
        type = 'const int',
        name = 'line',
      ),
      Param(
        type = 'const char *',
        name = 'pretty_function',
      ),
      Param(
        type = 'const char *',
        name = 'expression',
      ),
    ],
  ),
  'g_print': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_set_print_handler': Spec(
    return_type = 'GPrintFunc',
    parameters = [
      Param(
        type = 'GPrintFunc',
        name = 'func',
      ),
    ],
  ),
  'g_printerr': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_set_printerr_handler': Spec(
    return_type = 'GPrintFunc',
    parameters = [
      Param(
        type = 'GPrintFunc',
        name = 'func',
      ),
    ],
  ),
  'g_option_error_quark': Spec(
    return_type = 'GQuark',
    parameters = [
    ],
  ),
  'g_option_context_new': Spec(
    return_type = 'GOptionContext *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'parameter_string',
      ),
    ],
  ),
  'g_option_context_set_summary': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
      Param(
        type = 'const gchar *',
        name = 'summary',
      ),
    ],
  ),
  'g_option_context_get_summary': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
    ],
  ),
  'g_option_context_set_description': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
      Param(
        type = 'const gchar *',
        name = 'description',
      ),
    ],
  ),
  'g_option_context_get_description': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
    ],
  ),
  'g_option_context_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
    ],
  ),
  'g_option_context_set_help_enabled': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
      Param(
        type = 'gboolean',
        name = 'help_enabled',
      ),
    ],
  ),
  'g_option_context_get_help_enabled': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
    ],
  ),
  'g_option_context_set_ignore_unknown_options': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
      Param(
        type = 'gboolean',
        name = 'ignore_unknown',
      ),
    ],
  ),
  'g_option_context_get_ignore_unknown_options': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
    ],
  ),
  'g_option_context_add_main_entries': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
      Param(
        type = 'const GOptionEntry *',
        name = 'entries',
      ),
      Param(
        type = 'const gchar *',
        name = 'translation_domain',
      ),
    ],
  ),
  'g_option_context_parse': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
      Param(
        type = 'gint *',
        name = 'argc',
      ),
      Param(
        type = 'gchar ***',
        name = 'argv',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_option_context_set_translate_func': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
      Param(
        type = 'GTranslateFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'destroy_notify',
      ),
    ],
  ),
  'g_option_context_set_translation_domain': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
      Param(
        type = 'const gchar *',
        name = 'domain',
      ),
    ],
  ),
  'g_option_context_add_group': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
      Param(
        type = 'GOptionGroup *',
        name = 'group',
      ),
    ],
  ),
  'g_option_context_set_main_group': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
      Param(
        type = 'GOptionGroup *',
        name = 'group',
      ),
    ],
  ),
  'g_option_context_get_main_group': Spec(
    return_type = 'GOptionGroup *',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
    ],
  ),
  'g_option_context_get_help': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GOptionContext *',
        name = 'context',
      ),
      Param(
        type = 'gboolean',
        name = 'main_help',
      ),
      Param(
        type = 'GOptionGroup *',
        name = 'group',
      ),
    ],
  ),
  'g_option_group_new': Spec(
    return_type = 'GOptionGroup *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'description',
      ),
      Param(
        type = 'const gchar *',
        name = 'help_description',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'destroy',
      ),
    ],
  ),
  'g_option_group_set_parse_hooks': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionGroup *',
        name = 'group',
      ),
      Param(
        type = 'GOptionParseFunc',
        name = 'pre_parse_func',
      ),
      Param(
        type = 'GOptionParseFunc',
        name = 'post_parse_func',
      ),
    ],
  ),
  'g_option_group_set_error_hook': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionGroup *',
        name = 'group',
      ),
      Param(
        type = 'GOptionErrorFunc',
        name = 'error_func',
      ),
    ],
  ),
  'g_option_group_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionGroup *',
        name = 'group',
      ),
    ],
  ),
  'g_option_group_add_entries': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionGroup *',
        name = 'group',
      ),
      Param(
        type = 'const GOptionEntry *',
        name = 'entries',
      ),
    ],
  ),
  'g_option_group_set_translate_func': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionGroup *',
        name = 'group',
      ),
      Param(
        type = 'GTranslateFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'destroy_notify',
      ),
    ],
  ),
  'g_option_group_set_translation_domain': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GOptionGroup *',
        name = 'group',
      ),
      Param(
        type = 'const gchar *',
        name = 'domain',
      ),
    ],
  ),
  'g_pattern_spec_new': Spec(
    return_type = 'GPatternSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'pattern',
      ),
    ],
  ),
  'g_pattern_spec_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GPatternSpec *',
        name = 'pspec',
      ),
    ],
  ),
  'g_pattern_spec_equal': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GPatternSpec *',
        name = 'pspec1',
      ),
      Param(
        type = 'GPatternSpec *',
        name = 'pspec2',
      ),
    ],
  ),
  'g_pattern_match': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GPatternSpec *',
        name = 'pspec',
      ),
      Param(
        type = 'guint',
        name = 'string_length',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'string_reversed',
      ),
    ],
  ),
  'g_pattern_match_string': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GPatternSpec *',
        name = 'pspec',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_pattern_match_simple': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'pattern',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_spaced_primes_closest': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'guint',
        name = 'num',
      ),
    ],
  ),
  'g_qsort_with_data': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'pbase',
      ),
      Param(
        type = 'gint',
        name = 'total_elems',
      ),
      Param(
        type = 'gsize',
        name = 'size',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'compare_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_queue_new': Spec(
    return_type = 'GQueue *',
    parameters = [
    ],
  ),
  'g_queue_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_free_full': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'free_func',
      ),
    ],
  ),
  'g_queue_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_clear': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_is_empty': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_get_length': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_reverse': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_copy': Spec(
    return_type = 'GQueue *',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_foreach': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'GFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_queue_find': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
    ],
  ),
  'g_queue_find_custom': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
      Param(
        type = 'GCompareFunc',
        name = 'func',
      ),
    ],
  ),
  'g_queue_sort': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'compare_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_queue_push_head': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_queue_push_tail': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_queue_push_nth': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'gint',
        name = 'n',
      ),
    ],
  ),
  'g_queue_pop_head': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_pop_tail': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_pop_nth': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'guint',
        name = 'n',
      ),
    ],
  ),
  'g_queue_peek_head': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_peek_tail': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_peek_nth': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'guint',
        name = 'n',
      ),
    ],
  ),
  'g_queue_index': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
    ],
  ),
  'g_queue_remove': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
    ],
  ),
  'g_queue_remove_all': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
    ],
  ),
  'g_queue_insert_before': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'GList *',
        name = 'sibling',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_queue_insert_after': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'GList *',
        name = 'sibling',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_queue_insert_sorted': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_queue_push_head_link': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'GList *',
        name = 'link_',
      ),
    ],
  ),
  'g_queue_push_tail_link': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'GList *',
        name = 'link_',
      ),
    ],
  ),
  'g_queue_push_nth_link': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'gint',
        name = 'n',
      ),
      Param(
        type = 'GList *',
        name = 'link_',
      ),
    ],
  ),
  'g_queue_pop_head_link': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_pop_tail_link': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_pop_nth_link': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'guint',
        name = 'n',
      ),
    ],
  ),
  'g_queue_peek_head_link': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_peek_tail_link': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
    ],
  ),
  'g_queue_peek_nth_link': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'guint',
        name = 'n',
      ),
    ],
  ),
  'g_queue_link_index': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'GList *',
        name = 'link_',
      ),
    ],
  ),
  'g_queue_unlink': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'GList *',
        name = 'link_',
      ),
    ],
  ),
  'g_queue_delete_link': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GQueue *',
        name = 'queue',
      ),
      Param(
        type = 'GList *',
        name = 'link_',
      ),
    ],
  ),
  'g_rand_new_with_seed': Spec(
    return_type = 'GRand *',
    parameters = [
      Param(
        type = 'guint32',
        name = 'seed',
      ),
    ],
  ),
  'g_rand_new_with_seed_array': Spec(
    return_type = 'GRand *',
    parameters = [
      Param(
        type = 'const guint32 *',
        name = 'seed',
      ),
      Param(
        type = 'guint',
        name = 'seed_length',
      ),
    ],
  ),
  'g_rand_new': Spec(
    return_type = 'GRand *',
    parameters = [
    ],
  ),
  'g_rand_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRand *',
        name = 'rand_',
      ),
    ],
  ),
  'g_rand_copy': Spec(
    return_type = 'GRand *',
    parameters = [
      Param(
        type = 'GRand *',
        name = 'rand_',
      ),
    ],
  ),
  'g_rand_set_seed': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRand *',
        name = 'rand_',
      ),
      Param(
        type = 'guint32',
        name = 'seed',
      ),
    ],
  ),
  'g_rand_set_seed_array': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRand *',
        name = 'rand_',
      ),
      Param(
        type = 'const guint32 *',
        name = 'seed',
      ),
      Param(
        type = 'guint',
        name = 'seed_length',
      ),
    ],
  ),
  'g_rand_int': Spec(
    return_type = 'guint32',
    parameters = [
      Param(
        type = 'GRand *',
        name = 'rand_',
      ),
    ],
  ),
  'g_rand_int_range': Spec(
    return_type = 'gint32',
    parameters = [
      Param(
        type = 'GRand *',
        name = 'rand_',
      ),
      Param(
        type = 'gint32',
        name = 'begin',
      ),
      Param(
        type = 'gint32',
        name = 'end',
      ),
    ],
  ),
  'g_rand_double': Spec(
    return_type = 'gdouble',
    parameters = [
      Param(
        type = 'GRand *',
        name = 'rand_',
      ),
    ],
  ),
  'g_rand_double_range': Spec(
    return_type = 'gdouble',
    parameters = [
      Param(
        type = 'GRand *',
        name = 'rand_',
      ),
      Param(
        type = 'gdouble',
        name = 'begin',
      ),
      Param(
        type = 'gdouble',
        name = 'end',
      ),
    ],
  ),
  'g_random_set_seed': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'guint32',
        name = 'seed',
      ),
    ],
  ),
  'g_random_int': Spec(
    return_type = 'guint32',
    parameters = [
    ],
  ),
  'g_random_int_range': Spec(
    return_type = 'gint32',
    parameters = [
      Param(
        type = 'gint32',
        name = 'begin',
      ),
      Param(
        type = 'gint32',
        name = 'end',
      ),
    ],
  ),
  'g_random_double': Spec(
    return_type = 'gdouble',
    parameters = [
    ],
  ),
  'g_random_double_range': Spec(
    return_type = 'gdouble',
    parameters = [
      Param(
        type = 'gdouble',
        name = 'begin',
      ),
      Param(
        type = 'gdouble',
        name = 'end',
      ),
    ],
  ),
  'g_regex_error_quark': Spec(
    return_type = 'GQuark',
    parameters = [
    ],
  ),
  'g_regex_new': Spec(
    return_type = 'GRegex *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'pattern',
      ),
      Param(
        type = 'GRegexCompileFlags',
        name = 'compile_options',
      ),
      Param(
        type = 'GRegexMatchFlags',
        name = 'match_options',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_regex_ref': Spec(
    return_type = 'GRegex *',
    parameters = [
      Param(
        type = 'GRegex *',
        name = 'regex',
      ),
    ],
  ),
  'g_regex_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRegex *',
        name = 'regex',
      ),
    ],
  ),
  'g_regex_get_pattern': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
    ],
  ),
  'g_regex_get_max_backref': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
    ],
  ),
  'g_regex_get_capture_count': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
    ],
  ),
  'g_regex_get_has_cr_or_lf': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
    ],
  ),
  'g_regex_get_string_number': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
    ],
  ),
  'g_regex_escape_string': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'gint',
        name = 'length',
      ),
    ],
  ),
  'g_regex_escape_nul': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'gint',
        name = 'length',
      ),
    ],
  ),
  'g_regex_get_compile_flags': Spec(
    return_type = 'GRegexCompileFlags',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
    ],
  ),
  'g_regex_get_match_flags': Spec(
    return_type = 'GRegexMatchFlags',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
    ],
  ),
  'g_regex_match_simple': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'pattern',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'GRegexCompileFlags',
        name = 'compile_options',
      ),
      Param(
        type = 'GRegexMatchFlags',
        name = 'match_options',
      ),
    ],
  ),
  'g_regex_match': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'GRegexMatchFlags',
        name = 'match_options',
      ),
      Param(
        type = 'GMatchInfo **',
        name = 'match_info',
      ),
    ],
  ),
  'g_regex_match_full': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'gssize',
        name = 'string_len',
      ),
      Param(
        type = 'gint',
        name = 'start_position',
      ),
      Param(
        type = 'GRegexMatchFlags',
        name = 'match_options',
      ),
      Param(
        type = 'GMatchInfo **',
        name = 'match_info',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_regex_match_all': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'GRegexMatchFlags',
        name = 'match_options',
      ),
      Param(
        type = 'GMatchInfo **',
        name = 'match_info',
      ),
    ],
  ),
  'g_regex_match_all_full': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'gssize',
        name = 'string_len',
      ),
      Param(
        type = 'gint',
        name = 'start_position',
      ),
      Param(
        type = 'GRegexMatchFlags',
        name = 'match_options',
      ),
      Param(
        type = 'GMatchInfo **',
        name = 'match_info',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_regex_split_simple': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'pattern',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'GRegexCompileFlags',
        name = 'compile_options',
      ),
      Param(
        type = 'GRegexMatchFlags',
        name = 'match_options',
      ),
    ],
  ),
  'g_regex_split': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'GRegexMatchFlags',
        name = 'match_options',
      ),
    ],
  ),
  'g_regex_split_full': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'gssize',
        name = 'string_len',
      ),
      Param(
        type = 'gint',
        name = 'start_position',
      ),
      Param(
        type = 'GRegexMatchFlags',
        name = 'match_options',
      ),
      Param(
        type = 'gint',
        name = 'max_tokens',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_regex_replace': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'gssize',
        name = 'string_len',
      ),
      Param(
        type = 'gint',
        name = 'start_position',
      ),
      Param(
        type = 'const gchar *',
        name = 'replacement',
      ),
      Param(
        type = 'GRegexMatchFlags',
        name = 'match_options',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_regex_replace_literal': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'gssize',
        name = 'string_len',
      ),
      Param(
        type = 'gint',
        name = 'start_position',
      ),
      Param(
        type = 'const gchar *',
        name = 'replacement',
      ),
      Param(
        type = 'GRegexMatchFlags',
        name = 'match_options',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_regex_replace_eval': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const GRegex *',
        name = 'regex',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'gssize',
        name = 'string_len',
      ),
      Param(
        type = 'gint',
        name = 'start_position',
      ),
      Param(
        type = 'GRegexMatchFlags',
        name = 'match_options',
      ),
      Param(
        type = 'GRegexEvalCallback',
        name = 'eval',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_regex_check_replacement': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'replacement',
      ),
      Param(
        type = 'gboolean *',
        name = 'has_references',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_match_info_get_regex': Spec(
    return_type = 'GRegex *',
    parameters = [
      Param(
        type = 'const GMatchInfo *',
        name = 'match_info',
      ),
    ],
  ),
  'g_match_info_get_string': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const GMatchInfo *',
        name = 'match_info',
      ),
    ],
  ),
  'g_match_info_ref': Spec(
    return_type = 'GMatchInfo *',
    parameters = [
      Param(
        type = 'GMatchInfo *',
        name = 'match_info',
      ),
    ],
  ),
  'g_match_info_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMatchInfo *',
        name = 'match_info',
      ),
    ],
  ),
  'g_match_info_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMatchInfo *',
        name = 'match_info',
      ),
    ],
  ),
  'g_match_info_next': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GMatchInfo *',
        name = 'match_info',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_match_info_matches': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GMatchInfo *',
        name = 'match_info',
      ),
    ],
  ),
  'g_match_info_get_match_count': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const GMatchInfo *',
        name = 'match_info',
      ),
    ],
  ),
  'g_match_info_is_partial_match': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GMatchInfo *',
        name = 'match_info',
      ),
    ],
  ),
  'g_match_info_expand_references': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const GMatchInfo *',
        name = 'match_info',
      ),
      Param(
        type = 'const gchar *',
        name = 'string_to_expand',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_match_info_fetch': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const GMatchInfo *',
        name = 'match_info',
      ),
      Param(
        type = 'gint',
        name = 'match_num',
      ),
    ],
  ),
  'g_match_info_fetch_pos': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GMatchInfo *',
        name = 'match_info',
      ),
      Param(
        type = 'gint',
        name = 'match_num',
      ),
      Param(
        type = 'gint *',
        name = 'start_pos',
      ),
      Param(
        type = 'gint *',
        name = 'end_pos',
      ),
    ],
  ),
  'g_match_info_fetch_named': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const GMatchInfo *',
        name = 'match_info',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
    ],
  ),
  'g_match_info_fetch_named_pos': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GMatchInfo *',
        name = 'match_info',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'gint *',
        name = 'start_pos',
      ),
      Param(
        type = 'gint *',
        name = 'end_pos',
      ),
    ],
  ),
  'g_match_info_fetch_all': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'const GMatchInfo *',
        name = 'match_info',
      ),
    ],
  ),
  'g_scanner_new': Spec(
    return_type = 'GScanner *',
    parameters = [
      Param(
        type = 'const GScannerConfig *',
        name = 'config_templ',
      ),
    ],
  ),
  'g_scanner_destroy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
    ],
  ),
  'g_scanner_input_file': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
      Param(
        type = 'gint',
        name = 'input_fd',
      ),
    ],
  ),
  'g_scanner_sync_file_offset': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
    ],
  ),
  'g_scanner_input_text': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
      Param(
        type = 'const gchar *',
        name = 'text',
      ),
      Param(
        type = 'guint',
        name = 'text_len',
      ),
    ],
  ),
  'g_scanner_get_next_token': Spec(
    return_type = 'GTokenType',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
    ],
  ),
  'g_scanner_peek_next_token': Spec(
    return_type = 'GTokenType',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
    ],
  ),
  'g_scanner_cur_token': Spec(
    return_type = 'GTokenType',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
    ],
  ),
  'g_scanner_cur_value': Spec(
    return_type = 'GTokenValue',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
    ],
  ),
  'g_scanner_cur_line': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
    ],
  ),
  'g_scanner_cur_position': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
    ],
  ),
  'g_scanner_eof': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
    ],
  ),
  'g_scanner_set_scope': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
      Param(
        type = 'guint',
        name = 'scope_id',
      ),
    ],
  ),
  'g_scanner_scope_add_symbol': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
      Param(
        type = 'guint',
        name = 'scope_id',
      ),
      Param(
        type = 'const gchar *',
        name = 'symbol',
      ),
      Param(
        type = 'gpointer',
        name = 'value',
      ),
    ],
  ),
  'g_scanner_scope_remove_symbol': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
      Param(
        type = 'guint',
        name = 'scope_id',
      ),
      Param(
        type = 'const gchar *',
        name = 'symbol',
      ),
    ],
  ),
  'g_scanner_scope_lookup_symbol': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
      Param(
        type = 'guint',
        name = 'scope_id',
      ),
      Param(
        type = 'const gchar *',
        name = 'symbol',
      ),
    ],
  ),
  'g_scanner_scope_foreach_symbol': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
      Param(
        type = 'guint',
        name = 'scope_id',
      ),
      Param(
        type = 'GHFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_scanner_lookup_symbol': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
      Param(
        type = 'const gchar *',
        name = 'symbol',
      ),
    ],
  ),
  'g_scanner_unexp_token': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
      Param(
        type = 'GTokenType',
        name = 'expected_token',
      ),
      Param(
        type = 'const gchar *',
        name = 'identifier_spec',
      ),
      Param(
        type = 'const gchar *',
        name = 'symbol_spec',
      ),
      Param(
        type = 'const gchar *',
        name = 'symbol_name',
      ),
      Param(
        type = 'const gchar *',
        name = 'message',
      ),
      Param(
        type = 'gint',
        name = 'is_error',
      ),
    ],
  ),
  'g_scanner_error': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_scanner_warn': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GScanner *',
        name = 'scanner',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_sequence_new': Spec(
    return_type = 'GSequence *',
    parameters = [
      Param(
        type = 'GDestroyNotify',
        name = 'data_destroy',
      ),
    ],
  ),
  'g_sequence_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
    ],
  ),
  'g_sequence_get_length': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
    ],
  ),
  'g_sequence_foreach': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
      Param(
        type = 'GFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_sequence_foreach_range': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'begin',
      ),
      Param(
        type = 'GSequenceIter *',
        name = 'end',
      ),
      Param(
        type = 'GFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_sequence_sort': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'cmp_func',
      ),
      Param(
        type = 'gpointer',
        name = 'cmp_data',
      ),
    ],
  ),
  'g_sequence_sort_iter': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
      Param(
        type = 'GSequenceIterCompareFunc',
        name = 'cmp_func',
      ),
      Param(
        type = 'gpointer',
        name = 'cmp_data',
      ),
    ],
  ),
  'g_sequence_get_begin_iter': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
    ],
  ),
  'g_sequence_get_end_iter': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
    ],
  ),
  'g_sequence_get_iter_at_pos': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
      Param(
        type = 'gint',
        name = 'pos',
      ),
    ],
  ),
  'g_sequence_append': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_sequence_prepend': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_sequence_insert_before': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'iter',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_sequence_move': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'src',
      ),
      Param(
        type = 'GSequenceIter *',
        name = 'dest',
      ),
    ],
  ),
  'g_sequence_swap': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'a',
      ),
      Param(
        type = 'GSequenceIter *',
        name = 'b',
      ),
    ],
  ),
  'g_sequence_insert_sorted': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'cmp_func',
      ),
      Param(
        type = 'gpointer',
        name = 'cmp_data',
      ),
    ],
  ),
  'g_sequence_insert_sorted_iter': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GSequenceIterCompareFunc',
        name = 'iter_cmp',
      ),
      Param(
        type = 'gpointer',
        name = 'cmp_data',
      ),
    ],
  ),
  'g_sequence_sort_changed': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'iter',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'cmp_func',
      ),
      Param(
        type = 'gpointer',
        name = 'cmp_data',
      ),
    ],
  ),
  'g_sequence_sort_changed_iter': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'iter',
      ),
      Param(
        type = 'GSequenceIterCompareFunc',
        name = 'iter_cmp',
      ),
      Param(
        type = 'gpointer',
        name = 'cmp_data',
      ),
    ],
  ),
  'g_sequence_remove': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_sequence_remove_range': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'begin',
      ),
      Param(
        type = 'GSequenceIter *',
        name = 'end',
      ),
    ],
  ),
  'g_sequence_move_range': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'dest',
      ),
      Param(
        type = 'GSequenceIter *',
        name = 'begin',
      ),
      Param(
        type = 'GSequenceIter *',
        name = 'end',
      ),
    ],
  ),
  'g_sequence_search': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'cmp_func',
      ),
      Param(
        type = 'gpointer',
        name = 'cmp_data',
      ),
    ],
  ),
  'g_sequence_search_iter': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GSequenceIterCompareFunc',
        name = 'iter_cmp',
      ),
      Param(
        type = 'gpointer',
        name = 'cmp_data',
      ),
    ],
  ),
  'g_sequence_lookup': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'cmp_func',
      ),
      Param(
        type = 'gpointer',
        name = 'cmp_data',
      ),
    ],
  ),
  'g_sequence_lookup_iter': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequence *',
        name = 'seq',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GSequenceIterCompareFunc',
        name = 'iter_cmp',
      ),
      Param(
        type = 'gpointer',
        name = 'cmp_data',
      ),
    ],
  ),
  'g_sequence_get': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_sequence_set': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'iter',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_sequence_iter_is_begin': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_sequence_iter_is_end': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_sequence_iter_next': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_sequence_iter_prev': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_sequence_iter_get_position': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_sequence_iter_move': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'iter',
      ),
      Param(
        type = 'gint',
        name = 'delta',
      ),
    ],
  ),
  'g_sequence_iter_get_sequence': Spec(
    return_type = 'GSequence *',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_sequence_iter_compare': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'a',
      ),
      Param(
        type = 'GSequenceIter *',
        name = 'b',
      ),
    ],
  ),
  'g_sequence_range_get_midpoint': Spec(
    return_type = 'GSequenceIter *',
    parameters = [
      Param(
        type = 'GSequenceIter *',
        name = 'begin',
      ),
      Param(
        type = 'GSequenceIter *',
        name = 'end',
      ),
    ],
  ),
  'g_shell_error_quark': Spec(
    return_type = 'GQuark',
    parameters = [
    ],
  ),
  'g_shell_quote': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'unquoted_string',
      ),
    ],
  ),
  'g_shell_unquote': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'quoted_string',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_shell_parse_argv': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'command_line',
      ),
      Param(
        type = 'gint *',
        name = 'argcp',
      ),
      Param(
        type = 'gchar ***',
        name = 'argvp',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_slice_alloc': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gsize',
        name = 'block_size',
      ),
    ],
  ),
  'g_slice_alloc0': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gsize',
        name = 'block_size',
      ),
    ],
  ),
  'g_slice_copy': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gsize',
        name = 'block_size',
      ),
      Param(
        type = 'gconstpointer',
        name = 'mem_block',
      ),
    ],
  ),
  'g_slice_free1': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gsize',
        name = 'block_size',
      ),
      Param(
        type = 'gpointer',
        name = 'mem_block',
      ),
    ],
  ),
  'g_slice_free_chain_with_offset': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gsize',
        name = 'block_size',
      ),
      Param(
        type = 'gpointer',
        name = 'mem_chain',
      ),
      Param(
        type = 'gsize',
        name = 'next_offset',
      ),
    ],
  ),
  'g_slice_set_config': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSliceConfig',
        name = 'ckey',
      ),
      Param(
        type = 'gint64',
        name = 'value',
      ),
    ],
  ),
  'g_slice_get_config': Spec(
    return_type = 'gint64',
    parameters = [
      Param(
        type = 'GSliceConfig',
        name = 'ckey',
      ),
    ],
  ),
  'g_slice_get_config_state': Spec(
    return_type = 'gint64 *',
    parameters = [
      Param(
        type = 'GSliceConfig',
        name = 'ckey',
      ),
      Param(
        type = 'gint64',
        name = 'address',
      ),
      Param(
        type = 'guint *',
        name = 'n_values',
      ),
    ],
  ),
  'g_spawn_error_quark': Spec(
    return_type = 'GQuark',
    parameters = [
    ],
  ),
  'g_spawn_exit_error_quark': Spec(
    return_type = 'GQuark',
    parameters = [
    ],
  ),
  'g_spawn_async': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'working_directory',
      ),
      Param(
        type = 'gchar **',
        name = 'argv',
      ),
      Param(
        type = 'gchar **',
        name = 'envp',
      ),
      Param(
        type = 'GSpawnFlags',
        name = 'flags',
      ),
      Param(
        type = 'GSpawnChildSetupFunc',
        name = 'child_setup',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
      Param(
        type = 'GPid *',
        name = 'child_pid',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_spawn_async_with_pipes': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'working_directory',
      ),
      Param(
        type = 'gchar **',
        name = 'argv',
      ),
      Param(
        type = 'gchar **',
        name = 'envp',
      ),
      Param(
        type = 'GSpawnFlags',
        name = 'flags',
      ),
      Param(
        type = 'GSpawnChildSetupFunc',
        name = 'child_setup',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
      Param(
        type = 'GPid *',
        name = 'child_pid',
      ),
      Param(
        type = 'gint *',
        name = 'standard_input',
      ),
      Param(
        type = 'gint *',
        name = 'standard_output',
      ),
      Param(
        type = 'gint *',
        name = 'standard_error',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_spawn_sync': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'working_directory',
      ),
      Param(
        type = 'gchar **',
        name = 'argv',
      ),
      Param(
        type = 'gchar **',
        name = 'envp',
      ),
      Param(
        type = 'GSpawnFlags',
        name = 'flags',
      ),
      Param(
        type = 'GSpawnChildSetupFunc',
        name = 'child_setup',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
      Param(
        type = 'gchar **',
        name = 'standard_output',
      ),
      Param(
        type = 'gchar **',
        name = 'standard_error',
      ),
      Param(
        type = 'gint *',
        name = 'exit_status',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_spawn_command_line_sync': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'command_line',
      ),
      Param(
        type = 'gchar **',
        name = 'standard_output',
      ),
      Param(
        type = 'gchar **',
        name = 'standard_error',
      ),
      Param(
        type = 'gint *',
        name = 'exit_status',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_spawn_command_line_async': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'command_line',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_spawn_check_exit_status': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gint',
        name = 'exit_status',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_spawn_close_pid': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GPid',
        name = 'pid',
      ),
    ],
  ),
  'g_ascii_tolower': Spec(
    return_type = 'gchar',
    parameters = [
      Param(
        type = 'gchar',
        name = 'c',
      ),
    ],
  ),
  'g_ascii_toupper': Spec(
    return_type = 'gchar',
    parameters = [
      Param(
        type = 'gchar',
        name = 'c',
      ),
    ],
  ),
  'g_ascii_digit_value': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gchar',
        name = 'c',
      ),
    ],
  ),
  'g_ascii_xdigit_value': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gchar',
        name = 'c',
      ),
    ],
  ),
  'g_strdelimit': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'delimiters',
      ),
      Param(
        type = 'gchar',
        name = 'new_delimiter',
      ),
    ],
  ),
  'g_strcanon': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'valid_chars',
      ),
      Param(
        type = 'gchar',
        name = 'substitutor',
      ),
    ],
  ),
  'g_strerror': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'gint',
        name = 'errnum',
      ),
    ],
  ),
  'g_strsignal': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'gint',
        name = 'signum',
      ),
    ],
  ),
  'g_strreverse': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_strlcpy': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'dest',
      ),
      Param(
        type = 'const gchar *',
        name = 'src',
      ),
      Param(
        type = 'gsize',
        name = 'dest_size',
      ),
    ],
  ),
  'g_strlcat': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'dest',
      ),
      Param(
        type = 'const gchar *',
        name = 'src',
      ),
      Param(
        type = 'gsize',
        name = 'dest_size',
      ),
    ],
  ),
  'g_strstr_len': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'haystack',
      ),
      Param(
        type = 'gssize',
        name = 'haystack_len',
      ),
      Param(
        type = 'const gchar *',
        name = 'needle',
      ),
    ],
  ),
  'g_strrstr': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'haystack',
      ),
      Param(
        type = 'const gchar *',
        name = 'needle',
      ),
    ],
  ),
  'g_strrstr_len': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'haystack',
      ),
      Param(
        type = 'gssize',
        name = 'haystack_len',
      ),
      Param(
        type = 'const gchar *',
        name = 'needle',
      ),
    ],
  ),
  'g_str_has_suffix': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'const gchar *',
        name = 'suffix',
      ),
    ],
  ),
  'g_str_has_prefix': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'const gchar *',
        name = 'prefix',
      ),
    ],
  ),
  'g_strtod': Spec(
    return_type = 'gdouble',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'nptr',
      ),
      Param(
        type = 'gchar **',
        name = 'endptr',
      ),
    ],
  ),
  'g_ascii_strtod': Spec(
    return_type = 'gdouble',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'nptr',
      ),
      Param(
        type = 'gchar **',
        name = 'endptr',
      ),
    ],
  ),
  'g_ascii_strtoull': Spec(
    return_type = 'guint64',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'nptr',
      ),
      Param(
        type = 'gchar **',
        name = 'endptr',
      ),
      Param(
        type = 'guint',
        name = 'base',
      ),
    ],
  ),
  'g_ascii_strtoll': Spec(
    return_type = 'gint64',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'nptr',
      ),
      Param(
        type = 'gchar **',
        name = 'endptr',
      ),
      Param(
        type = 'guint',
        name = 'base',
      ),
    ],
  ),
  'g_ascii_dtostr': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'buffer',
      ),
      Param(
        type = 'gint',
        name = 'buf_len',
      ),
      Param(
        type = 'gdouble',
        name = 'd',
      ),
    ],
  ),
  'g_ascii_formatd': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'buffer',
      ),
      Param(
        type = 'gint',
        name = 'buf_len',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
      Param(
        type = 'gdouble',
        name = 'd',
      ),
    ],
  ),
  'g_strchug': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_strchomp': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_ascii_strcasecmp': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 's1',
      ),
      Param(
        type = 'const gchar *',
        name = 's2',
      ),
    ],
  ),
  'g_ascii_strncasecmp': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 's1',
      ),
      Param(
        type = 'const gchar *',
        name = 's2',
      ),
      Param(
        type = 'gsize',
        name = 'n',
      ),
    ],
  ),
  'g_ascii_strdown': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  'g_ascii_strup': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  'g_strcasecmp': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 's1',
      ),
      Param(
        type = 'const gchar *',
        name = 's2',
      ),
    ],
  ),
  'g_strncasecmp': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 's1',
      ),
      Param(
        type = 'const gchar *',
        name = 's2',
      ),
      Param(
        type = 'guint',
        name = 'n',
      ),
    ],
  ),
  'g_strdown': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_strup': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_strdup': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
    ],
  ),
  'g_strdup_printf': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_strdup_vprintf': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
    ],
  ),
  'g_strndup': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'str',
      ),
      Param(
        type = 'gsize',
        name = 'n',
      ),
    ],
  ),
  'g_strnfill': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gsize',
        name = 'length',
      ),
      Param(
        type = 'gchar',
        name = 'fill_char',
      ),
    ],
  ),
  'g_strconcat': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string1',
      ),
    ],
  ),
  'g_strjoin': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'separator',
      ),
    ],
  ),
  'g_strcompress': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'source',
      ),
    ],
  ),
  'g_strescape': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'source',
      ),
      Param(
        type = 'const gchar *',
        name = 'exceptions',
      ),
    ],
  ),
  'g_memdup': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'mem',
      ),
      Param(
        type = 'guint',
        name = 'byte_size',
      ),
    ],
  ),
  'g_strsplit': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'delimiter',
      ),
      Param(
        type = 'gint',
        name = 'max_tokens',
      ),
    ],
  ),
  'g_strsplit_set': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'delimiters',
      ),
      Param(
        type = 'gint',
        name = 'max_tokens',
      ),
    ],
  ),
  'g_strjoinv': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'separator',
      ),
      Param(
        type = 'gchar **',
        name = 'str_array',
      ),
    ],
  ),
  'g_strfreev': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gchar **',
        name = 'str_array',
      ),
    ],
  ),
  'g_strdupv': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'gchar **',
        name = 'str_array',
      ),
    ],
  ),
  'g_strv_length': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gchar **',
        name = 'str_array',
      ),
    ],
  ),
  'g_stpcpy': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'dest',
      ),
      Param(
        type = 'const char *',
        name = 'src',
      ),
    ],
  ),
  'g_string_chunk_new': Spec(
    return_type = 'GStringChunk *',
    parameters = [
      Param(
        type = 'gsize',
        name = 'size',
      ),
    ],
  ),
  'g_string_chunk_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStringChunk *',
        name = 'chunk',
      ),
    ],
  ),
  'g_string_chunk_clear': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStringChunk *',
        name = 'chunk',
      ),
    ],
  ),
  'g_string_chunk_insert': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GStringChunk *',
        name = 'chunk',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_string_chunk_insert_len': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GStringChunk *',
        name = 'chunk',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'gssize',
        name = 'len',
      ),
    ],
  ),
  'g_string_chunk_insert_const': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GStringChunk *',
        name = 'chunk',
      ),
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_strcmp0': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = 'str1',
      ),
      Param(
        type = 'const char *',
        name = 'str2',
      ),
    ],
  ),
  'g_test_minimized_result': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'double',
        name = 'minimized_quantity',
      ),
      Param(
        type = 'const char *',
        name = 'format',
      ),
    ],
  ),
  'g_test_maximized_result': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'double',
        name = 'maximized_quantity',
      ),
      Param(
        type = 'const char *',
        name = 'format',
      ),
    ],
  ),
  'g_test_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'int *',
        name = 'argc',
      ),
      Param(
        type = 'char ***',
        name = 'argv',
      ),
    ],
  ),
  'g_test_run': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  'g_test_add_func': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'testpath',
      ),
      Param(
        type = 'GTestFunc',
        name = 'test_func',
      ),
    ],
  ),
  'g_test_add_data_func': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'testpath',
      ),
      Param(
        type = 'gconstpointer',
        name = 'test_data',
      ),
      Param(
        type = 'GTestDataFunc',
        name = 'test_func',
      ),
    ],
  ),
  'g_test_add_data_func_full': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'testpath',
      ),
      Param(
        type = 'gpointer',
        name = 'test_data',
      ),
      Param(
        type = 'GTestDataFunc',
        name = 'test_func',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'data_free_func',
      ),
    ],
  ),
  'g_test_fail': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'g_test_message': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'format',
      ),
    ],
  ),
  'g_test_bug_base': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'uri_pattern',
      ),
    ],
  ),
  'g_test_bug': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'bug_uri_snippet',
      ),
    ],
  ),
  'g_test_timer_start': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'g_test_timer_elapsed': Spec(
    return_type = 'double',
    parameters = [
    ],
  ),
  'g_test_timer_last': Spec(
    return_type = 'double',
    parameters = [
    ],
  ),
  'g_test_queue_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'gfree_pointer',
      ),
    ],
  ),
  'g_test_queue_destroy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GDestroyNotify',
        name = 'destroy_func',
      ),
      Param(
        type = 'gpointer',
        name = 'destroy_data',
      ),
    ],
  ),
  'g_test_trap_fork': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'guint64',
        name = 'usec_timeout',
      ),
      Param(
        type = 'GTestTrapFlags',
        name = 'test_trap_flags',
      ),
    ],
  ),
  'g_test_trap_has_passed': Spec(
    return_type = 'gboolean',
    parameters = [
    ],
  ),
  'g_test_trap_reached_timeout': Spec(
    return_type = 'gboolean',
    parameters = [
    ],
  ),
  'g_test_rand_int': Spec(
    return_type = 'gint32',
    parameters = [
    ],
  ),
  'g_test_rand_int_range': Spec(
    return_type = 'gint32',
    parameters = [
      Param(
        type = 'gint32',
        name = 'begin',
      ),
      Param(
        type = 'gint32',
        name = 'end',
      ),
    ],
  ),
  'g_test_rand_double': Spec(
    return_type = 'double',
    parameters = [
    ],
  ),
  'g_test_rand_double_range': Spec(
    return_type = 'double',
    parameters = [
      Param(
        type = 'double',
        name = 'range_start',
      ),
      Param(
        type = 'double',
        name = 'range_end',
      ),
    ],
  ),
  'g_test_create_case': Spec(
    return_type = 'GTestCase *',
    parameters = [
      Param(
        type = 'const char *',
        name = 'test_name',
      ),
      Param(
        type = 'gsize',
        name = 'data_size',
      ),
      Param(
        type = 'gconstpointer',
        name = 'test_data',
      ),
      Param(
        type = 'GTestFixtureFunc',
        name = 'data_setup',
      ),
      Param(
        type = 'GTestFixtureFunc',
        name = 'data_test',
      ),
      Param(
        type = 'GTestFixtureFunc',
        name = 'data_teardown',
      ),
    ],
  ),
  'g_test_create_suite': Spec(
    return_type = 'GTestSuite *',
    parameters = [
      Param(
        type = 'const char *',
        name = 'suite_name',
      ),
    ],
  ),
  'g_test_get_root': Spec(
    return_type = 'GTestSuite *',
    parameters = [
    ],
  ),
  'g_test_suite_add': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTestSuite *',
        name = 'suite',
      ),
      Param(
        type = 'GTestCase *',
        name = 'test_case',
      ),
    ],
  ),
  'g_test_suite_add_suite': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTestSuite *',
        name = 'suite',
      ),
      Param(
        type = 'GTestSuite *',
        name = 'nestedsuite',
      ),
    ],
  ),
  'g_test_run_suite': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'GTestSuite *',
        name = 'suite',
      ),
    ],
  ),
  'g_test_trap_assertions': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'domain',
      ),
      Param(
        type = 'const char *',
        name = 'file',
      ),
      Param(
        type = 'int',
        name = 'line',
      ),
      Param(
        type = 'const char *',
        name = 'func',
      ),
      Param(
        type = 'guint64',
        name = 'assertion_flags',
      ),
      Param(
        type = 'const char *',
        name = 'pattern',
      ),
    ],
  ),
  'g_assertion_message': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'domain',
      ),
      Param(
        type = 'const char *',
        name = 'file',
      ),
      Param(
        type = 'int',
        name = 'line',
      ),
      Param(
        type = 'const char *',
        name = 'func',
      ),
      Param(
        type = 'const char *',
        name = 'message',
      ),
    ],
  ),
  'g_assertion_message_expr': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'domain',
      ),
      Param(
        type = 'const char *',
        name = 'file',
      ),
      Param(
        type = 'int',
        name = 'line',
      ),
      Param(
        type = 'const char *',
        name = 'func',
      ),
      Param(
        type = 'const char *',
        name = 'expr',
      ),
    ],
  ),
  'g_assertion_message_cmpstr': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'domain',
      ),
      Param(
        type = 'const char *',
        name = 'file',
      ),
      Param(
        type = 'int',
        name = 'line',
      ),
      Param(
        type = 'const char *',
        name = 'func',
      ),
      Param(
        type = 'const char *',
        name = 'expr',
      ),
      Param(
        type = 'const char *',
        name = 'arg1',
      ),
      Param(
        type = 'const char *',
        name = 'cmp',
      ),
      Param(
        type = 'const char *',
        name = 'arg2',
      ),
    ],
  ),
  'g_assertion_message_cmpnum': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'domain',
      ),
      Param(
        type = 'const char *',
        name = 'file',
      ),
      Param(
        type = 'int',
        name = 'line',
      ),
      Param(
        type = 'const char *',
        name = 'func',
      ),
      Param(
        type = 'const char *',
        name = 'expr',
      ),
      Param(
        type = 'long double',
        name = 'arg1',
      ),
      Param(
        type = 'const char *',
        name = 'cmp',
      ),
      Param(
        type = 'long double',
        name = 'arg2',
      ),
      Param(
        type = 'char',
        name = 'numtype',
      ),
    ],
  ),
  'g_assertion_message_error': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'domain',
      ),
      Param(
        type = 'const char *',
        name = 'file',
      ),
      Param(
        type = 'int',
        name = 'line',
      ),
      Param(
        type = 'const char *',
        name = 'func',
      ),
      Param(
        type = 'const char *',
        name = 'expr',
      ),
      Param(
        type = 'const GError *',
        name = 'error',
      ),
      Param(
        type = 'GQuark',
        name = 'error_domain',
      ),
      Param(
        type = 'int',
        name = 'error_code',
      ),
    ],
  ),
  'g_test_add_vtable': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'testpath',
      ),
      Param(
        type = 'gsize',
        name = 'data_size',
      ),
      Param(
        type = 'gconstpointer',
        name = 'test_data',
      ),
      Param(
        type = 'GTestFixtureFunc',
        name = 'data_setup',
      ),
      Param(
        type = 'GTestFixtureFunc',
        name = 'data_test',
      ),
      Param(
        type = 'GTestFixtureFunc',
        name = 'data_teardown',
      ),
    ],
  ),
  'g_test_log_type_name': Spec(
    return_type = 'const char *',
    parameters = [
      Param(
        type = 'GTestLogType',
        name = 'log_type',
      ),
    ],
  ),
  'g_test_log_buffer_new': Spec(
    return_type = 'GTestLogBuffer *',
    parameters = [
    ],
  ),
  'g_test_log_buffer_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTestLogBuffer *',
        name = 'tbuffer',
      ),
    ],
  ),
  'g_test_log_buffer_push': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTestLogBuffer *',
        name = 'tbuffer',
      ),
      Param(
        type = 'guint',
        name = 'n_bytes',
      ),
      Param(
        type = 'const guint8 *',
        name = 'bytes',
      ),
    ],
  ),
  'g_test_log_buffer_pop': Spec(
    return_type = 'GTestLogMsg *',
    parameters = [
      Param(
        type = 'GTestLogBuffer *',
        name = 'tbuffer',
      ),
    ],
  ),
  'g_test_log_msg_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTestLogMsg *',
        name = 'tmsg',
      ),
    ],
  ),
  'g_test_log_set_fatal_handler': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTestLogFatalFunc',
        name = 'log_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_test_expect_message': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'log_domain',
      ),
      Param(
        type = 'GLogLevelFlags',
        name = 'log_level',
      ),
      Param(
        type = 'const gchar *',
        name = 'pattern',
      ),
    ],
  ),
  'g_test_assert_expected_messages_internal': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = 'domain',
      ),
      Param(
        type = 'const char *',
        name = 'file',
      ),
      Param(
        type = 'int',
        name = 'line',
      ),
      Param(
        type = 'const char *',
        name = 'func',
      ),
    ],
  ),
  'g_thread_pool_new': Spec(
    return_type = 'GThreadPool *',
    parameters = [
      Param(
        type = 'GFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
      Param(
        type = 'gint',
        name = 'max_threads',
      ),
      Param(
        type = 'gboolean',
        name = 'exclusive',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_thread_pool_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GThreadPool *',
        name = 'pool',
      ),
      Param(
        type = 'gboolean',
        name = 'immediate',
      ),
      Param(
        type = 'gboolean',
        name = 'wait_',
      ),
    ],
  ),
  'g_thread_pool_push': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GThreadPool *',
        name = 'pool',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_thread_pool_unprocessed': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GThreadPool *',
        name = 'pool',
      ),
    ],
  ),
  'g_thread_pool_set_sort_function': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GThreadPool *',
        name = 'pool',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_thread_pool_set_max_threads': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GThreadPool *',
        name = 'pool',
      ),
      Param(
        type = 'gint',
        name = 'max_threads',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_thread_pool_get_max_threads': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GThreadPool *',
        name = 'pool',
      ),
    ],
  ),
  'g_thread_pool_get_num_threads': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GThreadPool *',
        name = 'pool',
      ),
    ],
  ),
  'g_thread_pool_set_max_unused_threads': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gint',
        name = 'max_threads',
      ),
    ],
  ),
  'g_thread_pool_get_max_unused_threads': Spec(
    return_type = 'gint',
    parameters = [
    ],
  ),
  'g_thread_pool_get_num_unused_threads': Spec(
    return_type = 'guint',
    parameters = [
    ],
  ),
  'g_thread_pool_stop_unused_threads': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'g_thread_pool_set_max_idle_time': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'guint',
        name = 'interval',
      ),
    ],
  ),
  'g_thread_pool_get_max_idle_time': Spec(
    return_type = 'guint',
    parameters = [
    ],
  ),
  'g_timer_new': Spec(
    return_type = 'GTimer *',
    parameters = [
    ],
  ),
  'g_timer_destroy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTimer *',
        name = 'timer',
      ),
    ],
  ),
  'g_timer_start': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTimer *',
        name = 'timer',
      ),
    ],
  ),
  'g_timer_stop': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTimer *',
        name = 'timer',
      ),
    ],
  ),
  'g_timer_reset': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTimer *',
        name = 'timer',
      ),
    ],
  ),
  'g_timer_continue': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTimer *',
        name = 'timer',
      ),
    ],
  ),
  'g_timer_elapsed': Spec(
    return_type = 'gdouble',
    parameters = [
      Param(
        type = 'GTimer *',
        name = 'timer',
      ),
      Param(
        type = 'gulong *',
        name = 'microseconds',
      ),
    ],
  ),
  'g_usleep': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gulong',
        name = 'microseconds',
      ),
    ],
  ),
  'g_time_val_add': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTimeVal *',
        name = 'time_',
      ),
      Param(
        type = 'glong',
        name = 'microseconds',
      ),
    ],
  ),
  'g_time_val_from_iso8601': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'iso_date',
      ),
      Param(
        type = 'GTimeVal *',
        name = 'time_',
      ),
    ],
  ),
  'g_time_val_to_iso8601': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GTimeVal *',
        name = 'time_',
      ),
    ],
  ),
  'g_trash_stack_push': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTrashStack **',
        name = 'stack_p',
      ),
      Param(
        type = 'gpointer',
        name = 'data_p',
      ),
    ],
  ),
  'g_trash_stack_pop': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GTrashStack **',
        name = 'stack_p',
      ),
    ],
  ),
  'g_trash_stack_peek': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GTrashStack **',
        name = 'stack_p',
      ),
    ],
  ),
  'g_trash_stack_height': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GTrashStack **',
        name = 'stack_p',
      ),
    ],
  ),
  'g_trash_stack_push': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTrashStack **',
        name = 'stack_p',
      ),
      Param(
        type = 'gpointer',
        name = 'data_p',
      ),
    ],
  ),
  'g_trash_stack_pop': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GTrashStack **',
        name = 'stack_p',
      ),
    ],
  ),
  'g_trash_stack_peek': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GTrashStack **',
        name = 'stack_p',
      ),
    ],
  ),
  'g_trash_stack_height': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GTrashStack **',
        name = 'stack_p',
      ),
    ],
  ),
  'g_tree_new': Spec(
    return_type = 'GTree *',
    parameters = [
      Param(
        type = 'GCompareFunc',
        name = 'key_compare_func',
      ),
    ],
  ),
  'g_tree_new_with_data': Spec(
    return_type = 'GTree *',
    parameters = [
      Param(
        type = 'GCompareDataFunc',
        name = 'key_compare_func',
      ),
      Param(
        type = 'gpointer',
        name = 'key_compare_data',
      ),
    ],
  ),
  'g_tree_new_full': Spec(
    return_type = 'GTree *',
    parameters = [
      Param(
        type = 'GCompareDataFunc',
        name = 'key_compare_func',
      ),
      Param(
        type = 'gpointer',
        name = 'key_compare_data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'key_destroy_func',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'value_destroy_func',
      ),
    ],
  ),
  'g_tree_ref': Spec(
    return_type = 'GTree *',
    parameters = [
      Param(
        type = 'GTree *',
        name = 'tree',
      ),
    ],
  ),
  'g_tree_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTree *',
        name = 'tree',
      ),
    ],
  ),
  'g_tree_destroy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTree *',
        name = 'tree',
      ),
    ],
  ),
  'g_tree_insert': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTree *',
        name = 'tree',
      ),
      Param(
        type = 'gpointer',
        name = 'key',
      ),
      Param(
        type = 'gpointer',
        name = 'value',
      ),
    ],
  ),
  'g_tree_replace': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTree *',
        name = 'tree',
      ),
      Param(
        type = 'gpointer',
        name = 'key',
      ),
      Param(
        type = 'gpointer',
        name = 'value',
      ),
    ],
  ),
  'g_tree_remove': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GTree *',
        name = 'tree',
      ),
      Param(
        type = 'gconstpointer',
        name = 'key',
      ),
    ],
  ),
  'g_tree_steal': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GTree *',
        name = 'tree',
      ),
      Param(
        type = 'gconstpointer',
        name = 'key',
      ),
    ],
  ),
  'g_tree_lookup': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GTree *',
        name = 'tree',
      ),
      Param(
        type = 'gconstpointer',
        name = 'key',
      ),
    ],
  ),
  'g_tree_lookup_extended': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GTree *',
        name = 'tree',
      ),
      Param(
        type = 'gconstpointer',
        name = 'lookup_key',
      ),
      Param(
        type = 'gpointer *',
        name = 'orig_key',
      ),
      Param(
        type = 'gpointer *',
        name = 'value',
      ),
    ],
  ),
  'g_tree_foreach': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTree *',
        name = 'tree',
      ),
      Param(
        type = 'GTraverseFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_tree_traverse': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTree *',
        name = 'tree',
      ),
      Param(
        type = 'GTraverseFunc',
        name = 'traverse_func',
      ),
      Param(
        type = 'GTraverseType',
        name = 'traverse_type',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_tree_search': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GTree *',
        name = 'tree',
      ),
      Param(
        type = 'GCompareFunc',
        name = 'search_func',
      ),
      Param(
        type = 'gconstpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_tree_height': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GTree *',
        name = 'tree',
      ),
    ],
  ),
  'g_tree_nnodes': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GTree *',
        name = 'tree',
      ),
    ],
  ),
  'g_uri_unescape_string': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'const char *',
        name = 'escaped_string',
      ),
      Param(
        type = 'const char *',
        name = 'illegal_characters',
      ),
    ],
  ),
  'g_uri_unescape_segment': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'const char *',
        name = 'escaped_string',
      ),
      Param(
        type = 'const char *',
        name = 'escaped_string_end',
      ),
      Param(
        type = 'const char *',
        name = 'illegal_characters',
      ),
    ],
  ),
  'g_uri_parse_scheme': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'const char *',
        name = 'uri',
      ),
    ],
  ),
  'g_uri_escape_string': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'const char *',
        name = 'unescaped',
      ),
      Param(
        type = 'const char *',
        name = 'reserved_chars_allowed',
      ),
      Param(
        type = 'gboolean',
        name = 'allow_utf8',
      ),
    ],
  ),
  'g_variant_type_string_is_valid': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'type_string',
      ),
    ],
  ),
  'g_variant_type_string_scan': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'limit',
      ),
      Param(
        type = 'const gchar **',
        name = 'endptr',
      ),
    ],
  ),
  'g_variant_type_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_copy': Spec(
    return_type = 'GVariantType *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_new': Spec(
    return_type = 'GVariantType *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'type_string',
      ),
    ],
  ),
  'g_variant_type_get_string_length': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_peek_string': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_dup_string': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_is_definite': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_is_container': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_is_basic': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_is_maybe': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_is_array': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_is_tuple': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_is_dict_entry': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_is_variant': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_hash': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_equal': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'type1',
      ),
      Param(
        type = 'gconstpointer',
        name = 'type2',
      ),
    ],
  ),
  'g_variant_type_is_subtype_of': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
      Param(
        type = 'const GVariantType *',
        name = 'supertype',
      ),
    ],
  ),
  'g_variant_type_element': Spec(
    return_type = 'const GVariantType *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_first': Spec(
    return_type = 'const GVariantType *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_next': Spec(
    return_type = 'const GVariantType *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_n_items': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_key': Spec(
    return_type = 'const GVariantType *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_value': Spec(
    return_type = 'const GVariantType *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_type_new_array': Spec(
    return_type = 'GVariantType *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'element',
      ),
    ],
  ),
  'g_variant_type_new_maybe': Spec(
    return_type = 'GVariantType *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'element',
      ),
    ],
  ),
  'g_variant_type_new_tuple': Spec(
    return_type = 'GVariantType *',
    parameters = [
      Param(
        type = 'const GVariantType *const *',
        name = 'items',
      ),
      Param(
        type = 'gint',
        name = 'length',
      ),
    ],
  ),
  'g_variant_type_new_dict_entry': Spec(
    return_type = 'GVariantType *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'key',
      ),
      Param(
        type = 'const GVariantType *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_type_checked_': Spec(
    return_type = 'const GVariantType *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = '',
      ),
    ],
  ),
  'g_variant_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_ref': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_ref_sink': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_is_floating': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_take_ref': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_type': Spec(
    return_type = 'const GVariantType *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_type_string': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_is_of_type': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_is_container': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_classify': Spec(
    return_type = 'GVariantClass',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_new_boolean': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'gboolean',
        name = 'value',
      ),
    ],
  ),
  'g_variant_new_byte': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'guchar',
        name = 'value',
      ),
    ],
  ),
  'g_variant_new_int16': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'gint16',
        name = 'value',
      ),
    ],
  ),
  'g_variant_new_uint16': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'guint16',
        name = 'value',
      ),
    ],
  ),
  'g_variant_new_int32': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'gint32',
        name = 'value',
      ),
    ],
  ),
  'g_variant_new_uint32': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'guint32',
        name = 'value',
      ),
    ],
  ),
  'g_variant_new_int64': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'gint64',
        name = 'value',
      ),
    ],
  ),
  'g_variant_new_uint64': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'guint64',
        name = 'value',
      ),
    ],
  ),
  'g_variant_new_handle': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'gint32',
        name = 'value',
      ),
    ],
  ),
  'g_variant_new_double': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'gdouble',
        name = 'value',
      ),
    ],
  ),
  'g_variant_new_string': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_variant_new_object_path': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'object_path',
      ),
    ],
  ),
  'g_variant_is_object_path': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_variant_new_signature': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'signature',
      ),
    ],
  ),
  'g_variant_is_signature': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_variant_new_variant': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_new_strv': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const gchar *const *',
        name = 'strv',
      ),
      Param(
        type = 'gssize',
        name = 'length',
      ),
    ],
  ),
  'g_variant_new_objv': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const gchar *const *',
        name = 'strv',
      ),
      Param(
        type = 'gssize',
        name = 'length',
      ),
    ],
  ),
  'g_variant_new_bytestring': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'string',
      ),
    ],
  ),
  'g_variant_new_bytestring_array': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const gchar *const *',
        name = 'strv',
      ),
      Param(
        type = 'gssize',
        name = 'length',
      ),
    ],
  ),
  'g_variant_new_fixed_array': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'element_type',
      ),
      Param(
        type = 'gconstpointer',
        name = 'elements',
      ),
      Param(
        type = 'gsize',
        name = 'n_elements',
      ),
      Param(
        type = 'gsize',
        name = 'element_size',
      ),
    ],
  ),
  'g_variant_get_boolean': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_byte': Spec(
    return_type = 'guchar',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_int16': Spec(
    return_type = 'gint16',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_uint16': Spec(
    return_type = 'guint16',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_int32': Spec(
    return_type = 'gint32',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_uint32': Spec(
    return_type = 'guint32',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_int64': Spec(
    return_type = 'gint64',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_uint64': Spec(
    return_type = 'guint64',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_handle': Spec(
    return_type = 'gint32',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_double': Spec(
    return_type = 'gdouble',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_variant': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_string': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
    ],
  ),
  'g_variant_dup_string': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
    ],
  ),
  'g_variant_get_strv': Spec(
    return_type = 'const gchar **',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
    ],
  ),
  'g_variant_dup_strv': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
    ],
  ),
  'g_variant_get_objv': Spec(
    return_type = 'const gchar **',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
    ],
  ),
  'g_variant_dup_objv': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
    ],
  ),
  'g_variant_get_bytestring': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_dup_bytestring': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
    ],
  ),
  'g_variant_get_bytestring_array': Spec(
    return_type = 'const gchar **',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
    ],
  ),
  'g_variant_dup_bytestring_array': Spec(
    return_type = 'gchar **',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'gsize *',
        name = 'length',
      ),
    ],
  ),
  'g_variant_new_maybe': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'child_type',
      ),
      Param(
        type = 'GVariant *',
        name = 'child',
      ),
    ],
  ),
  'g_variant_new_array': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'child_type',
      ),
      Param(
        type = 'GVariant *const *',
        name = 'children',
      ),
      Param(
        type = 'gsize',
        name = 'n_children',
      ),
    ],
  ),
  'g_variant_new_tuple': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'GVariant *const *',
        name = 'children',
      ),
      Param(
        type = 'gsize',
        name = 'n_children',
      ),
    ],
  ),
  'g_variant_new_dict_entry': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'key',
      ),
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_maybe': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_n_children': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_child': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'gsize',
        name = 'index_',
      ),
      Param(
        type = 'const gchar *',
        name = 'format_string',
      ),
    ],
  ),
  'g_variant_get_child_value': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'gsize',
        name = 'index_',
      ),
    ],
  ),
  'g_variant_lookup': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'dictionary',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'const gchar *',
        name = 'format_string',
      ),
    ],
  ),
  'g_variant_lookup_value': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'dictionary',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'const GVariantType *',
        name = 'expected_type',
      ),
    ],
  ),
  'g_variant_get_fixed_array': Spec(
    return_type = 'gconstpointer',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'gsize *',
        name = 'n_elements',
      ),
      Param(
        type = 'gsize',
        name = 'element_size',
      ),
    ],
  ),
  'g_variant_get_size': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_data': Spec(
    return_type = 'gconstpointer',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_get_data_as_bytes': Spec(
    return_type = 'GBytes *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_store': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_variant_print': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'gboolean',
        name = 'type_annotate',
      ),
    ],
  ),
  'g_variant_print_string': Spec(
    return_type = 'GString *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'GString *',
        name = 'string',
      ),
      Param(
        type = 'gboolean',
        name = 'type_annotate',
      ),
    ],
  ),
  'g_variant_hash': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'value',
      ),
    ],
  ),
  'g_variant_equal': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'one',
      ),
      Param(
        type = 'gconstpointer',
        name = 'two',
      ),
    ],
  ),
  'g_variant_get_normal_form': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_is_normal_form': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_byteswap': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_new_from_bytes': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
      Param(
        type = 'GBytes *',
        name = 'bytes',
      ),
      Param(
        type = 'gboolean',
        name = 'trusted',
      ),
    ],
  ),
  'g_variant_new_from_data': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
      Param(
        type = 'gconstpointer',
        name = 'data',
      ),
      Param(
        type = 'gsize',
        name = 'size',
      ),
      Param(
        type = 'gboolean',
        name = 'trusted',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'notify',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_variant_iter_new': Spec(
    return_type = 'GVariantIter *',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_iter_init': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'GVariantIter *',
        name = 'iter',
      ),
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_iter_copy': Spec(
    return_type = 'GVariantIter *',
    parameters = [
      Param(
        type = 'GVariantIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_variant_iter_n_children': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'GVariantIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_variant_iter_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariantIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_variant_iter_next_value': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'GVariantIter *',
        name = 'iter',
      ),
    ],
  ),
  'g_variant_iter_next': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GVariantIter *',
        name = 'iter',
      ),
      Param(
        type = 'const gchar *',
        name = 'format_string',
      ),
    ],
  ),
  'g_variant_iter_loop': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GVariantIter *',
        name = 'iter',
      ),
      Param(
        type = 'const gchar *',
        name = 'format_string',
      ),
    ],
  ),
  'g_variant_parser_get_error_quark': Spec(
    return_type = 'GQuark',
    parameters = [
    ],
  ),
  'g_variant_builder_new': Spec(
    return_type = 'GVariantBuilder *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_builder_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariantBuilder *',
        name = 'builder',
      ),
    ],
  ),
  'g_variant_builder_ref': Spec(
    return_type = 'GVariantBuilder *',
    parameters = [
      Param(
        type = 'GVariantBuilder *',
        name = 'builder',
      ),
    ],
  ),
  'g_variant_builder_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariantBuilder *',
        name = 'builder',
      ),
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_builder_end': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'GVariantBuilder *',
        name = 'builder',
      ),
    ],
  ),
  'g_variant_builder_clear': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariantBuilder *',
        name = 'builder',
      ),
    ],
  ),
  'g_variant_builder_open': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariantBuilder *',
        name = 'builder',
      ),
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
    ],
  ),
  'g_variant_builder_close': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariantBuilder *',
        name = 'builder',
      ),
    ],
  ),
  'g_variant_builder_add_value': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariantBuilder *',
        name = 'builder',
      ),
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
    ],
  ),
  'g_variant_builder_add': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariantBuilder *',
        name = 'builder',
      ),
      Param(
        type = 'const gchar *',
        name = 'format_string',
      ),
    ],
  ),
  'g_variant_builder_add_parsed': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariantBuilder *',
        name = 'builder',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_variant_new': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'format_string',
      ),
    ],
  ),
  'g_variant_get': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'const gchar *',
        name = 'format_string',
      ),
    ],
  ),
  'g_variant_new_va': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'format_string',
      ),
      Param(
        type = 'const gchar **',
        name = 'endptr',
      ),
      Param(
        type = 'va_list *',
        name = 'app',
      ),
    ],
  ),
  'g_variant_get_va': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'const gchar *',
        name = 'format_string',
      ),
      Param(
        type = 'const gchar **',
        name = 'endptr',
      ),
      Param(
        type = 'va_list *',
        name = 'app',
      ),
    ],
  ),
  'g_variant_check_format_string': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GVariant *',
        name = 'value',
      ),
      Param(
        type = 'const gchar *',
        name = 'format_string',
      ),
      Param(
        type = 'gboolean',
        name = 'copy_only',
      ),
    ],
  ),
  'g_variant_parse': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
      Param(
        type = 'const gchar *',
        name = 'text',
      ),
      Param(
        type = 'const gchar *',
        name = 'limit',
      ),
      Param(
        type = 'const gchar **',
        name = 'endptr',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_variant_new_parsed': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_variant_new_parsed_va': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
      Param(
        type = 'va_list *',
        name = 'app',
      ),
    ],
  ),
  'g_variant_compare': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gconstpointer',
        name = 'one',
      ),
      Param(
        type = 'gconstpointer',
        name = 'two',
      ),
    ],
  ),
  'glib_check_version': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'guint',
        name = 'required_major',
      ),
      Param(
        type = 'guint',
        name = 'required_minor',
      ),
      Param(
        type = 'guint',
        name = 'required_micro',
      ),
    ],
  ),
  'g_mem_chunk_new': Spec(
    return_type = 'GMemChunk *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'gint',
        name = 'atom_size',
      ),
      Param(
        type = 'gsize',
        name = 'area_size',
      ),
      Param(
        type = 'gint',
        name = 'type',
      ),
    ],
  ),
  'g_mem_chunk_destroy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMemChunk *',
        name = 'mem_chunk',
      ),
    ],
  ),
  'g_mem_chunk_alloc': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GMemChunk *',
        name = 'mem_chunk',
      ),
    ],
  ),
  'g_mem_chunk_alloc0': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GMemChunk *',
        name = 'mem_chunk',
      ),
    ],
  ),
  'g_mem_chunk_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMemChunk *',
        name = 'mem_chunk',
      ),
      Param(
        type = 'gpointer',
        name = 'mem',
      ),
    ],
  ),
  'g_mem_chunk_clean': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMemChunk *',
        name = 'mem_chunk',
      ),
    ],
  ),
  'g_mem_chunk_reset': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMemChunk *',
        name = 'mem_chunk',
      ),
    ],
  ),
  'g_mem_chunk_print': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMemChunk *',
        name = 'mem_chunk',
      ),
    ],
  ),
  'g_mem_chunk_info': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'g_blow_chunks': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'g_allocator_new': Spec(
    return_type = 'GAllocator *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'guint',
        name = 'n_preallocs',
      ),
    ],
  ),
  'g_allocator_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAllocator *',
        name = 'allocator',
      ),
    ],
  ),
  'g_list_push_allocator': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAllocator *',
        name = 'allocator',
      ),
    ],
  ),
  'g_list_pop_allocator': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'g_slist_push_allocator': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAllocator *',
        name = 'allocator',
      ),
    ],
  ),
  'g_slist_pop_allocator': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'g_node_push_allocator': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GAllocator *',
        name = 'allocator',
      ),
    ],
  ),
  'g_node_pop_allocator': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'g_cache_new': Spec(
    return_type = 'GCache *',
    parameters = [
      Param(
        type = 'GCacheNewFunc',
        name = 'value_new_func',
      ),
      Param(
        type = 'GCacheDestroyFunc',
        name = 'value_destroy_func',
      ),
      Param(
        type = 'GCacheDupFunc',
        name = 'key_dup_func',
      ),
      Param(
        type = 'GCacheDestroyFunc',
        name = 'key_destroy_func',
      ),
      Param(
        type = 'GHashFunc',
        name = 'hash_key_func',
      ),
      Param(
        type = 'GHashFunc',
        name = 'hash_value_func',
      ),
      Param(
        type = 'GEqualFunc',
        name = 'key_equal_func',
      ),
    ],
  ),
  'g_cache_destroy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCache *',
        name = 'cache',
      ),
    ],
  ),
  'g_cache_insert': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GCache *',
        name = 'cache',
      ),
      Param(
        type = 'gpointer',
        name = 'key',
      ),
    ],
  ),
  'g_cache_remove': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCache *',
        name = 'cache',
      ),
      Param(
        type = 'gconstpointer',
        name = 'value',
      ),
    ],
  ),
  'g_cache_key_foreach': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCache *',
        name = 'cache',
      ),
      Param(
        type = 'GHFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_cache_value_foreach': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCache *',
        name = 'cache',
      ),
      Param(
        type = 'GHFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_completion_new': Spec(
    return_type = 'GCompletion *',
    parameters = [
      Param(
        type = 'GCompletionFunc',
        name = 'func',
      ),
    ],
  ),
  'g_completion_add_items': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCompletion *',
        name = 'cmp',
      ),
      Param(
        type = 'GList *',
        name = 'items',
      ),
    ],
  ),
  'g_completion_remove_items': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCompletion *',
        name = 'cmp',
      ),
      Param(
        type = 'GList *',
        name = 'items',
      ),
    ],
  ),
  'g_completion_clear_items': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCompletion *',
        name = 'cmp',
      ),
    ],
  ),
  'g_completion_complete': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GCompletion *',
        name = 'cmp',
      ),
      Param(
        type = 'const gchar *',
        name = 'prefix',
      ),
      Param(
        type = 'gchar **',
        name = 'new_prefix',
      ),
    ],
  ),
  'g_completion_complete_utf8': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GCompletion *',
        name = 'cmp',
      ),
      Param(
        type = 'const gchar *',
        name = 'prefix',
      ),
      Param(
        type = 'gchar **',
        name = 'new_prefix',
      ),
    ],
  ),
  'g_completion_set_compare': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCompletion *',
        name = 'cmp',
      ),
      Param(
        type = 'GCompletionStrncmpFunc',
        name = 'strncmp_func',
      ),
    ],
  ),
  'g_completion_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCompletion *',
        name = 'cmp',
      ),
    ],
  ),
  'g_relation_new': Spec(
    return_type = 'GRelation *',
    parameters = [
      Param(
        type = 'gint',
        name = 'fields',
      ),
    ],
  ),
  'g_relation_destroy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRelation *',
        name = 'relation',
      ),
    ],
  ),
  'g_relation_index': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRelation *',
        name = 'relation',
      ),
      Param(
        type = 'gint',
        name = 'field',
      ),
      Param(
        type = 'GHashFunc',
        name = 'hash_func',
      ),
      Param(
        type = 'GEqualFunc',
        name = 'key_equal_func',
      ),
    ],
  ),
  'g_relation_insert': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRelation *',
        name = 'relation',
      ),
    ],
  ),
  'g_relation_delete': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GRelation *',
        name = 'relation',
      ),
      Param(
        type = 'gconstpointer',
        name = 'key',
      ),
      Param(
        type = 'gint',
        name = 'field',
      ),
    ],
  ),
  'g_relation_select': Spec(
    return_type = 'GTuples *',
    parameters = [
      Param(
        type = 'GRelation *',
        name = 'relation',
      ),
      Param(
        type = 'gconstpointer',
        name = 'key',
      ),
      Param(
        type = 'gint',
        name = 'field',
      ),
    ],
  ),
  'g_relation_count': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GRelation *',
        name = 'relation',
      ),
      Param(
        type = 'gconstpointer',
        name = 'key',
      ),
      Param(
        type = 'gint',
        name = 'field',
      ),
    ],
  ),
  'g_relation_exists': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GRelation *',
        name = 'relation',
      ),
    ],
  ),
  'g_relation_print': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GRelation *',
        name = 'relation',
      ),
    ],
  ),
  'g_tuples_destroy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTuples *',
        name = 'tuples',
      ),
    ],
  ),
  'g_tuples_index': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GTuples *',
        name = 'tuples',
      ),
      Param(
        type = 'gint',
        name = 'index_',
      ),
      Param(
        type = 'gint',
        name = 'field',
      ),
    ],
  ),
  'g_thread_create': Spec(
    return_type = 'GThread *',
    parameters = [
      Param(
        type = 'GThreadFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'gboolean',
        name = 'joinable',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_thread_create_full': Spec(
    return_type = 'GThread *',
    parameters = [
      Param(
        type = 'GThreadFunc',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'gulong',
        name = 'stack_size',
      ),
      Param(
        type = 'gboolean',
        name = 'joinable',
      ),
      Param(
        type = 'gboolean',
        name = 'bound',
      ),
      Param(
        type = 'GThreadPriority',
        name = 'priority',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_thread_set_priority': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GThread *',
        name = 'thread',
      ),
      Param(
        type = 'GThreadPriority',
        name = 'priority',
      ),
    ],
  ),
  'g_thread_foreach': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GFunc',
        name = 'thread_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  '__bswap_32': Spec(
    return_type = 'unsigned int',
    parameters = [
      Param(
        type = 'unsigned int',
        name = '__bsx',
      ),
    ],
  ),
  '__bswap_64': Spec(
    return_type = 'unsigned long long',
    parameters = [
      Param(
        type = 'unsigned long long',
        name = '__bsx',
      ),
    ],
  ),
  '__sched_cpucount': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'size_t',
        name = '__setsize',
      ),
      Param(
        type = 'const cpu_set_t *',
        name = '__setp',
      ),
    ],
  ),
  '__sched_cpualloc': Spec(
    return_type = 'cpu_set_t *',
    parameters = [
      Param(
        type = 'size_t',
        name = '__count',
      ),
    ],
  ),
  '__sched_cpufree': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'cpu_set_t *',
        name = '__set',
      ),
    ],
  ),
  'sched_setparam': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__pid_t',
        name = '__pid',
      ),
      Param(
        type = 'const struct sched_param *',
        name = '__param',
      ),
    ],
  ),
  'sched_getparam': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__pid_t',
        name = '__pid',
      ),
      Param(
        type = 'struct sched_param *',
        name = '__param',
      ),
    ],
  ),
  'sched_setscheduler': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__pid_t',
        name = '__pid',
      ),
      Param(
        type = 'int',
        name = '__policy',
      ),
      Param(
        type = 'const struct sched_param *',
        name = '__param',
      ),
    ],
  ),
  'sched_getscheduler': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__pid_t',
        name = '__pid',
      ),
    ],
  ),
  'sched_yield': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  'sched_get_priority_max': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__algorithm',
      ),
    ],
  ),
  'sched_get_priority_min': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__algorithm',
      ),
    ],
  ),
  'sched_rr_get_interval': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__pid_t',
        name = '__pid',
      ),
      Param(
        type = 'struct timespec *',
        name = '__t',
      ),
    ],
  ),
  'pthread_create': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_t *restrict',
        name = '__newthread',
      ),
      Param(
        type = 'const pthread_attr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'void *(*)(void *)',
        name = '__start_routine',
      ),
      Param(
        type = 'void *restrict',
        name = '__arg',
      ),
    ],
  ),
  'pthread_exit': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'void *',
        name = '__retval',
      ),
    ],
  ),
  'pthread_join': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_t',
        name = '__th',
      ),
      Param(
        type = 'void **',
        name = '__thread_return',
      ),
    ],
  ),
  'pthread_detach': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_t',
        name = '__th',
      ),
    ],
  ),
  'pthread_self': Spec(
    return_type = 'pthread_t',
    parameters = [
    ],
  ),
  'pthread_equal': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_t',
        name = '__thread1',
      ),
      Param(
        type = 'pthread_t',
        name = '__thread2',
      ),
    ],
  ),
  'pthread_attr_init': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_attr_t *',
        name = '__attr',
      ),
    ],
  ),
  'pthread_attr_destroy': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_attr_t *',
        name = '__attr',
      ),
    ],
  ),
  'pthread_attr_getdetachstate': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_attr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int *',
        name = '__detachstate',
      ),
    ],
  ),
  'pthread_attr_setdetachstate': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_attr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int',
        name = '__detachstate',
      ),
    ],
  ),
  'pthread_attr_getguardsize': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_attr_t *',
        name = '__attr',
      ),
      Param(
        type = 'size_t *',
        name = '__guardsize',
      ),
    ],
  ),
  'pthread_attr_setguardsize': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_attr_t *',
        name = '__attr',
      ),
      Param(
        type = 'size_t',
        name = '__guardsize',
      ),
    ],
  ),
  'pthread_attr_getschedparam': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_attr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'struct sched_param *restrict',
        name = '__param',
      ),
    ],
  ),
  'pthread_attr_setschedparam': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_attr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'const struct sched_param *restrict',
        name = '__param',
      ),
    ],
  ),
  'pthread_attr_getschedpolicy': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_attr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'int *restrict',
        name = '__policy',
      ),
    ],
  ),
  'pthread_attr_setschedpolicy': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_attr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int',
        name = '__policy',
      ),
    ],
  ),
  'pthread_attr_getinheritsched': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_attr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'int *restrict',
        name = '__inherit',
      ),
    ],
  ),
  'pthread_attr_setinheritsched': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_attr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int',
        name = '__inherit',
      ),
    ],
  ),
  'pthread_attr_getscope': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_attr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'int *restrict',
        name = '__scope',
      ),
    ],
  ),
  'pthread_attr_setscope': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_attr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int',
        name = '__scope',
      ),
    ],
  ),
  'pthread_attr_getstackaddr': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_attr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'void **restrict',
        name = '__stackaddr',
      ),
    ],
  ),
  'pthread_attr_setstackaddr': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_attr_t *',
        name = '__attr',
      ),
      Param(
        type = 'void *',
        name = '__stackaddr',
      ),
    ],
  ),
  'pthread_attr_getstacksize': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_attr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'size_t *restrict',
        name = '__stacksize',
      ),
    ],
  ),
  'pthread_attr_setstacksize': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_attr_t *',
        name = '__attr',
      ),
      Param(
        type = 'size_t',
        name = '__stacksize',
      ),
    ],
  ),
  'pthread_attr_getstack': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_attr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'void **restrict',
        name = '__stackaddr',
      ),
      Param(
        type = 'size_t *restrict',
        name = '__stacksize',
      ),
    ],
  ),
  'pthread_attr_setstack': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_attr_t *',
        name = '__attr',
      ),
      Param(
        type = 'void *',
        name = '__stackaddr',
      ),
      Param(
        type = 'size_t',
        name = '__stacksize',
      ),
    ],
  ),
  'pthread_setschedparam': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_t',
        name = '__target_thread',
      ),
      Param(
        type = 'int',
        name = '__policy',
      ),
      Param(
        type = 'const struct sched_param *',
        name = '__param',
      ),
    ],
  ),
  'pthread_getschedparam': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_t',
        name = '__target_thread',
      ),
      Param(
        type = 'int *restrict',
        name = '__policy',
      ),
      Param(
        type = 'struct sched_param *restrict',
        name = '__param',
      ),
    ],
  ),
  'pthread_setschedprio': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_t',
        name = '__target_thread',
      ),
      Param(
        type = 'int',
        name = '__prio',
      ),
    ],
  ),
  'pthread_once': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_once_t *',
        name = '__once_control',
      ),
      Param(
        type = 'void (*)(void)',
        name = '__init_routine',
      ),
    ],
  ),
  'pthread_setcancelstate': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__state',
      ),
      Param(
        type = 'int *',
        name = '__oldstate',
      ),
    ],
  ),
  'pthread_setcanceltype': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__type',
      ),
      Param(
        type = 'int *',
        name = '__oldtype',
      ),
    ],
  ),
  'pthread_cancel': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_t',
        name = '__th',
      ),
    ],
  ),
  'pthread_testcancel': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  '__pthread_register_cancel': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = '__pthread_unwind_buf_t *',
        name = '__buf',
      ),
    ],
  ),
  '__pthread_unregister_cancel': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = '__pthread_unwind_buf_t *',
        name = '__buf',
      ),
    ],
  ),
  '__pthread_unwind_next': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = '__pthread_unwind_buf_t *',
        name = '__buf',
      ),
    ],
  ),
  '__sigsetjmp': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'struct __jmp_buf_tag *',
        name = '__env',
      ),
      Param(
        type = 'int',
        name = '__savemask',
      ),
    ],
  ),
  'pthread_mutex_init': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutex_t *',
        name = '__mutex',
      ),
      Param(
        type = 'const pthread_mutexattr_t *',
        name = '__mutexattr',
      ),
    ],
  ),
  'pthread_mutex_destroy': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutex_t *',
        name = '__mutex',
      ),
    ],
  ),
  'pthread_mutex_trylock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutex_t *',
        name = '__mutex',
      ),
    ],
  ),
  'pthread_mutex_lock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutex_t *',
        name = '__mutex',
      ),
    ],
  ),
  'pthread_mutex_timedlock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutex_t *restrict',
        name = '__mutex',
      ),
      Param(
        type = 'const struct timespec *restrict',
        name = '__abstime',
      ),
    ],
  ),
  'pthread_mutex_unlock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutex_t *',
        name = '__mutex',
      ),
    ],
  ),
  'pthread_mutex_getprioceiling': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_mutex_t *restrict',
        name = '__mutex',
      ),
      Param(
        type = 'int *restrict',
        name = '__prioceiling',
      ),
    ],
  ),
  'pthread_mutex_setprioceiling': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutex_t *restrict',
        name = '__mutex',
      ),
      Param(
        type = 'int',
        name = '__prioceiling',
      ),
      Param(
        type = 'int *restrict',
        name = '__old_ceiling',
      ),
    ],
  ),
  'pthread_mutex_consistent': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutex_t *',
        name = '__mutex',
      ),
    ],
  ),
  'pthread_mutexattr_init': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutexattr_t *',
        name = '__attr',
      ),
    ],
  ),
  'pthread_mutexattr_destroy': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutexattr_t *',
        name = '__attr',
      ),
    ],
  ),
  'pthread_mutexattr_getpshared': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_mutexattr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'int *restrict',
        name = '__pshared',
      ),
    ],
  ),
  'pthread_mutexattr_setpshared': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutexattr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int',
        name = '__pshared',
      ),
    ],
  ),
  'pthread_mutexattr_gettype': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_mutexattr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'int *restrict',
        name = '__kind',
      ),
    ],
  ),
  'pthread_mutexattr_settype': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutexattr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int',
        name = '__kind',
      ),
    ],
  ),
  'pthread_mutexattr_getprotocol': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_mutexattr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'int *restrict',
        name = '__protocol',
      ),
    ],
  ),
  'pthread_mutexattr_setprotocol': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutexattr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int',
        name = '__protocol',
      ),
    ],
  ),
  'pthread_mutexattr_getprioceiling': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_mutexattr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'int *restrict',
        name = '__prioceiling',
      ),
    ],
  ),
  'pthread_mutexattr_setprioceiling': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutexattr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int',
        name = '__prioceiling',
      ),
    ],
  ),
  'pthread_mutexattr_getrobust': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_mutexattr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int *',
        name = '__robustness',
      ),
    ],
  ),
  'pthread_mutexattr_setrobust': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_mutexattr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int',
        name = '__robustness',
      ),
    ],
  ),
  'pthread_rwlock_init': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_rwlock_t *restrict',
        name = '__rwlock',
      ),
      Param(
        type = 'const pthread_rwlockattr_t *restrict',
        name = '__attr',
      ),
    ],
  ),
  'pthread_rwlock_destroy': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_rwlock_t *',
        name = '__rwlock',
      ),
    ],
  ),
  'pthread_rwlock_rdlock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_rwlock_t *',
        name = '__rwlock',
      ),
    ],
  ),
  'pthread_rwlock_tryrdlock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_rwlock_t *',
        name = '__rwlock',
      ),
    ],
  ),
  'pthread_rwlock_timedrdlock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_rwlock_t *restrict',
        name = '__rwlock',
      ),
      Param(
        type = 'const struct timespec *restrict',
        name = '__abstime',
      ),
    ],
  ),
  'pthread_rwlock_wrlock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_rwlock_t *',
        name = '__rwlock',
      ),
    ],
  ),
  'pthread_rwlock_trywrlock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_rwlock_t *',
        name = '__rwlock',
      ),
    ],
  ),
  'pthread_rwlock_timedwrlock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_rwlock_t *restrict',
        name = '__rwlock',
      ),
      Param(
        type = 'const struct timespec *restrict',
        name = '__abstime',
      ),
    ],
  ),
  'pthread_rwlock_unlock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_rwlock_t *',
        name = '__rwlock',
      ),
    ],
  ),
  'pthread_rwlockattr_init': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_rwlockattr_t *',
        name = '__attr',
      ),
    ],
  ),
  'pthread_rwlockattr_destroy': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_rwlockattr_t *',
        name = '__attr',
      ),
    ],
  ),
  'pthread_rwlockattr_getpshared': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_rwlockattr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'int *restrict',
        name = '__pshared',
      ),
    ],
  ),
  'pthread_rwlockattr_setpshared': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_rwlockattr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int',
        name = '__pshared',
      ),
    ],
  ),
  'pthread_rwlockattr_getkind_np': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_rwlockattr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'int *restrict',
        name = '__pref',
      ),
    ],
  ),
  'pthread_rwlockattr_setkind_np': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_rwlockattr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int',
        name = '__pref',
      ),
    ],
  ),
  'pthread_cond_init': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_cond_t *restrict',
        name = '__cond',
      ),
      Param(
        type = 'const pthread_condattr_t *restrict',
        name = '__cond_attr',
      ),
    ],
  ),
  'pthread_cond_destroy': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_cond_t *',
        name = '__cond',
      ),
    ],
  ),
  'pthread_cond_signal': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_cond_t *',
        name = '__cond',
      ),
    ],
  ),
  'pthread_cond_broadcast': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_cond_t *',
        name = '__cond',
      ),
    ],
  ),
  'pthread_cond_wait': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_cond_t *restrict',
        name = '__cond',
      ),
      Param(
        type = 'pthread_mutex_t *restrict',
        name = '__mutex',
      ),
    ],
  ),
  'pthread_cond_timedwait': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_cond_t *restrict',
        name = '__cond',
      ),
      Param(
        type = 'pthread_mutex_t *restrict',
        name = '__mutex',
      ),
      Param(
        type = 'const struct timespec *restrict',
        name = '__abstime',
      ),
    ],
  ),
  'pthread_condattr_init': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_condattr_t *',
        name = '__attr',
      ),
    ],
  ),
  'pthread_condattr_destroy': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_condattr_t *',
        name = '__attr',
      ),
    ],
  ),
  'pthread_condattr_getpshared': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_condattr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'int *restrict',
        name = '__pshared',
      ),
    ],
  ),
  'pthread_condattr_setpshared': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_condattr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int',
        name = '__pshared',
      ),
    ],
  ),
  'pthread_condattr_getclock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_condattr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = '__clockid_t *restrict',
        name = '__clock_id',
      ),
    ],
  ),
  'pthread_condattr_setclock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_condattr_t *',
        name = '__attr',
      ),
      Param(
        type = '__clockid_t',
        name = '__clock_id',
      ),
    ],
  ),
  'pthread_spin_init': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_spinlock_t *',
        name = '__lock',
      ),
      Param(
        type = 'int',
        name = '__pshared',
      ),
    ],
  ),
  'pthread_spin_destroy': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_spinlock_t *',
        name = '__lock',
      ),
    ],
  ),
  'pthread_spin_lock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_spinlock_t *',
        name = '__lock',
      ),
    ],
  ),
  'pthread_spin_trylock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_spinlock_t *',
        name = '__lock',
      ),
    ],
  ),
  'pthread_spin_unlock': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_spinlock_t *',
        name = '__lock',
      ),
    ],
  ),
  'pthread_barrier_init': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_barrier_t *restrict',
        name = '__barrier',
      ),
      Param(
        type = 'const pthread_barrierattr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'unsigned int',
        name = '__count',
      ),
    ],
  ),
  'pthread_barrier_destroy': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_barrier_t *',
        name = '__barrier',
      ),
    ],
  ),
  'pthread_barrier_wait': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_barrier_t *',
        name = '__barrier',
      ),
    ],
  ),
  'pthread_barrierattr_init': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_barrierattr_t *',
        name = '__attr',
      ),
    ],
  ),
  'pthread_barrierattr_destroy': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_barrierattr_t *',
        name = '__attr',
      ),
    ],
  ),
  'pthread_barrierattr_getpshared': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const pthread_barrierattr_t *restrict',
        name = '__attr',
      ),
      Param(
        type = 'int *restrict',
        name = '__pshared',
      ),
    ],
  ),
  'pthread_barrierattr_setpshared': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_barrierattr_t *',
        name = '__attr',
      ),
      Param(
        type = 'int',
        name = '__pshared',
      ),
    ],
  ),
  'pthread_key_create': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_key_t *',
        name = '__key',
      ),
      Param(
        type = 'void (*)(void *)',
        name = '__destr_function',
      ),
    ],
  ),
  'pthread_key_delete': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_key_t',
        name = '__key',
      ),
    ],
  ),
  'pthread_getspecific': Spec(
    return_type = 'void *',
    parameters = [
      Param(
        type = 'pthread_key_t',
        name = '__key',
      ),
    ],
  ),
  'pthread_setspecific': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_key_t',
        name = '__key',
      ),
      Param(
        type = 'const void *',
        name = '__pointer',
      ),
    ],
  ),
  'pthread_getcpuclockid': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'pthread_t',
        name = '__thread_id',
      ),
      Param(
        type = '__clockid_t *',
        name = '__clock_id',
      ),
    ],
  ),
  'pthread_atfork': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'void (*)(void)',
        name = '__prepare',
      ),
      Param(
        type = 'void (*)(void)',
        name = '__parent',
      ),
      Param(
        type = 'void (*)(void)',
        name = '__child',
      ),
    ],
  ),
  'g_static_mutex_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_static_mutex_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_static_mutex_get_mutex_impl': Spec(
    return_type = 'GMutex *',
    parameters = [
      Param(
        type = 'GStaticMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_static_rec_mutex_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticRecMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_static_rec_mutex_lock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticRecMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_static_rec_mutex_trylock': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GStaticRecMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_static_rec_mutex_unlock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticRecMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_static_rec_mutex_lock_full': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticRecMutex *',
        name = 'mutex',
      ),
      Param(
        type = 'guint',
        name = 'depth',
      ),
    ],
  ),
  'g_static_rec_mutex_unlock_full': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GStaticRecMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_static_rec_mutex_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticRecMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_static_rw_lock_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticRWLock *',
        name = 'lock',
      ),
    ],
  ),
  'g_static_rw_lock_reader_lock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticRWLock *',
        name = 'lock',
      ),
    ],
  ),
  'g_static_rw_lock_reader_trylock': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GStaticRWLock *',
        name = 'lock',
      ),
    ],
  ),
  'g_static_rw_lock_reader_unlock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticRWLock *',
        name = 'lock',
      ),
    ],
  ),
  'g_static_rw_lock_writer_lock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticRWLock *',
        name = 'lock',
      ),
    ],
  ),
  'g_static_rw_lock_writer_trylock': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GStaticRWLock *',
        name = 'lock',
      ),
    ],
  ),
  'g_static_rw_lock_writer_unlock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticRWLock *',
        name = 'lock',
      ),
    ],
  ),
  'g_static_rw_lock_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticRWLock *',
        name = 'lock',
      ),
    ],
  ),
  'g_private_new': Spec(
    return_type = 'GPrivate *',
    parameters = [
      Param(
        type = 'GDestroyNotify',
        name = 'notify',
      ),
    ],
  ),
  'g_static_private_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticPrivate *',
        name = 'private_key',
      ),
    ],
  ),
  'g_static_private_get': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GStaticPrivate *',
        name = 'private_key',
      ),
    ],
  ),
  'g_static_private_set': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticPrivate *',
        name = 'private_key',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'notify',
      ),
    ],
  ),
  'g_static_private_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GStaticPrivate *',
        name = 'private_key',
      ),
    ],
  ),
  'g_once_init_enter_impl': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'volatile gsize *',
        name = 'location',
      ),
    ],
  ),
  'g_thread_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'vtable',
      ),
    ],
  ),
  'g_thread_init_with_errorcheck_mutexes': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'vtable',
      ),
    ],
  ),
  'g_thread_get_initialized': Spec(
    return_type = 'gboolean',
    parameters = [
    ],
  ),
  'g_mutex_new': Spec(
    return_type = 'GMutex *',
    parameters = [
    ],
  ),
  'g_mutex_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GMutex *',
        name = 'mutex',
      ),
    ],
  ),
  'g_cond_new': Spec(
    return_type = 'GCond *',
    parameters = [
    ],
  ),
  'g_cond_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GCond *',
        name = 'cond',
      ),
    ],
  ),
  'g_cond_timed_wait': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GCond *',
        name = 'cond',
      ),
      Param(
        type = 'GMutex *',
        name = 'mutex',
      ),
      Param(
        type = 'GTimeVal *',
        name = 'timeval',
      ),
    ],
  ),
  'access': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__name',
      ),
      Param(
        type = 'int',
        name = '__type',
      ),
    ],
  ),
  'faccessat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *',
        name = '__file',
      ),
      Param(
        type = 'int',
        name = '__type',
      ),
      Param(
        type = 'int',
        name = '__flag',
      ),
    ],
  ),
  'lseek': Spec(
    return_type = '__off_t',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = '__off_t',
        name = '__offset',
      ),
      Param(
        type = 'int',
        name = '__whence',
      ),
    ],
  ),
  'close': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
    ],
  ),
  'read': Spec(
    return_type = 'ssize_t',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'void *',
        name = '__buf',
      ),
      Param(
        type = 'size_t',
        name = '__nbytes',
      ),
    ],
  ),
  'write': Spec(
    return_type = 'ssize_t',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const void *',
        name = '__buf',
      ),
      Param(
        type = 'size_t',
        name = '__n',
      ),
    ],
  ),
  'pread': Spec(
    return_type = 'ssize_t',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'void *',
        name = '__buf',
      ),
      Param(
        type = 'size_t',
        name = '__nbytes',
      ),
      Param(
        type = '__off_t',
        name = '__offset',
      ),
    ],
  ),
  'pwrite': Spec(
    return_type = 'ssize_t',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const void *',
        name = '__buf',
      ),
      Param(
        type = 'size_t',
        name = '__n',
      ),
      Param(
        type = '__off_t',
        name = '__offset',
      ),
    ],
  ),
  'pipe': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int [2]',
        name = '__pipedes',
      ),
    ],
  ),
  'alarm': Spec(
    return_type = 'unsigned int',
    parameters = [
      Param(
        type = 'unsigned int',
        name = '__seconds',
      ),
    ],
  ),
  'sleep': Spec(
    return_type = 'unsigned int',
    parameters = [
      Param(
        type = 'unsigned int',
        name = '__seconds',
      ),
    ],
  ),
  'ualarm': Spec(
    return_type = '__useconds_t',
    parameters = [
      Param(
        type = '__useconds_t',
        name = '__value',
      ),
      Param(
        type = '__useconds_t',
        name = '__interval',
      ),
    ],
  ),
  'usleep': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__useconds_t',
        name = '__useconds',
      ),
    ],
  ),
  'pause': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  'chown': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__file',
      ),
      Param(
        type = '__uid_t',
        name = '__owner',
      ),
      Param(
        type = '__gid_t',
        name = '__group',
      ),
    ],
  ),
  'fchown': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = '__uid_t',
        name = '__owner',
      ),
      Param(
        type = '__gid_t',
        name = '__group',
      ),
    ],
  ),
  'lchown': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__file',
      ),
      Param(
        type = '__uid_t',
        name = '__owner',
      ),
      Param(
        type = '__gid_t',
        name = '__group',
      ),
    ],
  ),
  'fchownat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *',
        name = '__file',
      ),
      Param(
        type = '__uid_t',
        name = '__owner',
      ),
      Param(
        type = '__gid_t',
        name = '__group',
      ),
      Param(
        type = 'int',
        name = '__flag',
      ),
    ],
  ),
  'chdir': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__path',
      ),
    ],
  ),
  'fchdir': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
    ],
  ),
  'getcwd': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'char *',
        name = '__buf',
      ),
      Param(
        type = 'size_t',
        name = '__size',
      ),
    ],
  ),
  'getwd': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'char *',
        name = '__buf',
      ),
    ],
  ),
  'dup': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
    ],
  ),
  'dup2': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'int',
        name = '__fd2',
      ),
    ],
  ),
  'execve': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__path',
      ),
      Param(
        type = 'char *const []',
        name = '__argv',
      ),
      Param(
        type = 'char *const []',
        name = '__envp',
      ),
    ],
  ),
  'fexecve': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'char *const []',
        name = '__argv',
      ),
      Param(
        type = 'char *const []',
        name = '__envp',
      ),
    ],
  ),
  'execv': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__path',
      ),
      Param(
        type = 'char *const []',
        name = '__argv',
      ),
    ],
  ),
  'execle': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__path',
      ),
      Param(
        type = 'const char *',
        name = '__arg',
      ),
    ],
  ),
  'execl': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__path',
      ),
      Param(
        type = 'const char *',
        name = '__arg',
      ),
    ],
  ),
  'execvp': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__file',
      ),
      Param(
        type = 'char *const []',
        name = '__argv',
      ),
    ],
  ),
  'execlp': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__file',
      ),
      Param(
        type = 'const char *',
        name = '__arg',
      ),
    ],
  ),
  'nice': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__inc',
      ),
    ],
  ),
  '_exit': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'int',
        name = '__status',
      ),
    ],
  ),
  'pathconf': Spec(
    return_type = 'long',
    parameters = [
      Param(
        type = 'const char *',
        name = '__path',
      ),
      Param(
        type = 'int',
        name = '__name',
      ),
    ],
  ),
  'fpathconf': Spec(
    return_type = 'long',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'int',
        name = '__name',
      ),
    ],
  ),
  'sysconf': Spec(
    return_type = 'long',
    parameters = [
      Param(
        type = 'int',
        name = '__name',
      ),
    ],
  ),
  'confstr': Spec(
    return_type = 'size_t',
    parameters = [
      Param(
        type = 'int',
        name = '__name',
      ),
      Param(
        type = 'char *',
        name = '__buf',
      ),
      Param(
        type = 'size_t',
        name = '__len',
      ),
    ],
  ),
  'getpid': Spec(
    return_type = '__pid_t',
    parameters = [
    ],
  ),
  'getppid': Spec(
    return_type = '__pid_t',
    parameters = [
    ],
  ),
  'getpgrp': Spec(
    return_type = '__pid_t',
    parameters = [
    ],
  ),
  '__getpgid': Spec(
    return_type = '__pid_t',
    parameters = [
      Param(
        type = '__pid_t',
        name = '__pid',
      ),
    ],
  ),
  'getpgid': Spec(
    return_type = '__pid_t',
    parameters = [
      Param(
        type = '__pid_t',
        name = '__pid',
      ),
    ],
  ),
  'setpgid': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__pid_t',
        name = '__pid',
      ),
      Param(
        type = '__pid_t',
        name = '__pgid',
      ),
    ],
  ),
  'setpgrp': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  'setsid': Spec(
    return_type = '__pid_t',
    parameters = [
    ],
  ),
  'getsid': Spec(
    return_type = '__pid_t',
    parameters = [
      Param(
        type = '__pid_t',
        name = '__pid',
      ),
    ],
  ),
  'getuid': Spec(
    return_type = '__uid_t',
    parameters = [
    ],
  ),
  'geteuid': Spec(
    return_type = '__uid_t',
    parameters = [
    ],
  ),
  'getgid': Spec(
    return_type = '__gid_t',
    parameters = [
    ],
  ),
  'getegid': Spec(
    return_type = '__gid_t',
    parameters = [
    ],
  ),
  'getgroups': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__size',
      ),
      Param(
        type = '__gid_t []',
        name = '__list',
      ),
    ],
  ),
  'setuid': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__uid_t',
        name = '__uid',
      ),
    ],
  ),
  'setreuid': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__uid_t',
        name = '__ruid',
      ),
      Param(
        type = '__uid_t',
        name = '__euid',
      ),
    ],
  ),
  'seteuid': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__uid_t',
        name = '__uid',
      ),
    ],
  ),
  'setgid': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__gid_t',
        name = '__gid',
      ),
    ],
  ),
  'setregid': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__gid_t',
        name = '__rgid',
      ),
      Param(
        type = '__gid_t',
        name = '__egid',
      ),
    ],
  ),
  'setegid': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '__gid_t',
        name = '__gid',
      ),
    ],
  ),
  'fork': Spec(
    return_type = '__pid_t',
    parameters = [
    ],
  ),
  'vfork': Spec(
    return_type = '__pid_t',
    parameters = [
    ],
  ),
  'ttyname': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
    ],
  ),
  'ttyname_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'char *',
        name = '__buf',
      ),
      Param(
        type = 'size_t',
        name = '__buflen',
      ),
    ],
  ),
  'isatty': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
    ],
  ),
  'ttyslot': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  'link': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__from',
      ),
      Param(
        type = 'const char *',
        name = '__to',
      ),
    ],
  ),
  'linkat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fromfd',
      ),
      Param(
        type = 'const char *',
        name = '__from',
      ),
      Param(
        type = 'int',
        name = '__tofd',
      ),
      Param(
        type = 'const char *',
        name = '__to',
      ),
      Param(
        type = 'int',
        name = '__flags',
      ),
    ],
  ),
  'symlink': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__from',
      ),
      Param(
        type = 'const char *',
        name = '__to',
      ),
    ],
  ),
  'readlink': Spec(
    return_type = 'ssize_t',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__path',
      ),
      Param(
        type = 'char *restrict',
        name = '__buf',
      ),
      Param(
        type = 'size_t',
        name = '__len',
      ),
    ],
  ),
  'symlinkat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__from',
      ),
      Param(
        type = 'int',
        name = '__tofd',
      ),
      Param(
        type = 'const char *',
        name = '__to',
      ),
    ],
  ),
  'readlinkat': Spec(
    return_type = 'ssize_t',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *restrict',
        name = '__path',
      ),
      Param(
        type = 'char *restrict',
        name = '__buf',
      ),
      Param(
        type = 'size_t',
        name = '__len',
      ),
    ],
  ),
  'unlink': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__name',
      ),
    ],
  ),
  'unlinkat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *',
        name = '__name',
      ),
      Param(
        type = 'int',
        name = '__flag',
      ),
    ],
  ),
  'rmdir': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__path',
      ),
    ],
  ),
  'tcgetpgrp': Spec(
    return_type = '__pid_t',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
    ],
  ),
  'tcsetpgrp': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = '__pid_t',
        name = '__pgrp_id',
      ),
    ],
  ),
  'getlogin': Spec(
    return_type = 'char *',
    parameters = [
    ],
  ),
  'getlogin_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'char *',
        name = '__name',
      ),
      Param(
        type = 'size_t',
        name = '__name_len',
      ),
    ],
  ),
  'setlogin': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__name',
      ),
    ],
  ),
  'getopt': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '___argc',
      ),
      Param(
        type = 'char *const *',
        name = '___argv',
      ),
      Param(
        type = 'const char *',
        name = '__shortopts',
      ),
    ],
  ),
  'gethostname': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'char *',
        name = '__name',
      ),
      Param(
        type = 'size_t',
        name = '__len',
      ),
    ],
  ),
  'sethostname': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__name',
      ),
      Param(
        type = 'size_t',
        name = '__len',
      ),
    ],
  ),
  'sethostid': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'long',
        name = '__id',
      ),
    ],
  ),
  'getdomainname': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'char *',
        name = '__name',
      ),
      Param(
        type = 'size_t',
        name = '__len',
      ),
    ],
  ),
  'setdomainname': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__name',
      ),
      Param(
        type = 'size_t',
        name = '__len',
      ),
    ],
  ),
  'vhangup': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  'revoke': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__file',
      ),
    ],
  ),
  'profil': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'unsigned short *',
        name = '__sample_buffer',
      ),
      Param(
        type = 'size_t',
        name = '__size',
      ),
      Param(
        type = 'size_t',
        name = '__offset',
      ),
      Param(
        type = 'unsigned int',
        name = '__scale',
      ),
    ],
  ),
  'acct': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__name',
      ),
    ],
  ),
  'getusershell': Spec(
    return_type = 'char *',
    parameters = [
    ],
  ),
  'endusershell': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'setusershell': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'daemon': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__nochdir',
      ),
      Param(
        type = 'int',
        name = '__noclose',
      ),
    ],
  ),
  'chroot': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__path',
      ),
    ],
  ),
  'getpass': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'const char *',
        name = '__prompt',
      ),
    ],
  ),
  'fsync': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
    ],
  ),
  'gethostid': Spec(
    return_type = 'long',
    parameters = [
    ],
  ),
  'sync': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'getpagesize': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  'getdtablesize': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  'truncate': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__file',
      ),
      Param(
        type = '__off_t',
        name = '__length',
      ),
    ],
  ),
  'ftruncate': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = '__off_t',
        name = '__length',
      ),
    ],
  ),
  'brk': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'void *',
        name = '__addr',
      ),
    ],
  ),
  'sbrk': Spec(
    return_type = 'void *',
    parameters = [
      Param(
        type = 'intptr_t',
        name = '__delta',
      ),
    ],
  ),
  'syscall': Spec(
    return_type = 'long',
    parameters = [
      Param(
        type = 'long',
        name = '__sysno',
      ),
    ],
  ),
  'lockf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'int',
        name = '__cmd',
      ),
      Param(
        type = '__off_t',
        name = '__len',
      ),
    ],
  ),
  'fdatasync': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fildes',
      ),
    ],
  ),
  '__errno_location': Spec(
    return_type = 'int *',
    parameters = [
    ],
  ),
  'wait': Spec(
    return_type = '__pid_t',
    parameters = [
      Param(
        type = '__WAIT_STATUS',
        name = '__stat_loc',
      ),
    ],
  ),
  'waitpid': Spec(
    return_type = '__pid_t',
    parameters = [
      Param(
        type = '__pid_t',
        name = '__pid',
      ),
      Param(
        type = 'int *',
        name = '__stat_loc',
      ),
      Param(
        type = 'int',
        name = '__options',
      ),
    ],
  ),
  'waitid': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'idtype_t',
        name = '__idtype',
      ),
      Param(
        type = '__id_t',
        name = '__id',
      ),
      Param(
        type = 'siginfo_t *',
        name = '__infop',
      ),
      Param(
        type = 'int',
        name = '__options',
      ),
    ],
  ),
  'wait3': Spec(
    return_type = '__pid_t',
    parameters = [
      Param(
        type = '__WAIT_STATUS',
        name = '__stat_loc',
      ),
      Param(
        type = 'int',
        name = '__options',
      ),
      Param(
        type = 'struct rusage *',
        name = '__usage',
      ),
    ],
  ),
  'wait4': Spec(
    return_type = '__pid_t',
    parameters = [
      Param(
        type = '__pid_t',
        name = '__pid',
      ),
      Param(
        type = '__WAIT_STATUS',
        name = '__stat_loc',
      ),
      Param(
        type = 'int',
        name = '__options',
      ),
      Param(
        type = 'struct rusage *',
        name = '__usage',
      ),
    ],
  ),
  '__ctype_get_mb_cur_max': Spec(
    return_type = 'size_t',
    parameters = [
    ],
  ),
  'atof': Spec(
    return_type = 'double',
    parameters = [
      Param(
        type = 'const char *',
        name = '__nptr',
      ),
    ],
  ),
  'atoi': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__nptr',
      ),
    ],
  ),
  'atol': Spec(
    return_type = 'long',
    parameters = [
      Param(
        type = 'const char *',
        name = '__nptr',
      ),
    ],
  ),
  'atoll': Spec(
    return_type = 'long long',
    parameters = [
      Param(
        type = 'const char *',
        name = '__nptr',
      ),
    ],
  ),
  'strtod': Spec(
    return_type = 'double',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__nptr',
      ),
      Param(
        type = 'char **restrict',
        name = '__endptr',
      ),
    ],
  ),
  'strtof': Spec(
    return_type = 'float',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__nptr',
      ),
      Param(
        type = 'char **restrict',
        name = '__endptr',
      ),
    ],
  ),
  'strtold': Spec(
    return_type = 'long double',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__nptr',
      ),
      Param(
        type = 'char **restrict',
        name = '__endptr',
      ),
    ],
  ),
  'strtol': Spec(
    return_type = 'long',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__nptr',
      ),
      Param(
        type = 'char **restrict',
        name = '__endptr',
      ),
      Param(
        type = 'int',
        name = '__base',
      ),
    ],
  ),
  'strtoul': Spec(
    return_type = 'unsigned long',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__nptr',
      ),
      Param(
        type = 'char **restrict',
        name = '__endptr',
      ),
      Param(
        type = 'int',
        name = '__base',
      ),
    ],
  ),
  'strtoq': Spec(
    return_type = 'long long',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__nptr',
      ),
      Param(
        type = 'char **restrict',
        name = '__endptr',
      ),
      Param(
        type = 'int',
        name = '__base',
      ),
    ],
  ),
  'strtouq': Spec(
    return_type = 'unsigned long long',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__nptr',
      ),
      Param(
        type = 'char **restrict',
        name = '__endptr',
      ),
      Param(
        type = 'int',
        name = '__base',
      ),
    ],
  ),
  'strtoll': Spec(
    return_type = 'long long',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__nptr',
      ),
      Param(
        type = 'char **restrict',
        name = '__endptr',
      ),
      Param(
        type = 'int',
        name = '__base',
      ),
    ],
  ),
  'strtoull': Spec(
    return_type = 'unsigned long long',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__nptr',
      ),
      Param(
        type = 'char **restrict',
        name = '__endptr',
      ),
      Param(
        type = 'int',
        name = '__base',
      ),
    ],
  ),
  'l64a': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'long',
        name = '__n',
      ),
    ],
  ),
  'a64l': Spec(
    return_type = 'long',
    parameters = [
      Param(
        type = 'const char *',
        name = '__s',
      ),
    ],
  ),
  'select': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__nfds',
      ),
      Param(
        type = 'fd_set *restrict',
        name = '__readfds',
      ),
      Param(
        type = 'fd_set *restrict',
        name = '__writefds',
      ),
      Param(
        type = 'fd_set *restrict',
        name = '__exceptfds',
      ),
      Param(
        type = 'struct timeval *restrict',
        name = '__timeout',
      ),
    ],
  ),
  'pselect': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__nfds',
      ),
      Param(
        type = 'fd_set *restrict',
        name = '__readfds',
      ),
      Param(
        type = 'fd_set *restrict',
        name = '__writefds',
      ),
      Param(
        type = 'fd_set *restrict',
        name = '__exceptfds',
      ),
      Param(
        type = 'const struct timespec *restrict',
        name = '__timeout',
      ),
      Param(
        type = 'const __sigset_t *restrict',
        name = '__sigmask',
      ),
    ],
  ),
  'gnu_dev_major': Spec(
    return_type = 'unsigned int',
    parameters = [
      Param(
        type = 'unsigned long long',
        name = '__dev',
      ),
    ],
  ),
  'gnu_dev_minor': Spec(
    return_type = 'unsigned int',
    parameters = [
      Param(
        type = 'unsigned long long',
        name = '__dev',
      ),
    ],
  ),
  'gnu_dev_makedev': Spec(
    return_type = 'unsigned long long',
    parameters = [
      Param(
        type = 'unsigned int',
        name = '__major',
      ),
      Param(
        type = 'unsigned int',
        name = '__minor',
      ),
    ],
  ),
  'random': Spec(
    return_type = 'long',
    parameters = [
    ],
  ),
  'srandom': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'unsigned int',
        name = '__seed',
      ),
    ],
  ),
  'initstate': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'unsigned int',
        name = '__seed',
      ),
      Param(
        type = 'char *',
        name = '__statebuf',
      ),
      Param(
        type = 'size_t',
        name = '__statelen',
      ),
    ],
  ),
  'setstate': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'char *',
        name = '__statebuf',
      ),
    ],
  ),
  'random_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'struct random_data *restrict',
        name = '__buf',
      ),
      Param(
        type = 'int32_t *restrict',
        name = '__result',
      ),
    ],
  ),
  'srandom_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'unsigned int',
        name = '__seed',
      ),
      Param(
        type = 'struct random_data *',
        name = '__buf',
      ),
    ],
  ),
  'initstate_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'unsigned int',
        name = '__seed',
      ),
      Param(
        type = 'char *restrict',
        name = '__statebuf',
      ),
      Param(
        type = 'size_t',
        name = '__statelen',
      ),
      Param(
        type = 'struct random_data *restrict',
        name = '__buf',
      ),
    ],
  ),
  'setstate_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'char *restrict',
        name = '__statebuf',
      ),
      Param(
        type = 'struct random_data *restrict',
        name = '__buf',
      ),
    ],
  ),
  'rand': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  'srand': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'unsigned int',
        name = '__seed',
      ),
    ],
  ),
  'rand_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'unsigned int *',
        name = '__seed',
      ),
    ],
  ),
  'drand48': Spec(
    return_type = 'double',
    parameters = [
    ],
  ),
  'erand48': Spec(
    return_type = 'double',
    parameters = [
      Param(
        type = 'unsigned short [3]',
        name = '__xsubi',
      ),
    ],
  ),
  'lrand48': Spec(
    return_type = 'long',
    parameters = [
    ],
  ),
  'nrand48': Spec(
    return_type = 'long',
    parameters = [
      Param(
        type = 'unsigned short [3]',
        name = '__xsubi',
      ),
    ],
  ),
  'mrand48': Spec(
    return_type = 'long',
    parameters = [
    ],
  ),
  'jrand48': Spec(
    return_type = 'long',
    parameters = [
      Param(
        type = 'unsigned short [3]',
        name = '__xsubi',
      ),
    ],
  ),
  'srand48': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'long',
        name = '__seedval',
      ),
    ],
  ),
  'seed48': Spec(
    return_type = 'unsigned short *',
    parameters = [
      Param(
        type = 'unsigned short [3]',
        name = '__seed16v',
      ),
    ],
  ),
  'lcong48': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'unsigned short [7]',
        name = '__param',
      ),
    ],
  ),
  'drand48_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'struct drand48_data *restrict',
        name = '__buffer',
      ),
      Param(
        type = 'double *restrict',
        name = '__result',
      ),
    ],
  ),
  'erand48_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'unsigned short [3]',
        name = '__xsubi',
      ),
      Param(
        type = 'struct drand48_data *restrict',
        name = '__buffer',
      ),
      Param(
        type = 'double *restrict',
        name = '__result',
      ),
    ],
  ),
  'lrand48_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'struct drand48_data *restrict',
        name = '__buffer',
      ),
      Param(
        type = 'long *restrict',
        name = '__result',
      ),
    ],
  ),
  'nrand48_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'unsigned short [3]',
        name = '__xsubi',
      ),
      Param(
        type = 'struct drand48_data *restrict',
        name = '__buffer',
      ),
      Param(
        type = 'long *restrict',
        name = '__result',
      ),
    ],
  ),
  'mrand48_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'struct drand48_data *restrict',
        name = '__buffer',
      ),
      Param(
        type = 'long *restrict',
        name = '__result',
      ),
    ],
  ),
  'jrand48_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'unsigned short [3]',
        name = '__xsubi',
      ),
      Param(
        type = 'struct drand48_data *restrict',
        name = '__buffer',
      ),
      Param(
        type = 'long *restrict',
        name = '__result',
      ),
    ],
  ),
  'srand48_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'long',
        name = '__seedval',
      ),
      Param(
        type = 'struct drand48_data *',
        name = '__buffer',
      ),
    ],
  ),
  'seed48_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'unsigned short [3]',
        name = '__seed16v',
      ),
      Param(
        type = 'struct drand48_data *',
        name = '__buffer',
      ),
    ],
  ),
  'lcong48_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'unsigned short [7]',
        name = '__param',
      ),
      Param(
        type = 'struct drand48_data *',
        name = '__buffer',
      ),
    ],
  ),
  'malloc': Spec(
    return_type = 'void *',
    parameters = [
      Param(
        type = 'size_t',
        name = '__size',
      ),
    ],
  ),
  'calloc': Spec(
    return_type = 'void *',
    parameters = [
      Param(
        type = 'size_t',
        name = '__nmemb',
      ),
      Param(
        type = 'size_t',
        name = '__size',
      ),
    ],
  ),
  'realloc': Spec(
    return_type = 'void *',
    parameters = [
      Param(
        type = 'void *',
        name = '__ptr',
      ),
      Param(
        type = 'size_t',
        name = '__size',
      ),
    ],
  ),
  'free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'void *',
        name = '__ptr',
      ),
    ],
  ),
  'cfree': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'void *',
        name = '__ptr',
      ),
    ],
  ),
  'alloca': Spec(
    return_type = 'void *',
    parameters = [
      Param(
        type = 'size_t',
        name = '__size',
      ),
    ],
  ),
  'valloc': Spec(
    return_type = 'void *',
    parameters = [
      Param(
        type = 'size_t',
        name = '__size',
      ),
    ],
  ),
  'posix_memalign': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'void **',
        name = '__memptr',
      ),
      Param(
        type = 'size_t',
        name = '__alignment',
      ),
      Param(
        type = 'size_t',
        name = '__size',
      ),
    ],
  ),
  'abort': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'atexit': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'void (*)(void)',
        name = '__func',
      ),
    ],
  ),
  'on_exit': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'void (*)(int, void *)',
        name = '__func',
      ),
      Param(
        type = 'void *',
        name = '__arg',
      ),
    ],
  ),
  'exit': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'int',
        name = '__status',
      ),
    ],
  ),
  '_Exit': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'int',
        name = '__status',
      ),
    ],
  ),
  'getenv': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'const char *',
        name = '__name',
      ),
    ],
  ),
  '__secure_getenv': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'const char *',
        name = '__name',
      ),
    ],
  ),
  'putenv': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'char *',
        name = '__string',
      ),
    ],
  ),
  'setenv': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__name',
      ),
      Param(
        type = 'const char *',
        name = '__value',
      ),
      Param(
        type = 'int',
        name = '__replace',
      ),
    ],
  ),
  'unsetenv': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__name',
      ),
    ],
  ),
  'clearenv': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  'mktemp': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'char *',
        name = '__template',
      ),
    ],
  ),
  'mkstemp': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'char *',
        name = '__template',
      ),
    ],
  ),
  'mkstemps': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'char *',
        name = '__template',
      ),
      Param(
        type = 'int',
        name = '__suffixlen',
      ),
    ],
  ),
  'mkdtemp': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'char *',
        name = '__template',
      ),
    ],
  ),
  'system': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__command',
      ),
    ],
  ),
  'realpath': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__name',
      ),
      Param(
        type = 'char *restrict',
        name = '__resolved',
      ),
    ],
  ),
  'bsearch': Spec(
    return_type = 'void *',
    parameters = [
      Param(
        type = 'const void *',
        name = '__key',
      ),
      Param(
        type = 'const void *',
        name = '__base',
      ),
      Param(
        type = 'size_t',
        name = '__nmemb',
      ),
      Param(
        type = 'size_t',
        name = '__size',
      ),
      Param(
        type = '__compar_fn_t',
        name = '__compar',
      ),
    ],
  ),
  'qsort': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'void *',
        name = '__base',
      ),
      Param(
        type = 'size_t',
        name = '__nmemb',
      ),
      Param(
        type = 'size_t',
        name = '__size',
      ),
      Param(
        type = '__compar_fn_t',
        name = '__compar',
      ),
    ],
  ),
  'abs': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__x',
      ),
    ],
  ),
  'labs': Spec(
    return_type = 'long',
    parameters = [
      Param(
        type = 'long',
        name = '__x',
      ),
    ],
  ),
  'llabs': Spec(
    return_type = 'long long',
    parameters = [
      Param(
        type = 'long long',
        name = '__x',
      ),
    ],
  ),
  'div': Spec(
    return_type = 'div_t',
    parameters = [
      Param(
        type = 'int',
        name = '__numer',
      ),
      Param(
        type = 'int',
        name = '__denom',
      ),
    ],
  ),
  'ldiv': Spec(
    return_type = 'ldiv_t',
    parameters = [
      Param(
        type = 'long',
        name = '__numer',
      ),
      Param(
        type = 'long',
        name = '__denom',
      ),
    ],
  ),
  'lldiv': Spec(
    return_type = 'lldiv_t',
    parameters = [
      Param(
        type = 'long long',
        name = '__numer',
      ),
      Param(
        type = 'long long',
        name = '__denom',
      ),
    ],
  ),
  'ecvt': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'double',
        name = '__value',
      ),
      Param(
        type = 'int',
        name = '__ndigit',
      ),
      Param(
        type = 'int *restrict',
        name = '__decpt',
      ),
      Param(
        type = 'int *restrict',
        name = '__sign',
      ),
    ],
  ),
  'fcvt': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'double',
        name = '__value',
      ),
      Param(
        type = 'int',
        name = '__ndigit',
      ),
      Param(
        type = 'int *restrict',
        name = '__decpt',
      ),
      Param(
        type = 'int *restrict',
        name = '__sign',
      ),
    ],
  ),
  'gcvt': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'double',
        name = '__value',
      ),
      Param(
        type = 'int',
        name = '__ndigit',
      ),
      Param(
        type = 'char *',
        name = '__buf',
      ),
    ],
  ),
  'qecvt': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'long double',
        name = '__value',
      ),
      Param(
        type = 'int',
        name = '__ndigit',
      ),
      Param(
        type = 'int *restrict',
        name = '__decpt',
      ),
      Param(
        type = 'int *restrict',
        name = '__sign',
      ),
    ],
  ),
  'qfcvt': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'long double',
        name = '__value',
      ),
      Param(
        type = 'int',
        name = '__ndigit',
      ),
      Param(
        type = 'int *restrict',
        name = '__decpt',
      ),
      Param(
        type = 'int *restrict',
        name = '__sign',
      ),
    ],
  ),
  'qgcvt': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'long double',
        name = '__value',
      ),
      Param(
        type = 'int',
        name = '__ndigit',
      ),
      Param(
        type = 'char *',
        name = '__buf',
      ),
    ],
  ),
  'ecvt_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'double',
        name = '__value',
      ),
      Param(
        type = 'int',
        name = '__ndigit',
      ),
      Param(
        type = 'int *restrict',
        name = '__decpt',
      ),
      Param(
        type = 'int *restrict',
        name = '__sign',
      ),
      Param(
        type = 'char *restrict',
        name = '__buf',
      ),
      Param(
        type = 'size_t',
        name = '__len',
      ),
    ],
  ),
  'fcvt_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'double',
        name = '__value',
      ),
      Param(
        type = 'int',
        name = '__ndigit',
      ),
      Param(
        type = 'int *restrict',
        name = '__decpt',
      ),
      Param(
        type = 'int *restrict',
        name = '__sign',
      ),
      Param(
        type = 'char *restrict',
        name = '__buf',
      ),
      Param(
        type = 'size_t',
        name = '__len',
      ),
    ],
  ),
  'qecvt_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'long double',
        name = '__value',
      ),
      Param(
        type = 'int',
        name = '__ndigit',
      ),
      Param(
        type = 'int *restrict',
        name = '__decpt',
      ),
      Param(
        type = 'int *restrict',
        name = '__sign',
      ),
      Param(
        type = 'char *restrict',
        name = '__buf',
      ),
      Param(
        type = 'size_t',
        name = '__len',
      ),
    ],
  ),
  'qfcvt_r': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'long double',
        name = '__value',
      ),
      Param(
        type = 'int',
        name = '__ndigit',
      ),
      Param(
        type = 'int *restrict',
        name = '__decpt',
      ),
      Param(
        type = 'int *restrict',
        name = '__sign',
      ),
      Param(
        type = 'char *restrict',
        name = '__buf',
      ),
      Param(
        type = 'size_t',
        name = '__len',
      ),
    ],
  ),
  'mblen': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__s',
      ),
      Param(
        type = 'size_t',
        name = '__n',
      ),
    ],
  ),
  'mbtowc': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'wchar_t *restrict',
        name = '__pwc',
      ),
      Param(
        type = 'const char *restrict',
        name = '__s',
      ),
      Param(
        type = 'size_t',
        name = '__n',
      ),
    ],
  ),
  'wctomb': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'char *',
        name = '__s',
      ),
      Param(
        type = 'wchar_t',
        name = '__wchar',
      ),
    ],
  ),
  'mbstowcs': Spec(
    return_type = 'size_t',
    parameters = [
      Param(
        type = 'wchar_t *restrict',
        name = '__pwcs',
      ),
      Param(
        type = 'const char *restrict',
        name = '__s',
      ),
      Param(
        type = 'size_t',
        name = '__n',
      ),
    ],
  ),
  'wcstombs': Spec(
    return_type = 'size_t',
    parameters = [
      Param(
        type = 'char *restrict',
        name = '__s',
      ),
      Param(
        type = 'const wchar_t *restrict',
        name = '__pwcs',
      ),
      Param(
        type = 'size_t',
        name = '__n',
      ),
    ],
  ),
  'rpmatch': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__response',
      ),
    ],
  ),
  'getsubopt': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'char **restrict',
        name = '__optionp',
      ),
      Param(
        type = 'char *const *restrict',
        name = '__tokens',
      ),
      Param(
        type = 'char **restrict',
        name = '__valuep',
      ),
    ],
  ),
  'getloadavg': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'double []',
        name = '__loadavg',
      ),
      Param(
        type = 'int',
        name = '__nelem',
      ),
    ],
  ),
  'fcntl': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'int',
        name = '__cmd',
      ),
    ],
  ),
  'open': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__file',
      ),
      Param(
        type = 'int',
        name = '__oflag',
      ),
    ],
  ),
  'openat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *',
        name = '__file',
      ),
      Param(
        type = 'int',
        name = '__oflag',
      ),
    ],
  ),
  'creat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__file',
      ),
      Param(
        type = '__mode_t',
        name = '__mode',
      ),
    ],
  ),
  'posix_fadvise': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = '__off_t',
        name = '__offset',
      ),
      Param(
        type = '__off_t',
        name = '__len',
      ),
      Param(
        type = 'int',
        name = '__advise',
      ),
    ],
  ),
  'posix_fallocate': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = '__off_t',
        name = '__offset',
      ),
      Param(
        type = '__off_t',
        name = '__len',
      ),
    ],
  ),
  'g_unix_error_quark': Spec(
    return_type = 'GQuark',
    parameters = [
    ],
  ),
  'g_unix_open_pipe': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gint *',
        name = 'fds',
      ),
      Param(
        type = 'gint',
        name = 'flags',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_unix_set_fd_nonblocking': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gint',
        name = 'fd',
      ),
      Param(
        type = 'gboolean',
        name = 'nonblock',
      ),
      Param(
        type = 'GError **',
        name = 'error',
      ),
    ],
  ),
  'g_unix_signal_source_new': Spec(
    return_type = 'GSource *',
    parameters = [
      Param(
        type = 'gint',
        name = 'signum',
      ),
    ],
  ),
  'g_unix_signal_add_full': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gint',
        name = 'priority',
      ),
      Param(
        type = 'gint',
        name = 'signum',
      ),
      Param(
        type = 'GSourceFunc',
        name = 'handler',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'notify',
      ),
    ],
  ),
  'g_unix_signal_add': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gint',
        name = 'signum',
      ),
      Param(
        type = 'GSourceFunc',
        name = 'handler',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_type_init': Spec(
    return_type = 'void',
    parameters = [
    ],
  ),
  'g_type_init_with_debug_flags': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTypeDebugFlags',
        name = 'debug_flags',
      ),
    ],
  ),
  'g_type_name': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
    ],
  ),
  'g_type_qname': Spec(
    return_type = 'GQuark',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
    ],
  ),
  'g_type_from_name': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
    ],
  ),
  'g_type_parent': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
    ],
  ),
  'g_type_depth': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
    ],
  ),
  'g_type_next_base': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'GType',
        name = 'leaf_type',
      ),
      Param(
        type = 'GType',
        name = 'root_type',
      ),
    ],
  ),
  'g_type_is_a': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
      Param(
        type = 'GType',
        name = 'is_a_type',
      ),
    ],
  ),
  'g_type_class_ref': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
    ],
  ),
  'g_type_class_peek': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
    ],
  ),
  'g_type_class_peek_static': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
    ],
  ),
  'g_type_class_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'g_class',
      ),
    ],
  ),
  'g_type_class_peek_parent': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'g_class',
      ),
    ],
  ),
  'g_type_interface_peek': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance_class',
      ),
      Param(
        type = 'GType',
        name = 'iface_type',
      ),
    ],
  ),
  'g_type_interface_peek_parent': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'g_iface',
      ),
    ],
  ),
  'g_type_default_interface_ref': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GType',
        name = 'g_type',
      ),
    ],
  ),
  'g_type_default_interface_peek': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GType',
        name = 'g_type',
      ),
    ],
  ),
  'g_type_default_interface_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'g_iface',
      ),
    ],
  ),
  'g_type_children': Spec(
    return_type = 'GType *',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
      Param(
        type = 'guint *',
        name = 'n_children',
      ),
    ],
  ),
  'g_type_interfaces': Spec(
    return_type = 'GType *',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
      Param(
        type = 'guint *',
        name = 'n_interfaces',
      ),
    ],
  ),
  'g_type_set_qdata': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
      Param(
        type = 'GQuark',
        name = 'quark',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_type_get_qdata': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
      Param(
        type = 'GQuark',
        name = 'quark',
      ),
    ],
  ),
  'g_type_query': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
      Param(
        type = 'GTypeQuery *',
        name = 'query',
      ),
    ],
  ),
  'g_type_register_static': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'GType',
        name = 'parent_type',
      ),
      Param(
        type = 'const gchar *',
        name = 'type_name',
      ),
      Param(
        type = 'const GTypeInfo *',
        name = 'info',
      ),
      Param(
        type = 'GTypeFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_type_register_static_simple': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'GType',
        name = 'parent_type',
      ),
      Param(
        type = 'const gchar *',
        name = 'type_name',
      ),
      Param(
        type = 'guint',
        name = 'class_size',
      ),
      Param(
        type = 'GClassInitFunc',
        name = 'class_init',
      ),
      Param(
        type = 'guint',
        name = 'instance_size',
      ),
      Param(
        type = 'GInstanceInitFunc',
        name = 'instance_init',
      ),
      Param(
        type = 'GTypeFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_type_register_dynamic': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'GType',
        name = 'parent_type',
      ),
      Param(
        type = 'const gchar *',
        name = 'type_name',
      ),
      Param(
        type = 'GTypePlugin *',
        name = 'plugin',
      ),
      Param(
        type = 'GTypeFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_type_register_fundamental': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'GType',
        name = 'type_id',
      ),
      Param(
        type = 'const gchar *',
        name = 'type_name',
      ),
      Param(
        type = 'const GTypeInfo *',
        name = 'info',
      ),
      Param(
        type = 'const GTypeFundamentalInfo *',
        name = 'finfo',
      ),
      Param(
        type = 'GTypeFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_type_add_interface_static': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GType',
        name = 'instance_type',
      ),
      Param(
        type = 'GType',
        name = 'interface_type',
      ),
      Param(
        type = 'const GInterfaceInfo *',
        name = 'info',
      ),
    ],
  ),
  'g_type_add_interface_dynamic': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GType',
        name = 'instance_type',
      ),
      Param(
        type = 'GType',
        name = 'interface_type',
      ),
      Param(
        type = 'GTypePlugin *',
        name = 'plugin',
      ),
    ],
  ),
  'g_type_interface_add_prerequisite': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GType',
        name = 'interface_type',
      ),
      Param(
        type = 'GType',
        name = 'prerequisite_type',
      ),
    ],
  ),
  'g_type_interface_prerequisites': Spec(
    return_type = 'GType *',
    parameters = [
      Param(
        type = 'GType',
        name = 'interface_type',
      ),
      Param(
        type = 'guint *',
        name = 'n_prerequisites',
      ),
    ],
  ),
  'g_type_class_add_private': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'g_class',
      ),
      Param(
        type = 'gsize',
        name = 'private_size',
      ),
    ],
  ),
  'g_type_instance_get_private': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GTypeInstance *',
        name = 'instance',
      ),
      Param(
        type = 'GType',
        name = 'private_type',
      ),
    ],
  ),
  'g_type_add_class_private': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GType',
        name = 'class_type',
      ),
      Param(
        type = 'gsize',
        name = 'private_size',
      ),
    ],
  ),
  'g_type_class_get_private': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GTypeClass *',
        name = 'klass',
      ),
      Param(
        type = 'GType',
        name = 'private_type',
      ),
    ],
  ),
  'g_type_ensure': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
    ],
  ),
  'g_type_get_plugin': Spec(
    return_type = 'GTypePlugin *',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
    ],
  ),
  'g_type_interface_get_plugin': Spec(
    return_type = 'GTypePlugin *',
    parameters = [
      Param(
        type = 'GType',
        name = 'instance_type',
      ),
      Param(
        type = 'GType',
        name = 'interface_type',
      ),
    ],
  ),
  'g_type_fundamental_next': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_type_fundamental': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'GType',
        name = 'type_id',
      ),
    ],
  ),
  'g_type_create_instance': Spec(
    return_type = 'GTypeInstance *',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
    ],
  ),
  'g_type_free_instance': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTypeInstance *',
        name = 'instance',
      ),
    ],
  ),
  'g_type_add_class_cache_func': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'cache_data',
      ),
      Param(
        type = 'GTypeClassCacheFunc',
        name = 'cache_func',
      ),
    ],
  ),
  'g_type_remove_class_cache_func': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'cache_data',
      ),
      Param(
        type = 'GTypeClassCacheFunc',
        name = 'cache_func',
      ),
    ],
  ),
  'g_type_class_unref_uncached': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'g_class',
      ),
    ],
  ),
  'g_type_add_interface_check': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'check_data',
      ),
      Param(
        type = 'GTypeInterfaceCheckFunc',
        name = 'check_func',
      ),
    ],
  ),
  'g_type_remove_interface_check': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'check_data',
      ),
      Param(
        type = 'GTypeInterfaceCheckFunc',
        name = 'check_func',
      ),
    ],
  ),
  'g_type_value_table_peek': Spec(
    return_type = 'GTypeValueTable *',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
    ],
  ),
  'g_type_check_instance': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GTypeInstance *',
        name = 'instance',
      ),
    ],
  ),
  'g_type_check_instance_cast': Spec(
    return_type = 'GTypeInstance *',
    parameters = [
      Param(
        type = 'GTypeInstance *',
        name = 'instance',
      ),
      Param(
        type = 'GType',
        name = 'iface_type',
      ),
    ],
  ),
  'g_type_check_instance_is_a': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GTypeInstance *',
        name = 'instance',
      ),
      Param(
        type = 'GType',
        name = 'iface_type',
      ),
    ],
  ),
  'g_type_check_class_cast': Spec(
    return_type = 'GTypeClass *',
    parameters = [
      Param(
        type = 'GTypeClass *',
        name = 'g_class',
      ),
      Param(
        type = 'GType',
        name = 'is_a_type',
      ),
    ],
  ),
  'g_type_check_class_is_a': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GTypeClass *',
        name = 'g_class',
      ),
      Param(
        type = 'GType',
        name = 'is_a_type',
      ),
    ],
  ),
  'g_type_check_is_value_type': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
    ],
  ),
  'g_type_check_value': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_type_check_value_holds': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'GType',
        name = 'type',
      ),
    ],
  ),
  'g_type_test_flags': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GType',
        name = 'type',
      ),
      Param(
        type = 'guint',
        name = 'flags',
      ),
    ],
  ),
  'g_type_name_from_instance': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GTypeInstance *',
        name = 'instance',
      ),
    ],
  ),
  'g_type_name_from_class': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GTypeClass *',
        name = 'g_class',
      ),
    ],
  ),
  'g_value_init': Spec(
    return_type = 'GValue *',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'GType',
        name = 'g_type',
      ),
    ],
  ),
  'g_value_copy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'src_value',
      ),
      Param(
        type = 'GValue *',
        name = 'dest_value',
      ),
    ],
  ),
  'g_value_reset': Spec(
    return_type = 'GValue *',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_unset': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_instance': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
    ],
  ),
  'g_value_fits_pointer': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_peek_pointer': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_type_compatible': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GType',
        name = 'src_type',
      ),
      Param(
        type = 'GType',
        name = 'dest_type',
      ),
    ],
  ),
  'g_value_type_transformable': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GType',
        name = 'src_type',
      ),
      Param(
        type = 'GType',
        name = 'dest_type',
      ),
    ],
  ),
  'g_value_transform': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'src_value',
      ),
      Param(
        type = 'GValue *',
        name = 'dest_value',
      ),
    ],
  ),
  'g_value_register_transform_func': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GType',
        name = 'src_type',
      ),
      Param(
        type = 'GType',
        name = 'dest_type',
      ),
      Param(
        type = 'GValueTransform',
        name = 'transform_func',
      ),
    ],
  ),
  'g_param_spec_ref': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
    ],
  ),
  'g_param_spec_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
    ],
  ),
  'g_param_spec_sink': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
    ],
  ),
  'g_param_spec_ref_sink': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
    ],
  ),
  'g_param_spec_get_qdata': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
      Param(
        type = 'GQuark',
        name = 'quark',
      ),
    ],
  ),
  'g_param_spec_set_qdata': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
      Param(
        type = 'GQuark',
        name = 'quark',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_param_spec_set_qdata_full': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
      Param(
        type = 'GQuark',
        name = 'quark',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'destroy',
      ),
    ],
  ),
  'g_param_spec_steal_qdata': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
      Param(
        type = 'GQuark',
        name = 'quark',
      ),
    ],
  ),
  'g_param_spec_get_redirect_target': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
    ],
  ),
  'g_param_value_set_default': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
      Param(
        type = 'GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_param_value_defaults': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
      Param(
        type = 'GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_param_value_validate': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
      Param(
        type = 'GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_param_value_convert': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
      Param(
        type = 'const GValue *',
        name = 'src_value',
      ),
      Param(
        type = 'GValue *',
        name = 'dest_value',
      ),
      Param(
        type = 'gboolean',
        name = 'strict_validation',
      ),
    ],
  ),
  'g_param_values_cmp': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
      Param(
        type = 'const GValue *',
        name = 'value1',
      ),
      Param(
        type = 'const GValue *',
        name = 'value2',
      ),
    ],
  ),
  'g_param_spec_get_name': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
    ],
  ),
  'g_param_spec_get_nick': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
    ],
  ),
  'g_param_spec_get_blurb': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
    ],
  ),
  'g_value_set_param': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'GParamSpec *',
        name = 'param',
      ),
    ],
  ),
  'g_value_get_param': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_dup_param': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_take_param': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'GParamSpec *',
        name = 'param',
      ),
    ],
  ),
  'g_value_set_param_take_ownership': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'GParamSpec *',
        name = 'param',
      ),
    ],
  ),
  'g_param_type_register_static': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const GParamSpecTypeInfo *',
        name = 'pspec_info',
      ),
    ],
  ),
  '_g_param_type_register_static_constant': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const GParamSpecTypeInfo *',
        name = 'pspec_info',
      ),
      Param(
        type = 'GType',
        name = 'opt_type',
      ),
    ],
  ),
  'g_param_spec_internal': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GType',
        name = 'param_type',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_pool_new': Spec(
    return_type = 'GParamSpecPool *',
    parameters = [
      Param(
        type = 'gboolean',
        name = 'type_prefixing',
      ),
    ],
  ),
  'g_param_spec_pool_insert': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GParamSpecPool *',
        name = 'pool',
      ),
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
      Param(
        type = 'GType',
        name = 'owner_type',
      ),
    ],
  ),
  'g_param_spec_pool_remove': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GParamSpecPool *',
        name = 'pool',
      ),
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
    ],
  ),
  'g_param_spec_pool_lookup': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'GParamSpecPool *',
        name = 'pool',
      ),
      Param(
        type = 'const gchar *',
        name = 'param_name',
      ),
      Param(
        type = 'GType',
        name = 'owner_type',
      ),
      Param(
        type = 'gboolean',
        name = 'walk_ancestors',
      ),
    ],
  ),
  'g_param_spec_pool_list_owned': Spec(
    return_type = 'GList *',
    parameters = [
      Param(
        type = 'GParamSpecPool *',
        name = 'pool',
      ),
      Param(
        type = 'GType',
        name = 'owner_type',
      ),
    ],
  ),
  'g_param_spec_pool_list': Spec(
    return_type = 'GParamSpec **',
    parameters = [
      Param(
        type = 'GParamSpecPool *',
        name = 'pool',
      ),
      Param(
        type = 'GType',
        name = 'owner_type',
      ),
      Param(
        type = 'guint *',
        name = 'n_pspecs_p',
      ),
    ],
  ),
  'g_cclosure_new': Spec(
    return_type = 'GClosure *',
    parameters = [
      Param(
        type = 'GCallback',
        name = 'callback_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
      Param(
        type = 'GClosureNotify',
        name = 'destroy_data',
      ),
    ],
  ),
  'g_cclosure_new_swap': Spec(
    return_type = 'GClosure *',
    parameters = [
      Param(
        type = 'GCallback',
        name = 'callback_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
      Param(
        type = 'GClosureNotify',
        name = 'destroy_data',
      ),
    ],
  ),
  'g_signal_type_cclosure_new': Spec(
    return_type = 'GClosure *',
    parameters = [
      Param(
        type = 'GType',
        name = 'itype',
      ),
      Param(
        type = 'guint',
        name = 'struct_offset',
      ),
    ],
  ),
  'g_closure_ref': Spec(
    return_type = 'GClosure *',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
    ],
  ),
  'g_closure_sink': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
    ],
  ),
  'g_closure_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
    ],
  ),
  'g_closure_new_simple': Spec(
    return_type = 'GClosure *',
    parameters = [
      Param(
        type = 'guint',
        name = 'sizeof_closure',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_closure_add_finalize_notifier': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'gpointer',
        name = 'notify_data',
      ),
      Param(
        type = 'GClosureNotify',
        name = 'notify_func',
      ),
    ],
  ),
  'g_closure_remove_finalize_notifier': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'gpointer',
        name = 'notify_data',
      ),
      Param(
        type = 'GClosureNotify',
        name = 'notify_func',
      ),
    ],
  ),
  'g_closure_add_invalidate_notifier': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'gpointer',
        name = 'notify_data',
      ),
      Param(
        type = 'GClosureNotify',
        name = 'notify_func',
      ),
    ],
  ),
  'g_closure_remove_invalidate_notifier': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'gpointer',
        name = 'notify_data',
      ),
      Param(
        type = 'GClosureNotify',
        name = 'notify_func',
      ),
    ],
  ),
  'g_closure_add_marshal_guards': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'gpointer',
        name = 'pre_marshal_data',
      ),
      Param(
        type = 'GClosureNotify',
        name = 'pre_marshal_notify',
      ),
      Param(
        type = 'gpointer',
        name = 'post_marshal_data',
      ),
      Param(
        type = 'GClosureNotify',
        name = 'post_marshal_notify',
      ),
    ],
  ),
  'g_closure_set_marshal': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GClosureMarshal',
        name = 'marshal',
      ),
    ],
  ),
  'g_closure_set_meta_marshal': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'GClosureMarshal',
        name = 'meta_marshal',
      ),
    ],
  ),
  'g_closure_invalidate': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
    ],
  ),
  'g_closure_invoke': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
    ],
  ),
  'g_cclosure_marshal_generic': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_gvalue',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_generic_va': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args_list',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__VOID': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__VOIDv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__BOOLEAN': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__BOOLEANv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__CHAR': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__CHARv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__UCHAR': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__UCHARv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__INT': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__INTv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__UINT': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__UINTv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__LONG': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__LONGv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__ULONG': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__ULONGv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__ENUM': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__ENUMv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__FLAGS': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__FLAGSv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__FLOAT': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__FLOATv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__DOUBLE': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__DOUBLEv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__STRING': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__STRINGv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__PARAM': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__PARAMv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__BOXED': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__BOXEDv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__POINTER': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__POINTERv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__OBJECT': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__OBJECTv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__VARIANT': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__VARIANTv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__UINT_POINTER': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_VOID__UINT_POINTERv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_BOOLEAN__FLAGS': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_BOOLEAN__FLAGSv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_STRING__OBJECT_POINTER': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_STRING__OBJECT_POINTERv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_cclosure_marshal_BOOLEAN__BOXED_BOXED': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'guint',
        name = 'n_param_values',
      ),
      Param(
        type = 'const GValue *',
        name = 'param_values',
      ),
      Param(
        type = 'gpointer',
        name = 'invocation_hint',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
    ],
  ),
  'g_cclosure_marshal_BOOLEAN__BOXED_BOXEDv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
      Param(
        type = 'gpointer',
        name = 'marshal_data',
      ),
      Param(
        type = 'int',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_signal_newv': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'signal_name',
      ),
      Param(
        type = 'GType',
        name = 'itype',
      ),
      Param(
        type = 'GSignalFlags',
        name = 'signal_flags',
      ),
      Param(
        type = 'GClosure *',
        name = 'class_closure',
      ),
      Param(
        type = 'GSignalAccumulator',
        name = 'accumulator',
      ),
      Param(
        type = 'gpointer',
        name = 'accu_data',
      ),
      Param(
        type = 'GSignalCMarshaller',
        name = 'c_marshaller',
      ),
      Param(
        type = 'GType',
        name = 'return_type',
      ),
      Param(
        type = 'guint',
        name = 'n_params',
      ),
      Param(
        type = 'GType *',
        name = 'param_types',
      ),
    ],
  ),
  'g_signal_new_valist': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'signal_name',
      ),
      Param(
        type = 'GType',
        name = 'itype',
      ),
      Param(
        type = 'GSignalFlags',
        name = 'signal_flags',
      ),
      Param(
        type = 'GClosure *',
        name = 'class_closure',
      ),
      Param(
        type = 'GSignalAccumulator',
        name = 'accumulator',
      ),
      Param(
        type = 'gpointer',
        name = 'accu_data',
      ),
      Param(
        type = 'GSignalCMarshaller',
        name = 'c_marshaller',
      ),
      Param(
        type = 'GType',
        name = 'return_type',
      ),
      Param(
        type = 'guint',
        name = 'n_params',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
    ],
  ),
  'g_signal_new': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'signal_name',
      ),
      Param(
        type = 'GType',
        name = 'itype',
      ),
      Param(
        type = 'GSignalFlags',
        name = 'signal_flags',
      ),
      Param(
        type = 'guint',
        name = 'class_offset',
      ),
      Param(
        type = 'GSignalAccumulator',
        name = 'accumulator',
      ),
      Param(
        type = 'gpointer',
        name = 'accu_data',
      ),
      Param(
        type = 'GSignalCMarshaller',
        name = 'c_marshaller',
      ),
      Param(
        type = 'GType',
        name = 'return_type',
      ),
      Param(
        type = 'guint',
        name = 'n_params',
      ),
    ],
  ),
  'g_signal_new_class_handler': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'signal_name',
      ),
      Param(
        type = 'GType',
        name = 'itype',
      ),
      Param(
        type = 'GSignalFlags',
        name = 'signal_flags',
      ),
      Param(
        type = 'GCallback',
        name = 'class_handler',
      ),
      Param(
        type = 'GSignalAccumulator',
        name = 'accumulator',
      ),
      Param(
        type = 'gpointer',
        name = 'accu_data',
      ),
      Param(
        type = 'GSignalCMarshaller',
        name = 'c_marshaller',
      ),
      Param(
        type = 'GType',
        name = 'return_type',
      ),
      Param(
        type = 'guint',
        name = 'n_params',
      ),
    ],
  ),
  'g_signal_set_va_marshaller': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'GType',
        name = 'instance_type',
      ),
      Param(
        type = 'GSignalCVaMarshaller',
        name = 'va_marshaller',
      ),
    ],
  ),
  'g_signal_emitv': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'instance_and_params',
      ),
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'GQuark',
        name = 'detail',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
    ],
  ),
  'g_signal_emit_valist': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'GQuark',
        name = 'detail',
      ),
      Param(
        type = 'va_list',
        name = 'var_args',
      ),
    ],
  ),
  'g_signal_emit': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'GQuark',
        name = 'detail',
      ),
    ],
  ),
  'g_signal_emit_by_name': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'const gchar *',
        name = 'detailed_signal',
      ),
    ],
  ),
  'g_signal_lookup': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'GType',
        name = 'itype',
      ),
    ],
  ),
  'g_signal_name': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
    ],
  ),
  'g_signal_query': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'GSignalQuery *',
        name = 'query',
      ),
    ],
  ),
  'g_signal_list_ids': Spec(
    return_type = 'guint *',
    parameters = [
      Param(
        type = 'GType',
        name = 'itype',
      ),
      Param(
        type = 'guint *',
        name = 'n_ids',
      ),
    ],
  ),
  'g_signal_parse_name': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'detailed_signal',
      ),
      Param(
        type = 'GType',
        name = 'itype',
      ),
      Param(
        type = 'guint *',
        name = 'signal_id_p',
      ),
      Param(
        type = 'GQuark *',
        name = 'detail_p',
      ),
      Param(
        type = 'gboolean',
        name = 'force_detail_quark',
      ),
    ],
  ),
  'g_signal_get_invocation_hint': Spec(
    return_type = 'GSignalInvocationHint *',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
    ],
  ),
  'g_signal_stop_emission': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'GQuark',
        name = 'detail',
      ),
    ],
  ),
  'g_signal_stop_emission_by_name': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'const gchar *',
        name = 'detailed_signal',
      ),
    ],
  ),
  'g_signal_add_emission_hook': Spec(
    return_type = 'gulong',
    parameters = [
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'GQuark',
        name = 'detail',
      ),
      Param(
        type = 'GSignalEmissionHook',
        name = 'hook_func',
      ),
      Param(
        type = 'gpointer',
        name = 'hook_data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'data_destroy',
      ),
    ],
  ),
  'g_signal_remove_emission_hook': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'gulong',
        name = 'hook_id',
      ),
    ],
  ),
  'g_signal_has_handler_pending': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'GQuark',
        name = 'detail',
      ),
      Param(
        type = 'gboolean',
        name = 'may_be_blocked',
      ),
    ],
  ),
  'g_signal_connect_closure_by_id': Spec(
    return_type = 'gulong',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'GQuark',
        name = 'detail',
      ),
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'gboolean',
        name = 'after',
      ),
    ],
  ),
  'g_signal_connect_closure': Spec(
    return_type = 'gulong',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'const gchar *',
        name = 'detailed_signal',
      ),
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'gboolean',
        name = 'after',
      ),
    ],
  ),
  'g_signal_connect_data': Spec(
    return_type = 'gulong',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'const gchar *',
        name = 'detailed_signal',
      ),
      Param(
        type = 'GCallback',
        name = 'c_handler',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GClosureNotify',
        name = 'destroy_data',
      ),
      Param(
        type = 'GConnectFlags',
        name = 'connect_flags',
      ),
    ],
  ),
  'g_signal_handler_block': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'gulong',
        name = 'handler_id',
      ),
    ],
  ),
  'g_signal_handler_unblock': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'gulong',
        name = 'handler_id',
      ),
    ],
  ),
  'g_signal_handler_disconnect': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'gulong',
        name = 'handler_id',
      ),
    ],
  ),
  'g_signal_handler_is_connected': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'gulong',
        name = 'handler_id',
      ),
    ],
  ),
  'g_signal_handler_find': Spec(
    return_type = 'gulong',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'GSignalMatchType',
        name = 'mask',
      ),
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'GQuark',
        name = 'detail',
      ),
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'gpointer',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_signal_handlers_block_matched': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'GSignalMatchType',
        name = 'mask',
      ),
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'GQuark',
        name = 'detail',
      ),
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'gpointer',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_signal_handlers_unblock_matched': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'GSignalMatchType',
        name = 'mask',
      ),
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'GQuark',
        name = 'detail',
      ),
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'gpointer',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_signal_handlers_disconnect_matched': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'GSignalMatchType',
        name = 'mask',
      ),
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'GQuark',
        name = 'detail',
      ),
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
      Param(
        type = 'gpointer',
        name = 'func',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_signal_override_class_closure': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'guint',
        name = 'signal_id',
      ),
      Param(
        type = 'GType',
        name = 'instance_type',
      ),
      Param(
        type = 'GClosure *',
        name = 'class_closure',
      ),
    ],
  ),
  'g_signal_override_class_handler': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'signal_name',
      ),
      Param(
        type = 'GType',
        name = 'instance_type',
      ),
      Param(
        type = 'GCallback',
        name = 'class_handler',
      ),
    ],
  ),
  'g_signal_chain_from_overridden': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'instance_and_params',
      ),
      Param(
        type = 'GValue *',
        name = 'return_value',
      ),
    ],
  ),
  'g_signal_chain_from_overridden_handler': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
    ],
  ),
  'g_signal_accumulator_true_handled': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GSignalInvocationHint *',
        name = 'ihint',
      ),
      Param(
        type = 'GValue *',
        name = 'return_accu',
      ),
      Param(
        type = 'const GValue *',
        name = 'handler_return',
      ),
      Param(
        type = 'gpointer',
        name = 'dummy',
      ),
    ],
  ),
  'g_signal_accumulator_first_wins': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GSignalInvocationHint *',
        name = 'ihint',
      ),
      Param(
        type = 'GValue *',
        name = 'return_accu',
      ),
      Param(
        type = 'const GValue *',
        name = 'handler_return',
      ),
      Param(
        type = 'gpointer',
        name = 'dummy',
      ),
    ],
  ),
  'g_signal_handlers_destroy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
    ],
  ),
  '_g_signals_destroy': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GType',
        name = 'itype',
      ),
    ],
  ),
  'g_date_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_strv_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_gstring_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_hash_table_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_array_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_byte_array_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_ptr_array_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_bytes_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_variant_type_get_gtype': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_regex_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_match_info_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_error_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_date_time_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_time_zone_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_io_channel_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_io_condition_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_variant_builder_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_key_file_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_main_loop_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_main_context_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_source_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_pollfd_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_thread_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_variant_get_gtype': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_boxed_copy': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GType',
        name = 'boxed_type',
      ),
      Param(
        type = 'gconstpointer',
        name = 'src_boxed',
      ),
    ],
  ),
  'g_boxed_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GType',
        name = 'boxed_type',
      ),
      Param(
        type = 'gpointer',
        name = 'boxed',
      ),
    ],
  ),
  'g_value_set_boxed': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gconstpointer',
        name = 'v_boxed',
      ),
    ],
  ),
  'g_value_set_static_boxed': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gconstpointer',
        name = 'v_boxed',
      ),
    ],
  ),
  'g_value_take_boxed': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gconstpointer',
        name = 'v_boxed',
      ),
    ],
  ),
  'g_value_set_boxed_take_ownership': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gconstpointer',
        name = 'v_boxed',
      ),
    ],
  ),
  'g_value_get_boxed': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_dup_boxed': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_boxed_type_register_static': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'GBoxedCopyFunc',
        name = 'boxed_copy',
      ),
      Param(
        type = 'GBoxedFreeFunc',
        name = 'boxed_free',
      ),
    ],
  ),
  'g_closure_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_value_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_initially_unowned_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_object_class_install_property': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObjectClass *',
        name = 'oclass',
      ),
      Param(
        type = 'guint',
        name = 'property_id',
      ),
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
    ],
  ),
  'g_object_class_find_property': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'GObjectClass *',
        name = 'oclass',
      ),
      Param(
        type = 'const gchar *',
        name = 'property_name',
      ),
    ],
  ),
  'g_object_class_list_properties': Spec(
    return_type = 'GParamSpec **',
    parameters = [
      Param(
        type = 'GObjectClass *',
        name = 'oclass',
      ),
      Param(
        type = 'guint *',
        name = 'n_properties',
      ),
    ],
  ),
  'g_object_class_override_property': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObjectClass *',
        name = 'oclass',
      ),
      Param(
        type = 'guint',
        name = 'property_id',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
    ],
  ),
  'g_object_class_install_properties': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObjectClass *',
        name = 'oclass',
      ),
      Param(
        type = 'guint',
        name = 'n_pspecs',
      ),
      Param(
        type = 'GParamSpec **',
        name = 'pspecs',
      ),
    ],
  ),
  'g_object_interface_install_property': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'g_iface',
      ),
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
    ],
  ),
  'g_object_interface_find_property': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'g_iface',
      ),
      Param(
        type = 'const gchar *',
        name = 'property_name',
      ),
    ],
  ),
  'g_object_interface_list_properties': Spec(
    return_type = 'GParamSpec **',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'g_iface',
      ),
      Param(
        type = 'guint *',
        name = 'n_properties_p',
      ),
    ],
  ),
  'g_object_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_object_new': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GType',
        name = 'object_type',
      ),
      Param(
        type = 'const gchar *',
        name = 'first_property_name',
      ),
    ],
  ),
  'g_object_newv': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GType',
        name = 'object_type',
      ),
      Param(
        type = 'guint',
        name = 'n_parameters',
      ),
      Param(
        type = 'GParameter *',
        name = 'parameters',
      ),
    ],
  ),
  'g_object_new_valist': Spec(
    return_type = 'GObject *',
    parameters = [
      Param(
        type = 'GType',
        name = 'object_type',
      ),
      Param(
        type = 'const gchar *',
        name = 'first_property_name',
      ),
      Param(
        type = 'va_list',
        name = 'var_args',
      ),
    ],
  ),
  'g_object_set': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'first_property_name',
      ),
    ],
  ),
  'g_object_get': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'first_property_name',
      ),
    ],
  ),
  'g_object_connect': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'signal_spec',
      ),
    ],
  ),
  'g_object_disconnect': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'signal_spec',
      ),
    ],
  ),
  'g_object_set_valist': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'first_property_name',
      ),
      Param(
        type = 'va_list',
        name = 'var_args',
      ),
    ],
  ),
  'g_object_get_valist': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'first_property_name',
      ),
      Param(
        type = 'va_list',
        name = 'var_args',
      ),
    ],
  ),
  'g_object_set_property': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'property_name',
      ),
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_object_get_property': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'property_name',
      ),
      Param(
        type = 'GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_object_freeze_notify': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
    ],
  ),
  'g_object_notify': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'property_name',
      ),
    ],
  ),
  'g_object_notify_by_pspec': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'GParamSpec *',
        name = 'pspec',
      ),
    ],
  ),
  'g_object_thaw_notify': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
    ],
  ),
  'g_object_is_floating': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'object',
      ),
    ],
  ),
  'g_object_ref_sink': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'object',
      ),
    ],
  ),
  'g_object_ref': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'object',
      ),
    ],
  ),
  'g_object_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'object',
      ),
    ],
  ),
  'g_object_weak_ref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'GWeakNotify',
        name = 'notify',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_object_weak_unref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'GWeakNotify',
        name = 'notify',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_object_add_weak_pointer': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'gpointer *',
        name = 'weak_pointer_location',
      ),
    ],
  ),
  'g_object_remove_weak_pointer': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'gpointer *',
        name = 'weak_pointer_location',
      ),
    ],
  ),
  'g_object_add_toggle_ref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'GToggleNotify',
        name = 'notify',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_object_remove_toggle_ref': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'GToggleNotify',
        name = 'notify',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_object_get_qdata': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'GQuark',
        name = 'quark',
      ),
    ],
  ),
  'g_object_set_qdata': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'GQuark',
        name = 'quark',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_object_set_qdata_full': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'GQuark',
        name = 'quark',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'destroy',
      ),
    ],
  ),
  'g_object_steal_qdata': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'GQuark',
        name = 'quark',
      ),
    ],
  ),
  'g_object_dup_qdata': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'GQuark',
        name = 'quark',
      ),
      Param(
        type = 'GDuplicateFunc',
        name = 'dup_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_object_replace_qdata': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'GQuark',
        name = 'quark',
      ),
      Param(
        type = 'gpointer',
        name = 'oldval',
      ),
      Param(
        type = 'gpointer',
        name = 'newval',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'destroy',
      ),
      Param(
        type = 'GDestroyNotify *',
        name = 'old_destroy',
      ),
    ],
  ),
  'g_object_get_data': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
    ],
  ),
  'g_object_set_data': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_object_set_data_full': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'destroy',
      ),
    ],
  ),
  'g_object_steal_data': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
    ],
  ),
  'g_object_dup_data': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'GDuplicateFunc',
        name = 'dup_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_object_replace_data': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'const gchar *',
        name = 'key',
      ),
      Param(
        type = 'gpointer',
        name = 'oldval',
      ),
      Param(
        type = 'gpointer',
        name = 'newval',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'destroy',
      ),
      Param(
        type = 'GDestroyNotify *',
        name = 'old_destroy',
      ),
    ],
  ),
  'g_object_watch_closure': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
    ],
  ),
  'g_cclosure_new_object': Spec(
    return_type = 'GClosure *',
    parameters = [
      Param(
        type = 'GCallback',
        name = 'callback_func',
      ),
      Param(
        type = 'GObject *',
        name = 'object',
      ),
    ],
  ),
  'g_cclosure_new_object_swap': Spec(
    return_type = 'GClosure *',
    parameters = [
      Param(
        type = 'GCallback',
        name = 'callback_func',
      ),
      Param(
        type = 'GObject *',
        name = 'object',
      ),
    ],
  ),
  'g_closure_new_object': Spec(
    return_type = 'GClosure *',
    parameters = [
      Param(
        type = 'guint',
        name = 'sizeof_closure',
      ),
      Param(
        type = 'GObject *',
        name = 'object',
      ),
    ],
  ),
  'g_value_set_object': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gpointer',
        name = 'v_object',
      ),
    ],
  ),
  'g_value_get_object': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_dup_object': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_signal_connect_object': Spec(
    return_type = 'gulong',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'instance',
      ),
      Param(
        type = 'const gchar *',
        name = 'detailed_signal',
      ),
      Param(
        type = 'GCallback',
        name = 'c_handler',
      ),
      Param(
        type = 'gpointer',
        name = 'gobject',
      ),
      Param(
        type = 'GConnectFlags',
        name = 'connect_flags',
      ),
    ],
  ),
  'g_object_force_floating': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
    ],
  ),
  'g_object_run_dispose': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GObject *',
        name = 'object',
      ),
    ],
  ),
  'g_value_take_object': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gpointer',
        name = 'v_object',
      ),
    ],
  ),
  'g_value_set_object_take_ownership': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gpointer',
        name = 'v_object',
      ),
    ],
  ),
  'g_object_compat_control': Spec(
    return_type = 'gsize',
    parameters = [
      Param(
        type = 'gsize',
        name = 'what',
      ),
      Param(
        type = 'gpointer',
        name = 'data',
      ),
    ],
  ),
  'g_clear_object': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'volatile GObject **',
        name = 'object_ptr',
      ),
    ],
  ),
  'g_weak_ref_init': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GWeakRef *',
        name = 'weak_ref',
      ),
      Param(
        type = 'gpointer',
        name = 'object',
      ),
    ],
  ),
  'g_weak_ref_clear': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GWeakRef *',
        name = 'weak_ref',
      ),
    ],
  ),
  'g_weak_ref_get': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'GWeakRef *',
        name = 'weak_ref',
      ),
    ],
  ),
  'g_weak_ref_set': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GWeakRef *',
        name = 'weak_ref',
      ),
      Param(
        type = 'gpointer',
        name = 'object',
      ),
    ],
  ),
  'g_binding_flags_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_binding_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_binding_get_flags': Spec(
    return_type = 'GBindingFlags',
    parameters = [
      Param(
        type = 'GBinding *',
        name = 'binding',
      ),
    ],
  ),
  'g_binding_get_source': Spec(
    return_type = 'GObject *',
    parameters = [
      Param(
        type = 'GBinding *',
        name = 'binding',
      ),
    ],
  ),
  'g_binding_get_target': Spec(
    return_type = 'GObject *',
    parameters = [
      Param(
        type = 'GBinding *',
        name = 'binding',
      ),
    ],
  ),
  'g_binding_get_source_property': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GBinding *',
        name = 'binding',
      ),
    ],
  ),
  'g_binding_get_target_property': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'GBinding *',
        name = 'binding',
      ),
    ],
  ),
  'g_object_bind_property': Spec(
    return_type = 'GBinding *',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'source',
      ),
      Param(
        type = 'const gchar *',
        name = 'source_property',
      ),
      Param(
        type = 'gpointer',
        name = 'target',
      ),
      Param(
        type = 'const gchar *',
        name = 'target_property',
      ),
      Param(
        type = 'GBindingFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_object_bind_property_full': Spec(
    return_type = 'GBinding *',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'source',
      ),
      Param(
        type = 'const gchar *',
        name = 'source_property',
      ),
      Param(
        type = 'gpointer',
        name = 'target',
      ),
      Param(
        type = 'const gchar *',
        name = 'target_property',
      ),
      Param(
        type = 'GBindingFlags',
        name = 'flags',
      ),
      Param(
        type = 'GBindingTransformFunc',
        name = 'transform_to',
      ),
      Param(
        type = 'GBindingTransformFunc',
        name = 'transform_from',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
      Param(
        type = 'GDestroyNotify',
        name = 'notify',
      ),
    ],
  ),
  'g_object_bind_property_with_closures': Spec(
    return_type = 'GBinding *',
    parameters = [
      Param(
        type = 'gpointer',
        name = 'source',
      ),
      Param(
        type = 'const gchar *',
        name = 'source_property',
      ),
      Param(
        type = 'gpointer',
        name = 'target',
      ),
      Param(
        type = 'const gchar *',
        name = 'target_property',
      ),
      Param(
        type = 'GBindingFlags',
        name = 'flags',
      ),
      Param(
        type = 'GClosure *',
        name = 'transform_to',
      ),
      Param(
        type = 'GClosure *',
        name = 'transform_from',
      ),
    ],
  ),
  'g_enum_get_value': Spec(
    return_type = 'GEnumValue *',
    parameters = [
      Param(
        type = 'GEnumClass *',
        name = 'enum_class',
      ),
      Param(
        type = 'gint',
        name = 'value',
      ),
    ],
  ),
  'g_enum_get_value_by_name': Spec(
    return_type = 'GEnumValue *',
    parameters = [
      Param(
        type = 'GEnumClass *',
        name = 'enum_class',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
    ],
  ),
  'g_enum_get_value_by_nick': Spec(
    return_type = 'GEnumValue *',
    parameters = [
      Param(
        type = 'GEnumClass *',
        name = 'enum_class',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
    ],
  ),
  'g_flags_get_first_value': Spec(
    return_type = 'GFlagsValue *',
    parameters = [
      Param(
        type = 'GFlagsClass *',
        name = 'flags_class',
      ),
      Param(
        type = 'guint',
        name = 'value',
      ),
    ],
  ),
  'g_flags_get_value_by_name': Spec(
    return_type = 'GFlagsValue *',
    parameters = [
      Param(
        type = 'GFlagsClass *',
        name = 'flags_class',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
    ],
  ),
  'g_flags_get_value_by_nick': Spec(
    return_type = 'GFlagsValue *',
    parameters = [
      Param(
        type = 'GFlagsClass *',
        name = 'flags_class',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
    ],
  ),
  'g_value_set_enum': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gint',
        name = 'v_enum',
      ),
    ],
  ),
  'g_value_get_enum': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_flags': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'guint',
        name = 'v_flags',
      ),
    ],
  ),
  'g_value_get_flags': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_enum_register_static': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const GEnumValue *',
        name = 'const_static_values',
      ),
    ],
  ),
  'g_flags_register_static': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const GFlagsValue *',
        name = 'const_static_values',
      ),
    ],
  ),
  'g_enum_complete_type_info': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GType',
        name = 'g_enum_type',
      ),
      Param(
        type = 'GTypeInfo *',
        name = 'info',
      ),
      Param(
        type = 'const GEnumValue *',
        name = 'const_values',
      ),
    ],
  ),
  'g_flags_complete_type_info': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GType',
        name = 'g_flags_type',
      ),
      Param(
        type = 'GTypeInfo *',
        name = 'info',
      ),
      Param(
        type = 'const GFlagsValue *',
        name = 'const_values',
      ),
    ],
  ),
  'g_param_spec_char': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'gint8',
        name = 'minimum',
      ),
      Param(
        type = 'gint8',
        name = 'maximum',
      ),
      Param(
        type = 'gint8',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_uchar': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'guint8',
        name = 'minimum',
      ),
      Param(
        type = 'guint8',
        name = 'maximum',
      ),
      Param(
        type = 'guint8',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_boolean': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'gboolean',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_int': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'gint',
        name = 'minimum',
      ),
      Param(
        type = 'gint',
        name = 'maximum',
      ),
      Param(
        type = 'gint',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_uint': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'guint',
        name = 'minimum',
      ),
      Param(
        type = 'guint',
        name = 'maximum',
      ),
      Param(
        type = 'guint',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_long': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'glong',
        name = 'minimum',
      ),
      Param(
        type = 'glong',
        name = 'maximum',
      ),
      Param(
        type = 'glong',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_ulong': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'gulong',
        name = 'minimum',
      ),
      Param(
        type = 'gulong',
        name = 'maximum',
      ),
      Param(
        type = 'gulong',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_int64': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'gint64',
        name = 'minimum',
      ),
      Param(
        type = 'gint64',
        name = 'maximum',
      ),
      Param(
        type = 'gint64',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_uint64': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'guint64',
        name = 'minimum',
      ),
      Param(
        type = 'guint64',
        name = 'maximum',
      ),
      Param(
        type = 'guint64',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_unichar': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'gunichar',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_enum': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'GType',
        name = 'enum_type',
      ),
      Param(
        type = 'gint',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_flags': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'GType',
        name = 'flags_type',
      ),
      Param(
        type = 'guint',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_float': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'gfloat',
        name = 'minimum',
      ),
      Param(
        type = 'gfloat',
        name = 'maximum',
      ),
      Param(
        type = 'gfloat',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_double': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'gdouble',
        name = 'minimum',
      ),
      Param(
        type = 'gdouble',
        name = 'maximum',
      ),
      Param(
        type = 'gdouble',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_string': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'const gchar *',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_param': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'GType',
        name = 'param_type',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_boxed': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'GType',
        name = 'boxed_type',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_pointer': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_value_array': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'GParamSpec *',
        name = 'element_spec',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_object': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'GType',
        name = 'object_type',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_override': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'GParamSpec *',
        name = 'overridden',
      ),
    ],
  ),
  'g_param_spec_gtype': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'GType',
        name = 'is_a_type',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_param_spec_variant': Spec(
    return_type = 'GParamSpec *',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const gchar *',
        name = 'nick',
      ),
      Param(
        type = 'const gchar *',
        name = 'blurb',
      ),
      Param(
        type = 'const GVariantType *',
        name = 'type',
      ),
      Param(
        type = 'GVariant *',
        name = 'default_value',
      ),
      Param(
        type = 'GParamFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_source_set_closure': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
      Param(
        type = 'GClosure *',
        name = 'closure',
      ),
    ],
  ),
  'g_source_set_dummy_callback': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GSource *',
        name = 'source',
      ),
    ],
  ),
  'g_type_module_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_type_module_use': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'GTypeModule *',
        name = 'module',
      ),
    ],
  ),
  'g_type_module_unuse': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTypeModule *',
        name = 'module',
      ),
    ],
  ),
  'g_type_module_set_name': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTypeModule *',
        name = 'module',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
    ],
  ),
  'g_type_module_register_type': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'GTypeModule *',
        name = 'module',
      ),
      Param(
        type = 'GType',
        name = 'parent_type',
      ),
      Param(
        type = 'const gchar *',
        name = 'type_name',
      ),
      Param(
        type = 'const GTypeInfo *',
        name = 'type_info',
      ),
      Param(
        type = 'GTypeFlags',
        name = 'flags',
      ),
    ],
  ),
  'g_type_module_add_interface': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTypeModule *',
        name = 'module',
      ),
      Param(
        type = 'GType',
        name = 'instance_type',
      ),
      Param(
        type = 'GType',
        name = 'interface_type',
      ),
      Param(
        type = 'const GInterfaceInfo *',
        name = 'interface_info',
      ),
    ],
  ),
  'g_type_module_register_enum': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'GTypeModule *',
        name = 'module',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const GEnumValue *',
        name = 'const_static_values',
      ),
    ],
  ),
  'g_type_module_register_flags': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'GTypeModule *',
        name = 'module',
      ),
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
      Param(
        type = 'const GFlagsValue *',
        name = 'const_static_values',
      ),
    ],
  ),
  'g_type_plugin_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_type_plugin_use': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTypePlugin *',
        name = 'plugin',
      ),
    ],
  ),
  'g_type_plugin_unuse': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTypePlugin *',
        name = 'plugin',
      ),
    ],
  ),
  'g_type_plugin_complete_type_info': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTypePlugin *',
        name = 'plugin',
      ),
      Param(
        type = 'GType',
        name = 'g_type',
      ),
      Param(
        type = 'GTypeInfo *',
        name = 'info',
      ),
      Param(
        type = 'GTypeValueTable *',
        name = 'value_table',
      ),
    ],
  ),
  'g_type_plugin_complete_interface_info': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GTypePlugin *',
        name = 'plugin',
      ),
      Param(
        type = 'GType',
        name = 'instance_type',
      ),
      Param(
        type = 'GType',
        name = 'interface_type',
      ),
      Param(
        type = 'GInterfaceInfo *',
        name = 'info',
      ),
    ],
  ),
  'g_value_array_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_value_array_get_nth': Spec(
    return_type = 'GValue *',
    parameters = [
      Param(
        type = 'GValueArray *',
        name = 'value_array',
      ),
      Param(
        type = 'guint',
        name = 'index_',
      ),
    ],
  ),
  'g_value_array_new': Spec(
    return_type = 'GValueArray *',
    parameters = [
      Param(
        type = 'guint',
        name = 'n_prealloced',
      ),
    ],
  ),
  'g_value_array_free': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValueArray *',
        name = 'value_array',
      ),
    ],
  ),
  'g_value_array_copy': Spec(
    return_type = 'GValueArray *',
    parameters = [
      Param(
        type = 'const GValueArray *',
        name = 'value_array',
      ),
    ],
  ),
  'g_value_array_prepend': Spec(
    return_type = 'GValueArray *',
    parameters = [
      Param(
        type = 'GValueArray *',
        name = 'value_array',
      ),
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_array_append': Spec(
    return_type = 'GValueArray *',
    parameters = [
      Param(
        type = 'GValueArray *',
        name = 'value_array',
      ),
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_array_insert': Spec(
    return_type = 'GValueArray *',
    parameters = [
      Param(
        type = 'GValueArray *',
        name = 'value_array',
      ),
      Param(
        type = 'guint',
        name = 'index_',
      ),
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_array_remove': Spec(
    return_type = 'GValueArray *',
    parameters = [
      Param(
        type = 'GValueArray *',
        name = 'value_array',
      ),
      Param(
        type = 'guint',
        name = 'index_',
      ),
    ],
  ),
  'g_value_array_sort': Spec(
    return_type = 'GValueArray *',
    parameters = [
      Param(
        type = 'GValueArray *',
        name = 'value_array',
      ),
      Param(
        type = 'GCompareFunc',
        name = 'compare_func',
      ),
    ],
  ),
  'g_value_array_sort_with_data': Spec(
    return_type = 'GValueArray *',
    parameters = [
      Param(
        type = 'GValueArray *',
        name = 'value_array',
      ),
      Param(
        type = 'GCompareDataFunc',
        name = 'compare_func',
      ),
      Param(
        type = 'gpointer',
        name = 'user_data',
      ),
    ],
  ),
  'g_value_set_char': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gchar',
        name = 'v_char',
      ),
    ],
  ),
  'g_value_get_char': Spec(
    return_type = 'gchar',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_schar': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gint8',
        name = 'v_char',
      ),
    ],
  ),
  'g_value_get_schar': Spec(
    return_type = 'gint8',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_uchar': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'guchar',
        name = 'v_uchar',
      ),
    ],
  ),
  'g_value_get_uchar': Spec(
    return_type = 'guchar',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_boolean': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gboolean',
        name = 'v_boolean',
      ),
    ],
  ),
  'g_value_get_boolean': Spec(
    return_type = 'gboolean',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_int': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gint',
        name = 'v_int',
      ),
    ],
  ),
  'g_value_get_int': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_uint': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'guint',
        name = 'v_uint',
      ),
    ],
  ),
  'g_value_get_uint': Spec(
    return_type = 'guint',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_long': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'glong',
        name = 'v_long',
      ),
    ],
  ),
  'g_value_get_long': Spec(
    return_type = 'glong',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_ulong': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gulong',
        name = 'v_ulong',
      ),
    ],
  ),
  'g_value_get_ulong': Spec(
    return_type = 'gulong',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_int64': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gint64',
        name = 'v_int64',
      ),
    ],
  ),
  'g_value_get_int64': Spec(
    return_type = 'gint64',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_uint64': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'guint64',
        name = 'v_uint64',
      ),
    ],
  ),
  'g_value_get_uint64': Spec(
    return_type = 'guint64',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_float': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gfloat',
        name = 'v_float',
      ),
    ],
  ),
  'g_value_get_float': Spec(
    return_type = 'gfloat',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_double': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gdouble',
        name = 'v_double',
      ),
    ],
  ),
  'g_value_get_double': Spec(
    return_type = 'gdouble',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_string': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'const gchar *',
        name = 'v_string',
      ),
    ],
  ),
  'g_value_set_static_string': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'const gchar *',
        name = 'v_string',
      ),
    ],
  ),
  'g_value_get_string': Spec(
    return_type = 'const gchar *',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_dup_string': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_pointer': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gpointer',
        name = 'v_pointer',
      ),
    ],
  ),
  'g_value_get_pointer': Spec(
    return_type = 'gpointer',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_gtype_get_type': Spec(
    return_type = 'GType',
    parameters = [
    ],
  ),
  'g_value_set_gtype': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'GType',
        name = 'v_gtype',
      ),
    ],
  ),
  'g_value_get_gtype': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_set_variant': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'GVariant *',
        name = 'variant',
      ),
    ],
  ),
  'g_value_take_variant': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'GVariant *',
        name = 'variant',
      ),
    ],
  ),
  'g_value_get_variant': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_dup_variant': Spec(
    return_type = 'GVariant *',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_pointer_type_register_static': Spec(
    return_type = 'GType',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'name',
      ),
    ],
  ),
  'g_strdup_value_contents': Spec(
    return_type = 'gchar *',
    parameters = [
      Param(
        type = 'const GValue *',
        name = 'value',
      ),
    ],
  ),
  'g_value_take_string': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gchar *',
        name = 'v_string',
      ),
    ],
  ),
  'g_value_set_string_take_ownership': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'GValue *',
        name = 'value',
      ),
      Param(
        type = 'gchar *',
        name = 'v_string',
      ),
    ],
  ),
  '__underflow': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '',
      ),
    ],
  ),
  '__uflow': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '',
      ),
    ],
  ),
  '__overflow': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '',
      ),
      Param(
        type = 'int',
        name = '',
      ),
    ],
  ),
  '_IO_getc': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '__fp',
      ),
    ],
  ),
  '_IO_putc': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__c',
      ),
      Param(
        type = '_IO_FILE *',
        name = '__fp',
      ),
    ],
  ),
  '_IO_feof': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '__fp',
      ),
    ],
  ),
  '_IO_ferror': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '__fp',
      ),
    ],
  ),
  '_IO_peekc_locked': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '__fp',
      ),
    ],
  ),
  '_IO_flockfile': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '',
      ),
    ],
  ),
  '_IO_funlockfile': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '',
      ),
    ],
  ),
  '_IO_ftrylockfile': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '',
      ),
    ],
  ),
  '_IO_vfscanf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '_IO_FILE *restrict',
        name = '',
      ),
      Param(
        type = 'const char *restrict',
        name = '',
      ),
      Param(
        type = '__gnuc_va_list',
        name = '',
      ),
      Param(
        type = 'int *restrict',
        name = '',
      ),
    ],
  ),
  '_IO_vfprintf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = '_IO_FILE *restrict',
        name = '',
      ),
      Param(
        type = 'const char *restrict',
        name = '',
      ),
      Param(
        type = '__gnuc_va_list',
        name = '',
      ),
    ],
  ),
  '_IO_padn': Spec(
    return_type = '__ssize_t',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '',
      ),
      Param(
        type = 'int',
        name = '',
      ),
      Param(
        type = '__ssize_t',
        name = '',
      ),
    ],
  ),
  '_IO_sgetn': Spec(
    return_type = 'size_t',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '',
      ),
      Param(
        type = 'void *',
        name = '',
      ),
      Param(
        type = 'size_t',
        name = '',
      ),
    ],
  ),
  '_IO_seekoff': Spec(
    return_type = '__off64_t',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '',
      ),
      Param(
        type = '__off64_t',
        name = '',
      ),
      Param(
        type = 'int',
        name = '',
      ),
      Param(
        type = 'int',
        name = '',
      ),
    ],
  ),
  '_IO_seekpos': Spec(
    return_type = '__off64_t',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '',
      ),
      Param(
        type = '__off64_t',
        name = '',
      ),
      Param(
        type = 'int',
        name = '',
      ),
    ],
  ),
  '_IO_free_backup_area': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = '_IO_FILE *',
        name = '',
      ),
    ],
  ),
  'remove': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__filename',
      ),
    ],
  ),
  'rename': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__old',
      ),
      Param(
        type = 'const char *',
        name = '__new',
      ),
    ],
  ),
  'renameat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__oldfd',
      ),
      Param(
        type = 'const char *',
        name = '__old',
      ),
      Param(
        type = 'int',
        name = '__newfd',
      ),
      Param(
        type = 'const char *',
        name = '__new',
      ),
    ],
  ),
  'tmpfile': Spec(
    return_type = 'FILE *',
    parameters = [
    ],
  ),
  'tmpnam': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'char *',
        name = '__s',
      ),
    ],
  ),
  'tmpnam_r': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'char *',
        name = '__s',
      ),
    ],
  ),
  'tempnam': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'const char *',
        name = '__dir',
      ),
      Param(
        type = 'const char *',
        name = '__pfx',
      ),
    ],
  ),
  'fclose': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'fflush': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'fflush_unlocked': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'fopen': Spec(
    return_type = 'FILE *',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__filename',
      ),
      Param(
        type = 'const char *restrict',
        name = '__modes',
      ),
    ],
  ),
  'freopen': Spec(
    return_type = 'FILE *',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__filename',
      ),
      Param(
        type = 'const char *restrict',
        name = '__modes',
      ),
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
    ],
  ),
  'fdopen': Spec(
    return_type = 'FILE *',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *',
        name = '__modes',
      ),
    ],
  ),
  'fmemopen': Spec(
    return_type = 'FILE *',
    parameters = [
      Param(
        type = 'void *',
        name = '__s',
      ),
      Param(
        type = 'size_t',
        name = '__len',
      ),
      Param(
        type = 'const char *',
        name = '__modes',
      ),
    ],
  ),
  'open_memstream': Spec(
    return_type = 'FILE *',
    parameters = [
      Param(
        type = 'char **',
        name = '__bufloc',
      ),
      Param(
        type = 'size_t *',
        name = '__sizeloc',
      ),
    ],
  ),
  'setbuf': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
      Param(
        type = 'char *restrict',
        name = '__buf',
      ),
    ],
  ),
  'setvbuf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
      Param(
        type = 'char *restrict',
        name = '__buf',
      ),
      Param(
        type = 'int',
        name = '__modes',
      ),
      Param(
        type = 'size_t',
        name = '__n',
      ),
    ],
  ),
  'setbuffer': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
      Param(
        type = 'char *restrict',
        name = '__buf',
      ),
      Param(
        type = 'size_t',
        name = '__size',
      ),
    ],
  ),
  'setlinebuf': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'fprintf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
    ],
  ),
  'printf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
    ],
  ),
  'sprintf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'char *restrict',
        name = '__s',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
    ],
  ),
  'vfprintf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *restrict',
        name = '__s',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
      Param(
        type = '__gnuc_va_list',
        name = '__arg',
      ),
    ],
  ),
  'vprintf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
      Param(
        type = '__gnuc_va_list',
        name = '__arg',
      ),
    ],
  ),
  'vsprintf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'char *restrict',
        name = '__s',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
      Param(
        type = '__gnuc_va_list',
        name = '__arg',
      ),
    ],
  ),
  'snprintf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'char *restrict',
        name = '__s',
      ),
      Param(
        type = 'size_t',
        name = '__maxlen',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
    ],
  ),
  'vsnprintf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'char *restrict',
        name = '__s',
      ),
      Param(
        type = 'size_t',
        name = '__maxlen',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
      Param(
        type = '__gnuc_va_list',
        name = '__arg',
      ),
    ],
  ),
  'vdprintf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *restrict',
        name = '__fmt',
      ),
      Param(
        type = '__gnuc_va_list',
        name = '__arg',
      ),
    ],
  ),
  'dprintf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *restrict',
        name = '__fmt',
      ),
    ],
  ),
  'fscanf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
    ],
  ),
  'scanf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
    ],
  ),
  'sscanf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__s',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
    ],
  ),
  'fscanf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
    ],
  ),
  'scanf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
    ],
  ),
  'sscanf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__s',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
    ],
  ),
  'vfscanf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *restrict',
        name = '__s',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
      Param(
        type = '__gnuc_va_list',
        name = '__arg',
      ),
    ],
  ),
  'vscanf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
      Param(
        type = '__gnuc_va_list',
        name = '__arg',
      ),
    ],
  ),
  'vsscanf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__s',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
      Param(
        type = '__gnuc_va_list',
        name = '__arg',
      ),
    ],
  ),
  'vfscanf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *restrict',
        name = '__s',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
      Param(
        type = '__gnuc_va_list',
        name = '__arg',
      ),
    ],
  ),
  'vscanf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
      Param(
        type = '__gnuc_va_list',
        name = '__arg',
      ),
    ],
  ),
  'vsscanf': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__s',
      ),
      Param(
        type = 'const char *restrict',
        name = '__format',
      ),
      Param(
        type = '__gnuc_va_list',
        name = '__arg',
      ),
    ],
  ),
  'fgetc': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'getc': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'getchar': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  'getc_unlocked': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'getchar_unlocked': Spec(
    return_type = 'int',
    parameters = [
    ],
  ),
  'fgetc_unlocked': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'fputc': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__c',
      ),
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'putc': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__c',
      ),
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'putchar': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__c',
      ),
    ],
  ),
  'fputc_unlocked': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__c',
      ),
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'putc_unlocked': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__c',
      ),
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'putchar_unlocked': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__c',
      ),
    ],
  ),
  'getw': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'putw': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__w',
      ),
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'fgets': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'char *restrict',
        name = '__s',
      ),
      Param(
        type = 'int',
        name = '__n',
      ),
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
    ],
  ),
  'gets': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'char *',
        name = '__s',
      ),
    ],
  ),
  '__getdelim': Spec(
    return_type = '__ssize_t',
    parameters = [
      Param(
        type = 'char **restrict',
        name = '__lineptr',
      ),
      Param(
        type = 'size_t *restrict',
        name = '__n',
      ),
      Param(
        type = 'int',
        name = '__delimiter',
      ),
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
    ],
  ),
  'getdelim': Spec(
    return_type = '__ssize_t',
    parameters = [
      Param(
        type = 'char **restrict',
        name = '__lineptr',
      ),
      Param(
        type = 'size_t *restrict',
        name = '__n',
      ),
      Param(
        type = 'int',
        name = '__delimiter',
      ),
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
    ],
  ),
  'getline': Spec(
    return_type = '__ssize_t',
    parameters = [
      Param(
        type = 'char **restrict',
        name = '__lineptr',
      ),
      Param(
        type = 'size_t *restrict',
        name = '__n',
      ),
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
    ],
  ),
  'fputs': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__s',
      ),
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
    ],
  ),
  'puts': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__s',
      ),
    ],
  ),
  'ungetc': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__c',
      ),
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'fread': Spec(
    return_type = 'size_t',
    parameters = [
      Param(
        type = 'void *restrict',
        name = '__ptr',
      ),
      Param(
        type = 'size_t',
        name = '__size',
      ),
      Param(
        type = 'size_t',
        name = '__n',
      ),
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
    ],
  ),
  'fwrite': Spec(
    return_type = 'size_t',
    parameters = [
      Param(
        type = 'const void *restrict',
        name = '__ptr',
      ),
      Param(
        type = 'size_t',
        name = '__size',
      ),
      Param(
        type = 'size_t',
        name = '__n',
      ),
      Param(
        type = 'FILE *restrict',
        name = '__s',
      ),
    ],
  ),
  'fread_unlocked': Spec(
    return_type = 'size_t',
    parameters = [
      Param(
        type = 'void *restrict',
        name = '__ptr',
      ),
      Param(
        type = 'size_t',
        name = '__size',
      ),
      Param(
        type = 'size_t',
        name = '__n',
      ),
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
    ],
  ),
  'fwrite_unlocked': Spec(
    return_type = 'size_t',
    parameters = [
      Param(
        type = 'const void *restrict',
        name = '__ptr',
      ),
      Param(
        type = 'size_t',
        name = '__size',
      ),
      Param(
        type = 'size_t',
        name = '__n',
      ),
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
    ],
  ),
  'fseek': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
      Param(
        type = 'long',
        name = '__off',
      ),
      Param(
        type = 'int',
        name = '__whence',
      ),
    ],
  ),
  'ftell': Spec(
    return_type = 'long',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'rewind': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'fseeko': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
      Param(
        type = '__off_t',
        name = '__off',
      ),
      Param(
        type = 'int',
        name = '__whence',
      ),
    ],
  ),
  'ftello': Spec(
    return_type = '__off_t',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'fgetpos': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *restrict',
        name = '__stream',
      ),
      Param(
        type = 'fpos_t *restrict',
        name = '__pos',
      ),
    ],
  ),
  'fsetpos': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
      Param(
        type = 'const fpos_t *',
        name = '__pos',
      ),
    ],
  ),
  'clearerr': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'feof': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'ferror': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'clearerr_unlocked': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'feof_unlocked': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'ferror_unlocked': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'perror': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'const char *',
        name = '__s',
      ),
    ],
  ),
  'fileno': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'fileno_unlocked': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'popen': Spec(
    return_type = 'FILE *',
    parameters = [
      Param(
        type = 'const char *',
        name = '__command',
      ),
      Param(
        type = 'const char *',
        name = '__modes',
      ),
    ],
  ),
  'pclose': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'ctermid': Spec(
    return_type = 'char *',
    parameters = [
      Param(
        type = 'char *',
        name = '__s',
      ),
    ],
  ),
  'flockfile': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'ftrylockfile': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'funlockfile': Spec(
    return_type = 'void',
    parameters = [
      Param(
        type = 'FILE *',
        name = '__stream',
      ),
    ],
  ),
  'g_printf': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_fprintf': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'FILE *',
        name = 'file',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_sprintf': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
    ],
  ),
  'g_vprintf': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
    ],
  ),
  'g_vfprintf': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'FILE *',
        name = 'file',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
    ],
  ),
  'g_vsprintf': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gchar *',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
    ],
  ),
  'g_vasprintf': Spec(
    return_type = 'gint',
    parameters = [
      Param(
        type = 'gchar **',
        name = 'string',
      ),
      Param(
        type = 'const gchar *',
        name = 'format',
      ),
      Param(
        type = 'va_list',
        name = 'args',
      ),
    ],
  ),
  'stat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__file',
      ),
      Param(
        type = 'struct stat *restrict',
        name = '__buf',
      ),
    ],
  ),
  'fstat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'struct stat *',
        name = '__buf',
      ),
    ],
  ),
  'fstatat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *restrict',
        name = '__file',
      ),
      Param(
        type = 'struct stat *restrict',
        name = '__buf',
      ),
      Param(
        type = 'int',
        name = '__flag',
      ),
    ],
  ),
  'lstat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *restrict',
        name = '__file',
      ),
      Param(
        type = 'struct stat *restrict',
        name = '__buf',
      ),
    ],
  ),
  'chmod': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__file',
      ),
      Param(
        type = '__mode_t',
        name = '__mode',
      ),
    ],
  ),
  'lchmod': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__file',
      ),
      Param(
        type = '__mode_t',
        name = '__mode',
      ),
    ],
  ),
  'fchmod': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = '__mode_t',
        name = '__mode',
      ),
    ],
  ),
  'fchmodat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *',
        name = '__file',
      ),
      Param(
        type = '__mode_t',
        name = '__mode',
      ),
      Param(
        type = 'int',
        name = '__flag',
      ),
    ],
  ),
  'umask': Spec(
    return_type = '__mode_t',
    parameters = [
      Param(
        type = '__mode_t',
        name = '__mask',
      ),
    ],
  ),
  'mkdir': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__path',
      ),
      Param(
        type = '__mode_t',
        name = '__mode',
      ),
    ],
  ),
  'mkdirat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *',
        name = '__path',
      ),
      Param(
        type = '__mode_t',
        name = '__mode',
      ),
    ],
  ),
  'mknod': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__path',
      ),
      Param(
        type = '__mode_t',
        name = '__mode',
      ),
      Param(
        type = '__dev_t',
        name = '__dev',
      ),
    ],
  ),
  'mknodat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *',
        name = '__path',
      ),
      Param(
        type = '__mode_t',
        name = '__mode',
      ),
      Param(
        type = '__dev_t',
        name = '__dev',
      ),
    ],
  ),
  'mkfifo': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const char *',
        name = '__path',
      ),
      Param(
        type = '__mode_t',
        name = '__mode',
      ),
    ],
  ),
  'mkfifoat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *',
        name = '__path',
      ),
      Param(
        type = '__mode_t',
        name = '__mode',
      ),
    ],
  ),
  'utimensat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *',
        name = '__path',
      ),
      Param(
        type = 'const struct timespec [2]',
        name = '__times',
      ),
      Param(
        type = 'int',
        name = '__flags',
      ),
    ],
  ),
  'futimens': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const struct timespec [2]',
        name = '__times',
      ),
    ],
  ),
  '__fxstat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__ver',
      ),
      Param(
        type = 'int',
        name = '__fildes',
      ),
      Param(
        type = 'struct stat *',
        name = '__stat_buf',
      ),
    ],
  ),
  '__xstat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__ver',
      ),
      Param(
        type = 'const char *',
        name = '__filename',
      ),
      Param(
        type = 'struct stat *',
        name = '__stat_buf',
      ),
    ],
  ),
  '__lxstat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__ver',
      ),
      Param(
        type = 'const char *',
        name = '__filename',
      ),
      Param(
        type = 'struct stat *',
        name = '__stat_buf',
      ),
    ],
  ),
  '__fxstatat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__ver',
      ),
      Param(
        type = 'int',
        name = '__fildes',
      ),
      Param(
        type = 'const char *',
        name = '__filename',
      ),
      Param(
        type = 'struct stat *',
        name = '__stat_buf',
      ),
      Param(
        type = 'int',
        name = '__flag',
      ),
    ],
  ),
  '__xmknod': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__ver',
      ),
      Param(
        type = 'const char *',
        name = '__path',
      ),
      Param(
        type = '__mode_t',
        name = '__mode',
      ),
      Param(
        type = '__dev_t *',
        name = '__dev',
      ),
    ],
  ),
  '__xmknodat': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'int',
        name = '__ver',
      ),
      Param(
        type = 'int',
        name = '__fd',
      ),
      Param(
        type = 'const char *',
        name = '__path',
      ),
      Param(
        type = '__mode_t',
        name = '__mode',
      ),
      Param(
        type = '__dev_t *',
        name = '__dev',
      ),
    ],
  ),
  'g_access': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'filename',
      ),
      Param(
        type = 'int',
        name = 'mode',
      ),
    ],
  ),
  'g_chdir': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'path',
      ),
    ],
  ),
  'g_unlink': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'filename',
      ),
    ],
  ),
  'g_rmdir': Spec(
    return_type = 'int',
    parameters = [
      Param(
        type = 'const gchar *',
        name = 'filename',
      ),
    ],
  ),
  '__builtin_bswap32': Spec(
    return_type = 'uint32_t',
    parameters = [
      Param(
        type = 'uint32_t',
        name = 'x',
      ),
    ],
  ),
  '__builtin_bswap64': Spec(
    return_type = 'uint64_t',
    parameters = [
      Param(
        type = 'uint64_t',
        name = 'x',
      ),
    ],
  ),
}