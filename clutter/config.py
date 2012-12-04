Strip_prefix_from_const = False

Compile_error_c_symbols = [
    'CLUTTER_VERSION',

    'g_clear_object',
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

]
