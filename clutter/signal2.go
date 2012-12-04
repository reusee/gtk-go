package clutter

import "C"
import (
  "unsafe"
)

//export CallCallback
func CallCallback(cb unsafe.Pointer) {
  callback := (*Callback)(cb)
  (*(callback.fun))()
  delete(_callbacks, callback.id)
}
