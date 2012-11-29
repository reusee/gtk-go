package gtk

// #cgo pkg-config: gtk+-3.0 gobject-2.0
// #include <gtk/gtkx.h>
// #include <stdlib.h>
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
  C.gtk_init(&argc, &p_c_args)
  for i, _ := range c_args {
    C.free(unsafe.Pointer(c_args[i]))
  }
}
