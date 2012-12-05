Strip_prefix_from_const = False

Compile_error_c_symbols = [
  'CLUTTER_VERSION',

  'g_clear_object',
  'gdk_pixbuf_gettext',

  'gdk_pixdata_serialize',
  'gdk_pixdata_from_pixbuf',
  'gdk_pixdata_to_csource',
  'gdk_pixbuf_from_pixdata',

  'GdkPixdata',

  'cogl_clutter_check_extension_CLUTTER',
  'cogl_clutter_winsys_has_feature_CLUTTER',
  'cogl_clutter_winsys_xlib_get_visual_info_CLUTTER',
  'cogl_onscreen_clutter_backend_set_size_CLUTTER',
  'cogl_xlib_renderer_add_filter_EXP',
  'cogl_xlib_renderer_get_display_EXP',
  'cogl_xlib_renderer_get_foreign_display_EXP',
  'cogl_xlib_renderer_handle_event_EXP',
  'cogl_xlib_renderer_remove_filter_EXP',
  'cogl_xlib_renderer_set_event_retrieval_enabled',
  'cogl_xlib_renderer_set_foreign_display_EXP',
]

Excluded_interfaces = [
  "Gio.Icon"
]

Conflict_type_names = [
  'Object',
  'Action',
  'Image',
  'Text',
  'ObjectClass',
  'Value',
  'Rectangle',
  'Color',
  'Path',
  'Texture',
]

Not_exported_c_macros = [
  'CLUTTER_WINDOWING_GDK',
  'CLUTTER_X11_XINPUT_KEY_PRESS_EVENT',
  'CLUTTER_X11_XINPUT_LAST_EVENT',
  'CLUTTER_X11_XINPUT_KEY_RELEASE_EVENT',
  'CLUTTER_INPUT_GDK',
  'CLUTTER_X11_XINPUT_MOTION_NOTIFY_EVENT',
  'CLUTTER_X11_FILTER_TRANSLATE',
  'CLUTTER_X11_FILTER_REMOVE',
  'CLUTTER_X11_XINPUT_BUTTON_PRESS_EVENT',
  'CLUTTER_X11_XINPUT_BUTTON_RELEASE_EVENT',
  'CLUTTER_X11_FILTER_CONTINUE',

  'G_VALUE_COLLECT_FORMAT_MAX_LENGTH',

  'GDK_PIXDATA_ENCODING_RLE',
  'GDK_PIXDATA_ENCODING_RAW',
  'GDK_PIXBUF_MAGIC_NUMBER',
  'GDK_PIXDATA_SAMPLE_WIDTH_8',
  'GDK_PIXDATA_DUMP_PIXDATA_STREAM',
  'GDK_PIXDATA_HEADER_LENGTH',
  'GDK_PIXDATA_COLOR_TYPE_RGBA',
  'GDK_PIXDATA_COLOR_TYPE_MASK',
  'GDK_PIXDATA_COLOR_TYPE_RGB',
  'GDK_PIXDATA_DUMP_MACROS',
  'GDK_PIXDATA_DUMP_STATIC',
  'GDK_PIXDATA_DUMP_CTYPES',
  'GDK_PIXDATA_DUMP_RLE_DECODER',
  'GDK_PIXDATA_ENCODING_MASK',
  'GDK_PIXDATA_DUMP_CONST',
  'GDK_PIXDATA_SAMPLE_WIDTH_MASK',
  'GDK_PIXDATA_DUMP_PIXDATA_STRUCT',
  'GDK_PIXDATA_DUMP_GTYPES',

]

Deprecated_c_symbols = [
  'clutter_rectangle_new_with_color',
  'clutter_rectangle_set_border_color',
  'clutter_rectangle_set_color',
  'clutter_rectangle_set_border_width',
  'clutter_behaviour_ellipse_set_angle_start',
  'clutter_behaviour_ellipse_set_direction',
  'clutter_behaviour_rotate_get_bounds',
  'clutter_behaviour_ellipse_get_angle_tilt',
  'clutter_behaviour_ellipse_set_tilt',
  'clutter_behaviour_ellipse_get_tilt',
  'clutter_behaviour_ellipse_get_angle_end',
  'clutter_behaviour_rotate_get_direction',
  'clutter_rectangle_new',
  'clutter_behaviour_rotate_set_center',
  'clutter_behaviour_rotate_set_axis',
  'clutter_behaviour_ellipse_new',
  'clutter_behaviour_ellipse_get_direction',
  'clutter_behaviour_ellipse_get_width',
  'clutter_behaviour_rotate_new',
  'clutter_behaviour_ellipse_get_center',
  'clutter_behaviour_rotate_set_direction',
  'clutter_behaviour_rotate_set_bounds',
  'clutter_behaviour_ellipse_set_height',
  'clutter_behaviour_ellipse_set_angle_end',
  'clutter_behaviour_ellipse_set_angle_tilt',
  'clutter_behaviour_rotate_get_axis',
  'clutter_rectangle_get_border_width',
  'clutter_behaviour_ellipse_get_height',
  'clutter_behaviour_ellipse_set_center',
  'clutter_behaviour_rotate_get_center',
  'clutter_shader_error_quark',
  'clutter_rectangle_get_border_color',
  'clutter_rectangle_get_color',
  'clutter_behaviour_ellipse_get_angle_start',
  'clutter_behaviour_ellipse_set_width',

  'g_object_compat_control',

  'cogl_program_uniform_int',
  'cogl_program_uniform_matrix',
]
