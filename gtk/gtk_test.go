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

func TestBasicWindow(t *testing.T) {
  Init(os.Args)
  window := WindowNew(WINDOW_TOPLEVEL)

  button := ButtonNewWithLabel("Hello, world!")
  window.Add(button)
  button.Show()

  window.Show()
  go func() {
    ticker := time.NewTicker(time.Millisecond * 50)
    countDown := time.After(time.Millisecond * 5000)
    for {
      select {
      case <-countDown:
        MainQuit()
      case <-ticker.C:
        button.SetLabel(fmt.Sprintf("%d", time.Now().UnixNano()))
      }
    }
  }()
  Main()
}
