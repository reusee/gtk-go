// gcc builtins
#include <stdint.h>
uint32_t __builtin_bswap32 (uint32_t x);
uint64_t __builtin_bswap64 (uint64_t x);

#include <clutter/clutter.h>

#include <gdk-pixbuf/gdk-pixdata.h>
#include <gdk-pixbuf/gdk-pixbuf-animation.h>
#include <gdk-pixbuf/gdk-pixbuf-loader.h>
#include <gdk-pixbuf/gdk-pixbuf-core.h>
#include <gdk-pixbuf/gdk-pixbuf-marshal.h>
#include <gdk-pixbuf/gdk-pixbuf-enum-types.h>
#include <gdk-pixbuf/gdk-pixbuf-simple-anim.h>
#include <gdk-pixbuf/gdk-pixbuf-features.h>
#include <gdk-pixbuf/gdk-pixbuf-transform.h>
#include <gdk-pixbuf/gdk-pixbuf.h>
#include <gdk-pixbuf/gdk-pixbuf-io.h>

#include <cogl/cogl.h>
