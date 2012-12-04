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
  stage.Show()

  canvas := ToCanvas(CanvasNew().GetGObject())
  canvas.SetSize(300, 300)

  actor := ActorNew()
  actor.SetContent(canvas)
  actor.SetContentGravity(CLUTTER_CONTENT_GRAVITY_CENTER)
  actor.SetContentScalingFilters(CLUTTER_SCALING_FILTER_TRILINEAR, CLUTTER_SCALING_FILTER_LINEAR)
  actor.SetPivotPoint(0.5, 0.5)

  stage.AddChild(actor)

  stage.Connect("destroy", func() { MainQuit() })

  Main()
}
