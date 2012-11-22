package gtk

import (
  "testing"
  "fmt"
  "time"
)

func TestGtk(t *testing.T) {
  Init(nil, nil)
  True()
  False()
  fmt.Printf("gtk %v.%v.%v\n", GetMajorVersion(), GetMinorVersion(), GetMicroVersion())
  go func() {
    <-time.After(time.Second * 1)
    MainQuit()
  }()
  Main()
  fmt.Printf("gtk main quit\n")
}
