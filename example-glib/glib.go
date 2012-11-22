package glib

// #cgo pkg-config: glib-2.0 gobject-2.0
// #include <glib-object.h>
// #include <glib/gstdio.h>
// #include <glib-unix.h>
// #include <glib.h>
/*
typedef long double longdouble;
typedef const gchar** _const_pp_gchar;
typedef GHook* _p_GHook;
typedef const gchar* _const_p_gchar;
typedef GPatternSpec* _p_GPatternSpec;
typedef glong* _p_glong;
typedef guchar* _p_guchar;
typedef gunichar* _p_gunichar;
typedef char* _p_char;
typedef char*** _ppp_char;
typedef const char** _const_pp_char;
typedef gchar** _pp_gchar;
typedef FILE* _p_FILE;
typedef gchar* _p_gchar;
typedef const guchar* _const_p_guchar;
typedef GError** _pp_GError;
typedef GHookList* _p_GHookList;
typedef GIOChannel* _p_GIOChannel;
typedef GHashTable* _p_GHashTable;
typedef GArray* _p_GArray;
typedef GPid* _p_GPid;
typedef const GDate* _const_p_GDate;
typedef gunichar2* _p_gunichar2;
typedef GThread* _p_GThread;
typedef GPollFD* _p_GPollFD;
typedef GBytes* _p_GBytes;
typedef const GError* _const_p_GError;
typedef gboolean* _p_gboolean;
typedef GData** _pp_GData;
typedef GTestSuite* _p_GTestSuite;
typedef gchar*** _ppp_gchar;
typedef const gunichar2* _const_p_gunichar2;
typedef GPtrArray* _p_GPtrArray;
typedef gint* _p_gint;
typedef guint* _p_guint;
typedef int* _p_int;
typedef GTestCase* _p_GTestCase;
typedef GSequenceIter* _p_GSequenceIter;
typedef GVariant* _p_GVariant;
typedef const gchar*** _const_ppp_gchar;
typedef GDebugKey* _p_GDebugKey;
typedef const gunichar* _const_p_gunichar;
typedef GMainContext* _p_GMainContext;
typedef gsize* _p_gsize;
typedef GTrashStack** _pp_GTrashStack;
typedef guint8* _p_guint8;
typedef const GVariantType* _const_p_GVariantType;
typedef GTimeVal* _p_GTimeVal;
typedef GDestroyNotify* _p_GDestroyNotify;
typedef GSource* _p_GSource;
typedef GError* _p_GError;
typedef GMemVTable* _p_GMemVTable;
typedef const char* _const_p_char;
typedef GString* _p_GString;
typedef GSourceFuncs* _p_GSourceFuncs;
typedef gpointer* _p_gpointer;
typedef GByteArray* _p_GByteArray;
*/
import "C"

func Access(filename C._const_p_gchar, mode C.int) C.int {
	return C.g_access(filename, mode)
}

func ArrayFree(array C._p_GArray, free_segment C.gboolean) C._p_gchar {
	return C.g_array_free(array, free_segment)
}

func ArrayGetElementSize(array C._p_GArray) C.guint {
	return C.g_array_get_element_size(array)
}

func ArraySetClearFunc(array C._p_GArray, clear_func C.GDestroyNotify) {
	C.g_array_set_clear_func(array, clear_func)
}

func ArrayUnref(array C._p_GArray) {
	C.g_array_unref(array)
}

func AsciiDigitValue(c C.gchar) C.gint {
	return C.g_ascii_digit_value(c)
}

func AsciiDtostr(buffer C._p_gchar, buf_len C.gint, d C.gdouble) C._p_gchar {
	return C.g_ascii_dtostr(buffer, buf_len, d)
}

func AsciiFormatd(buffer C._p_gchar, buf_len C.gint, format C._const_p_gchar, d C.gdouble) C._p_gchar {
	return C.g_ascii_formatd(buffer, buf_len, format, d)
}

func AsciiStrcasecmp(s1 C._const_p_gchar, s2 C._const_p_gchar) C.gint {
	return C.g_ascii_strcasecmp(s1, s2)
}

func AsciiStrdown(str C._const_p_gchar, _len C.gssize) C._p_gchar {
	return C.g_ascii_strdown(str, _len)
}

func AsciiStrncasecmp(s1 C._const_p_gchar, s2 C._const_p_gchar, n C.gsize) C.gint {
	return C.g_ascii_strncasecmp(s1, s2, n)
}

func AsciiStrtod(nptr C._const_p_gchar, endptr C._pp_gchar) C.gdouble {
	return C.g_ascii_strtod(nptr, endptr)
}

func AsciiStrtoll(nptr C._const_p_gchar, endptr C._pp_gchar, base C.guint) C.gint64 {
	return C.g_ascii_strtoll(nptr, endptr, base)
}

func AsciiStrtoull(nptr C._const_p_gchar, endptr C._pp_gchar, base C.guint) C.guint64 {
	return C.g_ascii_strtoull(nptr, endptr, base)
}

func AsciiStrup(str C._const_p_gchar, _len C.gssize) C._p_gchar {
	return C.g_ascii_strup(str, _len)
}

func AsciiTolower(c C.gchar) C.gchar {
	return C.g_ascii_tolower(c)
}

func AsciiToupper(c C.gchar) C.gchar {
	return C.g_ascii_toupper(c)
}

func AsciiXdigitValue(c C.gchar) C.gint {
	return C.g_ascii_xdigit_value(c)
}

//Skipped g_assert_warning

func AssertionMessage(domain C._const_p_char, file C._const_p_char, line C.int, _func C._const_p_char, message C._const_p_char) {
	C.g_assertion_message(domain, file, line, _func, message)
}

//TODO long double g_assertion_message_cmpnum

func AssertionMessageCmpstr(domain C._const_p_char, file C._const_p_char, line C.int, _func C._const_p_char, expr C._const_p_char, arg1 C._const_p_char, cmp C._const_p_char, arg2 C._const_p_char) {
	C.g_assertion_message_cmpstr(domain, file, line, _func, expr, arg1, cmp, arg2)
}

func AssertionMessageError(domain C._const_p_char, file C._const_p_char, line C.int, _func C._const_p_char, expr C._const_p_char, error C._const_p_GError, error_domain C.GQuark, error_code C.int) {
	C.g_assertion_message_error(domain, file, line, _func, expr, error, error_domain, error_code)
}

func AssertionMessageExpr(domain C._const_p_char, file C._const_p_char, line C.int, _func C._const_p_char, expr C._const_p_char) {
	C.g_assertion_message_expr(domain, file, line, _func, expr)
}

//Deprecated g_atexit

//Skipped g_atomic_int_add

//Skipped g_atomic_int_and

//Skipped g_atomic_int_compare_and_exchange

//Skipped g_atomic_int_dec_and_test

//Deprecated g_atomic_int_exchange_and_add

//Skipped g_atomic_int_get

//Skipped g_atomic_int_inc

//Skipped g_atomic_int_or

//Skipped g_atomic_int_set

//Skipped g_atomic_int_xor

//Skipped g_atomic_pointer_add

//Skipped g_atomic_pointer_and

//Skipped g_atomic_pointer_compare_and_exchange

//Skipped g_atomic_pointer_get

//Skipped g_atomic_pointer_or

//Skipped g_atomic_pointer_set

//Skipped g_atomic_pointer_xor

func Base64Decode(text C._const_p_gchar, out_len C._p_gsize) C._p_guchar {
	return C.g_base64_decode(text, out_len)
}

func Base64DecodeInplace(text C._p_gchar, out_len C._p_gsize) C._p_guchar {
	return C.g_base64_decode_inplace(text, out_len)
}

func Base64DecodeStep(in C._p_gchar, _len C.gsize, out C._p_guchar, state C._p_gint, save C._p_guint) C.gsize {
	return C.g_base64_decode_step(in, _len, out, state, save)
}

func Base64Encode(data C._p_guchar, _len C.gsize) C._p_gchar {
	return C.g_base64_encode(data, _len)
}

func Base64EncodeClose(break_lines C.gboolean, out C._p_gchar, state C._p_gint, save C._p_gint) C.gsize {
	return C.g_base64_encode_close(break_lines, out, state, save)
}

func Base64EncodeStep(in C._p_guchar, _len C.gsize, break_lines C.gboolean, out C._p_gchar, state C._p_gint, save C._p_gint) C.gsize {
	return C.g_base64_encode_step(in, _len, break_lines, out, state, save)
}

//Deprecated g_basename

func BitLock(address C._p_gint, lock_bit C.gint) {
	C.g_bit_lock(address, lock_bit)
}

func BitNthLsf(mask C.gulong, nth_bit C.gint) C.gint {
	return C.g_bit_nth_lsf(mask, nth_bit)
}

func BitNthMsf(mask C.gulong, nth_bit C.gint) C.gint {
	return C.g_bit_nth_msf(mask, nth_bit)
}

func BitStorage(number C.gulong) C.guint {
	return C.g_bit_storage(number)
}

func BitTrylock(address C._p_gint, lock_bit C.gint) C.gboolean {
	return C.g_bit_trylock(address, lock_bit)
}

func BitUnlock(address C._p_gint, lock_bit C.gint) {
	C.g_bit_unlock(address, lock_bit)
}

func BookmarkFileErrorQuark() C.GQuark {
	return C.g_bookmark_file_error_quark()
}

//TODO varargs g_build_filename

func BuildFilenamev(args C._pp_gchar) C._p_gchar {
	return C.g_build_filenamev(args)
}

//TODO varargs g_build_path

func BuildPathv(separator C._const_p_gchar, args C._pp_gchar) C._p_gchar {
	return C.g_build_pathv(separator, args)
}

func ByteArrayFree(array C._p_GByteArray, free_segment C.gboolean) C._p_guint8 {
	return C.g_byte_array_free(array, free_segment)
}

func ByteArrayFreeToBytes(array C._p_GByteArray) C._p_GBytes {
	return C.g_byte_array_free_to_bytes(array)
}

func ByteArrayNew() C._p_GByteArray {
	return C.g_byte_array_new()
}

func ByteArrayNewTake(data C._p_guint8, _len C.gsize) C._p_GByteArray {
	return C.g_byte_array_new_take(data, _len)
}

func ByteArrayUnref(array C._p_GByteArray) {
	C.g_byte_array_unref(array)
}

func Chdir(path C._const_p_gchar) C.int {
	return C.g_chdir(path)
}

func CheckVersion(required_major C.guint, required_minor C.guint, required_micro C.guint) C._const_p_gchar {
	return C.glib_check_version(required_major, required_minor, required_micro)
}

func ChecksumTypeGetLength(checksum_type C.GChecksumType) C.gssize {
	return C.g_checksum_type_get_length(checksum_type)
}

func ChildWatchAdd(pid C.GPid, function C.GChildWatchFunc, data C.gpointer) C.guint {
	return C.g_child_watch_add(pid, function, data)
}

func ChildWatchAddFull(priority C.gint, pid C.GPid, function C.GChildWatchFunc, data C.gpointer, notify C.GDestroyNotify) C.guint {
	return C.g_child_watch_add_full(priority, pid, function, data, notify)
}

func ChildWatchSourceNew(pid C.GPid) C._p_GSource {
	return C.g_child_watch_source_new(pid)
}

func ClearError(err C._pp_GError) {
	C.g_clear_error(err)
}

//Skipped g_clear_pointer

func ComputeChecksumForBytes(checksum_type C.GChecksumType, data C._p_GBytes) C._p_gchar {
	return C.g_compute_checksum_for_bytes(checksum_type, data)
}

func ComputeChecksumForData(checksum_type C.GChecksumType, data C._const_p_guchar, length C.gsize) C._p_gchar {
	return C.g_compute_checksum_for_data(checksum_type, data, length)
}

func ComputeChecksumForString(checksum_type C.GChecksumType, str C._const_p_gchar, length C.gssize) C._p_gchar {
	return C.g_compute_checksum_for_string(checksum_type, str, length)
}

func ComputeHmacForData(digest_type C.GChecksumType, key C._p_guchar, key_len C.gsize, data C._const_p_guchar, length C.gsize) C._p_gchar {
	return C.g_compute_hmac_for_data(digest_type, key, key_len, data, length)
}

func ComputeHmacForString(digest_type C.GChecksumType, key C._p_guchar, key_len C.gsize, str C._const_p_gchar, length C.gssize) C._p_gchar {
	return C.g_compute_hmac_for_string(digest_type, key, key_len, str, length)
}

func Convert(str C._const_p_gchar, _len C.gssize, to_codeset C._const_p_gchar, from_codeset C._const_p_gchar, bytes_read C._p_gsize, bytes_written C._p_gsize, err C._pp_GError) C._p_gchar {
	return C.g_convert(str, _len, to_codeset, from_codeset, bytes_read, bytes_written, err)
}

func ConvertErrorQuark() C.GQuark {
	return C.g_convert_error_quark()
}

func ConvertWithFallback(str C._const_p_gchar, _len C.gssize, to_codeset C._const_p_gchar, from_codeset C._const_p_gchar, fallback C._const_p_gchar, bytes_read C._p_gsize, bytes_written C._p_gsize, err C._pp_GError) C._p_gchar {
	return C.g_convert_with_fallback(str, _len, to_codeset, from_codeset, fallback, bytes_read, bytes_written, err)
}

func ConvertWithIconv(str C._const_p_gchar, _len C.gssize, converter C.GIConv, bytes_read C._p_gsize, bytes_written C._p_gsize, err C._pp_GError) C._p_gchar {
	return C.g_convert_with_iconv(str, _len, converter, bytes_read, bytes_written, err)
}

func DatalistClear(datalist C._pp_GData) {
	C.g_datalist_clear(datalist)
}

func DatalistForeach(datalist C._pp_GData, _func C.GDataForeachFunc, user_data C.gpointer) {
	C.g_datalist_foreach(datalist, _func, user_data)
}

func DatalistGetData(datalist C._pp_GData, key C._const_p_gchar) C.gpointer {
	return C.g_datalist_get_data(datalist, key)
}

func DatalistGetFlags(datalist C._pp_GData) C.guint {
	return C.g_datalist_get_flags(datalist)
}

func DatalistIdDupData(datalist C._pp_GData, key_id C.GQuark, dup_func C.GDuplicateFunc, user_data C.gpointer) C.gpointer {
	return C.g_datalist_id_dup_data(datalist, key_id, dup_func, user_data)
}

func DatalistIdGetData(datalist C._pp_GData, key_id C.GQuark) C.gpointer {
	return C.g_datalist_id_get_data(datalist, key_id)
}

func DatalistIdRemoveNoNotify(datalist C._pp_GData, key_id C.GQuark) C.gpointer {
	return C.g_datalist_id_remove_no_notify(datalist, key_id)
}

func DatalistIdReplaceData(datalist C._pp_GData, key_id C.GQuark, oldval C.gpointer, newval C.gpointer, destroy C.GDestroyNotify, old_destroy C._p_GDestroyNotify) C.gboolean {
	return C.g_datalist_id_replace_data(datalist, key_id, oldval, newval, destroy, old_destroy)
}

func DatalistIdSetDataFull(datalist C._pp_GData, key_id C.GQuark, data C.gpointer, destroy_func C.GDestroyNotify) {
	C.g_datalist_id_set_data_full(datalist, key_id, data, destroy_func)
}

func DatalistInit(datalist C._pp_GData) {
	C.g_datalist_init(datalist)
}

func DatalistSetFlags(datalist C._pp_GData, flags C.guint) {
	C.g_datalist_set_flags(datalist, flags)
}

func DatalistUnsetFlags(datalist C._pp_GData, flags C.guint) {
	C.g_datalist_unset_flags(datalist, flags)
}

func DatasetDestroy(dataset_location C.gconstpointer) {
	C.g_dataset_destroy(dataset_location)
}

func DatasetForeach(dataset_location C.gconstpointer, _func C.GDataForeachFunc, user_data C.gpointer) {
	C.g_dataset_foreach(dataset_location, _func, user_data)
}

func DatasetIdGetData(dataset_location C.gconstpointer, key_id C.GQuark) C.gpointer {
	return C.g_dataset_id_get_data(dataset_location, key_id)
}

func DatasetIdRemoveNoNotify(dataset_location C.gconstpointer, key_id C.GQuark) C.gpointer {
	return C.g_dataset_id_remove_no_notify(dataset_location, key_id)
}

func DatasetIdSetDataFull(dataset_location C.gconstpointer, key_id C.GQuark, data C.gpointer, destroy_func C.GDestroyNotify) {
	C.g_dataset_id_set_data_full(dataset_location, key_id, data, destroy_func)
}

func DateGetDaysInMonth(month C.GDateMonth, year C.GDateYear) C.guint8 {
	return C.g_date_get_days_in_month(month, year)
}

func DateGetMondayWeeksInYear(year C.GDateYear) C.guint8 {
	return C.g_date_get_monday_weeks_in_year(year)
}

func DateGetSundayWeeksInYear(year C.GDateYear) C.guint8 {
	return C.g_date_get_sunday_weeks_in_year(year)
}

func DateIsLeapYear(year C.GDateYear) C.gboolean {
	return C.g_date_is_leap_year(year)
}

func DateStrftime(s C._p_gchar, slen C.gsize, format C._const_p_gchar, date C._const_p_GDate) C.gsize {
	return C.g_date_strftime(s, slen, format, date)
}

func DateTimeCompare(dt1 C.gconstpointer, dt2 C.gconstpointer) C.gint {
	return C.g_date_time_compare(dt1, dt2)
}

func DateTimeEqual(dt1 C.gconstpointer, dt2 C.gconstpointer) C.gboolean {
	return C.g_date_time_equal(dt1, dt2)
}

func DateTimeHash(datetime C.gconstpointer) C.guint {
	return C.g_date_time_hash(datetime)
}

func DateValidDay(day C.GDateDay) C.gboolean {
	return C.g_date_valid_day(day)
}

func DateValidDmy(day C.GDateDay, month C.GDateMonth, year C.GDateYear) C.gboolean {
	return C.g_date_valid_dmy(day, month, year)
}

func DateValidJulian(julian_date C.guint32) C.gboolean {
	return C.g_date_valid_julian(julian_date)
}

func DateValidMonth(month C.GDateMonth) C.gboolean {
	return C.g_date_valid_month(month)
}

func DateValidWeekday(weekday C.GDateWeekday) C.gboolean {
	return C.g_date_valid_weekday(weekday)
}

func DateValidYear(year C.GDateYear) C.gboolean {
	return C.g_date_valid_year(year)
}

func Dcgettext(domain C._const_p_gchar, msgid C._const_p_gchar, category C.gint) C._const_p_gchar {
	return C.g_dcgettext(domain, msgid, category)
}

func Dgettext(domain C._const_p_gchar, msgid C._const_p_gchar) C._const_p_gchar {
	return C.g_dgettext(domain, msgid)
}

func DirMakeTmp(tmpl C._p_gchar, err C._pp_GError) C._p_gchar {
	return C.g_dir_make_tmp(tmpl, err)
}

func DirectEqual(v1 C.gconstpointer, v2 C.gconstpointer) C.gboolean {
	return C.g_direct_equal(v1, v2)
}

func DirectHash(v C.gconstpointer) C.guint {
	return C.g_direct_hash(v)
}

func Dngettext(domain C._const_p_gchar, msgid C._const_p_gchar, msgid_plural C._const_p_gchar, n C.gulong) C._const_p_gchar {
	return C.g_dngettext(domain, msgid, msgid_plural, n)
}

func DoubleEqual(v1 C.gconstpointer, v2 C.gconstpointer) C.gboolean {
	return C.g_double_equal(v1, v2)
}

func DoubleHash(v C.gconstpointer) C.guint {
	return C.g_double_hash(v)
}

func Dpgettext(domain C._const_p_gchar, msgctxtid C._const_p_gchar, msgidoffset C.gsize) C._const_p_gchar {
	return C.g_dpgettext(domain, msgctxtid, msgidoffset)
}

func Dpgettext2(domain C._const_p_gchar, context C._const_p_gchar, msgid C._const_p_gchar) C._const_p_gchar {
	return C.g_dpgettext2(domain, context, msgid)
}

func EnvironGetenv(envp C._pp_gchar, variable C._const_p_gchar) C._const_p_gchar {
	return C.g_environ_getenv(envp, variable)
}

func EnvironSetenv(envp C._pp_gchar, variable C._const_p_gchar, value C._const_p_gchar, overwrite C.gboolean) C._pp_gchar {
	return C.g_environ_setenv(envp, variable, value, overwrite)
}

func EnvironUnsetenv(envp C._pp_gchar, variable C._const_p_gchar) C._pp_gchar {
	return C.g_environ_unsetenv(envp, variable)
}

func FileErrorFromErrno(err_no C.gint) C.GFileError {
	return C.g_file_error_from_errno(err_no)
}

func FileErrorQuark() C.GQuark {
	return C.g_file_error_quark()
}

func FileGetContents(filename C._p_gchar, contents C._pp_gchar, length C._p_gsize, err C._pp_GError) C.gboolean {
	return C.g_file_get_contents(filename, contents, length, err)
}

func FileOpenTmp(tmpl C._p_gchar, name_used C._pp_gchar, err C._pp_GError) C.gint {
	return C.g_file_open_tmp(tmpl, name_used, err)
}

func FileReadLink(filename C._const_p_gchar, err C._pp_GError) C._p_gchar {
	return C.g_file_read_link(filename, err)
}

func FileSetContents(filename C._p_gchar, contents C._p_gchar, length C.gssize, err C._pp_GError) C.gboolean {
	return C.g_file_set_contents(filename, contents, length, err)
}

func FileTest(filename C._const_p_gchar, test C.GFileTest) C.gboolean {
	return C.g_file_test(filename, test)
}

func FilenameDisplayBasename(filename C._const_p_gchar) C._p_gchar {
	return C.g_filename_display_basename(filename)
}

func FilenameDisplayName(filename C._const_p_gchar) C._p_gchar {
	return C.g_filename_display_name(filename)
}

func FilenameFromUri(uri C._const_p_gchar, hostname C._pp_gchar, err C._pp_GError) C._p_gchar {
	return C.g_filename_from_uri(uri, hostname, err)
}

func FilenameFromUtf8(utf8string C._const_p_gchar, _len C.gssize, bytes_read C._p_gsize, bytes_written C._p_gsize, err C._pp_GError) C._p_gchar {
	return C.g_filename_from_utf8(utf8string, _len, bytes_read, bytes_written, err)
}

func FilenameToUri(filename C._const_p_gchar, hostname C._const_p_gchar, err C._pp_GError) C._p_gchar {
	return C.g_filename_to_uri(filename, hostname, err)
}

func FilenameToUtf8(opsysstring C._const_p_gchar, _len C.gssize, bytes_read C._p_gsize, bytes_written C._p_gsize, err C._pp_GError) C._p_gchar {
	return C.g_filename_to_utf8(opsysstring, _len, bytes_read, bytes_written, err)
}

func FindProgramInPath(program C._const_p_gchar) C._p_gchar {
	return C.g_find_program_in_path(program)
}

func FormatSize(size C.guint64) C._p_gchar {
	return C.g_format_size(size)
}

//Deprecated g_format_size_for_display

func FormatSizeFull(size C.guint64, flags C.GFormatSizeFlags) C._p_gchar {
	return C.g_format_size_full(size, flags)
}

//TODO varargs g_fprintf

func Free(mem C.gpointer) {
	C.g_free(mem)
}

func GetApplicationName() C._const_p_gchar {
	return C.g_get_application_name()
}

func GetCharset(charset C._const_pp_char) C.gboolean {
	return C.g_get_charset(charset)
}

func GetCodeset() C._p_gchar {
	return C.g_get_codeset()
}

func GetCurrentDir() C._p_gchar {
	return C.g_get_current_dir()
}

func GetCurrentTime(result C._p_GTimeVal) {
	C.g_get_current_time(result)
}

func GetEnviron() C._pp_gchar {
	return C.g_get_environ()
}

func GetFilenameCharsets(charsets C._const_ppp_gchar) C.gboolean {
	return C.g_get_filename_charsets(charsets)
}

func GetHomeDir() C._const_p_gchar {
	return C.g_get_home_dir()
}

func GetHostName() C._const_p_gchar {
	return C.g_get_host_name()
}

func GetLanguageNames() C._pp_gchar {
	return C.g_get_language_names()
}

func GetLocaleVariants(locale C._const_p_gchar) C._pp_gchar {
	return C.g_get_locale_variants(locale)
}

func GetMonotonicTime() C.gint64 {
	return C.g_get_monotonic_time()
}

func GetPrgname() C._p_gchar {
	return C.g_get_prgname()
}

func GetRealName() C._const_p_gchar {
	return C.g_get_real_name()
}

func GetRealTime() C.gint64 {
	return C.g_get_real_time()
}

func GetSystemConfigDirs() C._pp_gchar {
	return C.g_get_system_config_dirs()
}

func GetSystemDataDirs() C._pp_gchar {
	return C.g_get_system_data_dirs()
}

func GetTmpDir() C._const_p_gchar {
	return C.g_get_tmp_dir()
}

func GetUserCacheDir() C._const_p_gchar {
	return C.g_get_user_cache_dir()
}

func GetUserConfigDir() C._const_p_gchar {
	return C.g_get_user_config_dir()
}

func GetUserDataDir() C._const_p_gchar {
	return C.g_get_user_data_dir()
}

func GetUserName() C._const_p_gchar {
	return C.g_get_user_name()
}

func GetUserRuntimeDir() C._const_p_gchar {
	return C.g_get_user_runtime_dir()
}

func GetUserSpecialDir(directory C.GUserDirectory) C._const_p_gchar {
	return C.g_get_user_special_dir(directory)
}

func Getenv(variable C._const_p_gchar) C._const_p_gchar {
	return C.g_getenv(variable)
}

func HashTableAdd(hash_table C._p_GHashTable, key C.gpointer) {
	C.g_hash_table_add(hash_table, key)
}

func HashTableContains(hash_table C._p_GHashTable, key C.gconstpointer) C.gboolean {
	return C.g_hash_table_contains(hash_table, key)
}

func HashTableDestroy(hash_table C._p_GHashTable) {
	C.g_hash_table_destroy(hash_table)
}

func HashTableInsert(hash_table C._p_GHashTable, key C.gpointer, value C.gpointer) {
	C.g_hash_table_insert(hash_table, key, value)
}

func HashTableLookupExtended(hash_table C._p_GHashTable, lookup_key C.gconstpointer, orig_key C._p_gpointer, value C._p_gpointer) C.gboolean {
	return C.g_hash_table_lookup_extended(hash_table, lookup_key, orig_key, value)
}

func HashTableRemove(hash_table C._p_GHashTable, key C.gconstpointer) C.gboolean {
	return C.g_hash_table_remove(hash_table, key)
}

func HashTableRemoveAll(hash_table C._p_GHashTable) {
	C.g_hash_table_remove_all(hash_table)
}

func HashTableReplace(hash_table C._p_GHashTable, key C.gpointer, value C.gpointer) {
	C.g_hash_table_replace(hash_table, key, value)
}

func HashTableSize(hash_table C._p_GHashTable) C.guint {
	return C.g_hash_table_size(hash_table)
}

func HashTableSteal(hash_table C._p_GHashTable, key C.gconstpointer) C.gboolean {
	return C.g_hash_table_steal(hash_table, key)
}

func HashTableStealAll(hash_table C._p_GHashTable) {
	C.g_hash_table_steal_all(hash_table)
}

func HashTableUnref(hash_table C._p_GHashTable) {
	C.g_hash_table_unref(hash_table)
}

func HookDestroy(hook_list C._p_GHookList, hook_id C.gulong) C.gboolean {
	return C.g_hook_destroy(hook_list, hook_id)
}

func HookDestroyLink(hook_list C._p_GHookList, hook C._p_GHook) {
	C.g_hook_destroy_link(hook_list, hook)
}

func HookFree(hook_list C._p_GHookList, hook C._p_GHook) {
	C.g_hook_free(hook_list, hook)
}

func HookInsertBefore(hook_list C._p_GHookList, sibling C._p_GHook, hook C._p_GHook) {
	C.g_hook_insert_before(hook_list, sibling, hook)
}

func HookPrepend(hook_list C._p_GHookList, hook C._p_GHook) {
	C.g_hook_prepend(hook_list, hook)
}

func HookUnref(hook_list C._p_GHookList, hook C._p_GHook) {
	C.g_hook_unref(hook_list, hook)
}

func HostnameIsAsciiEncoded(hostname C._const_p_gchar) C.gboolean {
	return C.g_hostname_is_ascii_encoded(hostname)
}

func HostnameIsIpAddress(hostname C._const_p_gchar) C.gboolean {
	return C.g_hostname_is_ip_address(hostname)
}

func HostnameIsNonAscii(hostname C._const_p_gchar) C.gboolean {
	return C.g_hostname_is_non_ascii(hostname)
}

func HostnameToAscii(hostname C._const_p_gchar) C._p_gchar {
	return C.g_hostname_to_ascii(hostname)
}

func HostnameToUnicode(hostname C._const_p_gchar) C._p_gchar {
	return C.g_hostname_to_unicode(hostname)
}

func IdleAdd(function C.GSourceFunc, data C.gpointer) C.guint {
	return C.g_idle_add(function, data)
}

func IdleAddFull(priority C.gint, function C.GSourceFunc, data C.gpointer, notify C.GDestroyNotify) C.guint {
	return C.g_idle_add_full(priority, function, data, notify)
}

func IdleRemoveByData(data C.gpointer) C.gboolean {
	return C.g_idle_remove_by_data(data)
}

func IdleSourceNew() C._p_GSource {
	return C.g_idle_source_new()
}

func Int64Equal(v1 C.gconstpointer, v2 C.gconstpointer) C.gboolean {
	return C.g_int64_equal(v1, v2)
}

func Int64Hash(v C.gconstpointer) C.guint {
	return C.g_int64_hash(v)
}

func IntEqual(v1 C.gconstpointer, v2 C.gconstpointer) C.gboolean {
	return C.g_int_equal(v1, v2)
}

func IntHash(v C.gconstpointer) C.guint {
	return C.g_int_hash(v)
}

func InternStaticString(string C._const_p_gchar) C._const_p_gchar {
	return C.g_intern_static_string(string)
}

func InternString(string C._const_p_gchar) C._const_p_gchar {
	return C.g_intern_string(string)
}

func IoAddWatch(channel C._p_GIOChannel, condition C.GIOCondition, _func C.GIOFunc, user_data C.gpointer) C.guint {
	return C.g_io_add_watch(channel, condition, _func, user_data)
}

func IoAddWatchFull(channel C._p_GIOChannel, priority C.gint, condition C.GIOCondition, _func C.GIOFunc, user_data C.gpointer, notify C.GDestroyNotify) C.guint {
	return C.g_io_add_watch_full(channel, priority, condition, _func, user_data, notify)
}

func IoChannelErrorFromErrno(en C.gint) C.GIOChannelError {
	return C.g_io_channel_error_from_errno(en)
}

func IoChannelErrorQuark() C.GQuark {
	return C.g_io_channel_error_quark()
}

func IoCreateWatch(channel C._p_GIOChannel, condition C.GIOCondition) C._p_GSource {
	return C.g_io_create_watch(channel, condition)
}

func KeyFileErrorQuark() C.GQuark {
	return C.g_key_file_error_quark()
}

func Listenv() C._pp_gchar {
	return C.g_listenv()
}

func LocaleFromUtf8(utf8string C._const_p_gchar, _len C.gssize, bytes_read C._p_gsize, bytes_written C._p_gsize, err C._pp_GError) C._p_gchar {
	return C.g_locale_from_utf8(utf8string, _len, bytes_read, bytes_written, err)
}

func LocaleToUtf8(opsysstring C._const_p_gchar, _len C.gssize, bytes_read C._p_gsize, bytes_written C._p_gsize, err C._pp_GError) C._p_gchar {
	return C.g_locale_to_utf8(opsysstring, _len, bytes_read, bytes_written, err)
}

//TODO varargs g_log

func LogDefaultHandler(log_domain C._const_p_gchar, log_level C.GLogLevelFlags, message C._const_p_gchar, unused_data C.gpointer) {
	C.g_log_default_handler(log_domain, log_level, message, unused_data)
}

func LogRemoveHandler(log_domain C._const_p_gchar, handler_id C.guint) {
	C.g_log_remove_handler(log_domain, handler_id)
}

func LogSetAlwaysFatal(fatal_mask C.GLogLevelFlags) C.GLogLevelFlags {
	return C.g_log_set_always_fatal(fatal_mask)
}

func LogSetDefaultHandler(log_func C.GLogFunc, user_data C.gpointer) C.GLogFunc {
	return C.g_log_set_default_handler(log_func, user_data)
}

func LogSetFatalMask(log_domain C._const_p_gchar, fatal_mask C.GLogLevelFlags) C.GLogLevelFlags {
	return C.g_log_set_fatal_mask(log_domain, fatal_mask)
}

func LogSetHandler(log_domain C._const_p_gchar, log_levels C.GLogLevelFlags, log_func C.GLogFunc, user_data C.gpointer) C.guint {
	return C.g_log_set_handler(log_domain, log_levels, log_func, user_data)
}

//TODO va_list g_logv

func MainContextDefault() C._p_GMainContext {
	return C.g_main_context_default()
}

func MainContextGetThreadDefault() C._p_GMainContext {
	return C.g_main_context_get_thread_default()
}

func MainContextRefThreadDefault() C._p_GMainContext {
	return C.g_main_context_ref_thread_default()
}

func MainCurrentSource() C._p_GSource {
	return C.g_main_current_source()
}

func MainDepth() C.gint {
	return C.g_main_depth()
}

func Malloc(n_bytes C.gsize) C.gpointer {
	return C.g_malloc(n_bytes)
}

func Malloc0(n_bytes C.gsize) C.gpointer {
	return C.g_malloc0(n_bytes)
}

func Malloc0N(n_blocks C.gsize, n_block_bytes C.gsize) C.gpointer {
	return C.g_malloc0_n(n_blocks, n_block_bytes)
}

func MallocN(n_blocks C.gsize, n_block_bytes C.gsize) C.gpointer {
	return C.g_malloc_n(n_blocks, n_block_bytes)
}

//TODO varargs g_markup_collect_attributes

func MarkupErrorQuark() C.GQuark {
	return C.g_markup_error_quark()
}

func MarkupEscapeText(text C._const_p_gchar, length C.gssize) C._p_gchar {
	return C.g_markup_escape_text(text, length)
}

//TODO varargs g_markup_printf_escaped

//TODO va_list g_markup_vprintf_escaped

func MemIsSystemMalloc() C.gboolean {
	return C.g_mem_is_system_malloc()
}

func MemProfile() {
	C.g_mem_profile()
}

func MemSetVtable(vtable C._p_GMemVTable) {
	C.g_mem_set_vtable(vtable)
}

func Memdup(mem C.gconstpointer, byte_size C.guint) C.gpointer {
	return C.g_memdup(mem, byte_size)
}

func MkdirWithParents(pathname C._const_p_gchar, mode C.gint) C.gint {
	return C.g_mkdir_with_parents(pathname, mode)
}

func Mkdtemp(tmpl C._p_gchar) C._p_gchar {
	return C.g_mkdtemp(tmpl)
}

func MkdtempFull(tmpl C._p_gchar, mode C.gint) C._p_gchar {
	return C.g_mkdtemp_full(tmpl, mode)
}

func Mkstemp(tmpl C._p_gchar) C.gint {
	return C.g_mkstemp(tmpl)
}

func MkstempFull(tmpl C._p_gchar, flags C.gint, mode C.gint) C.gint {
	return C.g_mkstemp_full(tmpl, flags, mode)
}

func NullifyPointer(nullify_location C._p_gpointer) {
	C.g_nullify_pointer(nullify_location)
}

func OnErrorQuery(prg_name C._const_p_gchar) {
	C.g_on_error_query(prg_name)
}

func OnErrorStackTrace(prg_name C._const_p_gchar) {
	C.g_on_error_stack_trace(prg_name)
}

//Skipped g_once_init_enter

//Skipped g_once_init_leave

func OptionErrorQuark() C.GQuark {
	return C.g_option_error_quark()
}

func ParseDebugString(string C._const_p_gchar, keys C._p_GDebugKey, nkeys C.guint) C.guint {
	return C.g_parse_debug_string(string, keys, nkeys)
}

func PathGetBasename(file_name C._const_p_gchar) C._p_gchar {
	return C.g_path_get_basename(file_name)
}

func PathGetDirname(file_name C._const_p_gchar) C._p_gchar {
	return C.g_path_get_dirname(file_name)
}

func PathIsAbsolute(file_name C._const_p_gchar) C.gboolean {
	return C.g_path_is_absolute(file_name)
}

func PathSkipRoot(file_name C._const_p_gchar) C._const_p_gchar {
	return C.g_path_skip_root(file_name)
}

func PatternMatch(pspec C._p_GPatternSpec, string_length C.guint, string C._const_p_gchar, string_reversed C._const_p_gchar) C.gboolean {
	return C.g_pattern_match(pspec, string_length, string, string_reversed)
}

func PatternMatchSimple(pattern C._const_p_gchar, string C._const_p_gchar) C.gboolean {
	return C.g_pattern_match_simple(pattern, string)
}

func PatternMatchString(pspec C._p_GPatternSpec, string C._const_p_gchar) C.gboolean {
	return C.g_pattern_match_string(pspec, string)
}

//Skipped g_pointer_bit_lock

//Skipped g_pointer_bit_trylock

//Skipped g_pointer_bit_unlock

func Poll(fds C._p_GPollFD, nfds C.guint, timeout C.gint) C.gint {
	return C.g_poll(fds, nfds, timeout)
}

//TODO varargs g_prefix_error

//TODO varargs g_print

//TODO varargs g_printerr

//TODO varargs g_printf

//TODO va_list g_printf_string_upper_bound

func PropagateError(dest C._pp_GError, src C._p_GError) {
	C.g_propagate_error(dest, src)
}

//TODO varargs g_propagate_prefixed_error

func PtrArrayAdd(array C._p_GPtrArray, data C.gpointer) {
	C.g_ptr_array_add(array, data)
}

func PtrArrayRemove(array C._p_GPtrArray, data C.gpointer) C.gboolean {
	return C.g_ptr_array_remove(array, data)
}

func PtrArrayRemoveFast(array C._p_GPtrArray, data C.gpointer) C.gboolean {
	return C.g_ptr_array_remove_fast(array, data)
}

func PtrArrayRemoveRange(array C._p_GPtrArray, index_ C.guint, length C.guint) {
	C.g_ptr_array_remove_range(array, index_, length)
}

func PtrArraySetFreeFunc(array C._p_GPtrArray, element_free_func C.GDestroyNotify) {
	C.g_ptr_array_set_free_func(array, element_free_func)
}

func PtrArraySetSize(array C._p_GPtrArray, length C.gint) {
	C.g_ptr_array_set_size(array, length)
}

func PtrArrayUnref(array C._p_GPtrArray) {
	C.g_ptr_array_unref(array)
}

func QsortWithData(pbase C.gconstpointer, total_elems C.gint, size C.gsize, compare_func C.GCompareDataFunc, user_data C.gpointer) {
	C.g_qsort_with_data(pbase, total_elems, size, compare_func, user_data)
}

func QuarkFromStaticString(string C._const_p_gchar) C.GQuark {
	return C.g_quark_from_static_string(string)
}

func QuarkFromString(string C._const_p_gchar) C.GQuark {
	return C.g_quark_from_string(string)
}

func QuarkToString(quark C.GQuark) C._const_p_gchar {
	return C.g_quark_to_string(quark)
}

func QuarkTryString(string C._const_p_gchar) C.GQuark {
	return C.g_quark_try_string(string)
}

func RandomDouble() C.gdouble {
	return C.g_random_double()
}

func RandomDoubleRange(begin C.gdouble, end C.gdouble) C.gdouble {
	return C.g_random_double_range(begin, end)
}

func RandomInt() C.guint32 {
	return C.g_random_int()
}

func RandomIntRange(begin C.gint32, end C.gint32) C.gint32 {
	return C.g_random_int_range(begin, end)
}

func RandomSetSeed(seed C.guint32) {
	C.g_random_set_seed(seed)
}

func Realloc(mem C.gpointer, n_bytes C.gsize) C.gpointer {
	return C.g_realloc(mem, n_bytes)
}

func ReallocN(mem C.gpointer, n_blocks C.gsize, n_block_bytes C.gsize) C.gpointer {
	return C.g_realloc_n(mem, n_blocks, n_block_bytes)
}

func RegexCheckReplacement(replacement C._const_p_gchar, has_references C._p_gboolean, err C._pp_GError) C.gboolean {
	return C.g_regex_check_replacement(replacement, has_references, err)
}

func RegexErrorQuark() C.GQuark {
	return C.g_regex_error_quark()
}

func RegexEscapeNul(string C._const_p_gchar, length C.gint) C._p_gchar {
	return C.g_regex_escape_nul(string, length)
}

func RegexEscapeString(string C._p_gchar, length C.gint) C._p_gchar {
	return C.g_regex_escape_string(string, length)
}

func RegexMatchSimple(pattern C._const_p_gchar, string C._const_p_gchar, compile_options C.GRegexCompileFlags, match_options C.GRegexMatchFlags) C.gboolean {
	return C.g_regex_match_simple(pattern, string, compile_options, match_options)
}

func RegexSplitSimple(pattern C._const_p_gchar, string C._const_p_gchar, compile_options C.GRegexCompileFlags, match_options C.GRegexMatchFlags) C._pp_gchar {
	return C.g_regex_split_simple(pattern, string, compile_options, match_options)
}

func ReloadUserSpecialDirsCache() {
	C.g_reload_user_special_dirs_cache()
}

func ReturnIfFailWarning(log_domain C._const_p_char, pretty_function C._const_p_char, expression C._const_p_char) {
	C.g_return_if_fail_warning(log_domain, pretty_function, expression)
}

func Rmdir(filename C._const_p_gchar) C.int {
	return C.g_rmdir(filename)
}

func SequenceMove(src C._p_GSequenceIter, dest C._p_GSequenceIter) {
	C.g_sequence_move(src, dest)
}

func SequenceMoveRange(dest C._p_GSequenceIter, begin C._p_GSequenceIter, end C._p_GSequenceIter) {
	C.g_sequence_move_range(dest, begin, end)
}

func SequenceRemove(iter C._p_GSequenceIter) {
	C.g_sequence_remove(iter)
}

func SequenceRemoveRange(begin C._p_GSequenceIter, end C._p_GSequenceIter) {
	C.g_sequence_remove_range(begin, end)
}

func SequenceSet(iter C._p_GSequenceIter, data C.gpointer) {
	C.g_sequence_set(iter, data)
}

func SequenceSwap(a C._p_GSequenceIter, b C._p_GSequenceIter) {
	C.g_sequence_swap(a, b)
}

func SetApplicationName(application_name C._const_p_gchar) {
	C.g_set_application_name(application_name)
}

//TODO varargs g_set_error

func SetErrorLiteral(err C._pp_GError, domain C.GQuark, code C.gint, message C._const_p_gchar) {
	C.g_set_error_literal(err, domain, code, message)
}

func SetPrgname(prgname C._const_p_gchar) {
	C.g_set_prgname(prgname)
}

func SetPrintHandler(_func C.GPrintFunc) C.GPrintFunc {
	return C.g_set_print_handler(_func)
}

func SetPrinterrHandler(_func C.GPrintFunc) C.GPrintFunc {
	return C.g_set_printerr_handler(_func)
}

func Setenv(variable C._const_p_gchar, value C._const_p_gchar, overwrite C.gboolean) C.gboolean {
	return C.g_setenv(variable, value, overwrite)
}

func ShellErrorQuark() C.GQuark {
	return C.g_shell_error_quark()
}

func ShellParseArgv(command_line C._const_p_gchar, argcp C._p_gint, argvp C._ppp_gchar, err C._pp_GError) C.gboolean {
	return C.g_shell_parse_argv(command_line, argcp, argvp, err)
}

func ShellQuote(unquoted_string C._const_p_gchar) C._p_gchar {
	return C.g_shell_quote(unquoted_string)
}

func ShellUnquote(quoted_string C._const_p_gchar, err C._pp_GError) C._p_gchar {
	return C.g_shell_unquote(quoted_string, err)
}

func SliceAlloc(block_size C.gsize) C.gpointer {
	return C.g_slice_alloc(block_size)
}

func SliceAlloc0(block_size C.gsize) C.gpointer {
	return C.g_slice_alloc0(block_size)
}

func SliceCopy(block_size C.gsize, mem_block C.gconstpointer) C.gpointer {
	return C.g_slice_copy(block_size, mem_block)
}

func SliceFree1(block_size C.gsize, mem_block C.gpointer) {
	C.g_slice_free1(block_size, mem_block)
}

func SliceFreeChainWithOffset(block_size C.gsize, mem_chain C.gpointer, next_offset C.gsize) {
	C.g_slice_free_chain_with_offset(block_size, mem_chain, next_offset)
}

//Skipped g_slice_get_config

//Skipped g_slice_get_config_state

//Skipped g_slice_set_config

//TODO varargs g_snprintf

func SourceRemove(tag C.guint) C.gboolean {
	return C.g_source_remove(tag)
}

func SourceRemoveByFuncsUserData(funcs C._p_GSourceFuncs, user_data C.gpointer) C.gboolean {
	return C.g_source_remove_by_funcs_user_data(funcs, user_data)
}

func SourceRemoveByUserData(user_data C.gpointer) C.gboolean {
	return C.g_source_remove_by_user_data(user_data)
}

func SourceSetNameById(tag C.guint, name C._const_p_char) {
	C.g_source_set_name_by_id(tag, name)
}

func SpacedPrimesClosest(num C.guint) C.guint {
	return C.g_spaced_primes_closest(num)
}

func SpawnAsync(working_directory C._const_p_gchar, argv C._pp_gchar, envp C._pp_gchar, flags C.GSpawnFlags, child_setup C.GSpawnChildSetupFunc, user_data C.gpointer, child_pid C._p_GPid, err C._pp_GError) C.gboolean {
	return C.g_spawn_async(working_directory, argv, envp, flags, child_setup, user_data, child_pid, err)
}

func SpawnAsyncWithPipes(working_directory C._const_p_gchar, argv C._pp_gchar, envp C._pp_gchar, flags C.GSpawnFlags, child_setup C.GSpawnChildSetupFunc, user_data C.gpointer, child_pid C._p_GPid, standard_input C._p_gint, standard_output C._p_gint, standard_error C._p_gint, err C._pp_GError) C.gboolean {
	return C.g_spawn_async_with_pipes(working_directory, argv, envp, flags, child_setup, user_data, child_pid, standard_input, standard_output, standard_error, err)
}

func SpawnCheckExitStatus(exit_status C.gint, err C._pp_GError) C.gboolean {
	return C.g_spawn_check_exit_status(exit_status, err)
}

func SpawnClosePid(pid C.GPid) {
	C.g_spawn_close_pid(pid)
}

func SpawnCommandLineAsync(command_line C._const_p_gchar, err C._pp_GError) C.gboolean {
	return C.g_spawn_command_line_async(command_line, err)
}

func SpawnCommandLineSync(command_line C._const_p_gchar, standard_output C._pp_gchar, standard_error C._pp_gchar, exit_status C._p_gint, err C._pp_GError) C.gboolean {
	return C.g_spawn_command_line_sync(command_line, standard_output, standard_error, exit_status, err)
}

func SpawnErrorQuark() C.GQuark {
	return C.g_spawn_error_quark()
}

func SpawnExitErrorQuark() C.GQuark {
	return C.g_spawn_exit_error_quark()
}

func SpawnSync(working_directory C._const_p_gchar, argv C._pp_gchar, envp C._pp_gchar, flags C.GSpawnFlags, child_setup C.GSpawnChildSetupFunc, user_data C.gpointer, standard_output C._pp_gchar, standard_error C._pp_gchar, exit_status C._p_gint, err C._pp_GError) C.gboolean {
	return C.g_spawn_sync(working_directory, argv, envp, flags, child_setup, user_data, standard_output, standard_error, exit_status, err)
}

//TODO varargs g_sprintf

func Stpcpy(dest C._p_gchar, src C._const_p_char) C._p_gchar {
	return C.g_stpcpy(dest, src)
}

func StrEqual(v1 C.gconstpointer, v2 C.gconstpointer) C.gboolean {
	return C.g_str_equal(v1, v2)
}

func StrHasPrefix(str C._const_p_gchar, prefix C._const_p_gchar) C.gboolean {
	return C.g_str_has_prefix(str, prefix)
}

func StrHasSuffix(str C._const_p_gchar, suffix C._const_p_gchar) C.gboolean {
	return C.g_str_has_suffix(str, suffix)
}

func StrHash(v C.gconstpointer) C.guint {
	return C.g_str_hash(v)
}

func Strcanon(string C._p_gchar, valid_chars C._const_p_gchar, substitutor C.gchar) C._p_gchar {
	return C.g_strcanon(string, valid_chars, substitutor)
}

//Deprecated g_strcasecmp

func Strchomp(string C._p_gchar) C._p_gchar {
	return C.g_strchomp(string)
}

func Strchug(string C._p_gchar) C._p_gchar {
	return C.g_strchug(string)
}

func Strcmp0(str1 C._const_p_char, str2 C._const_p_char) C.int {
	return C.g_strcmp0(str1, str2)
}

func Strcompress(source C._const_p_gchar) C._p_gchar {
	return C.g_strcompress(source)
}

//TODO varargs g_strconcat

func Strdelimit(string C._p_gchar, delimiters C._const_p_gchar, new_delimiter C.gchar) C._p_gchar {
	return C.g_strdelimit(string, delimiters, new_delimiter)
}

//Deprecated g_strdown

func Strdup(str C._const_p_gchar) C._p_gchar {
	return C.g_strdup(str)
}

//TODO varargs g_strdup_printf

//TODO va_list g_strdup_vprintf

func Strdupv(str_array C._pp_gchar) C._pp_gchar {
	return C.g_strdupv(str_array)
}

func Strerror(errnum C.gint) C._const_p_gchar {
	return C.g_strerror(errnum)
}

func Strescape(source C._const_p_gchar, exceptions C._const_p_gchar) C._p_gchar {
	return C.g_strescape(source, exceptions)
}

func Strfreev(str_array C._pp_gchar) {
	C.g_strfreev(str_array)
}

func StringNew(init C._const_p_gchar) C._p_GString {
	return C.g_string_new(init)
}

func StringNewLen(init C._const_p_gchar, _len C.gssize) C._p_GString {
	return C.g_string_new_len(init, _len)
}

func StringSizedNew(dfl_size C.gsize) C._p_GString {
	return C.g_string_sized_new(dfl_size)
}

func StripContext(msgid C._const_p_gchar, msgval C._const_p_gchar) C._const_p_gchar {
	return C.g_strip_context(msgid, msgval)
}

//TODO varargs g_strjoin

func Strjoinv(separator C._const_p_gchar, str_array C._pp_gchar) C._p_gchar {
	return C.g_strjoinv(separator, str_array)
}

func Strlcat(dest C._p_gchar, src C._const_p_gchar, dest_size C.gsize) C.gsize {
	return C.g_strlcat(dest, src, dest_size)
}

func Strlcpy(dest C._p_gchar, src C._const_p_gchar, dest_size C.gsize) C.gsize {
	return C.g_strlcpy(dest, src, dest_size)
}

//Deprecated g_strncasecmp

func Strndup(str C._const_p_gchar, n C.gsize) C._p_gchar {
	return C.g_strndup(str, n)
}

func Strnfill(length C.gsize, fill_char C.gchar) C._p_gchar {
	return C.g_strnfill(length, fill_char)
}

func Strreverse(string C._p_gchar) C._p_gchar {
	return C.g_strreverse(string)
}

func Strrstr(haystack C._const_p_gchar, needle C._const_p_gchar) C._p_gchar {
	return C.g_strrstr(haystack, needle)
}

func StrrstrLen(haystack C._const_p_gchar, haystack_len C.gssize, needle C._const_p_gchar) C._p_gchar {
	return C.g_strrstr_len(haystack, haystack_len, needle)
}

func Strsignal(signum C.gint) C._const_p_gchar {
	return C.g_strsignal(signum)
}

func Strsplit(string C._const_p_gchar, delimiter C._const_p_gchar, max_tokens C.gint) C._pp_gchar {
	return C.g_strsplit(string, delimiter, max_tokens)
}

func StrsplitSet(string C._const_p_gchar, delimiters C._const_p_gchar, max_tokens C.gint) C._pp_gchar {
	return C.g_strsplit_set(string, delimiters, max_tokens)
}

func StrstrLen(haystack C._const_p_gchar, haystack_len C.gssize, needle C._const_p_gchar) C._p_gchar {
	return C.g_strstr_len(haystack, haystack_len, needle)
}

func Strtod(nptr C._const_p_gchar, endptr C._pp_gchar) C.gdouble {
	return C.g_strtod(nptr, endptr)
}

//Deprecated g_strup

func StrvGetType() C.GType {
	return C.g_strv_get_type()
}

func StrvLength(str_array C._pp_gchar) C.guint {
	return C.g_strv_length(str_array)
}

func TestAddDataFunc(testpath C._const_p_char, test_data C.gconstpointer, test_func C.GTestDataFunc) {
	C.g_test_add_data_func(testpath, test_data, test_func)
}

func TestAddDataFuncFull(testpath C._const_p_char, test_data C.gpointer, test_func C.GTestDataFunc, data_free_func C.GDestroyNotify) {
	C.g_test_add_data_func_full(testpath, test_data, test_func, data_free_func)
}

func TestAddFunc(testpath C._const_p_char, test_func C.GTestFunc) {
	C.g_test_add_func(testpath, test_func)
}

func TestAddVtable(testpath C._const_p_char, data_size C.gsize, test_data C.gconstpointer, data_setup C.GTestFixtureFunc, data_test C.GTestFixtureFunc, data_teardown C.GTestFixtureFunc) {
	C.g_test_add_vtable(testpath, data_size, test_data, data_setup, data_test, data_teardown)
}

func TestAssertExpectedMessagesInternal(domain C._const_p_char, file C._const_p_char, line C.int, _func C._const_p_char) {
	C.g_test_assert_expected_messages_internal(domain, file, line, _func)
}

func TestBug(bug_uri_snippet C._const_p_char) {
	C.g_test_bug(bug_uri_snippet)
}

func TestBugBase(uri_pattern C._const_p_char) {
	C.g_test_bug_base(uri_pattern)
}

func TestCreateCase(test_name C._const_p_char, data_size C.gsize, test_data C.gconstpointer, data_setup C.GTestFixtureFunc, data_test C.GTestFixtureFunc, data_teardown C.GTestFixtureFunc) C._p_GTestCase {
	return C.g_test_create_case(test_name, data_size, test_data, data_setup, data_test, data_teardown)
}

func TestCreateSuite(suite_name C._const_p_char) C._p_GTestSuite {
	return C.g_test_create_suite(suite_name)
}

func TestExpectMessage(log_domain C._const_p_gchar, log_level C.GLogLevelFlags, pattern C._const_p_gchar) {
	C.g_test_expect_message(log_domain, log_level, pattern)
}

func TestFail() {
	C.g_test_fail()
}

func TestGetRoot() C._p_GTestSuite {
	return C.g_test_get_root()
}

//TODO varargs g_test_init

func TestLogSetFatalHandler(log_func C.GTestLogFatalFunc, user_data C.gpointer) {
	C.g_test_log_set_fatal_handler(log_func, user_data)
}

func TestLogTypeName(log_type C.GTestLogType) C._const_p_char {
	return C.g_test_log_type_name(log_type)
}

//TODO varargs g_test_maximized_result

//TODO varargs g_test_message

//TODO varargs g_test_minimized_result

func TestQueueDestroy(destroy_func C.GDestroyNotify, destroy_data C.gpointer) {
	C.g_test_queue_destroy(destroy_func, destroy_data)
}

func TestQueueFree(gfree_pointer C.gpointer) {
	C.g_test_queue_free(gfree_pointer)
}

func TestRandDouble() C.double {
	return C.g_test_rand_double()
}

func TestRandDoubleRange(range_start C.double, range_end C.double) C.double {
	return C.g_test_rand_double_range(range_start, range_end)
}

func TestRandInt() C.gint32 {
	return C.g_test_rand_int()
}

func TestRandIntRange(begin C.gint32, end C.gint32) C.gint32 {
	return C.g_test_rand_int_range(begin, end)
}

func TestRun() C.int {
	return C.g_test_run()
}

func TestRunSuite(suite C._p_GTestSuite) C.int {
	return C.g_test_run_suite(suite)
}

func TestTimerElapsed() C.double {
	return C.g_test_timer_elapsed()
}

func TestTimerLast() C.double {
	return C.g_test_timer_last()
}

func TestTimerStart() {
	C.g_test_timer_start()
}

func TestTrapAssertions(domain C._const_p_char, file C._const_p_char, line C.int, _func C._const_p_char, assertion_flags C.guint64, pattern C._const_p_char) {
	C.g_test_trap_assertions(domain, file, line, _func, assertion_flags, pattern)
}

func TestTrapFork(usec_timeout C.guint64, test_trap_flags C.GTestTrapFlags) C.gboolean {
	return C.g_test_trap_fork(usec_timeout, test_trap_flags)
}

func TestTrapHasPassed() C.gboolean {
	return C.g_test_trap_has_passed()
}

func TestTrapReachedTimeout() C.gboolean {
	return C.g_test_trap_reached_timeout()
}

func ThreadErrorQuark() C.GQuark {
	return C.g_thread_error_quark()
}

func ThreadExit(retval C.gpointer) {
	C.g_thread_exit(retval)
}

func ThreadPoolGetMaxIdleTime() C.guint {
	return C.g_thread_pool_get_max_idle_time()
}

func ThreadPoolGetMaxUnusedThreads() C.gint {
	return C.g_thread_pool_get_max_unused_threads()
}

func ThreadPoolGetNumUnusedThreads() C.guint {
	return C.g_thread_pool_get_num_unused_threads()
}

func ThreadPoolSetMaxIdleTime(interval C.guint) {
	C.g_thread_pool_set_max_idle_time(interval)
}

func ThreadPoolSetMaxUnusedThreads(max_threads C.gint) {
	C.g_thread_pool_set_max_unused_threads(max_threads)
}

func ThreadPoolStopUnusedThreads() {
	C.g_thread_pool_stop_unused_threads()
}

func ThreadSelf() C._p_GThread {
	return C.g_thread_self()
}

func ThreadYield() {
	C.g_thread_yield()
}

func TimeValFromIso8601(iso_date C._const_p_gchar, time_ C._p_GTimeVal) C.gboolean {
	return C.g_time_val_from_iso8601(iso_date, time_)
}

func TimeoutAdd(interval C.guint, function C.GSourceFunc, data C.gpointer) C.guint {
	return C.g_timeout_add(interval, function, data)
}

func TimeoutAddFull(priority C.gint, interval C.guint, function C.GSourceFunc, data C.gpointer, notify C.GDestroyNotify) C.guint {
	return C.g_timeout_add_full(priority, interval, function, data, notify)
}

func TimeoutAddSeconds(interval C.guint, function C.GSourceFunc, data C.gpointer) C.guint {
	return C.g_timeout_add_seconds(interval, function, data)
}

func TimeoutAddSecondsFull(priority C.gint, interval C.guint, function C.GSourceFunc, data C.gpointer, notify C.GDestroyNotify) C.guint {
	return C.g_timeout_add_seconds_full(priority, interval, function, data, notify)
}

func TimeoutSourceNew(interval C.guint) C._p_GSource {
	return C.g_timeout_source_new(interval)
}

func TimeoutSourceNewSeconds(interval C.guint) C._p_GSource {
	return C.g_timeout_source_new_seconds(interval)
}

func TrashStackHeight(stack_p C._pp_GTrashStack) C.guint {
	return C.g_trash_stack_height(stack_p)
}

func TrashStackPush(stack_p C._pp_GTrashStack, data_p C.gpointer) {
	C.g_trash_stack_push(stack_p, data_p)
}

func TryMalloc(n_bytes C.gsize) C.gpointer {
	return C.g_try_malloc(n_bytes)
}

func TryMalloc0(n_bytes C.gsize) C.gpointer {
	return C.g_try_malloc0(n_bytes)
}

func TryMalloc0N(n_blocks C.gsize, n_block_bytes C.gsize) C.gpointer {
	return C.g_try_malloc0_n(n_blocks, n_block_bytes)
}

func TryMallocN(n_blocks C.gsize, n_block_bytes C.gsize) C.gpointer {
	return C.g_try_malloc_n(n_blocks, n_block_bytes)
}

func TryRealloc(mem C.gpointer, n_bytes C.gsize) C.gpointer {
	return C.g_try_realloc(mem, n_bytes)
}

func TryReallocN(mem C.gpointer, n_blocks C.gsize, n_block_bytes C.gsize) C.gpointer {
	return C.g_try_realloc_n(mem, n_blocks, n_block_bytes)
}

func Ucs4ToUtf16(str C._const_p_gunichar, _len C.glong, items_read C._p_glong, items_written C._p_glong, err C._pp_GError) C._p_gunichar2 {
	return C.g_ucs4_to_utf16(str, _len, items_read, items_written, err)
}

func Ucs4ToUtf8(str C._const_p_gunichar, _len C.glong, items_read C._p_glong, items_written C._p_glong, err C._pp_GError) C._p_gchar {
	return C.g_ucs4_to_utf8(str, _len, items_read, items_written, err)
}

func UnicharBreakType(c C.gunichar) C.GUnicodeBreakType {
	return C.g_unichar_break_type(c)
}

func UnicharCombiningClass(uc C.gunichar) C.gint {
	return C.g_unichar_combining_class(uc)
}

func UnicharCompose(a C.gunichar, b C.gunichar, ch C._p_gunichar) C.gboolean {
	return C.g_unichar_compose(a, b, ch)
}

func UnicharDecompose(ch C.gunichar, a C._p_gunichar, b C._p_gunichar) C.gboolean {
	return C.g_unichar_decompose(ch, a, b)
}

func UnicharDigitValue(c C.gunichar) C.gint {
	return C.g_unichar_digit_value(c)
}

func UnicharFullyDecompose(ch C.gunichar, compat C.gboolean, result C._p_gunichar, result_len C.gsize) C.gsize {
	return C.g_unichar_fully_decompose(ch, compat, result, result_len)
}

func UnicharGetMirrorChar(ch C.gunichar, mirrored_ch C._p_gunichar) C.gboolean {
	return C.g_unichar_get_mirror_char(ch, mirrored_ch)
}

func UnicharGetScript(ch C.gunichar) C.GUnicodeScript {
	return C.g_unichar_get_script(ch)
}

func UnicharIsalnum(c C.gunichar) C.gboolean {
	return C.g_unichar_isalnum(c)
}

func UnicharIsalpha(c C.gunichar) C.gboolean {
	return C.g_unichar_isalpha(c)
}

func UnicharIscntrl(c C.gunichar) C.gboolean {
	return C.g_unichar_iscntrl(c)
}

func UnicharIsdefined(c C.gunichar) C.gboolean {
	return C.g_unichar_isdefined(c)
}

func UnicharIsdigit(c C.gunichar) C.gboolean {
	return C.g_unichar_isdigit(c)
}

func UnicharIsgraph(c C.gunichar) C.gboolean {
	return C.g_unichar_isgraph(c)
}

func UnicharIslower(c C.gunichar) C.gboolean {
	return C.g_unichar_islower(c)
}

func UnicharIsmark(c C.gunichar) C.gboolean {
	return C.g_unichar_ismark(c)
}

func UnicharIsprint(c C.gunichar) C.gboolean {
	return C.g_unichar_isprint(c)
}

func UnicharIspunct(c C.gunichar) C.gboolean {
	return C.g_unichar_ispunct(c)
}

func UnicharIsspace(c C.gunichar) C.gboolean {
	return C.g_unichar_isspace(c)
}

func UnicharIstitle(c C.gunichar) C.gboolean {
	return C.g_unichar_istitle(c)
}

func UnicharIsupper(c C.gunichar) C.gboolean {
	return C.g_unichar_isupper(c)
}

func UnicharIswide(c C.gunichar) C.gboolean {
	return C.g_unichar_iswide(c)
}

func UnicharIswideCjk(c C.gunichar) C.gboolean {
	return C.g_unichar_iswide_cjk(c)
}

func UnicharIsxdigit(c C.gunichar) C.gboolean {
	return C.g_unichar_isxdigit(c)
}

func UnicharIszerowidth(c C.gunichar) C.gboolean {
	return C.g_unichar_iszerowidth(c)
}

func UnicharToUtf8(c C.gunichar, outbuf C._p_gchar) C.gint {
	return C.g_unichar_to_utf8(c, outbuf)
}

func UnicharTolower(c C.gunichar) C.gunichar {
	return C.g_unichar_tolower(c)
}

func UnicharTotitle(c C.gunichar) C.gunichar {
	return C.g_unichar_totitle(c)
}

func UnicharToupper(c C.gunichar) C.gunichar {
	return C.g_unichar_toupper(c)
}

func UnicharType(c C.gunichar) C.GUnicodeType {
	return C.g_unichar_type(c)
}

func UnicharValidate(ch C.gunichar) C.gboolean {
	return C.g_unichar_validate(ch)
}

func UnicharXdigitValue(c C.gunichar) C.gint {
	return C.g_unichar_xdigit_value(c)
}

//Deprecated g_unicode_canonical_decomposition

func UnicodeCanonicalOrdering(string C._p_gunichar, _len C.gsize) {
	C.g_unicode_canonical_ordering(string, _len)
}

func UnicodeScriptFromIso15924(iso15924 C.guint32) C.GUnicodeScript {
	return C.g_unicode_script_from_iso15924(iso15924)
}

func UnicodeScriptToIso15924(script C.GUnicodeScript) C.guint32 {
	return C.g_unicode_script_to_iso15924(script)
}

func UnixErrorQuark() C.GQuark {
	return C.g_unix_error_quark()
}

func UnixOpenPipe(fds C._p_gint, flags C.gint, err C._pp_GError) C.gboolean {
	return C.g_unix_open_pipe(fds, flags, err)
}

func UnixSetFdNonblocking(fd C.gint, nonblock C.gboolean, err C._pp_GError) C.gboolean {
	return C.g_unix_set_fd_nonblocking(fd, nonblock, err)
}

func UnixSignalAdd(signum C.gint, handler C.GSourceFunc, user_data C.gpointer) C.guint {
	return C.g_unix_signal_add(signum, handler, user_data)
}

func UnixSignalAddFull(priority C.gint, signum C.gint, handler C.GSourceFunc, user_data C.gpointer, notify C.GDestroyNotify) C.guint {
	return C.g_unix_signal_add_full(priority, signum, handler, user_data, notify)
}

func UnixSignalSourceNew(signum C.gint) C._p_GSource {
	return C.g_unix_signal_source_new(signum)
}

func Unlink(filename C._const_p_gchar) C.int {
	return C.g_unlink(filename)
}

func Unsetenv(variable C._const_p_gchar) {
	C.g_unsetenv(variable)
}

func UriEscapeString(unescaped C._const_p_char, reserved_chars_allowed C._const_p_char, allow_utf8 C.gboolean) C._p_char {
	return C.g_uri_escape_string(unescaped, reserved_chars_allowed, allow_utf8)
}

func UriListExtractUris(uri_list C._const_p_gchar) C._pp_gchar {
	return C.g_uri_list_extract_uris(uri_list)
}

func UriParseScheme(uri C._const_p_char) C._p_char {
	return C.g_uri_parse_scheme(uri)
}

func UriUnescapeSegment(escaped_string C._const_p_char, escaped_string_end C._const_p_char, illegal_characters C._const_p_char) C._p_char {
	return C.g_uri_unescape_segment(escaped_string, escaped_string_end, illegal_characters)
}

func UriUnescapeString(escaped_string C._const_p_char, illegal_characters C._const_p_char) C._p_char {
	return C.g_uri_unescape_string(escaped_string, illegal_characters)
}

func Usleep(microseconds C.gulong) {
	C.g_usleep(microseconds)
}

func Utf16ToUcs4(str C._const_p_gunichar2, _len C.glong, items_read C._p_glong, items_written C._p_glong, err C._pp_GError) C._p_gunichar {
	return C.g_utf16_to_ucs4(str, _len, items_read, items_written, err)
}

func Utf16ToUtf8(str C._const_p_gunichar2, _len C.glong, items_read C._p_glong, items_written C._p_glong, err C._pp_GError) C._p_gchar {
	return C.g_utf16_to_utf8(str, _len, items_read, items_written, err)
}

func Utf8Casefold(str C._const_p_gchar, _len C.gssize) C._p_gchar {
	return C.g_utf8_casefold(str, _len)
}

func Utf8Collate(str1 C._const_p_gchar, str2 C._const_p_gchar) C.gint {
	return C.g_utf8_collate(str1, str2)
}

func Utf8CollateKey(str C._const_p_gchar, _len C.gssize) C._p_gchar {
	return C.g_utf8_collate_key(str, _len)
}

func Utf8CollateKeyForFilename(str C._const_p_gchar, _len C.gssize) C._p_gchar {
	return C.g_utf8_collate_key_for_filename(str, _len)
}

func Utf8FindNextChar(p C._const_p_gchar, end C._const_p_gchar) C._p_gchar {
	return C.g_utf8_find_next_char(p, end)
}

func Utf8FindPrevChar(str C._const_p_gchar, p C._const_p_gchar) C._p_gchar {
	return C.g_utf8_find_prev_char(str, p)
}

func Utf8GetChar(p C._const_p_gchar) C.gunichar {
	return C.g_utf8_get_char(p)
}

func Utf8GetCharValidated(p C._const_p_gchar, max_len C.gssize) C.gunichar {
	return C.g_utf8_get_char_validated(p, max_len)
}

func Utf8Normalize(str C._const_p_gchar, _len C.gssize, mode C.GNormalizeMode) C._p_gchar {
	return C.g_utf8_normalize(str, _len, mode)
}

func Utf8OffsetToPointer(str C._const_p_gchar, offset C.glong) C._p_gchar {
	return C.g_utf8_offset_to_pointer(str, offset)
}

func Utf8PointerToOffset(str C._const_p_gchar, pos C._const_p_gchar) C.glong {
	return C.g_utf8_pointer_to_offset(str, pos)
}

func Utf8PrevChar(p C._const_p_gchar) C._p_gchar {
	return C.g_utf8_prev_char(p)
}

func Utf8Strchr(p C._const_p_gchar, _len C.gssize, c C.gunichar) C._p_gchar {
	return C.g_utf8_strchr(p, _len, c)
}

func Utf8Strdown(str C._const_p_gchar, _len C.gssize) C._p_gchar {
	return C.g_utf8_strdown(str, _len)
}

func Utf8Strlen(p C._const_p_gchar, max C.gssize) C.glong {
	return C.g_utf8_strlen(p, max)
}

func Utf8Strncpy(dest C._p_gchar, src C._const_p_gchar, n C.gsize) C._p_gchar {
	return C.g_utf8_strncpy(dest, src, n)
}

func Utf8Strrchr(p C._const_p_gchar, _len C.gssize, c C.gunichar) C._p_gchar {
	return C.g_utf8_strrchr(p, _len, c)
}

func Utf8Strreverse(str C._const_p_gchar, _len C.gssize) C._p_gchar {
	return C.g_utf8_strreverse(str, _len)
}

func Utf8Strup(str C._const_p_gchar, _len C.gssize) C._p_gchar {
	return C.g_utf8_strup(str, _len)
}

func Utf8Substring(str C._const_p_gchar, start_pos C.glong, end_pos C.glong) C._p_gchar {
	return C.g_utf8_substring(str, start_pos, end_pos)
}

func Utf8ToUcs4(str C._const_p_gchar, _len C.glong, items_read C._p_glong, items_written C._p_glong, err C._pp_GError) C._p_gunichar {
	return C.g_utf8_to_ucs4(str, _len, items_read, items_written, err)
}

func Utf8ToUcs4Fast(str C._const_p_gchar, _len C.glong, items_written C._p_glong) C._p_gunichar {
	return C.g_utf8_to_ucs4_fast(str, _len, items_written)
}

func Utf8ToUtf16(str C._const_p_gchar, _len C.glong, items_read C._p_glong, items_written C._p_glong, err C._pp_GError) C._p_gunichar2 {
	return C.g_utf8_to_utf16(str, _len, items_read, items_written, err)
}

func Utf8Validate(str C._p_gchar, max_len C.gssize, end C._const_pp_gchar) C.gboolean {
	return C.g_utf8_validate(str, max_len, end)
}

//Skipped g_variant_get_gtype

func VariantIsObjectPath(string C._const_p_gchar) C.gboolean {
	return C.g_variant_is_object_path(string)
}

func VariantIsSignature(string C._const_p_gchar) C.gboolean {
	return C.g_variant_is_signature(string)
}

func VariantParse(_type C._const_p_GVariantType, text C._const_p_gchar, limit C._const_p_gchar, endptr C._const_pp_gchar, err C._pp_GError) C._p_GVariant {
	return C.g_variant_parse(_type, text, limit, endptr, err)
}

func VariantParserGetErrorQuark() C.GQuark {
	return C.g_variant_parser_get_error_quark()
}

func VariantTypeChecked(arg_0 C._const_p_gchar) C._const_p_GVariantType {
	return C.g_variant_type_checked_(arg_0)
}

func VariantTypeStringIsValid(type_string C._const_p_gchar) C.gboolean {
	return C.g_variant_type_string_is_valid(type_string)
}

func VariantTypeStringScan(string C._const_p_gchar, limit C._const_p_gchar, endptr C._const_pp_gchar) C.gboolean {
	return C.g_variant_type_string_scan(string, limit, endptr)
}

//TODO va_list g_vasprintf

//TODO va_list g_vfprintf

//TODO va_list g_vprintf

//TODO va_list g_vsnprintf

//TODO va_list g_vsprintf

func WarnMessage(domain C._const_p_char, file C._const_p_char, line C.int, _func C._const_p_char, warnexpr C._const_p_char) {
	C.g_warn_message(domain, file, line, _func, warnexpr)
}

const (
	BOOKMARK_FILE_ERROR_INVALID_URI = C.G_BOOKMARK_FILE_ERROR_INVALID_URI
	BOOKMARK_FILE_ERROR_INVALID_VALUE = C.G_BOOKMARK_FILE_ERROR_INVALID_VALUE
	BOOKMARK_FILE_ERROR_APP_NOT_REGISTERED = C.G_BOOKMARK_FILE_ERROR_APP_NOT_REGISTERED
	BOOKMARK_FILE_ERROR_URI_NOT_FOUND = C.G_BOOKMARK_FILE_ERROR_URI_NOT_FOUND
	BOOKMARK_FILE_ERROR_READ = C.G_BOOKMARK_FILE_ERROR_READ
	BOOKMARK_FILE_ERROR_UNKNOWN_ENCODING = C.G_BOOKMARK_FILE_ERROR_UNKNOWN_ENCODING
	BOOKMARK_FILE_ERROR_WRITE = C.G_BOOKMARK_FILE_ERROR_WRITE
	BOOKMARK_FILE_ERROR_FILE_NOT_FOUND = C.G_BOOKMARK_FILE_ERROR_FILE_NOT_FOUND
	CHECKSUM_MD5 = C.G_CHECKSUM_MD5
	CHECKSUM_SHA1 = C.G_CHECKSUM_SHA1
	CHECKSUM_SHA256 = C.G_CHECKSUM_SHA256
	CHECKSUM_SHA512 = C.G_CHECKSUM_SHA512
	CONVERT_ERROR_NO_CONVERSION = C.G_CONVERT_ERROR_NO_CONVERSION
	CONVERT_ERROR_ILLEGAL_SEQUENCE = C.G_CONVERT_ERROR_ILLEGAL_SEQUENCE
	CONVERT_ERROR_FAILED = C.G_CONVERT_ERROR_FAILED
	CONVERT_ERROR_PARTIAL_INPUT = C.G_CONVERT_ERROR_PARTIAL_INPUT
	CONVERT_ERROR_BAD_URI = C.G_CONVERT_ERROR_BAD_URI
	CONVERT_ERROR_NOT_ABSOLUTE_PATH = C.G_CONVERT_ERROR_NOT_ABSOLUTE_PATH
	DATE_DAY = C.G_DATE_DAY
	DATE_MONTH = C.G_DATE_MONTH
	DATE_YEAR = C.G_DATE_YEAR
	DATE_BAD_MONTH = C.G_DATE_BAD_MONTH
	DATE_JANUARY = C.G_DATE_JANUARY
	DATE_FEBRUARY = C.G_DATE_FEBRUARY
	DATE_MARCH = C.G_DATE_MARCH
	DATE_APRIL = C.G_DATE_APRIL
	DATE_MAY = C.G_DATE_MAY
	DATE_JUNE = C.G_DATE_JUNE
	DATE_JULY = C.G_DATE_JULY
	DATE_AUGUST = C.G_DATE_AUGUST
	DATE_SEPTEMBER = C.G_DATE_SEPTEMBER
	DATE_OCTOBER = C.G_DATE_OCTOBER
	DATE_NOVEMBER = C.G_DATE_NOVEMBER
	DATE_DECEMBER = C.G_DATE_DECEMBER
	DATE_BAD_WEEKDAY = C.G_DATE_BAD_WEEKDAY
	DATE_MONDAY = C.G_DATE_MONDAY
	DATE_TUESDAY = C.G_DATE_TUESDAY
	DATE_WEDNESDAY = C.G_DATE_WEDNESDAY
	DATE_THURSDAY = C.G_DATE_THURSDAY
	DATE_FRIDAY = C.G_DATE_FRIDAY
	DATE_SATURDAY = C.G_DATE_SATURDAY
	DATE_SUNDAY = C.G_DATE_SUNDAY
	ERR_UNKNOWN = C.G_ERR_UNKNOWN
	ERR_UNEXP_EOF = C.G_ERR_UNEXP_EOF
	ERR_UNEXP_EOF_IN_STRING = C.G_ERR_UNEXP_EOF_IN_STRING
	ERR_UNEXP_EOF_IN_COMMENT = C.G_ERR_UNEXP_EOF_IN_COMMENT
	ERR_NON_DIGIT_IN_CONST = C.G_ERR_NON_DIGIT_IN_CONST
	ERR_DIGIT_RADIX = C.G_ERR_DIGIT_RADIX
	ERR_FLOAT_RADIX = C.G_ERR_FLOAT_RADIX
	ERR_FLOAT_MALFORMED = C.G_ERR_FLOAT_MALFORMED
	FILE_ERROR_EXIST = C.G_FILE_ERROR_EXIST
	FILE_ERROR_ISDIR = C.G_FILE_ERROR_ISDIR
	FILE_ERROR_ACCES = C.G_FILE_ERROR_ACCES
	FILE_ERROR_NAMETOOLONG = C.G_FILE_ERROR_NAMETOOLONG
	FILE_ERROR_NOENT = C.G_FILE_ERROR_NOENT
	FILE_ERROR_NOTDIR = C.G_FILE_ERROR_NOTDIR
	FILE_ERROR_NXIO = C.G_FILE_ERROR_NXIO
	FILE_ERROR_NODEV = C.G_FILE_ERROR_NODEV
	FILE_ERROR_ROFS = C.G_FILE_ERROR_ROFS
	FILE_ERROR_TXTBSY = C.G_FILE_ERROR_TXTBSY
	FILE_ERROR_FAULT = C.G_FILE_ERROR_FAULT
	FILE_ERROR_LOOP = C.G_FILE_ERROR_LOOP
	FILE_ERROR_NOSPC = C.G_FILE_ERROR_NOSPC
	FILE_ERROR_NOMEM = C.G_FILE_ERROR_NOMEM
	FILE_ERROR_MFILE = C.G_FILE_ERROR_MFILE
	FILE_ERROR_NFILE = C.G_FILE_ERROR_NFILE
	FILE_ERROR_BADF = C.G_FILE_ERROR_BADF
	FILE_ERROR_INVAL = C.G_FILE_ERROR_INVAL
	FILE_ERROR_PIPE = C.G_FILE_ERROR_PIPE
	FILE_ERROR_AGAIN = C.G_FILE_ERROR_AGAIN
	FILE_ERROR_INTR = C.G_FILE_ERROR_INTR
	FILE_ERROR_IO = C.G_FILE_ERROR_IO
	FILE_ERROR_PERM = C.G_FILE_ERROR_PERM
	FILE_ERROR_NOSYS = C.G_FILE_ERROR_NOSYS
	FILE_ERROR_FAILED = C.G_FILE_ERROR_FAILED
	IO_CHANNEL_ERROR_FBIG = C.G_IO_CHANNEL_ERROR_FBIG
	IO_CHANNEL_ERROR_INVAL = C.G_IO_CHANNEL_ERROR_INVAL
	IO_CHANNEL_ERROR_IO = C.G_IO_CHANNEL_ERROR_IO
	IO_CHANNEL_ERROR_ISDIR = C.G_IO_CHANNEL_ERROR_ISDIR
	IO_CHANNEL_ERROR_NOSPC = C.G_IO_CHANNEL_ERROR_NOSPC
	IO_CHANNEL_ERROR_NXIO = C.G_IO_CHANNEL_ERROR_NXIO
	IO_CHANNEL_ERROR_OVERFLOW = C.G_IO_CHANNEL_ERROR_OVERFLOW
	IO_CHANNEL_ERROR_PIPE = C.G_IO_CHANNEL_ERROR_PIPE
	IO_CHANNEL_ERROR_FAILED = C.G_IO_CHANNEL_ERROR_FAILED
	IO_ERROR_NONE = C.G_IO_ERROR_NONE
	IO_ERROR_AGAIN = C.G_IO_ERROR_AGAIN
	IO_ERROR_INVAL = C.G_IO_ERROR_INVAL
	IO_ERROR_UNKNOWN = C.G_IO_ERROR_UNKNOWN
	IO_STATUS_ERROR = C.G_IO_STATUS_ERROR
	IO_STATUS_NORMAL = C.G_IO_STATUS_NORMAL
	IO_STATUS_EOF = C.G_IO_STATUS_EOF
	IO_STATUS_AGAIN = C.G_IO_STATUS_AGAIN
	KEY_FILE_ERROR_UNKNOWN_ENCODING = C.G_KEY_FILE_ERROR_UNKNOWN_ENCODING
	KEY_FILE_ERROR_PARSE = C.G_KEY_FILE_ERROR_PARSE
	KEY_FILE_ERROR_NOT_FOUND = C.G_KEY_FILE_ERROR_NOT_FOUND
	KEY_FILE_ERROR_KEY_NOT_FOUND = C.G_KEY_FILE_ERROR_KEY_NOT_FOUND
	KEY_FILE_ERROR_GROUP_NOT_FOUND = C.G_KEY_FILE_ERROR_GROUP_NOT_FOUND
	KEY_FILE_ERROR_INVALID_VALUE = C.G_KEY_FILE_ERROR_INVALID_VALUE
	MARKUP_ERROR_BAD_UTF8 = C.G_MARKUP_ERROR_BAD_UTF8
	MARKUP_ERROR_EMPTY = C.G_MARKUP_ERROR_EMPTY
	MARKUP_ERROR_PARSE = C.G_MARKUP_ERROR_PARSE
	MARKUP_ERROR_UNKNOWN_ELEMENT = C.G_MARKUP_ERROR_UNKNOWN_ELEMENT
	MARKUP_ERROR_UNKNOWN_ATTRIBUTE = C.G_MARKUP_ERROR_UNKNOWN_ATTRIBUTE
	MARKUP_ERROR_INVALID_CONTENT = C.G_MARKUP_ERROR_INVALID_CONTENT
	MARKUP_ERROR_MISSING_ATTRIBUTE = C.G_MARKUP_ERROR_MISSING_ATTRIBUTE
	NORMALIZE_DEFAULT = C.G_NORMALIZE_DEFAULT
	NORMALIZE_NFD = C.G_NORMALIZE_NFD
	NORMALIZE_DEFAULT_COMPOSE = C.G_NORMALIZE_DEFAULT_COMPOSE
	NORMALIZE_NFC = C.G_NORMALIZE_NFC
	NORMALIZE_ALL = C.G_NORMALIZE_ALL
	NORMALIZE_NFKD = C.G_NORMALIZE_NFKD
	NORMALIZE_ALL_COMPOSE = C.G_NORMALIZE_ALL_COMPOSE
	NORMALIZE_NFKC = C.G_NORMALIZE_NFKC
	ONCE_STATUS_NOTCALLED = C.G_ONCE_STATUS_NOTCALLED
	ONCE_STATUS_PROGRESS = C.G_ONCE_STATUS_PROGRESS
	ONCE_STATUS_READY = C.G_ONCE_STATUS_READY
	OPTION_ARG_NONE = C.G_OPTION_ARG_NONE
	OPTION_ARG_STRING = C.G_OPTION_ARG_STRING
	OPTION_ARG_INT = C.G_OPTION_ARG_INT
	OPTION_ARG_CALLBACK = C.G_OPTION_ARG_CALLBACK
	OPTION_ARG_FILENAME = C.G_OPTION_ARG_FILENAME
	OPTION_ARG_STRING_ARRAY = C.G_OPTION_ARG_STRING_ARRAY
	OPTION_ARG_FILENAME_ARRAY = C.G_OPTION_ARG_FILENAME_ARRAY
	OPTION_ARG_DOUBLE = C.G_OPTION_ARG_DOUBLE
	OPTION_ARG_INT64 = C.G_OPTION_ARG_INT64
	OPTION_ERROR_UNKNOWN_OPTION = C.G_OPTION_ERROR_UNKNOWN_OPTION
	OPTION_ERROR_BAD_VALUE = C.G_OPTION_ERROR_BAD_VALUE
	OPTION_ERROR_FAILED = C.G_OPTION_ERROR_FAILED
	REGEX_ERROR_COMPILE = C.G_REGEX_ERROR_COMPILE
	REGEX_ERROR_OPTIMIZE = C.G_REGEX_ERROR_OPTIMIZE
	REGEX_ERROR_REPLACE = C.G_REGEX_ERROR_REPLACE
	REGEX_ERROR_MATCH = C.G_REGEX_ERROR_MATCH
	REGEX_ERROR_INTERNAL = C.G_REGEX_ERROR_INTERNAL
	REGEX_ERROR_STRAY_BACKSLASH = C.G_REGEX_ERROR_STRAY_BACKSLASH
	REGEX_ERROR_MISSING_CONTROL_CHAR = C.G_REGEX_ERROR_MISSING_CONTROL_CHAR
	REGEX_ERROR_UNRECOGNIZED_ESCAPE = C.G_REGEX_ERROR_UNRECOGNIZED_ESCAPE
	REGEX_ERROR_QUANTIFIERS_OUT_OF_ORDER = C.G_REGEX_ERROR_QUANTIFIERS_OUT_OF_ORDER
	REGEX_ERROR_QUANTIFIER_TOO_BIG = C.G_REGEX_ERROR_QUANTIFIER_TOO_BIG
	REGEX_ERROR_UNTERMINATED_CHARACTER_CLASS = C.G_REGEX_ERROR_UNTERMINATED_CHARACTER_CLASS
	REGEX_ERROR_INVALID_ESCAPE_IN_CHARACTER_CLASS = C.G_REGEX_ERROR_INVALID_ESCAPE_IN_CHARACTER_CLASS
	REGEX_ERROR_RANGE_OUT_OF_ORDER = C.G_REGEX_ERROR_RANGE_OUT_OF_ORDER
	REGEX_ERROR_NOTHING_TO_REPEAT = C.G_REGEX_ERROR_NOTHING_TO_REPEAT
	REGEX_ERROR_UNRECOGNIZED_CHARACTER = C.G_REGEX_ERROR_UNRECOGNIZED_CHARACTER
	REGEX_ERROR_POSIX_NAMED_CLASS_OUTSIDE_CLASS = C.G_REGEX_ERROR_POSIX_NAMED_CLASS_OUTSIDE_CLASS
	REGEX_ERROR_UNMATCHED_PARENTHESIS = C.G_REGEX_ERROR_UNMATCHED_PARENTHESIS
	REGEX_ERROR_INEXISTENT_SUBPATTERN_REFERENCE = C.G_REGEX_ERROR_INEXISTENT_SUBPATTERN_REFERENCE
	REGEX_ERROR_UNTERMINATED_COMMENT = C.G_REGEX_ERROR_UNTERMINATED_COMMENT
	REGEX_ERROR_EXPRESSION_TOO_LARGE = C.G_REGEX_ERROR_EXPRESSION_TOO_LARGE
	REGEX_ERROR_MEMORY_ERROR = C.G_REGEX_ERROR_MEMORY_ERROR
	REGEX_ERROR_VARIABLE_LENGTH_LOOKBEHIND = C.G_REGEX_ERROR_VARIABLE_LENGTH_LOOKBEHIND
	REGEX_ERROR_MALFORMED_CONDITION = C.G_REGEX_ERROR_MALFORMED_CONDITION
	REGEX_ERROR_TOO_MANY_CONDITIONAL_BRANCHES = C.G_REGEX_ERROR_TOO_MANY_CONDITIONAL_BRANCHES
	REGEX_ERROR_ASSERTION_EXPECTED = C.G_REGEX_ERROR_ASSERTION_EXPECTED
	REGEX_ERROR_UNKNOWN_POSIX_CLASS_NAME = C.G_REGEX_ERROR_UNKNOWN_POSIX_CLASS_NAME
	REGEX_ERROR_POSIX_COLLATING_ELEMENTS_NOT_SUPPORTED = C.G_REGEX_ERROR_POSIX_COLLATING_ELEMENTS_NOT_SUPPORTED
	REGEX_ERROR_HEX_CODE_TOO_LARGE = C.G_REGEX_ERROR_HEX_CODE_TOO_LARGE
	REGEX_ERROR_INVALID_CONDITION = C.G_REGEX_ERROR_INVALID_CONDITION
	REGEX_ERROR_SINGLE_BYTE_MATCH_IN_LOOKBEHIND = C.G_REGEX_ERROR_SINGLE_BYTE_MATCH_IN_LOOKBEHIND
	REGEX_ERROR_INFINITE_LOOP = C.G_REGEX_ERROR_INFINITE_LOOP
	REGEX_ERROR_MISSING_SUBPATTERN_NAME_TERMINATOR = C.G_REGEX_ERROR_MISSING_SUBPATTERN_NAME_TERMINATOR
	REGEX_ERROR_DUPLICATE_SUBPATTERN_NAME = C.G_REGEX_ERROR_DUPLICATE_SUBPATTERN_NAME
	REGEX_ERROR_MALFORMED_PROPERTY = C.G_REGEX_ERROR_MALFORMED_PROPERTY
	REGEX_ERROR_UNKNOWN_PROPERTY = C.G_REGEX_ERROR_UNKNOWN_PROPERTY
	REGEX_ERROR_SUBPATTERN_NAME_TOO_LONG = C.G_REGEX_ERROR_SUBPATTERN_NAME_TOO_LONG
	REGEX_ERROR_TOO_MANY_SUBPATTERNS = C.G_REGEX_ERROR_TOO_MANY_SUBPATTERNS
	REGEX_ERROR_INVALID_OCTAL_VALUE = C.G_REGEX_ERROR_INVALID_OCTAL_VALUE
	REGEX_ERROR_TOO_MANY_BRANCHES_IN_DEFINE = C.G_REGEX_ERROR_TOO_MANY_BRANCHES_IN_DEFINE
	REGEX_ERROR_DEFINE_REPETION = C.G_REGEX_ERROR_DEFINE_REPETION
	REGEX_ERROR_INCONSISTENT_NEWLINE_OPTIONS = C.G_REGEX_ERROR_INCONSISTENT_NEWLINE_OPTIONS
	REGEX_ERROR_MISSING_BACK_REFERENCE = C.G_REGEX_ERROR_MISSING_BACK_REFERENCE
	REGEX_ERROR_INVALID_RELATIVE_REFERENCE = C.G_REGEX_ERROR_INVALID_RELATIVE_REFERENCE
	REGEX_ERROR_BACKTRACKING_CONTROL_VERB_ARGUMENT_FORBIDDEN = C.G_REGEX_ERROR_BACKTRACKING_CONTROL_VERB_ARGUMENT_FORBIDDEN
	REGEX_ERROR_UNKNOWN_BACKTRACKING_CONTROL_VERB = C.G_REGEX_ERROR_UNKNOWN_BACKTRACKING_CONTROL_VERB
	REGEX_ERROR_NUMBER_TOO_BIG = C.G_REGEX_ERROR_NUMBER_TOO_BIG
	REGEX_ERROR_MISSING_SUBPATTERN_NAME = C.G_REGEX_ERROR_MISSING_SUBPATTERN_NAME
	REGEX_ERROR_MISSING_DIGIT = C.G_REGEX_ERROR_MISSING_DIGIT
	REGEX_ERROR_INVALID_DATA_CHARACTER = C.G_REGEX_ERROR_INVALID_DATA_CHARACTER
	REGEX_ERROR_EXTRA_SUBPATTERN_NAME = C.G_REGEX_ERROR_EXTRA_SUBPATTERN_NAME
	REGEX_ERROR_BACKTRACKING_CONTROL_VERB_ARGUMENT_REQUIRED = C.G_REGEX_ERROR_BACKTRACKING_CONTROL_VERB_ARGUMENT_REQUIRED
	REGEX_ERROR_INVALID_CONTROL_CHAR = C.G_REGEX_ERROR_INVALID_CONTROL_CHAR
	REGEX_ERROR_MISSING_NAME = C.G_REGEX_ERROR_MISSING_NAME
	REGEX_ERROR_NOT_SUPPORTED_IN_CLASS = C.G_REGEX_ERROR_NOT_SUPPORTED_IN_CLASS
	REGEX_ERROR_TOO_MANY_FORWARD_REFERENCES = C.G_REGEX_ERROR_TOO_MANY_FORWARD_REFERENCES
	REGEX_ERROR_NAME_TOO_LONG = C.G_REGEX_ERROR_NAME_TOO_LONG
	REGEX_ERROR_CHARACTER_VALUE_TOO_LARGE = C.G_REGEX_ERROR_CHARACTER_VALUE_TOO_LARGE
	SEEK_CUR = C.G_SEEK_CUR
	SEEK_SET = C.G_SEEK_SET
	SEEK_END = C.G_SEEK_END
	SHELL_ERROR_BAD_QUOTING = C.G_SHELL_ERROR_BAD_QUOTING
	SHELL_ERROR_EMPTY_STRING = C.G_SHELL_ERROR_EMPTY_STRING
	SHELL_ERROR_FAILED = C.G_SHELL_ERROR_FAILED
	SLICE_CONFIG_ALWAYS_MALLOC = C.G_SLICE_CONFIG_ALWAYS_MALLOC
	SLICE_CONFIG_BYPASS_MAGAZINES = C.G_SLICE_CONFIG_BYPASS_MAGAZINES
	SLICE_CONFIG_WORKING_SET_MSECS = C.G_SLICE_CONFIG_WORKING_SET_MSECS
	SLICE_CONFIG_COLOR_INCREMENT = C.G_SLICE_CONFIG_COLOR_INCREMENT
	SLICE_CONFIG_CHUNK_SIZES = C.G_SLICE_CONFIG_CHUNK_SIZES
	SLICE_CONFIG_CONTENTION_COUNTER = C.G_SLICE_CONFIG_CONTENTION_COUNTER
	SPAWN_ERROR_FORK = C.G_SPAWN_ERROR_FORK
	SPAWN_ERROR_READ = C.G_SPAWN_ERROR_READ
	SPAWN_ERROR_CHDIR = C.G_SPAWN_ERROR_CHDIR
	SPAWN_ERROR_ACCES = C.G_SPAWN_ERROR_ACCES
	SPAWN_ERROR_PERM = C.G_SPAWN_ERROR_PERM
	SPAWN_ERROR_TOO_BIG = C.G_SPAWN_ERROR_TOO_BIG
	SPAWN_ERROR_2BIG = C.G_SPAWN_ERROR_2BIG
	SPAWN_ERROR_NOEXEC = C.G_SPAWN_ERROR_NOEXEC
	SPAWN_ERROR_NAMETOOLONG = C.G_SPAWN_ERROR_NAMETOOLONG
	SPAWN_ERROR_NOENT = C.G_SPAWN_ERROR_NOENT
	SPAWN_ERROR_NOMEM = C.G_SPAWN_ERROR_NOMEM
	SPAWN_ERROR_NOTDIR = C.G_SPAWN_ERROR_NOTDIR
	SPAWN_ERROR_LOOP = C.G_SPAWN_ERROR_LOOP
	SPAWN_ERROR_TXTBUSY = C.G_SPAWN_ERROR_TXTBUSY
	SPAWN_ERROR_IO = C.G_SPAWN_ERROR_IO
	SPAWN_ERROR_NFILE = C.G_SPAWN_ERROR_NFILE
	SPAWN_ERROR_MFILE = C.G_SPAWN_ERROR_MFILE
	SPAWN_ERROR_INVAL = C.G_SPAWN_ERROR_INVAL
	SPAWN_ERROR_ISDIR = C.G_SPAWN_ERROR_ISDIR
	SPAWN_ERROR_LIBBAD = C.G_SPAWN_ERROR_LIBBAD
	SPAWN_ERROR_FAILED = C.G_SPAWN_ERROR_FAILED
	TEST_LOG_NONE = C.G_TEST_LOG_NONE
	TEST_LOG_ERROR = C.G_TEST_LOG_ERROR
	TEST_LOG_START_BINARY = C.G_TEST_LOG_START_BINARY
	TEST_LOG_LIST_CASE = C.G_TEST_LOG_LIST_CASE
	TEST_LOG_SKIP_CASE = C.G_TEST_LOG_SKIP_CASE
	TEST_LOG_START_CASE = C.G_TEST_LOG_START_CASE
	TEST_LOG_STOP_CASE = C.G_TEST_LOG_STOP_CASE
	TEST_LOG_MIN_RESULT = C.G_TEST_LOG_MIN_RESULT
	TEST_LOG_MAX_RESULT = C.G_TEST_LOG_MAX_RESULT
	TEST_LOG_MESSAGE = C.G_TEST_LOG_MESSAGE
	THREAD_ERROR_AGAIN = C.G_THREAD_ERROR_AGAIN
	TIME_TYPE_STANDARD = C.G_TIME_TYPE_STANDARD
	TIME_TYPE_DAYLIGHT = C.G_TIME_TYPE_DAYLIGHT
	TIME_TYPE_UNIVERSAL = C.G_TIME_TYPE_UNIVERSAL
	TOKEN_EOF = C.G_TOKEN_EOF
	TOKEN_LEFT_PAREN = C.G_TOKEN_LEFT_PAREN
	TOKEN_RIGHT_PAREN = C.G_TOKEN_RIGHT_PAREN
	TOKEN_LEFT_CURLY = C.G_TOKEN_LEFT_CURLY
	TOKEN_RIGHT_CURLY = C.G_TOKEN_RIGHT_CURLY
	TOKEN_LEFT_BRACE = C.G_TOKEN_LEFT_BRACE
	TOKEN_RIGHT_BRACE = C.G_TOKEN_RIGHT_BRACE
	TOKEN_EQUAL_SIGN = C.G_TOKEN_EQUAL_SIGN
	TOKEN_COMMA = C.G_TOKEN_COMMA
	TOKEN_NONE = C.G_TOKEN_NONE
	TOKEN_ERROR = C.G_TOKEN_ERROR
	TOKEN_CHAR = C.G_TOKEN_CHAR
	TOKEN_BINARY = C.G_TOKEN_BINARY
	TOKEN_OCTAL = C.G_TOKEN_OCTAL
	TOKEN_INT = C.G_TOKEN_INT
	TOKEN_HEX = C.G_TOKEN_HEX
	TOKEN_FLOAT = C.G_TOKEN_FLOAT
	TOKEN_STRING = C.G_TOKEN_STRING
	TOKEN_SYMBOL = C.G_TOKEN_SYMBOL
	TOKEN_IDENTIFIER = C.G_TOKEN_IDENTIFIER
	TOKEN_IDENTIFIER_NULL = C.G_TOKEN_IDENTIFIER_NULL
	TOKEN_COMMENT_SINGLE = C.G_TOKEN_COMMENT_SINGLE
	TOKEN_COMMENT_MULTI = C.G_TOKEN_COMMENT_MULTI
	IN_ORDER = C.G_IN_ORDER
	PRE_ORDER = C.G_PRE_ORDER
	POST_ORDER = C.G_POST_ORDER
	LEVEL_ORDER = C.G_LEVEL_ORDER
	UNICODE_BREAK_MANDATORY = C.G_UNICODE_BREAK_MANDATORY
	UNICODE_BREAK_CARRIAGE_RETURN = C.G_UNICODE_BREAK_CARRIAGE_RETURN
	UNICODE_BREAK_LINE_FEED = C.G_UNICODE_BREAK_LINE_FEED
	UNICODE_BREAK_COMBINING_MARK = C.G_UNICODE_BREAK_COMBINING_MARK
	UNICODE_BREAK_SURROGATE = C.G_UNICODE_BREAK_SURROGATE
	UNICODE_BREAK_ZERO_WIDTH_SPACE = C.G_UNICODE_BREAK_ZERO_WIDTH_SPACE
	UNICODE_BREAK_INSEPARABLE = C.G_UNICODE_BREAK_INSEPARABLE
	UNICODE_BREAK_NON_BREAKING_GLUE = C.G_UNICODE_BREAK_NON_BREAKING_GLUE
	UNICODE_BREAK_CONTINGENT = C.G_UNICODE_BREAK_CONTINGENT
	UNICODE_BREAK_SPACE = C.G_UNICODE_BREAK_SPACE
	UNICODE_BREAK_AFTER = C.G_UNICODE_BREAK_AFTER
	UNICODE_BREAK_BEFORE = C.G_UNICODE_BREAK_BEFORE
	UNICODE_BREAK_BEFORE_AND_AFTER = C.G_UNICODE_BREAK_BEFORE_AND_AFTER
	UNICODE_BREAK_HYPHEN = C.G_UNICODE_BREAK_HYPHEN
	UNICODE_BREAK_NON_STARTER = C.G_UNICODE_BREAK_NON_STARTER
	UNICODE_BREAK_OPEN_PUNCTUATION = C.G_UNICODE_BREAK_OPEN_PUNCTUATION
	UNICODE_BREAK_CLOSE_PUNCTUATION = C.G_UNICODE_BREAK_CLOSE_PUNCTUATION
	UNICODE_BREAK_QUOTATION = C.G_UNICODE_BREAK_QUOTATION
	UNICODE_BREAK_EXCLAMATION = C.G_UNICODE_BREAK_EXCLAMATION
	UNICODE_BREAK_IDEOGRAPHIC = C.G_UNICODE_BREAK_IDEOGRAPHIC
	UNICODE_BREAK_NUMERIC = C.G_UNICODE_BREAK_NUMERIC
	UNICODE_BREAK_INFIX_SEPARATOR = C.G_UNICODE_BREAK_INFIX_SEPARATOR
	UNICODE_BREAK_SYMBOL = C.G_UNICODE_BREAK_SYMBOL
	UNICODE_BREAK_ALPHABETIC = C.G_UNICODE_BREAK_ALPHABETIC
	UNICODE_BREAK_PREFIX = C.G_UNICODE_BREAK_PREFIX
	UNICODE_BREAK_POSTFIX = C.G_UNICODE_BREAK_POSTFIX
	UNICODE_BREAK_COMPLEX_CONTEXT = C.G_UNICODE_BREAK_COMPLEX_CONTEXT
	UNICODE_BREAK_AMBIGUOUS = C.G_UNICODE_BREAK_AMBIGUOUS
	UNICODE_BREAK_UNKNOWN = C.G_UNICODE_BREAK_UNKNOWN
	UNICODE_BREAK_NEXT_LINE = C.G_UNICODE_BREAK_NEXT_LINE
	UNICODE_BREAK_WORD_JOINER = C.G_UNICODE_BREAK_WORD_JOINER
	UNICODE_BREAK_HANGUL_L_JAMO = C.G_UNICODE_BREAK_HANGUL_L_JAMO
	UNICODE_BREAK_HANGUL_V_JAMO = C.G_UNICODE_BREAK_HANGUL_V_JAMO
	UNICODE_BREAK_HANGUL_T_JAMO = C.G_UNICODE_BREAK_HANGUL_T_JAMO
	UNICODE_BREAK_HANGUL_LV_SYLLABLE = C.G_UNICODE_BREAK_HANGUL_LV_SYLLABLE
	UNICODE_BREAK_HANGUL_LVT_SYLLABLE = C.G_UNICODE_BREAK_HANGUL_LVT_SYLLABLE
	UNICODE_BREAK_CLOSE_PARANTHESIS = C.G_UNICODE_BREAK_CLOSE_PARANTHESIS
	UNICODE_BREAK_CONDITIONAL_JAPANESE_STARTER = C.G_UNICODE_BREAK_CONDITIONAL_JAPANESE_STARTER
	UNICODE_BREAK_HEBREW_LETTER = C.G_UNICODE_BREAK_HEBREW_LETTER
	UNICODE_BREAK_REGIONAL_INDICATOR = C.G_UNICODE_BREAK_REGIONAL_INDICATOR
	UNICODE_SCRIPT_INVALID_CODE = C.G_UNICODE_SCRIPT_INVALID_CODE
	UNICODE_SCRIPT_COMMON = C.G_UNICODE_SCRIPT_COMMON
	UNICODE_SCRIPT_INHERITED = C.G_UNICODE_SCRIPT_INHERITED
	UNICODE_SCRIPT_ARABIC = C.G_UNICODE_SCRIPT_ARABIC
	UNICODE_SCRIPT_ARMENIAN = C.G_UNICODE_SCRIPT_ARMENIAN
	UNICODE_SCRIPT_BENGALI = C.G_UNICODE_SCRIPT_BENGALI
	UNICODE_SCRIPT_BOPOMOFO = C.G_UNICODE_SCRIPT_BOPOMOFO
	UNICODE_SCRIPT_CHEROKEE = C.G_UNICODE_SCRIPT_CHEROKEE
	UNICODE_SCRIPT_COPTIC = C.G_UNICODE_SCRIPT_COPTIC
	UNICODE_SCRIPT_CYRILLIC = C.G_UNICODE_SCRIPT_CYRILLIC
	UNICODE_SCRIPT_DESERET = C.G_UNICODE_SCRIPT_DESERET
	UNICODE_SCRIPT_DEVANAGARI = C.G_UNICODE_SCRIPT_DEVANAGARI
	UNICODE_SCRIPT_ETHIOPIC = C.G_UNICODE_SCRIPT_ETHIOPIC
	UNICODE_SCRIPT_GEORGIAN = C.G_UNICODE_SCRIPT_GEORGIAN
	UNICODE_SCRIPT_GOTHIC = C.G_UNICODE_SCRIPT_GOTHIC
	UNICODE_SCRIPT_GREEK = C.G_UNICODE_SCRIPT_GREEK
	UNICODE_SCRIPT_GUJARATI = C.G_UNICODE_SCRIPT_GUJARATI
	UNICODE_SCRIPT_GURMUKHI = C.G_UNICODE_SCRIPT_GURMUKHI
	UNICODE_SCRIPT_HAN = C.G_UNICODE_SCRIPT_HAN
	UNICODE_SCRIPT_HANGUL = C.G_UNICODE_SCRIPT_HANGUL
	UNICODE_SCRIPT_HEBREW = C.G_UNICODE_SCRIPT_HEBREW
	UNICODE_SCRIPT_HIRAGANA = C.G_UNICODE_SCRIPT_HIRAGANA
	UNICODE_SCRIPT_KANNADA = C.G_UNICODE_SCRIPT_KANNADA
	UNICODE_SCRIPT_KATAKANA = C.G_UNICODE_SCRIPT_KATAKANA
	UNICODE_SCRIPT_KHMER = C.G_UNICODE_SCRIPT_KHMER
	UNICODE_SCRIPT_LAO = C.G_UNICODE_SCRIPT_LAO
	UNICODE_SCRIPT_LATIN = C.G_UNICODE_SCRIPT_LATIN
	UNICODE_SCRIPT_MALAYALAM = C.G_UNICODE_SCRIPT_MALAYALAM
	UNICODE_SCRIPT_MONGOLIAN = C.G_UNICODE_SCRIPT_MONGOLIAN
	UNICODE_SCRIPT_MYANMAR = C.G_UNICODE_SCRIPT_MYANMAR
	UNICODE_SCRIPT_OGHAM = C.G_UNICODE_SCRIPT_OGHAM
	UNICODE_SCRIPT_OLD_ITALIC = C.G_UNICODE_SCRIPT_OLD_ITALIC
	UNICODE_SCRIPT_ORIYA = C.G_UNICODE_SCRIPT_ORIYA
	UNICODE_SCRIPT_RUNIC = C.G_UNICODE_SCRIPT_RUNIC
	UNICODE_SCRIPT_SINHALA = C.G_UNICODE_SCRIPT_SINHALA
	UNICODE_SCRIPT_SYRIAC = C.G_UNICODE_SCRIPT_SYRIAC
	UNICODE_SCRIPT_TAMIL = C.G_UNICODE_SCRIPT_TAMIL
	UNICODE_SCRIPT_TELUGU = C.G_UNICODE_SCRIPT_TELUGU
	UNICODE_SCRIPT_THAANA = C.G_UNICODE_SCRIPT_THAANA
	UNICODE_SCRIPT_THAI = C.G_UNICODE_SCRIPT_THAI
	UNICODE_SCRIPT_TIBETAN = C.G_UNICODE_SCRIPT_TIBETAN
	UNICODE_SCRIPT_CANADIAN_ABORIGINAL = C.G_UNICODE_SCRIPT_CANADIAN_ABORIGINAL
	UNICODE_SCRIPT_YI = C.G_UNICODE_SCRIPT_YI
	UNICODE_SCRIPT_TAGALOG = C.G_UNICODE_SCRIPT_TAGALOG
	UNICODE_SCRIPT_HANUNOO = C.G_UNICODE_SCRIPT_HANUNOO
	UNICODE_SCRIPT_BUHID = C.G_UNICODE_SCRIPT_BUHID
	UNICODE_SCRIPT_TAGBANWA = C.G_UNICODE_SCRIPT_TAGBANWA
	UNICODE_SCRIPT_BRAILLE = C.G_UNICODE_SCRIPT_BRAILLE
	UNICODE_SCRIPT_CYPRIOT = C.G_UNICODE_SCRIPT_CYPRIOT
	UNICODE_SCRIPT_LIMBU = C.G_UNICODE_SCRIPT_LIMBU
	UNICODE_SCRIPT_OSMANYA = C.G_UNICODE_SCRIPT_OSMANYA
	UNICODE_SCRIPT_SHAVIAN = C.G_UNICODE_SCRIPT_SHAVIAN
	UNICODE_SCRIPT_LINEAR_B = C.G_UNICODE_SCRIPT_LINEAR_B
	UNICODE_SCRIPT_TAI_LE = C.G_UNICODE_SCRIPT_TAI_LE
	UNICODE_SCRIPT_UGARITIC = C.G_UNICODE_SCRIPT_UGARITIC
	UNICODE_SCRIPT_NEW_TAI_LUE = C.G_UNICODE_SCRIPT_NEW_TAI_LUE
	UNICODE_SCRIPT_BUGINESE = C.G_UNICODE_SCRIPT_BUGINESE
	UNICODE_SCRIPT_GLAGOLITIC = C.G_UNICODE_SCRIPT_GLAGOLITIC
	UNICODE_SCRIPT_TIFINAGH = C.G_UNICODE_SCRIPT_TIFINAGH
	UNICODE_SCRIPT_SYLOTI_NAGRI = C.G_UNICODE_SCRIPT_SYLOTI_NAGRI
	UNICODE_SCRIPT_OLD_PERSIAN = C.G_UNICODE_SCRIPT_OLD_PERSIAN
	UNICODE_SCRIPT_KHAROSHTHI = C.G_UNICODE_SCRIPT_KHAROSHTHI
	UNICODE_SCRIPT_UNKNOWN = C.G_UNICODE_SCRIPT_UNKNOWN
	UNICODE_SCRIPT_BALINESE = C.G_UNICODE_SCRIPT_BALINESE
	UNICODE_SCRIPT_CUNEIFORM = C.G_UNICODE_SCRIPT_CUNEIFORM
	UNICODE_SCRIPT_PHOENICIAN = C.G_UNICODE_SCRIPT_PHOENICIAN
	UNICODE_SCRIPT_PHAGS_PA = C.G_UNICODE_SCRIPT_PHAGS_PA
	UNICODE_SCRIPT_NKO = C.G_UNICODE_SCRIPT_NKO
	UNICODE_SCRIPT_KAYAH_LI = C.G_UNICODE_SCRIPT_KAYAH_LI
	UNICODE_SCRIPT_LEPCHA = C.G_UNICODE_SCRIPT_LEPCHA
	UNICODE_SCRIPT_REJANG = C.G_UNICODE_SCRIPT_REJANG
	UNICODE_SCRIPT_SUNDANESE = C.G_UNICODE_SCRIPT_SUNDANESE
	UNICODE_SCRIPT_SAURASHTRA = C.G_UNICODE_SCRIPT_SAURASHTRA
	UNICODE_SCRIPT_CHAM = C.G_UNICODE_SCRIPT_CHAM
	UNICODE_SCRIPT_OL_CHIKI = C.G_UNICODE_SCRIPT_OL_CHIKI
	UNICODE_SCRIPT_VAI = C.G_UNICODE_SCRIPT_VAI
	UNICODE_SCRIPT_CARIAN = C.G_UNICODE_SCRIPT_CARIAN
	UNICODE_SCRIPT_LYCIAN = C.G_UNICODE_SCRIPT_LYCIAN
	UNICODE_SCRIPT_LYDIAN = C.G_UNICODE_SCRIPT_LYDIAN
	UNICODE_SCRIPT_AVESTAN = C.G_UNICODE_SCRIPT_AVESTAN
	UNICODE_SCRIPT_BAMUM = C.G_UNICODE_SCRIPT_BAMUM
	UNICODE_SCRIPT_EGYPTIAN_HIEROGLYPHS = C.G_UNICODE_SCRIPT_EGYPTIAN_HIEROGLYPHS
	UNICODE_SCRIPT_IMPERIAL_ARAMAIC = C.G_UNICODE_SCRIPT_IMPERIAL_ARAMAIC
	UNICODE_SCRIPT_INSCRIPTIONAL_PAHLAVI = C.G_UNICODE_SCRIPT_INSCRIPTIONAL_PAHLAVI
	UNICODE_SCRIPT_INSCRIPTIONAL_PARTHIAN = C.G_UNICODE_SCRIPT_INSCRIPTIONAL_PARTHIAN
	UNICODE_SCRIPT_JAVANESE = C.G_UNICODE_SCRIPT_JAVANESE
	UNICODE_SCRIPT_KAITHI = C.G_UNICODE_SCRIPT_KAITHI
	UNICODE_SCRIPT_LISU = C.G_UNICODE_SCRIPT_LISU
	UNICODE_SCRIPT_MEETEI_MAYEK = C.G_UNICODE_SCRIPT_MEETEI_MAYEK
	UNICODE_SCRIPT_OLD_SOUTH_ARABIAN = C.G_UNICODE_SCRIPT_OLD_SOUTH_ARABIAN
	UNICODE_SCRIPT_OLD_TURKIC = C.G_UNICODE_SCRIPT_OLD_TURKIC
	UNICODE_SCRIPT_SAMARITAN = C.G_UNICODE_SCRIPT_SAMARITAN
	UNICODE_SCRIPT_TAI_THAM = C.G_UNICODE_SCRIPT_TAI_THAM
	UNICODE_SCRIPT_TAI_VIET = C.G_UNICODE_SCRIPT_TAI_VIET
	UNICODE_SCRIPT_BATAK = C.G_UNICODE_SCRIPT_BATAK
	UNICODE_SCRIPT_BRAHMI = C.G_UNICODE_SCRIPT_BRAHMI
	UNICODE_SCRIPT_MANDAIC = C.G_UNICODE_SCRIPT_MANDAIC
	UNICODE_SCRIPT_CHAKMA = C.G_UNICODE_SCRIPT_CHAKMA
	UNICODE_SCRIPT_MEROITIC_CURSIVE = C.G_UNICODE_SCRIPT_MEROITIC_CURSIVE
	UNICODE_SCRIPT_MEROITIC_HIEROGLYPHS = C.G_UNICODE_SCRIPT_MEROITIC_HIEROGLYPHS
	UNICODE_SCRIPT_MIAO = C.G_UNICODE_SCRIPT_MIAO
	UNICODE_SCRIPT_SHARADA = C.G_UNICODE_SCRIPT_SHARADA
	UNICODE_SCRIPT_SORA_SOMPENG = C.G_UNICODE_SCRIPT_SORA_SOMPENG
	UNICODE_SCRIPT_TAKRI = C.G_UNICODE_SCRIPT_TAKRI
	UNICODE_CONTROL = C.G_UNICODE_CONTROL
	UNICODE_FORMAT = C.G_UNICODE_FORMAT
	UNICODE_UNASSIGNED = C.G_UNICODE_UNASSIGNED
	UNICODE_PRIVATE_USE = C.G_UNICODE_PRIVATE_USE
	UNICODE_SURROGATE = C.G_UNICODE_SURROGATE
	UNICODE_LOWERCASE_LETTER = C.G_UNICODE_LOWERCASE_LETTER
	UNICODE_MODIFIER_LETTER = C.G_UNICODE_MODIFIER_LETTER
	UNICODE_OTHER_LETTER = C.G_UNICODE_OTHER_LETTER
	UNICODE_TITLECASE_LETTER = C.G_UNICODE_TITLECASE_LETTER
	UNICODE_UPPERCASE_LETTER = C.G_UNICODE_UPPERCASE_LETTER
	UNICODE_SPACING_MARK = C.G_UNICODE_SPACING_MARK
	UNICODE_ENCLOSING_MARK = C.G_UNICODE_ENCLOSING_MARK
	UNICODE_NON_SPACING_MARK = C.G_UNICODE_NON_SPACING_MARK
	UNICODE_DECIMAL_NUMBER = C.G_UNICODE_DECIMAL_NUMBER
	UNICODE_LETTER_NUMBER = C.G_UNICODE_LETTER_NUMBER
	UNICODE_OTHER_NUMBER = C.G_UNICODE_OTHER_NUMBER
	UNICODE_CONNECT_PUNCTUATION = C.G_UNICODE_CONNECT_PUNCTUATION
	UNICODE_DASH_PUNCTUATION = C.G_UNICODE_DASH_PUNCTUATION
	UNICODE_CLOSE_PUNCTUATION = C.G_UNICODE_CLOSE_PUNCTUATION
	UNICODE_FINAL_PUNCTUATION = C.G_UNICODE_FINAL_PUNCTUATION
	UNICODE_INITIAL_PUNCTUATION = C.G_UNICODE_INITIAL_PUNCTUATION
	UNICODE_OTHER_PUNCTUATION = C.G_UNICODE_OTHER_PUNCTUATION
	UNICODE_OPEN_PUNCTUATION = C.G_UNICODE_OPEN_PUNCTUATION
	UNICODE_CURRENCY_SYMBOL = C.G_UNICODE_CURRENCY_SYMBOL
	UNICODE_MODIFIER_SYMBOL = C.G_UNICODE_MODIFIER_SYMBOL
	UNICODE_MATH_SYMBOL = C.G_UNICODE_MATH_SYMBOL
	UNICODE_OTHER_SYMBOL = C.G_UNICODE_OTHER_SYMBOL
	UNICODE_LINE_SEPARATOR = C.G_UNICODE_LINE_SEPARATOR
	UNICODE_PARAGRAPH_SEPARATOR = C.G_UNICODE_PARAGRAPH_SEPARATOR
	UNICODE_SPACE_SEPARATOR = C.G_UNICODE_SPACE_SEPARATOR
	USER_DIRECTORY_DESKTOP = C.G_USER_DIRECTORY_DESKTOP
	USER_DIRECTORY_DOCUMENTS = C.G_USER_DIRECTORY_DOCUMENTS
	USER_DIRECTORY_DOWNLOAD = C.G_USER_DIRECTORY_DOWNLOAD
	USER_DIRECTORY_MUSIC = C.G_USER_DIRECTORY_MUSIC
	USER_DIRECTORY_PICTURES = C.G_USER_DIRECTORY_PICTURES
	USER_DIRECTORY_PUBLIC_SHARE = C.G_USER_DIRECTORY_PUBLIC_SHARE
	USER_DIRECTORY_TEMPLATES = C.G_USER_DIRECTORY_TEMPLATES
	USER_DIRECTORY_VIDEOS = C.G_USER_DIRECTORY_VIDEOS
	USER_N_DIRECTORIES = C.G_USER_N_DIRECTORIES
	VARIANT_CLASS_BOOLEAN = C.G_VARIANT_CLASS_BOOLEAN
	VARIANT_CLASS_BYTE = C.G_VARIANT_CLASS_BYTE
	VARIANT_CLASS_INT16 = C.G_VARIANT_CLASS_INT16
	VARIANT_CLASS_UINT16 = C.G_VARIANT_CLASS_UINT16
	VARIANT_CLASS_INT32 = C.G_VARIANT_CLASS_INT32
	VARIANT_CLASS_UINT32 = C.G_VARIANT_CLASS_UINT32
	VARIANT_CLASS_INT64 = C.G_VARIANT_CLASS_INT64
	VARIANT_CLASS_UINT64 = C.G_VARIANT_CLASS_UINT64
	VARIANT_CLASS_HANDLE = C.G_VARIANT_CLASS_HANDLE
	VARIANT_CLASS_DOUBLE = C.G_VARIANT_CLASS_DOUBLE
	VARIANT_CLASS_STRING = C.G_VARIANT_CLASS_STRING
	VARIANT_CLASS_OBJECT_PATH = C.G_VARIANT_CLASS_OBJECT_PATH
	VARIANT_CLASS_SIGNATURE = C.G_VARIANT_CLASS_SIGNATURE
	VARIANT_CLASS_VARIANT = C.G_VARIANT_CLASS_VARIANT
	VARIANT_CLASS_MAYBE = C.G_VARIANT_CLASS_MAYBE
	VARIANT_CLASS_ARRAY = C.G_VARIANT_CLASS_ARRAY
	VARIANT_CLASS_TUPLE = C.G_VARIANT_CLASS_TUPLE
	VARIANT_CLASS_DICT_ENTRY = C.G_VARIANT_CLASS_DICT_ENTRY
	VARIANT_PARSE_ERROR_FAILED = C.G_VARIANT_PARSE_ERROR_FAILED
	VARIANT_PARSE_ERROR_BASIC_TYPE_EXPECTED = C.G_VARIANT_PARSE_ERROR_BASIC_TYPE_EXPECTED
	VARIANT_PARSE_ERROR_CANNOT_INFER_TYPE = C.G_VARIANT_PARSE_ERROR_CANNOT_INFER_TYPE
	VARIANT_PARSE_ERROR_DEFINITE_TYPE_EXPECTED = C.G_VARIANT_PARSE_ERROR_DEFINITE_TYPE_EXPECTED
	VARIANT_PARSE_ERROR_INPUT_NOT_AT_END = C.G_VARIANT_PARSE_ERROR_INPUT_NOT_AT_END
	VARIANT_PARSE_ERROR_INVALID_CHARACTER = C.G_VARIANT_PARSE_ERROR_INVALID_CHARACTER
	VARIANT_PARSE_ERROR_INVALID_FORMAT_STRING = C.G_VARIANT_PARSE_ERROR_INVALID_FORMAT_STRING
	VARIANT_PARSE_ERROR_INVALID_OBJECT_PATH = C.G_VARIANT_PARSE_ERROR_INVALID_OBJECT_PATH
	VARIANT_PARSE_ERROR_INVALID_SIGNATURE = C.G_VARIANT_PARSE_ERROR_INVALID_SIGNATURE
	VARIANT_PARSE_ERROR_INVALID_TYPE_STRING = C.G_VARIANT_PARSE_ERROR_INVALID_TYPE_STRING
	VARIANT_PARSE_ERROR_NO_COMMON_TYPE = C.G_VARIANT_PARSE_ERROR_NO_COMMON_TYPE
	VARIANT_PARSE_ERROR_NUMBER_OUT_OF_RANGE = C.G_VARIANT_PARSE_ERROR_NUMBER_OUT_OF_RANGE
	VARIANT_PARSE_ERROR_NUMBER_TOO_BIG = C.G_VARIANT_PARSE_ERROR_NUMBER_TOO_BIG
	VARIANT_PARSE_ERROR_TYPE_ERROR = C.G_VARIANT_PARSE_ERROR_TYPE_ERROR
	VARIANT_PARSE_ERROR_UNEXPECTED_TOKEN = C.G_VARIANT_PARSE_ERROR_UNEXPECTED_TOKEN
	VARIANT_PARSE_ERROR_UNKNOWN_KEYWORD = C.G_VARIANT_PARSE_ERROR_UNKNOWN_KEYWORD
	VARIANT_PARSE_ERROR_UNTERMINATED_STRING_CONSTANT = C.G_VARIANT_PARSE_ERROR_UNTERMINATED_STRING_CONSTANT
	VARIANT_PARSE_ERROR_VALUE_EXPECTED = C.G_VARIANT_PARSE_ERROR_VALUE_EXPECTED
)
const (
	ASCII_DTOSTR_BUF_SIZE = C.G_ASCII_DTOSTR_BUF_SIZE
	BIG_ENDIAN = C.G_BIG_ENDIAN
	CAN_INLINE = C.G_CAN_INLINE
	CSET_A_2_Z = C.G_CSET_A_2_Z
	CSET_DIGITS = C.G_CSET_DIGITS
	CSET_a_2_z = C.G_CSET_a_2_z
	DATALIST_FLAGS_MASK = C.G_DATALIST_FLAGS_MASK
	DATE_BAD_DAY = C.G_DATE_BAD_DAY
	DATE_BAD_JULIAN = C.G_DATE_BAD_JULIAN
	DATE_BAD_YEAR = C.G_DATE_BAD_YEAR
	DIR_SEPARATOR = C.G_DIR_SEPARATOR
	DIR_SEPARATOR_S = C.G_DIR_SEPARATOR_S
	GINT16_FORMAT = C.G_GINT16_FORMAT
	GINT16_MODIFIER = C.G_GINT16_MODIFIER
	GINT32_FORMAT = C.G_GINT32_FORMAT
	GINT32_MODIFIER = C.G_GINT32_MODIFIER
	GINT64_FORMAT = C.G_GINT64_FORMAT
	GINT64_MODIFIER = C.G_GINT64_MODIFIER
	GINTPTR_FORMAT = C.G_GINTPTR_FORMAT
	GINTPTR_MODIFIER = C.G_GINTPTR_MODIFIER
	GNUC_FUNCTION = C.G_GNUC_FUNCTION
	GNUC_PRETTY_FUNCTION = C.G_GNUC_PRETTY_FUNCTION
	GSIZE_FORMAT = C.G_GSIZE_FORMAT
	GSIZE_MODIFIER = C.G_GSIZE_MODIFIER
	GSSIZE_FORMAT = C.G_GSSIZE_FORMAT
	GUINT16_FORMAT = C.G_GUINT16_FORMAT
	GUINT32_FORMAT = C.G_GUINT32_FORMAT
	GUINT64_FORMAT = C.G_GUINT64_FORMAT
	GUINTPTR_FORMAT = C.G_GUINTPTR_FORMAT
	HAVE_GINT64 = C.G_HAVE_GINT64
	HAVE_GNUC_VARARGS = C.G_HAVE_GNUC_VARARGS
	HAVE_GNUC_VISIBILITY = C.G_HAVE_GNUC_VISIBILITY
	HAVE_GROWING_STACK = C.G_HAVE_GROWING_STACK
	HAVE_INLINE = C.G_HAVE_INLINE
	HAVE_ISO_VARARGS = C.G_HAVE_ISO_VARARGS
	HAVE___INLINE = C.G_HAVE___INLINE
	HAVE___INLINE__ = C.G_HAVE___INLINE__
	HOOK_FLAG_USER_SHIFT = C.G_HOOK_FLAG_USER_SHIFT
	IEEE754_DOUBLE_BIAS = C.G_IEEE754_DOUBLE_BIAS
	IEEE754_FLOAT_BIAS = C.G_IEEE754_FLOAT_BIAS
	KEY_FILE_DESKTOP_GROUP = C.G_KEY_FILE_DESKTOP_GROUP
	KEY_FILE_DESKTOP_KEY_CATEGORIES = C.G_KEY_FILE_DESKTOP_KEY_CATEGORIES
	KEY_FILE_DESKTOP_KEY_COMMENT = C.G_KEY_FILE_DESKTOP_KEY_COMMENT
	KEY_FILE_DESKTOP_KEY_EXEC = C.G_KEY_FILE_DESKTOP_KEY_EXEC
	KEY_FILE_DESKTOP_KEY_GENERIC_NAME = C.G_KEY_FILE_DESKTOP_KEY_GENERIC_NAME
	KEY_FILE_DESKTOP_KEY_HIDDEN = C.G_KEY_FILE_DESKTOP_KEY_HIDDEN
	KEY_FILE_DESKTOP_KEY_ICON = C.G_KEY_FILE_DESKTOP_KEY_ICON
	KEY_FILE_DESKTOP_KEY_MIME_TYPE = C.G_KEY_FILE_DESKTOP_KEY_MIME_TYPE
	KEY_FILE_DESKTOP_KEY_NAME = C.G_KEY_FILE_DESKTOP_KEY_NAME
	KEY_FILE_DESKTOP_KEY_NOT_SHOW_IN = C.G_KEY_FILE_DESKTOP_KEY_NOT_SHOW_IN
	KEY_FILE_DESKTOP_KEY_NO_DISPLAY = C.G_KEY_FILE_DESKTOP_KEY_NO_DISPLAY
	KEY_FILE_DESKTOP_KEY_ONLY_SHOW_IN = C.G_KEY_FILE_DESKTOP_KEY_ONLY_SHOW_IN
	KEY_FILE_DESKTOP_KEY_PATH = C.G_KEY_FILE_DESKTOP_KEY_PATH
	KEY_FILE_DESKTOP_KEY_STARTUP_NOTIFY = C.G_KEY_FILE_DESKTOP_KEY_STARTUP_NOTIFY
	KEY_FILE_DESKTOP_KEY_STARTUP_WM_CLASS = C.G_KEY_FILE_DESKTOP_KEY_STARTUP_WM_CLASS
	KEY_FILE_DESKTOP_KEY_TERMINAL = C.G_KEY_FILE_DESKTOP_KEY_TERMINAL
	KEY_FILE_DESKTOP_KEY_TRY_EXEC = C.G_KEY_FILE_DESKTOP_KEY_TRY_EXEC
	KEY_FILE_DESKTOP_KEY_TYPE = C.G_KEY_FILE_DESKTOP_KEY_TYPE
	KEY_FILE_DESKTOP_KEY_URL = C.G_KEY_FILE_DESKTOP_KEY_URL
	KEY_FILE_DESKTOP_KEY_VERSION = C.G_KEY_FILE_DESKTOP_KEY_VERSION
	KEY_FILE_DESKTOP_TYPE_APPLICATION = C.G_KEY_FILE_DESKTOP_TYPE_APPLICATION
	KEY_FILE_DESKTOP_TYPE_DIRECTORY = C.G_KEY_FILE_DESKTOP_TYPE_DIRECTORY
	KEY_FILE_DESKTOP_TYPE_LINK = C.G_KEY_FILE_DESKTOP_TYPE_LINK
	LITTLE_ENDIAN = C.G_LITTLE_ENDIAN
	LOG_FATAL_MASK = C.G_LOG_FATAL_MASK
	LOG_LEVEL_USER_SHIFT = C.G_LOG_LEVEL_USER_SHIFT
	MAJOR_VERSION = C.GLIB_MAJOR_VERSION
	MAXINT16 = C.G_MAXINT16
	MAXINT32 = C.G_MAXINT32
	MAXINT64 = C.G_MAXINT64
	MAXINT8 = C.G_MAXINT8
	MAXUINT16 = C.G_MAXUINT16
	MAXUINT32 = C.G_MAXUINT32
	MAXUINT64 = C.G_MAXUINT64
	MAXUINT8 = C.G_MAXUINT8
	MICRO_VERSION = C.GLIB_MICRO_VERSION
	MININT16 = C.G_MININT16
	MININT32 = C.G_MININT32
	MININT64 = C.G_MININT64
	MININT8 = C.G_MININT8
	MINOR_VERSION = C.GLIB_MINOR_VERSION
	MODULE_SUFFIX = C.G_MODULE_SUFFIX
	OPTION_REMAINING = C.G_OPTION_REMAINING
	PDP_ENDIAN = C.G_PDP_ENDIAN
	POLLFD_FORMAT = C.G_POLLFD_FORMAT
	PRIORITY_DEFAULT = C.G_PRIORITY_DEFAULT
	PRIORITY_DEFAULT_IDLE = C.G_PRIORITY_DEFAULT_IDLE
	PRIORITY_HIGH = C.G_PRIORITY_HIGH
	PRIORITY_HIGH_IDLE = C.G_PRIORITY_HIGH_IDLE
	PRIORITY_LOW = C.G_PRIORITY_LOW
	SEARCHPATH_SEPARATOR = C.G_SEARCHPATH_SEPARATOR
	SEARCHPATH_SEPARATOR_S = C.G_SEARCHPATH_SEPARATOR_S
	SIZEOF_LONG = C.GLIB_SIZEOF_LONG
	SIZEOF_SIZE_T = C.GLIB_SIZEOF_SIZE_T
	SIZEOF_VOID_P = C.GLIB_SIZEOF_VOID_P
	STR_DELIMITERS = C.G_STR_DELIMITERS
	SYSDEF_AF_INET = C.GLIB_SYSDEF_AF_INET
	SYSDEF_AF_INET6 = C.GLIB_SYSDEF_AF_INET6
	SYSDEF_AF_UNIX = C.GLIB_SYSDEF_AF_UNIX
	SYSDEF_MSG_DONTROUTE = C.GLIB_SYSDEF_MSG_DONTROUTE
	SYSDEF_MSG_OOB = C.GLIB_SYSDEF_MSG_OOB
	SYSDEF_MSG_PEEK = C.GLIB_SYSDEF_MSG_PEEK
	TIME_SPAN_DAY = C.G_TIME_SPAN_DAY
	TIME_SPAN_HOUR = C.G_TIME_SPAN_HOUR
	TIME_SPAN_MILLISECOND = C.G_TIME_SPAN_MILLISECOND
	TIME_SPAN_MINUTE = C.G_TIME_SPAN_MINUTE
	TIME_SPAN_SECOND = C.G_TIME_SPAN_SECOND
	UNICHAR_MAX_DECOMPOSITION_LENGTH = C.G_UNICHAR_MAX_DECOMPOSITION_LENGTH
	URI_RESERVED_CHARS_GENERIC_DELIMITERS = C.G_URI_RESERVED_CHARS_GENERIC_DELIMITERS
	URI_RESERVED_CHARS_SUBCOMPONENT_DELIMITERS = C.G_URI_RESERVED_CHARS_SUBCOMPONENT_DELIMITERS
	USEC_PER_SEC = C.G_USEC_PER_SEC
	VA_COPY_AS_ARRAY = C.G_VA_COPY_AS_ARRAY
	VERSION_MIN_REQUIRED = C.GLIB_VERSION_MIN_REQUIRED
)
