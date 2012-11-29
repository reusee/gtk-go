package glib

import (
  "testing"
  "fmt"
  "time"
  "os"
  "os/user"
)

func TestStringMapping(t *testing.T) {
  cwd, _ := os.Getwd()
  if GetCurrentDir() != cwd {
    t.Fail()
  }
  usr, _ := user.Current()
  if GetHomeDir() != usr.HomeDir {
    t.Fail()
  }
  hostname, _ := os.Hostname()
  if GetHostName() != hostname {
    t.Fail()
  }
  if FilenameDisplayBasename("foo/bar/baz") != "baz" {
    t.Fail()
  }

  if AsciiStrcasecmp("foo", "bar") <= 0 {
    t.Fail()
  }
  if AsciiStrcasecmp("bar", "foo") >= 0 {
    t.Fail()
  }
}

func TestConstructor(t *testing.T) {
  DateNew()
  KeyFileNew()
}

func TestBool(t *testing.T) {
  if StrHasSuffix("foo", "oo") != true {
    t.Fail()
  }
  if StrHasSuffix("foo", "xx") != false {
    t.Fail()
  }
  if StrHasPrefix("foo", "fo") != true {
    t.Fail()
  }
  if StrHasPrefix("foo", "bar") != false {
    t.Fail()
  }
}

//func TestBase64(t *testing.T) {
//  data := []byte("hello")
//  expected := "aGVsbG8="
//  l := uint64(len(data))
//  if expected != Base64Encode(data, l) {
//    t.Fail()
//  }
//  if !bytes.Equal(data, Base64Decode(expected, &l)) {
//    t.Fail()
//  }
//}

func TestRecordConstruct(t *testing.T) {
  AsyncQueueNew()
  TimerNew()
}

func TestDateTime(t *testing.T) {
  now := DateTimeNewNowLocal()
  y, m, d := now.GetYmd()
  expectedNow := time.Now()
  if fmt.Sprintf("%d-%d-%d", y, m, d) != fmt.Sprintf("%d-%d-%d",
    expectedNow.Year(), expectedNow.Month(), expectedNow.Day()) {
    t.Fail()
  }
}

func TestCallerAllocatesOutParam(t *testing.T) {
  ok, timeVal := TimeValFromIso8601("1994-11-05T08:15:30-05:00")
  if !ok {
    t.Fail()
  }
  dateTime := DateTimeNewFromTimevalLocal((*TimeVal)(timeVal))
  y, m, d := dateTime.GetYmd()
  if fmt.Sprintf("%d-%d-%d", y, m, d) != "1994-11-5" {
    t.Fail()
  }
}

func TestParameterTypeMapping(t *testing.T) {
  year := 1987
  dateTime := DateTimeNewLocal(year, 7, 14, 18, 20, 35)
  y, m, d := dateTime.GetYmd()
  if y != 1987 || m != 7 || d != 14 {
    t.Fail()
  }
}
