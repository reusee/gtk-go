package gtk

import (
  "testing"
  "fmt"
  "time"
)

func TestBasicFunc(t *testing.T) {
  Init(nil, nil)
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
