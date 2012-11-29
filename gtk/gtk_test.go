package gtk

import (
  "testing"
  "fmt"
  "time"
  "os"
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
