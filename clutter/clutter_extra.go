package clutter

// #cgo pkg-config: clutter-1.0 gobject-2.0 gtk+-3.0
// #include <string.h>
// #include <glib-object.h>
// #include <glib/gstdio.h>
// #include <glib-unix.h>
// #include <clutter/clutter.h>
import "C"
import (
  "unsafe"
)

func Init(args []string) {
  argc := C.int(len(args))
  c_args := make([]*C.char, argc)
  for i, arg := range args {
    c_args[i] = C.CString(arg)
  }
  p_c_args := &c_args[0]
  C.clutter_init(&argc, &p_c_args)
  for i, _ := range c_args {
    C.free(unsafe.Pointer(c_args[i]))
  }
}
