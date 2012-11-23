package glib

import (
  "testing"
  "fmt"
  "bytes"
)

func TestStringMapping(t *testing.T) {
  fmt.Printf("current dir%s\n", GetCurrentDir())
  fmt.Printf("codeset %s\n", GetCodeset())
  fmt.Printf("home dir %s\n", GetHomeDir())
  fmt.Printf("host name %s\n", GetHostName())
  fmt.Printf("real name %s\n", GetRealName())
  fmt.Printf("tmp dir %s\n", GetTmpDir())
  fmt.Printf("user cache dir %s\n", GetUserCacheDir())
  fmt.Printf("user config dir %s\n", GetUserConfigDir())
  fmt.Printf("user data dir %s\n", GetUserDataDir())
  fmt.Printf("user name %s\n", GetUserName())
  fmt.Printf("user runtime dir %s\n", GetUserRuntimeDir())

  fmt.Printf("%s\n", FilenameDisplayBasename("foo/bar"))
  fmt.Printf("%v\n", AsciiStrcasecmp("foo", "bar"))
  fmt.Printf("%v\n", AsciiStrcasecmp("bar", "foo"))
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

func TestBase64(t *testing.T) {
  data := []byte("hello")
  expected := "aGVsbG8="
  l := uint64(len(data))
  if expected != Base64Encode(data, l) {
    t.Fail()
  }
  if !bytes.Equal(data, Base64Decode(expected, &l)) {
    t.Fail()
  }
}

func TestAsyncQueue(t *testing.T) {
  AsyncQueueNew()
}
