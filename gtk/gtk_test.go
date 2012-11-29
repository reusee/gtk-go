package gtk

import (
  "testing"
  "fmt"
  "time"
  "os"
  "unsafe"
)

func TestBasicFunc(t *testing.T) {
  Init(os.Args)
  True()
  False()
  fmt.Printf("gtk %v.%v.%v\n", GetMajorVersion(), GetMinorVersion(), GetMicroVersion())
  go func() {
    <-time.After(time.Millisecond * 500)
    MainQuit()
  }()
  Main()
  fmt.Printf("gtk main quit\n")
}

func TestBasicWindow(t *testing.T) {
  Init(os.Args)
  window := WindowNew(WINDOW_TOPLEVEL)
  (*Widget)(unsafe.Pointer(window)).Show()
  go func() {
    <-time.After(time.Millisecond * 500)
    MainQuit()
  }()
  Main()
}
