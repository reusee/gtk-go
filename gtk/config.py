Strip_prefix_from_const = True

# skip symbols

Compile_error_c_symbols = [
  'g_clear_object',
  'g_io_module_query',
  'g_io_module_load',
  'g_io_module_unload',

  'gdk_pixbuf_gettext',

  'gdk_pixdata_serialize',
  'gdk_pixdata_from_pixbuf',
  'gdk_pixdata_to_csource',
  'gdk_pixbuf_from_pixdata',

  'GdkPixdata',
]

Not_exported_c_macros = [
  'G_VALUE_COLLECT_FORMAT_MAX_LENGTH',

  'GDK_PIXDATA_DUMP_CTYPES',
  'GDK_PIXDATA_DUMP_MACROS',
  'GDK_PIXDATA_DUMP_CONST',
  'GDK_PIXDATA_ENCODING_RLE',
  'GDK_PIXDATA_SAMPLE_WIDTH_MASK',
  'GDK_PIXDATA_DUMP_PIXDATA_STRUCT',
  'GDK_PIXDATA_DUMP_PIXDATA_STREAM',
  'GDK_PIXBUF_MAGIC_NUMBER',
  'GDK_PIXDATA_HEADER_LENGTH',
  'GDK_PIXDATA_DUMP_RLE_DECODER',
  'GDK_PIXDATA_DUMP_STATIC',
  'GDK_PIXDATA_ENCODING_RAW',
  'GDK_PIXDATA_COLOR_TYPE_MASK',
  'GDK_PIXDATA_COLOR_TYPE_RGBA',
  'GDK_PIXDATA_COLOR_TYPE_RGB',
  'GDK_PIXDATA_SAMPLE_WIDTH_8',
  'GDK_PIXDATA_DUMP_GTYPES',
  'GDK_PIXDATA_ENCODING_MASK',

]

Manually_implement_c_symbols = [
  'gtk_init',
  'gtk_init_check',
  'gtk_init_with_args',
  'gtk_parse_args',
]

Deprecated_c_symbols = [
  'g_object_compat_control',
  'gtk_color_selection_palette_from_string',
  'gtk_color_selection_get_current_alpha',
  'gtk_color_selection_get_current_rgba',
  'gtk_color_selection_get_has_opacity_control',
  'gtk_color_selection_get_has_palette',
  'gtk_color_selection_get_previous_alpha',
  'gtk_color_selection_get_previous_rgba',
  'gtk_color_selection_is_adjusting',
  'gtk_color_selection_set_current_alpha',
  'gtk_color_selection_set_current_rgba',
  'gtk_color_selection_set_has_opacity_control',
  'gtk_color_selection_set_has_palette',
  'gtk_color_selection_set_previous_alpha',
  'gtk_color_selection_set_previous_rgba',
  'gtk_color_selection_dialog_new',
  'gtk_color_selection_dialog_get_color_selection',
  'gtk_color_selection_palette_to_string',
  'gtk_color_selection_new',
  'gtk_hsv_get_color',
  'gtk_hsv_get_metrics',
  'gtk_hsv_is_adjusting',
  'gtk_hsv_set_color',
  'gtk_hsv_set_metrics',
  'gtk_style_get_style_property',
  'gtk_hsv_new',
  'gtk_style_get_valist',
]

# name conflict

Conflict_function_names = [
  'SocketNew',
  'ApplicationNew',
  'MenuNew',
  'MenuItemNew',
  'MountOperationNew',
  'PlugNew',
]

Conflict_const_names = [
  'STATE_SELECTED',
  'STATE_ACTIVE',
  'STATE_FOCUSED',
]

Conflict_type_names = [
    'Socket',
    'Application',
    'Menu',
    'MenuItem',
    'Misc',
    'MountOperation',
    'Plug',
    'Settings',
    'Object',
    'SocketClass',
    'ActionEntry',
    'ApplicationClass',
    'ApplicationPrivate',
    'MiscClass',
    'MountOperationClass',
    'MountOperationPrivate',
    'PlugClass',
    'SettingsClass',
    'SettingsPrivate',
    'SocketPrivate',
    'ObjectClass',
    'AppLaunchContext',
    'Action',
    'ActionGroup',
    'Image',
    'Table',
    'Window',
    'Value',
]
