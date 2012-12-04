Introduction
------------

This package provides full GTK+ 3.0 support for golang

Install
-------

```go get github.com/reusee/gtk-go/gtk```

Demo
----

```
package main

import (
  "github.com/reusee/gtk-go/gtk"
  "os"
)

func main() {
  gtk.Init(os.Args)
  window := gtk.WindowNew(gtk.WINDOW_TOPLEVEL)
  window.Connect("destroy", func() { gtk.MainQuit() })
  button := gtk.ButtonNewWithLabel("Hello, world!")
  window.Add(button)
  button.Connect("clicked", func() {
    println("clicked")
  })
  window.ShowAll()
  gtk.Main()
}
```
