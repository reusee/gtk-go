package clutter

import (
  "testing"
  "os"
)

func TestTest(t *testing.T) {
  Init(os.Args)

  stage := StageNew()
  //stage.SetBackgroundColor(ColorNew(0, 0, 0, 0))
  stage.SetSize(500, 600)

  actor := ActorNew()
  stage.AddChild(actor)

  imageBuf, err := PixbufNewFromFile("a.jpg")
  if err != nil {
    t.Fatal(err)
  }

  image := ImageNew()
  pixelFormat := COGL_PIXEL_FORMAT_RGB_888
  if imageBuf.GetHasAlpha() {
    pixelFormat = COGL_PIXEL_FORMAT_RGBA_8888
  }
  ok, err := image.SetData(imageBuf.GetPixels(),
    pixelFormat,
    uint(imageBuf.GetWidth()),
    uint(imageBuf.GetHeight()),
    uint(imageBuf.GetRowstride()))
  if !ok {
    t.Fail()
  }
  if err != nil {
    t.Fatal(err)
  }
  actor.SetContentScalingFilters(
    CLUTTER_SCALING_FILTER_TRILINEAR,
    CLUTTER_SCALING_FILTER_LINEAR)
  actor.SetContent(image)
  actor.SetPosition(1, 1)

  info := TextNewWithText("monaco", "hello, world!")
  stage.AddChild(info)
  info.SetPosition(0, 0)

  stage.Connect("destroy", func() { MainQuit() })
  stage.Show()

  Main()
}
