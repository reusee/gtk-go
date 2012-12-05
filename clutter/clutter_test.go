package clutter

import (
  "testing"
  "os"
)

func TestTest(t *testing.T) {
  Init(os.Args)

  stage := StageNew()
  stage.SetBackgroundColor(ColorNew(0, 0, 0, 0))
  stage.SetSize(500, 600)

  actor := ActorNew()
  stage.AddChild(actor)

  imageBuf, _ := PixbufNewFromFile("a.jpg")

  image := ImageNew()
  pixelFormat := COGL_PIXEL_FORMAT_RGB_888
  if imageBuf.GetHasAlpha() {
    pixelFormat = COGL_PIXEL_FORMAT_RGBA_8888
  }
  image.SetData(imageBuf.GetPixels(),
    pixelFormat,
    uint(imageBuf.GetWidth()),
    uint(imageBuf.GetHeight()),
    uint(imageBuf.GetRowstride()))
  actor.SetContent(image)
  actor.Show()

  stage.Connect("destroy", func() { MainQuit() })
  stage.Show()

  Main()
}
