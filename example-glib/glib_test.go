package glib

import (
  "testing"
  "fmt"
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
}
