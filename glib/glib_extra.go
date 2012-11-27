package glib

// #cgo pkg-config: glib-2.0 gobject-2.0
// #include <glib-object.h>
// #include <glib/gstdio.h>
// #include <glib-unix.h>
// #include <glib.h>
/*
const gdouble _G_SQRT2         = G_SQRT2;
const gdouble _G_PI_4          = G_PI_4;
const gdouble _G_PI_2          = G_PI_2;
const gdouble _G_PI            = G_PI;
const char* _G_LOG_DOMAIN    = G_LOG_DOMAIN;
const double _G_LOG_2_BASE_10 = G_LOG_2_BASE_10;
const double _G_LN2           = G_LN2;
const double _G_LN10          = G_LN10;
const gdouble _G_E             = G_E;
*/
import "C"

var (
  SQRT2         = C._G_SQRT2
  PI_4          = C._G_PI_4
  PI_2          = C._G_PI_2
  PI            = C._G_PI
  LOG_DOMAIN    = C._G_LOG_DOMAIN
  LOG_2_BASE_10 = C._G_LOG_2_BASE_10
  LN2           = C._G_LN2
  LN10          = C._G_LN10
  E             = C._G_E
)
