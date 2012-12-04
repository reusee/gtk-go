package clutter

// #cgo pkg-config: gtk+-3.0 gobject-2.0
// #include <gtk/gtkx.h>
// #include <stdlib.h>
/*
extern void CallCallback(void*);

void call_callback(void* object, void* cb) {
  CallCallback(cb);
}
void _signal_connect(void* object, char* signal, void* cb) {
  g_signal_connect(G_OBJECT(object), 
    signal,
    G_CALLBACK(call_callback),
    cb);
}
*/
import "C"
import (
  "unsafe"
)

func (self *GObjectObject) Connect(signal string, fun func()) {
  cgo_signal := C.CString(signal)
  defer C.free(unsafe.Pointer(cgo_signal))

  callback := &Callback{uintptr(unsafe.Pointer(&fun)), &fun}
  _callbacks[callback.id] = callback

  C._signal_connect(self.GetGObject(),
    cgo_signal, unsafe.Pointer(callback))
}

var _callbacks map[uintptr]*Callback

func init() {
  _callbacks = make(map[uintptr]*Callback)
}

type Callback struct {
  id uintptr
  fun *func()
}
