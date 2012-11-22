package glib

// #cgo pkg-config: glib-2.0 gobject-2.0
// #include <glib-object.h>
// #include <glib/gstdio.h>
// #include <glib-unix.h>
// #include <glib.h>
/*
typedef long double longdouble;
int _g_access(void* filename, int mode) {
	return g_access((const gchar*)(filename), mode);
}
gchar* _g_ascii_formatd(gchar* buffer, gint buf_len, void* format, gdouble d) {
	return g_ascii_formatd(buffer, buf_len, (const gchar*)(format), d);
}
gint _g_ascii_strcasecmp(void* s1, void* s2) {
	return g_ascii_strcasecmp((const gchar*)(s1), (const gchar*)(s2));
}
gchar* _g_ascii_strdown(void* str, gssize _len) {
	return g_ascii_strdown((const gchar*)(str), _len);
}
gint _g_ascii_strncasecmp(void* s1, void* s2, gsize n) {
	return g_ascii_strncasecmp((const gchar*)(s1), (const gchar*)(s2), n);
}
gdouble _g_ascii_strtod(void* nptr, void* endptr) {
	return g_ascii_strtod((const gchar*)(nptr), (gchar**)(endptr));
}
gint64 _g_ascii_strtoll(void* nptr, void* endptr, guint base) {
	return g_ascii_strtoll((const gchar*)(nptr), (gchar**)(endptr), base);
}
guint64 _g_ascii_strtoull(void* nptr, void* endptr, guint base) {
	return g_ascii_strtoull((const gchar*)(nptr), (gchar**)(endptr), base);
}
gchar* _g_ascii_strup(void* str, gssize _len) {
	return g_ascii_strup((const gchar*)(str), _len);
}
void _g_assertion_message(void* domain, void* file, int line, void* _func, void* message) {
	g_assertion_message((const char*)(domain), (const char*)(file), line, (const char*)(_func), (const char*)(message));
}
void _g_assertion_message_cmpstr(void* domain, void* file, int line, void* _func, void* expr, void* arg1, void* cmp, void* arg2) {
	g_assertion_message_cmpstr((const char*)(domain), (const char*)(file), line, (const char*)(_func), (const char*)(expr), (const char*)(arg1), (const char*)(cmp), (const char*)(arg2));
}
void _g_assertion_message_error(void* domain, void* file, int line, void* _func, void* expr, void* error, GQuark error_domain, int error_code) {
	g_assertion_message_error((const char*)(domain), (const char*)(file), line, (const char*)(_func), (const char*)(expr), (const GError*)(error), error_domain, error_code);
}
void _g_assertion_message_expr(void* domain, void* file, int line, void* _func, void* expr) {
	g_assertion_message_expr((const char*)(domain), (const char*)(file), line, (const char*)(_func), (const char*)(expr));
}
guchar* _g_base64_decode(void* text, gsize* out_len) {
	return g_base64_decode((const gchar*)(text), out_len);
}
gchar* _g_build_filenamev(void* args) {
	return g_build_filenamev((gchar**)(args));
}
gchar* _g_build_pathv(void* separator, void* args) {
	return g_build_pathv((const gchar*)(separator), (gchar**)(args));
}
int _g_chdir(void* path) {
	return g_chdir((const gchar*)(path));
}
void _g_clear_error(void* err) {
	g_clear_error((GError**)(err));
}
gchar* _g_compute_checksum_for_data(GChecksumType checksum_type, void* data, gsize length) {
	return g_compute_checksum_for_data(checksum_type, (const guchar*)(data), length);
}
gchar* _g_compute_checksum_for_string(GChecksumType checksum_type, void* str, gssize length) {
	return g_compute_checksum_for_string(checksum_type, (const gchar*)(str), length);
}
gchar* _g_compute_hmac_for_data(GChecksumType digest_type, guchar* key, gsize key_len, void* data, gsize length) {
	return g_compute_hmac_for_data(digest_type, key, key_len, (const guchar*)(data), length);
}
gchar* _g_compute_hmac_for_string(GChecksumType digest_type, guchar* key, gsize key_len, void* str, gssize length) {
	return g_compute_hmac_for_string(digest_type, key, key_len, (const gchar*)(str), length);
}
gchar* _g_convert(void* str, gssize _len, void* to_codeset, void* from_codeset, gsize* bytes_read, gsize* bytes_written, void* err) {
	return g_convert((const gchar*)(str), _len, (const gchar*)(to_codeset), (const gchar*)(from_codeset), bytes_read, bytes_written, (GError**)(err));
}
gchar* _g_convert_with_fallback(void* str, gssize _len, void* to_codeset, void* from_codeset, void* fallback, gsize* bytes_read, gsize* bytes_written, void* err) {
	return g_convert_with_fallback((const gchar*)(str), _len, (const gchar*)(to_codeset), (const gchar*)(from_codeset), (const gchar*)(fallback), bytes_read, bytes_written, (GError**)(err));
}
gchar* _g_convert_with_iconv(void* str, gssize _len, GIConv converter, gsize* bytes_read, gsize* bytes_written, void* err) {
	return g_convert_with_iconv((const gchar*)(str), _len, converter, bytes_read, bytes_written, (GError**)(err));
}
void _g_datalist_clear(void* datalist) {
	g_datalist_clear((GData**)(datalist));
}
void _g_datalist_foreach(void* datalist, GDataForeachFunc _func, gpointer user_data) {
	g_datalist_foreach((GData**)(datalist), _func, user_data);
}
gpointer _g_datalist_get_data(void* datalist, void* key) {
	return g_datalist_get_data((GData**)(datalist), (const gchar*)(key));
}
guint _g_datalist_get_flags(void* datalist) {
	return g_datalist_get_flags((GData**)(datalist));
}
gpointer _g_datalist_id_dup_data(void* datalist, GQuark key_id, GDuplicateFunc dup_func, gpointer user_data) {
	return g_datalist_id_dup_data((GData**)(datalist), key_id, dup_func, user_data);
}
gpointer _g_datalist_id_get_data(void* datalist, GQuark key_id) {
	return g_datalist_id_get_data((GData**)(datalist), key_id);
}
gpointer _g_datalist_id_remove_no_notify(void* datalist, GQuark key_id) {
	return g_datalist_id_remove_no_notify((GData**)(datalist), key_id);
}
gboolean _g_datalist_id_replace_data(void* datalist, GQuark key_id, gpointer oldval, gpointer newval, GDestroyNotify destroy, GDestroyNotify* old_destroy) {
	return g_datalist_id_replace_data((GData**)(datalist), key_id, oldval, newval, destroy, old_destroy);
}
void _g_datalist_id_set_data_full(void* datalist, GQuark key_id, gpointer data, GDestroyNotify destroy_func) {
	g_datalist_id_set_data_full((GData**)(datalist), key_id, data, destroy_func);
}
void _g_datalist_init(void* datalist) {
	g_datalist_init((GData**)(datalist));
}
void _g_datalist_set_flags(void* datalist, guint flags) {
	g_datalist_set_flags((GData**)(datalist), flags);
}
void _g_datalist_unset_flags(void* datalist, guint flags) {
	g_datalist_unset_flags((GData**)(datalist), flags);
}
gsize _g_date_strftime(gchar* s, gsize slen, void* format, void* date) {
	return g_date_strftime(s, slen, (const gchar*)(format), (const GDate*)(date));
}
const gchar* _g_dcgettext(void* domain, void* msgid, gint category) {
	return g_dcgettext((const gchar*)(domain), (const gchar*)(msgid), category);
}
const gchar* _g_dgettext(void* domain, void* msgid) {
	return g_dgettext((const gchar*)(domain), (const gchar*)(msgid));
}
gchar* _g_dir_make_tmp(gchar* tmpl, void* err) {
	return g_dir_make_tmp(tmpl, (GError**)(err));
}
const gchar* _g_dngettext(void* domain, void* msgid, void* msgid_plural, gulong n) {
	return g_dngettext((const gchar*)(domain), (const gchar*)(msgid), (const gchar*)(msgid_plural), n);
}
const gchar* _g_dpgettext(void* domain, void* msgctxtid, gsize msgidoffset) {
	return g_dpgettext((const gchar*)(domain), (const gchar*)(msgctxtid), msgidoffset);
}
const gchar* _g_dpgettext2(void* domain, void* context, void* msgid) {
	return g_dpgettext2((const gchar*)(domain), (const gchar*)(context), (const gchar*)(msgid));
}
const gchar* _g_environ_getenv(void* envp, void* variable) {
	return g_environ_getenv((gchar**)(envp), (const gchar*)(variable));
}
gchar** _g_environ_setenv(void* envp, void* variable, void* value, gboolean overwrite) {
	return g_environ_setenv((gchar**)(envp), (const gchar*)(variable), (const gchar*)(value), overwrite);
}
gchar** _g_environ_unsetenv(void* envp, void* variable) {
	return g_environ_unsetenv((gchar**)(envp), (const gchar*)(variable));
}
gboolean _g_file_get_contents(gchar* filename, void* contents, gsize* length, void* err) {
	return g_file_get_contents(filename, (gchar**)(contents), length, (GError**)(err));
}
gint _g_file_open_tmp(gchar* tmpl, void* name_used, void* err) {
	return g_file_open_tmp(tmpl, (gchar**)(name_used), (GError**)(err));
}
gchar* _g_file_read_link(void* filename, void* err) {
	return g_file_read_link((const gchar*)(filename), (GError**)(err));
}
gboolean _g_file_set_contents(gchar* filename, gchar* contents, gssize length, void* err) {
	return g_file_set_contents(filename, contents, length, (GError**)(err));
}
gboolean _g_file_test(void* filename, GFileTest test) {
	return g_file_test((const gchar*)(filename), test);
}
gchar* _g_filename_display_basename(void* filename) {
	return g_filename_display_basename((const gchar*)(filename));
}
gchar* _g_filename_display_name(void* filename) {
	return g_filename_display_name((const gchar*)(filename));
}
gchar* _g_filename_from_uri(void* uri, void* hostname, void* err) {
	return g_filename_from_uri((const gchar*)(uri), (gchar**)(hostname), (GError**)(err));
}
gchar* _g_filename_from_utf8(void* utf8string, gssize _len, gsize* bytes_read, gsize* bytes_written, void* err) {
	return g_filename_from_utf8((const gchar*)(utf8string), _len, bytes_read, bytes_written, (GError**)(err));
}
gchar* _g_filename_to_uri(void* filename, void* hostname, void* err) {
	return g_filename_to_uri((const gchar*)(filename), (const gchar*)(hostname), (GError**)(err));
}
gchar* _g_filename_to_utf8(void* opsysstring, gssize _len, gsize* bytes_read, gsize* bytes_written, void* err) {
	return g_filename_to_utf8((const gchar*)(opsysstring), _len, bytes_read, bytes_written, (GError**)(err));
}
gchar* _g_find_program_in_path(void* program) {
	return g_find_program_in_path((const gchar*)(program));
}
gboolean _g_get_charset(void* charset) {
	return g_get_charset((const char**)(charset));
}
gboolean _g_get_filename_charsets(void* charsets) {
	return g_get_filename_charsets((const gchar***)(charsets));
}
gchar** _g_get_locale_variants(void* locale) {
	return g_get_locale_variants((const gchar*)(locale));
}
const gchar* _g_getenv(void* variable) {
	return g_getenv((const gchar*)(variable));
}
gboolean _g_hostname_is_ascii_encoded(void* hostname) {
	return g_hostname_is_ascii_encoded((const gchar*)(hostname));
}
gboolean _g_hostname_is_ip_address(void* hostname) {
	return g_hostname_is_ip_address((const gchar*)(hostname));
}
gboolean _g_hostname_is_non_ascii(void* hostname) {
	return g_hostname_is_non_ascii((const gchar*)(hostname));
}
gchar* _g_hostname_to_ascii(void* hostname) {
	return g_hostname_to_ascii((const gchar*)(hostname));
}
gchar* _g_hostname_to_unicode(void* hostname) {
	return g_hostname_to_unicode((const gchar*)(hostname));
}
const gchar* _g_intern_static_string(void* string) {
	return g_intern_static_string((const gchar*)(string));
}
const gchar* _g_intern_string(void* string) {
	return g_intern_string((const gchar*)(string));
}
gchar* _g_locale_from_utf8(void* utf8string, gssize _len, gsize* bytes_read, gsize* bytes_written, void* err) {
	return g_locale_from_utf8((const gchar*)(utf8string), _len, bytes_read, bytes_written, (GError**)(err));
}
gchar* _g_locale_to_utf8(void* opsysstring, gssize _len, gsize* bytes_read, gsize* bytes_written, void* err) {
	return g_locale_to_utf8((const gchar*)(opsysstring), _len, bytes_read, bytes_written, (GError**)(err));
}
void _g_log_default_handler(void* log_domain, GLogLevelFlags log_level, void* message, gpointer unused_data) {
	g_log_default_handler((const gchar*)(log_domain), log_level, (const gchar*)(message), unused_data);
}
void _g_log_remove_handler(void* log_domain, guint handler_id) {
	g_log_remove_handler((const gchar*)(log_domain), handler_id);
}
GLogLevelFlags _g_log_set_fatal_mask(void* log_domain, GLogLevelFlags fatal_mask) {
	return g_log_set_fatal_mask((const gchar*)(log_domain), fatal_mask);
}
guint _g_log_set_handler(void* log_domain, GLogLevelFlags log_levels, GLogFunc log_func, gpointer user_data) {
	return g_log_set_handler((const gchar*)(log_domain), log_levels, log_func, user_data);
}
gchar* _g_markup_escape_text(void* text, gssize length) {
	return g_markup_escape_text((const gchar*)(text), length);
}
gint _g_mkdir_with_parents(void* pathname, gint mode) {
	return g_mkdir_with_parents((const gchar*)(pathname), mode);
}
void _g_on_error_query(void* prg_name) {
	g_on_error_query((const gchar*)(prg_name));
}
void _g_on_error_stack_trace(void* prg_name) {
	g_on_error_stack_trace((const gchar*)(prg_name));
}
guint _g_parse_debug_string(void* string, GDebugKey* keys, guint nkeys) {
	return g_parse_debug_string((const gchar*)(string), keys, nkeys);
}
gchar* _g_path_get_basename(void* file_name) {
	return g_path_get_basename((const gchar*)(file_name));
}
gchar* _g_path_get_dirname(void* file_name) {
	return g_path_get_dirname((const gchar*)(file_name));
}
gboolean _g_path_is_absolute(void* file_name) {
	return g_path_is_absolute((const gchar*)(file_name));
}
const gchar* _g_path_skip_root(void* file_name) {
	return g_path_skip_root((const gchar*)(file_name));
}
gboolean _g_pattern_match(GPatternSpec* pspec, guint string_length, void* string, void* string_reversed) {
	return g_pattern_match(pspec, string_length, (const gchar*)(string), (const gchar*)(string_reversed));
}
gboolean _g_pattern_match_simple(void* pattern, void* string) {
	return g_pattern_match_simple((const gchar*)(pattern), (const gchar*)(string));
}
gboolean _g_pattern_match_string(GPatternSpec* pspec, void* string) {
	return g_pattern_match_string(pspec, (const gchar*)(string));
}
void _g_propagate_error(void* dest, GError* src) {
	g_propagate_error((GError**)(dest), src);
}
GQuark _g_quark_from_static_string(void* string) {
	return g_quark_from_static_string((const gchar*)(string));
}
GQuark _g_quark_from_string(void* string) {
	return g_quark_from_string((const gchar*)(string));
}
GQuark _g_quark_try_string(void* string) {
	return g_quark_try_string((const gchar*)(string));
}
gboolean _g_regex_check_replacement(void* replacement, gboolean* has_references, void* err) {
	return g_regex_check_replacement((const gchar*)(replacement), has_references, (GError**)(err));
}
gchar* _g_regex_escape_nul(void* string, gint length) {
	return g_regex_escape_nul((const gchar*)(string), length);
}
gboolean _g_regex_match_simple(void* pattern, void* string, GRegexCompileFlags compile_options, GRegexMatchFlags match_options) {
	return g_regex_match_simple((const gchar*)(pattern), (const gchar*)(string), compile_options, match_options);
}
gchar** _g_regex_split_simple(void* pattern, void* string, GRegexCompileFlags compile_options, GRegexMatchFlags match_options) {
	return g_regex_split_simple((const gchar*)(pattern), (const gchar*)(string), compile_options, match_options);
}
void _g_return_if_fail_warning(void* log_domain, void* pretty_function, void* expression) {
	g_return_if_fail_warning((const char*)(log_domain), (const char*)(pretty_function), (const char*)(expression));
}
int _g_rmdir(void* filename) {
	return g_rmdir((const gchar*)(filename));
}
void _g_set_application_name(void* application_name) {
	g_set_application_name((const gchar*)(application_name));
}
void _g_set_error_literal(void* err, GQuark domain, gint code, void* message) {
	g_set_error_literal((GError**)(err), domain, code, (const gchar*)(message));
}
void _g_set_prgname(void* prgname) {
	g_set_prgname((const gchar*)(prgname));
}
gboolean _g_setenv(void* variable, void* value, gboolean overwrite) {
	return g_setenv((const gchar*)(variable), (const gchar*)(value), overwrite);
}
gboolean _g_shell_parse_argv(void* command_line, gint* argcp, void* argvp, void* err) {
	return g_shell_parse_argv((const gchar*)(command_line), argcp, (gchar***)(argvp), (GError**)(err));
}
gchar* _g_shell_quote(void* unquoted_string) {
	return g_shell_quote((const gchar*)(unquoted_string));
}
gchar* _g_shell_unquote(void* quoted_string, void* err) {
	return g_shell_unquote((const gchar*)(quoted_string), (GError**)(err));
}
void _g_source_set_name_by_id(guint tag, void* name) {
	g_source_set_name_by_id(tag, (const char*)(name));
}
gboolean _g_spawn_async(void* working_directory, void* argv, void* envp, GSpawnFlags flags, GSpawnChildSetupFunc child_setup, gpointer user_data, GPid* child_pid, void* err) {
	return g_spawn_async((const gchar*)(working_directory), (gchar**)(argv), (gchar**)(envp), flags, child_setup, user_data, child_pid, (GError**)(err));
}
gboolean _g_spawn_async_with_pipes(void* working_directory, void* argv, void* envp, GSpawnFlags flags, GSpawnChildSetupFunc child_setup, gpointer user_data, GPid* child_pid, gint* standard_input, gint* standard_output, gint* standard_error, void* err) {
	return g_spawn_async_with_pipes((const gchar*)(working_directory), (gchar**)(argv), (gchar**)(envp), flags, child_setup, user_data, child_pid, standard_input, standard_output, standard_error, (GError**)(err));
}
gboolean _g_spawn_check_exit_status(gint exit_status, void* err) {
	return g_spawn_check_exit_status(exit_status, (GError**)(err));
}
gboolean _g_spawn_command_line_async(void* command_line, void* err) {
	return g_spawn_command_line_async((const gchar*)(command_line), (GError**)(err));
}
gboolean _g_spawn_command_line_sync(void* command_line, void* standard_output, void* standard_error, gint* exit_status, void* err) {
	return g_spawn_command_line_sync((const gchar*)(command_line), (gchar**)(standard_output), (gchar**)(standard_error), exit_status, (GError**)(err));
}
gboolean _g_spawn_sync(void* working_directory, void* argv, void* envp, GSpawnFlags flags, GSpawnChildSetupFunc child_setup, gpointer user_data, void* standard_output, void* standard_error, gint* exit_status, void* err) {
	return g_spawn_sync((const gchar*)(working_directory), (gchar**)(argv), (gchar**)(envp), flags, child_setup, user_data, (gchar**)(standard_output), (gchar**)(standard_error), exit_status, (GError**)(err));
}
gchar* _g_stpcpy(gchar* dest, void* src) {
	return g_stpcpy(dest, (const char*)(src));
}
gboolean _g_str_has_prefix(void* str, void* prefix) {
	return g_str_has_prefix((const gchar*)(str), (const gchar*)(prefix));
}
gboolean _g_str_has_suffix(void* str, void* suffix) {
	return g_str_has_suffix((const gchar*)(str), (const gchar*)(suffix));
}
gchar* _g_strcanon(gchar* string, void* valid_chars, gchar substitutor) {
	return g_strcanon(string, (const gchar*)(valid_chars), substitutor);
}
int _g_strcmp0(void* str1, void* str2) {
	return g_strcmp0((const char*)(str1), (const char*)(str2));
}
gchar* _g_strcompress(void* source) {
	return g_strcompress((const gchar*)(source));
}
gchar* _g_strdelimit(gchar* string, void* delimiters, gchar new_delimiter) {
	return g_strdelimit(string, (const gchar*)(delimiters), new_delimiter);
}
gchar* _g_strdup(void* str) {
	return g_strdup((const gchar*)(str));
}
gchar** _g_strdupv(void* str_array) {
	return g_strdupv((gchar**)(str_array));
}
gchar* _g_strescape(void* source, void* exceptions) {
	return g_strescape((const gchar*)(source), (const gchar*)(exceptions));
}
void _g_strfreev(void* str_array) {
	g_strfreev((gchar**)(str_array));
}
GString* _g_string_new(void* init) {
	return g_string_new((const gchar*)(init));
}
GString* _g_string_new_len(void* init, gssize _len) {
	return g_string_new_len((const gchar*)(init), _len);
}
const gchar* _g_strip_context(void* msgid, void* msgval) {
	return g_strip_context((const gchar*)(msgid), (const gchar*)(msgval));
}
gchar* _g_strjoinv(void* separator, void* str_array) {
	return g_strjoinv((const gchar*)(separator), (gchar**)(str_array));
}
gsize _g_strlcat(gchar* dest, void* src, gsize dest_size) {
	return g_strlcat(dest, (const gchar*)(src), dest_size);
}
gsize _g_strlcpy(gchar* dest, void* src, gsize dest_size) {
	return g_strlcpy(dest, (const gchar*)(src), dest_size);
}
gchar* _g_strndup(void* str, gsize n) {
	return g_strndup((const gchar*)(str), n);
}
gchar* _g_strrstr(void* haystack, void* needle) {
	return g_strrstr((const gchar*)(haystack), (const gchar*)(needle));
}
gchar* _g_strrstr_len(void* haystack, gssize haystack_len, void* needle) {
	return g_strrstr_len((const gchar*)(haystack), haystack_len, (const gchar*)(needle));
}
gchar** _g_strsplit(void* string, void* delimiter, gint max_tokens) {
	return g_strsplit((const gchar*)(string), (const gchar*)(delimiter), max_tokens);
}
gchar** _g_strsplit_set(void* string, void* delimiters, gint max_tokens) {
	return g_strsplit_set((const gchar*)(string), (const gchar*)(delimiters), max_tokens);
}
gchar* _g_strstr_len(void* haystack, gssize haystack_len, void* needle) {
	return g_strstr_len((const gchar*)(haystack), haystack_len, (const gchar*)(needle));
}
gdouble _g_strtod(void* nptr, void* endptr) {
	return g_strtod((const gchar*)(nptr), (gchar**)(endptr));
}
guint _g_strv_length(void* str_array) {
	return g_strv_length((gchar**)(str_array));
}
void _g_test_add_data_func(void* testpath, gconstpointer test_data, GTestDataFunc test_func) {
	g_test_add_data_func((const char*)(testpath), test_data, test_func);
}
void _g_test_add_data_func_full(void* testpath, gpointer test_data, GTestDataFunc test_func, GDestroyNotify data_free_func) {
	g_test_add_data_func_full((const char*)(testpath), test_data, test_func, data_free_func);
}
void _g_test_add_func(void* testpath, GTestFunc test_func) {
	g_test_add_func((const char*)(testpath), test_func);
}
void _g_test_add_vtable(void* testpath, gsize data_size, gconstpointer test_data, GTestFixtureFunc data_setup, GTestFixtureFunc data_test, GTestFixtureFunc data_teardown) {
	g_test_add_vtable((const char*)(testpath), data_size, test_data, data_setup, data_test, data_teardown);
}
void _g_test_assert_expected_messages_internal(void* domain, void* file, int line, void* _func) {
	g_test_assert_expected_messages_internal((const char*)(domain), (const char*)(file), line, (const char*)(_func));
}
void _g_test_bug(void* bug_uri_snippet) {
	g_test_bug((const char*)(bug_uri_snippet));
}
void _g_test_bug_base(void* uri_pattern) {
	g_test_bug_base((const char*)(uri_pattern));
}
GTestCase* _g_test_create_case(void* test_name, gsize data_size, gconstpointer test_data, GTestFixtureFunc data_setup, GTestFixtureFunc data_test, GTestFixtureFunc data_teardown) {
	return g_test_create_case((const char*)(test_name), data_size, test_data, data_setup, data_test, data_teardown);
}
GTestSuite* _g_test_create_suite(void* suite_name) {
	return g_test_create_suite((const char*)(suite_name));
}
void _g_test_expect_message(void* log_domain, GLogLevelFlags log_level, void* pattern) {
	g_test_expect_message((const gchar*)(log_domain), log_level, (const gchar*)(pattern));
}
void _g_test_trap_assertions(void* domain, void* file, int line, void* _func, guint64 assertion_flags, void* pattern) {
	g_test_trap_assertions((const char*)(domain), (const char*)(file), line, (const char*)(_func), assertion_flags, (const char*)(pattern));
}
gboolean _g_time_val_from_iso8601(void* iso_date, GTimeVal* time_) {
	return g_time_val_from_iso8601((const gchar*)(iso_date), time_);
}
guint _g_trash_stack_height(void* stack_p) {
	return g_trash_stack_height((GTrashStack**)(stack_p));
}
void _g_trash_stack_push(void* stack_p, gpointer data_p) {
	g_trash_stack_push((GTrashStack**)(stack_p), data_p);
}
gunichar2* _g_ucs4_to_utf16(void* str, glong _len, glong* items_read, glong* items_written, void* err) {
	return g_ucs4_to_utf16((const gunichar*)(str), _len, items_read, items_written, (GError**)(err));
}
gchar* _g_ucs4_to_utf8(void* str, glong _len, glong* items_read, glong* items_written, void* err) {
	return g_ucs4_to_utf8((const gunichar*)(str), _len, items_read, items_written, (GError**)(err));
}
gboolean _g_unix_open_pipe(gint* fds, gint flags, void* err) {
	return g_unix_open_pipe(fds, flags, (GError**)(err));
}
gboolean _g_unix_set_fd_nonblocking(gint fd, gboolean nonblock, void* err) {
	return g_unix_set_fd_nonblocking(fd, nonblock, (GError**)(err));
}
int _g_unlink(void* filename) {
	return g_unlink((const gchar*)(filename));
}
void _g_unsetenv(void* variable) {
	g_unsetenv((const gchar*)(variable));
}
char* _g_uri_escape_string(void* unescaped, void* reserved_chars_allowed, gboolean allow_utf8) {
	return g_uri_escape_string((const char*)(unescaped), (const char*)(reserved_chars_allowed), allow_utf8);
}
gchar** _g_uri_list_extract_uris(void* uri_list) {
	return g_uri_list_extract_uris((const gchar*)(uri_list));
}
char* _g_uri_parse_scheme(void* uri) {
	return g_uri_parse_scheme((const char*)(uri));
}
char* _g_uri_unescape_segment(void* escaped_string, void* escaped_string_end, void* illegal_characters) {
	return g_uri_unescape_segment((const char*)(escaped_string), (const char*)(escaped_string_end), (const char*)(illegal_characters));
}
char* _g_uri_unescape_string(void* escaped_string, void* illegal_characters) {
	return g_uri_unescape_string((const char*)(escaped_string), (const char*)(illegal_characters));
}
gunichar* _g_utf16_to_ucs4(void* str, glong _len, glong* items_read, glong* items_written, void* err) {
	return g_utf16_to_ucs4((const gunichar2*)(str), _len, items_read, items_written, (GError**)(err));
}
gchar* _g_utf16_to_utf8(void* str, glong _len, glong* items_read, glong* items_written, void* err) {
	return g_utf16_to_utf8((const gunichar2*)(str), _len, items_read, items_written, (GError**)(err));
}
gchar* _g_utf8_casefold(void* str, gssize _len) {
	return g_utf8_casefold((const gchar*)(str), _len);
}
gint _g_utf8_collate(void* str1, void* str2) {
	return g_utf8_collate((const gchar*)(str1), (const gchar*)(str2));
}
gchar* _g_utf8_collate_key(void* str, gssize _len) {
	return g_utf8_collate_key((const gchar*)(str), _len);
}
gchar* _g_utf8_collate_key_for_filename(void* str, gssize _len) {
	return g_utf8_collate_key_for_filename((const gchar*)(str), _len);
}
gchar* _g_utf8_find_next_char(void* p, void* end) {
	return g_utf8_find_next_char((const gchar*)(p), (const gchar*)(end));
}
gchar* _g_utf8_find_prev_char(void* str, void* p) {
	return g_utf8_find_prev_char((const gchar*)(str), (const gchar*)(p));
}
gunichar _g_utf8_get_char(void* p) {
	return g_utf8_get_char((const gchar*)(p));
}
gunichar _g_utf8_get_char_validated(void* p, gssize max_len) {
	return g_utf8_get_char_validated((const gchar*)(p), max_len);
}
gchar* _g_utf8_normalize(void* str, gssize _len, GNormalizeMode mode) {
	return g_utf8_normalize((const gchar*)(str), _len, mode);
}
gchar* _g_utf8_offset_to_pointer(void* str, glong offset) {
	return g_utf8_offset_to_pointer((const gchar*)(str), offset);
}
glong _g_utf8_pointer_to_offset(void* str, void* pos) {
	return g_utf8_pointer_to_offset((const gchar*)(str), (const gchar*)(pos));
}
gchar* _g_utf8_prev_char(void* p) {
	return g_utf8_prev_char((const gchar*)(p));
}
gchar* _g_utf8_strchr(void* p, gssize _len, gunichar c) {
	return g_utf8_strchr((const gchar*)(p), _len, c);
}
gchar* _g_utf8_strdown(void* str, gssize _len) {
	return g_utf8_strdown((const gchar*)(str), _len);
}
glong _g_utf8_strlen(void* p, gssize max) {
	return g_utf8_strlen((const gchar*)(p), max);
}
gchar* _g_utf8_strncpy(gchar* dest, void* src, gsize n) {
	return g_utf8_strncpy(dest, (const gchar*)(src), n);
}
gchar* _g_utf8_strrchr(void* p, gssize _len, gunichar c) {
	return g_utf8_strrchr((const gchar*)(p), _len, c);
}
gchar* _g_utf8_strreverse(void* str, gssize _len) {
	return g_utf8_strreverse((const gchar*)(str), _len);
}
gchar* _g_utf8_strup(void* str, gssize _len) {
	return g_utf8_strup((const gchar*)(str), _len);
}
gchar* _g_utf8_substring(void* str, glong start_pos, glong end_pos) {
	return g_utf8_substring((const gchar*)(str), start_pos, end_pos);
}
gunichar* _g_utf8_to_ucs4(void* str, glong _len, glong* items_read, glong* items_written, void* err) {
	return g_utf8_to_ucs4((const gchar*)(str), _len, items_read, items_written, (GError**)(err));
}
gunichar* _g_utf8_to_ucs4_fast(void* str, glong _len, glong* items_written) {
	return g_utf8_to_ucs4_fast((const gchar*)(str), _len, items_written);
}
gunichar2* _g_utf8_to_utf16(void* str, glong _len, glong* items_read, glong* items_written, void* err) {
	return g_utf8_to_utf16((const gchar*)(str), _len, items_read, items_written, (GError**)(err));
}
gboolean _g_utf8_validate(gchar* str, gssize max_len, void* end) {
	return g_utf8_validate(str, max_len, (const gchar**)(end));
}
gboolean _g_variant_is_object_path(void* string) {
	return g_variant_is_object_path((const gchar*)(string));
}
gboolean _g_variant_is_signature(void* string) {
	return g_variant_is_signature((const gchar*)(string));
}
GVariant* _g_variant_parse(void* _type, void* text, void* limit, void* endptr, void* err) {
	return g_variant_parse((const GVariantType*)(_type), (const gchar*)(text), (const gchar*)(limit), (const gchar**)(endptr), (GError**)(err));
}
const GVariantType* _g_variant_type_checked_(void* arg_0) {
	return g_variant_type_checked_((const gchar*)(arg_0));
}
gboolean _g_variant_type_string_is_valid(void* type_string) {
	return g_variant_type_string_is_valid((const gchar*)(type_string));
}
gboolean _g_variant_type_string_scan(void* string, void* limit, void* endptr) {
	return g_variant_type_string_scan((const gchar*)(string), (const gchar*)(limit), (const gchar**)(endptr));
}
void _g_warn_message(void* domain, void* file, int line, void* _func, void* warnexpr) {
	g_warn_message((const char*)(domain), (const char*)(file), line, (const char*)(_func), (const char*)(warnexpr));
}
*/
import "C"
import (
	"unsafe"
)

func Access(filename *C.gchar, mode C.int) C.int {
	return C._g_access(unsafe.Pointer(filename), mode)
}

func ArrayFree(array *C.GArray, free_segment C.gboolean) *C.gchar {
	return C.g_array_free(array, free_segment)
}

func ArrayGetElementSize(array *C.GArray) C.guint {
	return C.g_array_get_element_size(array)
}

func ArraySetClearFunc(array *C.GArray, clear_func C.GDestroyNotify) {
	C.g_array_set_clear_func(array, clear_func)
}

func ArrayUnref(array *C.GArray) {
	C.g_array_unref(array)
}

func AsciiDigitValue(c C.gchar) C.gint {
	return C.g_ascii_digit_value(c)
}

func AsciiDtostr(buffer *C.gchar, buf_len C.gint, d C.gdouble) *C.gchar {
	return C.g_ascii_dtostr(buffer, buf_len, d)
}

func AsciiFormatd(buffer *C.gchar, buf_len C.gint, format *C.gchar, d C.gdouble) *C.gchar {
	return C._g_ascii_formatd(buffer, buf_len, unsafe.Pointer(format), d)
}

func AsciiStrcasecmp(s1 *C.gchar, s2 *C.gchar) C.gint {
	return C._g_ascii_strcasecmp(unsafe.Pointer(s1), unsafe.Pointer(s2))
}

func AsciiStrdown(str *C.gchar, _len C.gssize) *C.gchar {
	return C._g_ascii_strdown(unsafe.Pointer(str), _len)
}

func AsciiStrncasecmp(s1 *C.gchar, s2 *C.gchar, n C.gsize) C.gint {
	return C._g_ascii_strncasecmp(unsafe.Pointer(s1), unsafe.Pointer(s2), n)
}

func AsciiStrtod(nptr *C.gchar, endptr unsafe.Pointer) C.gdouble {
	return C._g_ascii_strtod(unsafe.Pointer(nptr), unsafe.Pointer(endptr))
}

func AsciiStrtoll(nptr *C.gchar, endptr unsafe.Pointer, base C.guint) C.gint64 {
	return C._g_ascii_strtoll(unsafe.Pointer(nptr), unsafe.Pointer(endptr), base)
}

func AsciiStrtoull(nptr *C.gchar, endptr unsafe.Pointer, base C.guint) C.guint64 {
	return C._g_ascii_strtoull(unsafe.Pointer(nptr), unsafe.Pointer(endptr), base)
}

func AsciiStrup(str *C.gchar, _len C.gssize) *C.gchar {
	return C._g_ascii_strup(unsafe.Pointer(str), _len)
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

func AssertionMessage(domain *C.char, file *C.char, line C.int, _func *C.char, message *C.char) {
	C._g_assertion_message(unsafe.Pointer(domain), unsafe.Pointer(file), line, unsafe.Pointer(_func), unsafe.Pointer(message))
}

//TODO long double g_assertion_message_cmpnum

func AssertionMessageCmpstr(domain *C.char, file *C.char, line C.int, _func *C.char, expr *C.char, arg1 *C.char, cmp *C.char, arg2 *C.char) {
	C._g_assertion_message_cmpstr(unsafe.Pointer(domain), unsafe.Pointer(file), line, unsafe.Pointer(_func), unsafe.Pointer(expr), unsafe.Pointer(arg1), unsafe.Pointer(cmp), unsafe.Pointer(arg2))
}

func AssertionMessageError(domain *C.char, file *C.char, line C.int, _func *C.char, expr *C.char, error *C.GError, error_domain C.GQuark, error_code C.int) {
	C._g_assertion_message_error(unsafe.Pointer(domain), unsafe.Pointer(file), line, unsafe.Pointer(_func), unsafe.Pointer(expr), unsafe.Pointer(error), error_domain, error_code)
}

func AssertionMessageExpr(domain *C.char, file *C.char, line C.int, _func *C.char, expr *C.char) {
	C._g_assertion_message_expr(unsafe.Pointer(domain), unsafe.Pointer(file), line, unsafe.Pointer(_func), unsafe.Pointer(expr))
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

func Base64Decode(text *C.gchar, out_len *C.gsize) *C.guchar {
	return C._g_base64_decode(unsafe.Pointer(text), out_len)
}

func Base64DecodeInplace(text *C.gchar, out_len *C.gsize) *C.guchar {
	return C.g_base64_decode_inplace(text, out_len)
}

func Base64DecodeStep(in *C.gchar, _len C.gsize, out *C.guchar, state *C.gint, save *C.guint) C.gsize {
	return C.g_base64_decode_step(in, _len, out, state, save)
}

func Base64Encode(data *C.guchar, _len C.gsize) *C.gchar {
	return C.g_base64_encode(data, _len)
}

func Base64EncodeClose(break_lines C.gboolean, out *C.gchar, state *C.gint, save *C.gint) C.gsize {
	return C.g_base64_encode_close(break_lines, out, state, save)
}

func Base64EncodeStep(in *C.guchar, _len C.gsize, break_lines C.gboolean, out *C.gchar, state *C.gint, save *C.gint) C.gsize {
	return C.g_base64_encode_step(in, _len, break_lines, out, state, save)
}

//Deprecated g_basename

func BitLock(address *C.gint, lock_bit C.gint) {
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

func BitTrylock(address *C.gint, lock_bit C.gint) C.gboolean {
	return C.g_bit_trylock(address, lock_bit)
}

func BitUnlock(address *C.gint, lock_bit C.gint) {
	C.g_bit_unlock(address, lock_bit)
}

func BookmarkFileErrorQuark() C.GQuark {
	return C.g_bookmark_file_error_quark()
}

//TODO varargs g_build_filename

func BuildFilenamev(args unsafe.Pointer) *C.gchar {
	return C._g_build_filenamev(unsafe.Pointer(args))
}

//TODO varargs g_build_path

func BuildPathv(separator *C.gchar, args unsafe.Pointer) *C.gchar {
	return C._g_build_pathv(unsafe.Pointer(separator), unsafe.Pointer(args))
}

func ByteArrayFree(array *C.GByteArray, free_segment C.gboolean) *C.guint8 {
	return C.g_byte_array_free(array, free_segment)
}

func ByteArrayFreeToBytes(array *C.GByteArray) *C.GBytes {
	return C.g_byte_array_free_to_bytes(array)
}

func ByteArrayNew() *C.GByteArray {
	return C.g_byte_array_new()
}

func ByteArrayNewTake(data *C.guint8, _len C.gsize) *C.GByteArray {
	return C.g_byte_array_new_take(data, _len)
}

func ByteArrayUnref(array *C.GByteArray) {
	C.g_byte_array_unref(array)
}

func Chdir(path *C.gchar) C.int {
	return C._g_chdir(unsafe.Pointer(path))
}

func CheckVersion(required_major C.guint, required_minor C.guint, required_micro C.guint) *C.gchar {
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

func ChildWatchSourceNew(pid C.GPid) *C.GSource {
	return C.g_child_watch_source_new(pid)
}

func ClearError(err unsafe.Pointer) {
	C._g_clear_error(unsafe.Pointer(err))
}

//Skipped g_clear_pointer

func ComputeChecksumForBytes(checksum_type C.GChecksumType, data *C.GBytes) *C.gchar {
	return C.g_compute_checksum_for_bytes(checksum_type, data)
}

func ComputeChecksumForData(checksum_type C.GChecksumType, data *C.guchar, length C.gsize) *C.gchar {
	return C._g_compute_checksum_for_data(checksum_type, unsafe.Pointer(data), length)
}

func ComputeChecksumForString(checksum_type C.GChecksumType, str *C.gchar, length C.gssize) *C.gchar {
	return C._g_compute_checksum_for_string(checksum_type, unsafe.Pointer(str), length)
}

func ComputeHmacForData(digest_type C.GChecksumType, key *C.guchar, key_len C.gsize, data *C.guchar, length C.gsize) *C.gchar {
	return C._g_compute_hmac_for_data(digest_type, key, key_len, unsafe.Pointer(data), length)
}

func ComputeHmacForString(digest_type C.GChecksumType, key *C.guchar, key_len C.gsize, str *C.gchar, length C.gssize) *C.gchar {
	return C._g_compute_hmac_for_string(digest_type, key, key_len, unsafe.Pointer(str), length)
}

func Convert(str *C.gchar, _len C.gssize, to_codeset *C.gchar, from_codeset *C.gchar, bytes_read *C.gsize, bytes_written *C.gsize, err unsafe.Pointer) *C.gchar {
	return C._g_convert(unsafe.Pointer(str), _len, unsafe.Pointer(to_codeset), unsafe.Pointer(from_codeset), bytes_read, bytes_written, unsafe.Pointer(err))
}

func ConvertErrorQuark() C.GQuark {
	return C.g_convert_error_quark()
}

func ConvertWithFallback(str *C.gchar, _len C.gssize, to_codeset *C.gchar, from_codeset *C.gchar, fallback *C.gchar, bytes_read *C.gsize, bytes_written *C.gsize, err unsafe.Pointer) *C.gchar {
	return C._g_convert_with_fallback(unsafe.Pointer(str), _len, unsafe.Pointer(to_codeset), unsafe.Pointer(from_codeset), unsafe.Pointer(fallback), bytes_read, bytes_written, unsafe.Pointer(err))
}

func ConvertWithIconv(str *C.gchar, _len C.gssize, converter C.GIConv, bytes_read *C.gsize, bytes_written *C.gsize, err unsafe.Pointer) *C.gchar {
	return C._g_convert_with_iconv(unsafe.Pointer(str), _len, converter, bytes_read, bytes_written, unsafe.Pointer(err))
}

func DatalistClear(datalist unsafe.Pointer) {
	C._g_datalist_clear(unsafe.Pointer(datalist))
}

func DatalistForeach(datalist unsafe.Pointer, _func C.GDataForeachFunc, user_data C.gpointer) {
	C._g_datalist_foreach(unsafe.Pointer(datalist), _func, user_data)
}

func DatalistGetData(datalist unsafe.Pointer, key *C.gchar) C.gpointer {
	return C._g_datalist_get_data(unsafe.Pointer(datalist), unsafe.Pointer(key))
}

func DatalistGetFlags(datalist unsafe.Pointer) C.guint {
	return C._g_datalist_get_flags(unsafe.Pointer(datalist))
}

func DatalistIdDupData(datalist unsafe.Pointer, key_id C.GQuark, dup_func C.GDuplicateFunc, user_data C.gpointer) C.gpointer {
	return C._g_datalist_id_dup_data(unsafe.Pointer(datalist), key_id, dup_func, user_data)
}

func DatalistIdGetData(datalist unsafe.Pointer, key_id C.GQuark) C.gpointer {
	return C._g_datalist_id_get_data(unsafe.Pointer(datalist), key_id)
}

func DatalistIdRemoveNoNotify(datalist unsafe.Pointer, key_id C.GQuark) C.gpointer {
	return C._g_datalist_id_remove_no_notify(unsafe.Pointer(datalist), key_id)
}

func DatalistIdReplaceData(datalist unsafe.Pointer, key_id C.GQuark, oldval C.gpointer, newval C.gpointer, destroy C.GDestroyNotify, old_destroy *C.GDestroyNotify) C.gboolean {
	return C._g_datalist_id_replace_data(unsafe.Pointer(datalist), key_id, oldval, newval, destroy, old_destroy)
}

func DatalistIdSetDataFull(datalist unsafe.Pointer, key_id C.GQuark, data C.gpointer, destroy_func C.GDestroyNotify) {
	C._g_datalist_id_set_data_full(unsafe.Pointer(datalist), key_id, data, destroy_func)
}

func DatalistInit(datalist unsafe.Pointer) {
	C._g_datalist_init(unsafe.Pointer(datalist))
}

func DatalistSetFlags(datalist unsafe.Pointer, flags C.guint) {
	C._g_datalist_set_flags(unsafe.Pointer(datalist), flags)
}

func DatalistUnsetFlags(datalist unsafe.Pointer, flags C.guint) {
	C._g_datalist_unset_flags(unsafe.Pointer(datalist), flags)
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

func DateStrftime(s *C.gchar, slen C.gsize, format *C.gchar, date *C.GDate) C.gsize {
	return C._g_date_strftime(s, slen, unsafe.Pointer(format), unsafe.Pointer(date))
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

func Dcgettext(domain *C.gchar, msgid *C.gchar, category C.gint) *C.gchar {
	return C._g_dcgettext(unsafe.Pointer(domain), unsafe.Pointer(msgid), category)
}

func Dgettext(domain *C.gchar, msgid *C.gchar) *C.gchar {
	return C._g_dgettext(unsafe.Pointer(domain), unsafe.Pointer(msgid))
}

func DirMakeTmp(tmpl *C.gchar, err unsafe.Pointer) *C.gchar {
	return C._g_dir_make_tmp(tmpl, unsafe.Pointer(err))
}

func DirectEqual(v1 C.gconstpointer, v2 C.gconstpointer) C.gboolean {
	return C.g_direct_equal(v1, v2)
}

func DirectHash(v C.gconstpointer) C.guint {
	return C.g_direct_hash(v)
}

func Dngettext(domain *C.gchar, msgid *C.gchar, msgid_plural *C.gchar, n C.gulong) *C.gchar {
	return C._g_dngettext(unsafe.Pointer(domain), unsafe.Pointer(msgid), unsafe.Pointer(msgid_plural), n)
}

func DoubleEqual(v1 C.gconstpointer, v2 C.gconstpointer) C.gboolean {
	return C.g_double_equal(v1, v2)
}

func DoubleHash(v C.gconstpointer) C.guint {
	return C.g_double_hash(v)
}

func Dpgettext(domain *C.gchar, msgctxtid *C.gchar, msgidoffset C.gsize) *C.gchar {
	return C._g_dpgettext(unsafe.Pointer(domain), unsafe.Pointer(msgctxtid), msgidoffset)
}

func Dpgettext2(domain *C.gchar, context *C.gchar, msgid *C.gchar) *C.gchar {
	return C._g_dpgettext2(unsafe.Pointer(domain), unsafe.Pointer(context), unsafe.Pointer(msgid))
}

func EnvironGetenv(envp unsafe.Pointer, variable *C.gchar) *C.gchar {
	return C._g_environ_getenv(unsafe.Pointer(envp), unsafe.Pointer(variable))
}

func EnvironSetenv(envp unsafe.Pointer, variable *C.gchar, value *C.gchar, overwrite C.gboolean) unsafe.Pointer {
	return unsafe.Pointer(C._g_environ_setenv(unsafe.Pointer(envp), unsafe.Pointer(variable), unsafe.Pointer(value), overwrite))
}

func EnvironUnsetenv(envp unsafe.Pointer, variable *C.gchar) unsafe.Pointer {
	return unsafe.Pointer(C._g_environ_unsetenv(unsafe.Pointer(envp), unsafe.Pointer(variable)))
}

func FileErrorFromErrno(err_no C.gint) C.GFileError {
	return C.g_file_error_from_errno(err_no)
}

func FileErrorQuark() C.GQuark {
	return C.g_file_error_quark()
}

func FileGetContents(filename *C.gchar, contents unsafe.Pointer, length *C.gsize, err unsafe.Pointer) C.gboolean {
	return C._g_file_get_contents(filename, unsafe.Pointer(contents), length, unsafe.Pointer(err))
}

func FileOpenTmp(tmpl *C.gchar, name_used unsafe.Pointer, err unsafe.Pointer) C.gint {
	return C._g_file_open_tmp(tmpl, unsafe.Pointer(name_used), unsafe.Pointer(err))
}

func FileReadLink(filename *C.gchar, err unsafe.Pointer) *C.gchar {
	return C._g_file_read_link(unsafe.Pointer(filename), unsafe.Pointer(err))
}

func FileSetContents(filename *C.gchar, contents *C.gchar, length C.gssize, err unsafe.Pointer) C.gboolean {
	return C._g_file_set_contents(filename, contents, length, unsafe.Pointer(err))
}

func FileTest(filename *C.gchar, test C.GFileTest) C.gboolean {
	return C._g_file_test(unsafe.Pointer(filename), test)
}

func FilenameDisplayBasename(filename *C.gchar) *C.gchar {
	return C._g_filename_display_basename(unsafe.Pointer(filename))
}

func FilenameDisplayName(filename *C.gchar) *C.gchar {
	return C._g_filename_display_name(unsafe.Pointer(filename))
}

func FilenameFromUri(uri *C.gchar, hostname unsafe.Pointer, err unsafe.Pointer) *C.gchar {
	return C._g_filename_from_uri(unsafe.Pointer(uri), unsafe.Pointer(hostname), unsafe.Pointer(err))
}

func FilenameFromUtf8(utf8string *C.gchar, _len C.gssize, bytes_read *C.gsize, bytes_written *C.gsize, err unsafe.Pointer) *C.gchar {
	return C._g_filename_from_utf8(unsafe.Pointer(utf8string), _len, bytes_read, bytes_written, unsafe.Pointer(err))
}

func FilenameToUri(filename *C.gchar, hostname *C.gchar, err unsafe.Pointer) *C.gchar {
	return C._g_filename_to_uri(unsafe.Pointer(filename), unsafe.Pointer(hostname), unsafe.Pointer(err))
}

func FilenameToUtf8(opsysstring *C.gchar, _len C.gssize, bytes_read *C.gsize, bytes_written *C.gsize, err unsafe.Pointer) *C.gchar {
	return C._g_filename_to_utf8(unsafe.Pointer(opsysstring), _len, bytes_read, bytes_written, unsafe.Pointer(err))
}

func FindProgramInPath(program *C.gchar) *C.gchar {
	return C._g_find_program_in_path(unsafe.Pointer(program))
}

func FormatSize(size C.guint64) *C.gchar {
	return C.g_format_size(size)
}

//Deprecated g_format_size_for_display

func FormatSizeFull(size C.guint64, flags C.GFormatSizeFlags) *C.gchar {
	return C.g_format_size_full(size, flags)
}

//TODO varargs g_fprintf

func Free(mem C.gpointer) {
	C.g_free(mem)
}

func GetApplicationName() *C.gchar {
	return C.g_get_application_name()
}

func GetCharset(charset unsafe.Pointer) C.gboolean {
	return C._g_get_charset(unsafe.Pointer(charset))
}

func GetCodeset() *C.gchar {
	return C.g_get_codeset()
}

func GetCurrentDir() *C.gchar {
	return C.g_get_current_dir()
}

func GetCurrentTime(result *C.GTimeVal) {
	C.g_get_current_time(result)
}

func GetEnviron() unsafe.Pointer {
	return unsafe.Pointer(C.g_get_environ())
}

func GetFilenameCharsets(charsets unsafe.Pointer) C.gboolean {
	return C._g_get_filename_charsets(unsafe.Pointer(charsets))
}

func GetHomeDir() *C.gchar {
	return C.g_get_home_dir()
}

func GetHostName() *C.gchar {
	return C.g_get_host_name()
}

func GetLanguageNames() unsafe.Pointer {
	return unsafe.Pointer(C.g_get_language_names())
}

func GetLocaleVariants(locale *C.gchar) unsafe.Pointer {
	return unsafe.Pointer(C._g_get_locale_variants(unsafe.Pointer(locale)))
}

func GetMonotonicTime() C.gint64 {
	return C.g_get_monotonic_time()
}

func GetPrgname() *C.gchar {
	return C.g_get_prgname()
}

func GetRealName() *C.gchar {
	return C.g_get_real_name()
}

func GetRealTime() C.gint64 {
	return C.g_get_real_time()
}

func GetSystemConfigDirs() unsafe.Pointer {
	return unsafe.Pointer(C.g_get_system_config_dirs())
}

func GetSystemDataDirs() unsafe.Pointer {
	return unsafe.Pointer(C.g_get_system_data_dirs())
}

func GetTmpDir() *C.gchar {
	return C.g_get_tmp_dir()
}

func GetUserCacheDir() *C.gchar {
	return C.g_get_user_cache_dir()
}

func GetUserConfigDir() *C.gchar {
	return C.g_get_user_config_dir()
}

func GetUserDataDir() *C.gchar {
	return C.g_get_user_data_dir()
}

func GetUserName() *C.gchar {
	return C.g_get_user_name()
}

func GetUserRuntimeDir() *C.gchar {
	return C.g_get_user_runtime_dir()
}

func GetUserSpecialDir(directory C.GUserDirectory) *C.gchar {
	return C.g_get_user_special_dir(directory)
}

func Getenv(variable *C.gchar) *C.gchar {
	return C._g_getenv(unsafe.Pointer(variable))
}

func HashTableAdd(hash_table *C.GHashTable, key C.gpointer) {
	C.g_hash_table_add(hash_table, key)
}

func HashTableContains(hash_table *C.GHashTable, key C.gconstpointer) C.gboolean {
	return C.g_hash_table_contains(hash_table, key)
}

func HashTableDestroy(hash_table *C.GHashTable) {
	C.g_hash_table_destroy(hash_table)
}

func HashTableInsert(hash_table *C.GHashTable, key C.gpointer, value C.gpointer) {
	C.g_hash_table_insert(hash_table, key, value)
}

func HashTableLookupExtended(hash_table *C.GHashTable, lookup_key C.gconstpointer, orig_key *C.gpointer, value *C.gpointer) C.gboolean {
	return C.g_hash_table_lookup_extended(hash_table, lookup_key, orig_key, value)
}

func HashTableRemove(hash_table *C.GHashTable, key C.gconstpointer) C.gboolean {
	return C.g_hash_table_remove(hash_table, key)
}

func HashTableRemoveAll(hash_table *C.GHashTable) {
	C.g_hash_table_remove_all(hash_table)
}

func HashTableReplace(hash_table *C.GHashTable, key C.gpointer, value C.gpointer) {
	C.g_hash_table_replace(hash_table, key, value)
}

func HashTableSize(hash_table *C.GHashTable) C.guint {
	return C.g_hash_table_size(hash_table)
}

func HashTableSteal(hash_table *C.GHashTable, key C.gconstpointer) C.gboolean {
	return C.g_hash_table_steal(hash_table, key)
}

func HashTableStealAll(hash_table *C.GHashTable) {
	C.g_hash_table_steal_all(hash_table)
}

func HashTableUnref(hash_table *C.GHashTable) {
	C.g_hash_table_unref(hash_table)
}

func HookDestroy(hook_list *C.GHookList, hook_id C.gulong) C.gboolean {
	return C.g_hook_destroy(hook_list, hook_id)
}

func HookDestroyLink(hook_list *C.GHookList, hook *C.GHook) {
	C.g_hook_destroy_link(hook_list, hook)
}

func HookFree(hook_list *C.GHookList, hook *C.GHook) {
	C.g_hook_free(hook_list, hook)
}

func HookInsertBefore(hook_list *C.GHookList, sibling *C.GHook, hook *C.GHook) {
	C.g_hook_insert_before(hook_list, sibling, hook)
}

func HookPrepend(hook_list *C.GHookList, hook *C.GHook) {
	C.g_hook_prepend(hook_list, hook)
}

func HookUnref(hook_list *C.GHookList, hook *C.GHook) {
	C.g_hook_unref(hook_list, hook)
}

func HostnameIsAsciiEncoded(hostname *C.gchar) C.gboolean {
	return C._g_hostname_is_ascii_encoded(unsafe.Pointer(hostname))
}

func HostnameIsIpAddress(hostname *C.gchar) C.gboolean {
	return C._g_hostname_is_ip_address(unsafe.Pointer(hostname))
}

func HostnameIsNonAscii(hostname *C.gchar) C.gboolean {
	return C._g_hostname_is_non_ascii(unsafe.Pointer(hostname))
}

func HostnameToAscii(hostname *C.gchar) *C.gchar {
	return C._g_hostname_to_ascii(unsafe.Pointer(hostname))
}

func HostnameToUnicode(hostname *C.gchar) *C.gchar {
	return C._g_hostname_to_unicode(unsafe.Pointer(hostname))
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

func IdleSourceNew() *C.GSource {
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

func InternStaticString(string *C.gchar) *C.gchar {
	return C._g_intern_static_string(unsafe.Pointer(string))
}

func InternString(string *C.gchar) *C.gchar {
	return C._g_intern_string(unsafe.Pointer(string))
}

func IoAddWatch(channel *C.GIOChannel, condition C.GIOCondition, _func C.GIOFunc, user_data C.gpointer) C.guint {
	return C.g_io_add_watch(channel, condition, _func, user_data)
}

func IoAddWatchFull(channel *C.GIOChannel, priority C.gint, condition C.GIOCondition, _func C.GIOFunc, user_data C.gpointer, notify C.GDestroyNotify) C.guint {
	return C.g_io_add_watch_full(channel, priority, condition, _func, user_data, notify)
}

func IoChannelErrorFromErrno(en C.gint) C.GIOChannelError {
	return C.g_io_channel_error_from_errno(en)
}

func IoChannelErrorQuark() C.GQuark {
	return C.g_io_channel_error_quark()
}

func IoCreateWatch(channel *C.GIOChannel, condition C.GIOCondition) *C.GSource {
	return C.g_io_create_watch(channel, condition)
}

func KeyFileErrorQuark() C.GQuark {
	return C.g_key_file_error_quark()
}

func Listenv() unsafe.Pointer {
	return unsafe.Pointer(C.g_listenv())
}

func LocaleFromUtf8(utf8string *C.gchar, _len C.gssize, bytes_read *C.gsize, bytes_written *C.gsize, err unsafe.Pointer) *C.gchar {
	return C._g_locale_from_utf8(unsafe.Pointer(utf8string), _len, bytes_read, bytes_written, unsafe.Pointer(err))
}

func LocaleToUtf8(opsysstring *C.gchar, _len C.gssize, bytes_read *C.gsize, bytes_written *C.gsize, err unsafe.Pointer) *C.gchar {
	return C._g_locale_to_utf8(unsafe.Pointer(opsysstring), _len, bytes_read, bytes_written, unsafe.Pointer(err))
}

//TODO varargs g_log

func LogDefaultHandler(log_domain *C.gchar, log_level C.GLogLevelFlags, message *C.gchar, unused_data C.gpointer) {
	C._g_log_default_handler(unsafe.Pointer(log_domain), log_level, unsafe.Pointer(message), unused_data)
}

func LogRemoveHandler(log_domain *C.gchar, handler_id C.guint) {
	C._g_log_remove_handler(unsafe.Pointer(log_domain), handler_id)
}

func LogSetAlwaysFatal(fatal_mask C.GLogLevelFlags) C.GLogLevelFlags {
	return C.g_log_set_always_fatal(fatal_mask)
}

func LogSetDefaultHandler(log_func C.GLogFunc, user_data C.gpointer) C.GLogFunc {
	return C.g_log_set_default_handler(log_func, user_data)
}

func LogSetFatalMask(log_domain *C.gchar, fatal_mask C.GLogLevelFlags) C.GLogLevelFlags {
	return C._g_log_set_fatal_mask(unsafe.Pointer(log_domain), fatal_mask)
}

func LogSetHandler(log_domain *C.gchar, log_levels C.GLogLevelFlags, log_func C.GLogFunc, user_data C.gpointer) C.guint {
	return C._g_log_set_handler(unsafe.Pointer(log_domain), log_levels, log_func, user_data)
}

//TODO va_list g_logv

func MainContextDefault() *C.GMainContext {
	return C.g_main_context_default()
}

func MainContextGetThreadDefault() *C.GMainContext {
	return C.g_main_context_get_thread_default()
}

func MainContextRefThreadDefault() *C.GMainContext {
	return C.g_main_context_ref_thread_default()
}

func MainCurrentSource() *C.GSource {
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

func MarkupEscapeText(text *C.gchar, length C.gssize) *C.gchar {
	return C._g_markup_escape_text(unsafe.Pointer(text), length)
}

//TODO varargs g_markup_printf_escaped

//TODO va_list g_markup_vprintf_escaped

func MemIsSystemMalloc() C.gboolean {
	return C.g_mem_is_system_malloc()
}

func MemProfile() {
	C.g_mem_profile()
}

func MemSetVtable(vtable *C.GMemVTable) {
	C.g_mem_set_vtable(vtable)
}

func Memdup(mem C.gconstpointer, byte_size C.guint) C.gpointer {
	return C.g_memdup(mem, byte_size)
}

func MkdirWithParents(pathname *C.gchar, mode C.gint) C.gint {
	return C._g_mkdir_with_parents(unsafe.Pointer(pathname), mode)
}

func Mkdtemp(tmpl *C.gchar) *C.gchar {
	return C.g_mkdtemp(tmpl)
}

func MkdtempFull(tmpl *C.gchar, mode C.gint) *C.gchar {
	return C.g_mkdtemp_full(tmpl, mode)
}

func Mkstemp(tmpl *C.gchar) C.gint {
	return C.g_mkstemp(tmpl)
}

func MkstempFull(tmpl *C.gchar, flags C.gint, mode C.gint) C.gint {
	return C.g_mkstemp_full(tmpl, flags, mode)
}

func NullifyPointer(nullify_location *C.gpointer) {
	C.g_nullify_pointer(nullify_location)
}

func OnErrorQuery(prg_name *C.gchar) {
	C._g_on_error_query(unsafe.Pointer(prg_name))
}

func OnErrorStackTrace(prg_name *C.gchar) {
	C._g_on_error_stack_trace(unsafe.Pointer(prg_name))
}

//Skipped g_once_init_enter

//Skipped g_once_init_leave

func OptionErrorQuark() C.GQuark {
	return C.g_option_error_quark()
}

func ParseDebugString(string *C.gchar, keys *C.GDebugKey, nkeys C.guint) C.guint {
	return C._g_parse_debug_string(unsafe.Pointer(string), keys, nkeys)
}

func PathGetBasename(file_name *C.gchar) *C.gchar {
	return C._g_path_get_basename(unsafe.Pointer(file_name))
}

func PathGetDirname(file_name *C.gchar) *C.gchar {
	return C._g_path_get_dirname(unsafe.Pointer(file_name))
}

func PathIsAbsolute(file_name *C.gchar) C.gboolean {
	return C._g_path_is_absolute(unsafe.Pointer(file_name))
}

func PathSkipRoot(file_name *C.gchar) *C.gchar {
	return C._g_path_skip_root(unsafe.Pointer(file_name))
}

func PatternMatch(pspec *C.GPatternSpec, string_length C.guint, string *C.gchar, string_reversed *C.gchar) C.gboolean {
	return C._g_pattern_match(pspec, string_length, unsafe.Pointer(string), unsafe.Pointer(string_reversed))
}

func PatternMatchSimple(pattern *C.gchar, string *C.gchar) C.gboolean {
	return C._g_pattern_match_simple(unsafe.Pointer(pattern), unsafe.Pointer(string))
}

func PatternMatchString(pspec *C.GPatternSpec, string *C.gchar) C.gboolean {
	return C._g_pattern_match_string(pspec, unsafe.Pointer(string))
}

//Skipped g_pointer_bit_lock

//Skipped g_pointer_bit_trylock

//Skipped g_pointer_bit_unlock

func Poll(fds *C.GPollFD, nfds C.guint, timeout C.gint) C.gint {
	return C.g_poll(fds, nfds, timeout)
}

//TODO varargs g_prefix_error

//TODO varargs g_print

//TODO varargs g_printerr

//TODO varargs g_printf

//TODO va_list g_printf_string_upper_bound

func PropagateError(dest unsafe.Pointer, src *C.GError) {
	C._g_propagate_error(unsafe.Pointer(dest), src)
}

//TODO varargs g_propagate_prefixed_error

func PtrArrayAdd(array *C.GPtrArray, data C.gpointer) {
	C.g_ptr_array_add(array, data)
}

func PtrArrayRemove(array *C.GPtrArray, data C.gpointer) C.gboolean {
	return C.g_ptr_array_remove(array, data)
}

func PtrArrayRemoveFast(array *C.GPtrArray, data C.gpointer) C.gboolean {
	return C.g_ptr_array_remove_fast(array, data)
}

func PtrArrayRemoveRange(array *C.GPtrArray, index_ C.guint, length C.guint) {
	C.g_ptr_array_remove_range(array, index_, length)
}

func PtrArraySetFreeFunc(array *C.GPtrArray, element_free_func C.GDestroyNotify) {
	C.g_ptr_array_set_free_func(array, element_free_func)
}

func PtrArraySetSize(array *C.GPtrArray, length C.gint) {
	C.g_ptr_array_set_size(array, length)
}

func PtrArrayUnref(array *C.GPtrArray) {
	C.g_ptr_array_unref(array)
}

func QsortWithData(pbase C.gconstpointer, total_elems C.gint, size C.gsize, compare_func C.GCompareDataFunc, user_data C.gpointer) {
	C.g_qsort_with_data(pbase, total_elems, size, compare_func, user_data)
}

func QuarkFromStaticString(string *C.gchar) C.GQuark {
	return C._g_quark_from_static_string(unsafe.Pointer(string))
}

func QuarkFromString(string *C.gchar) C.GQuark {
	return C._g_quark_from_string(unsafe.Pointer(string))
}

func QuarkToString(quark C.GQuark) *C.gchar {
	return C.g_quark_to_string(quark)
}

func QuarkTryString(string *C.gchar) C.GQuark {
	return C._g_quark_try_string(unsafe.Pointer(string))
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

func RegexCheckReplacement(replacement *C.gchar, has_references *C.gboolean, err unsafe.Pointer) C.gboolean {
	return C._g_regex_check_replacement(unsafe.Pointer(replacement), has_references, unsafe.Pointer(err))
}

func RegexErrorQuark() C.GQuark {
	return C.g_regex_error_quark()
}

func RegexEscapeNul(string *C.gchar, length C.gint) *C.gchar {
	return C._g_regex_escape_nul(unsafe.Pointer(string), length)
}

func RegexEscapeString(string *C.gchar, length C.gint) *C.gchar {
	return C.g_regex_escape_string(string, length)
}

func RegexMatchSimple(pattern *C.gchar, string *C.gchar, compile_options C.GRegexCompileFlags, match_options C.GRegexMatchFlags) C.gboolean {
	return C._g_regex_match_simple(unsafe.Pointer(pattern), unsafe.Pointer(string), compile_options, match_options)
}

func RegexSplitSimple(pattern *C.gchar, string *C.gchar, compile_options C.GRegexCompileFlags, match_options C.GRegexMatchFlags) unsafe.Pointer {
	return unsafe.Pointer(C._g_regex_split_simple(unsafe.Pointer(pattern), unsafe.Pointer(string), compile_options, match_options))
}

func ReloadUserSpecialDirsCache() {
	C.g_reload_user_special_dirs_cache()
}

func ReturnIfFailWarning(log_domain *C.char, pretty_function *C.char, expression *C.char) {
	C._g_return_if_fail_warning(unsafe.Pointer(log_domain), unsafe.Pointer(pretty_function), unsafe.Pointer(expression))
}

func Rmdir(filename *C.gchar) C.int {
	return C._g_rmdir(unsafe.Pointer(filename))
}

func SequenceMove(src *C.GSequenceIter, dest *C.GSequenceIter) {
	C.g_sequence_move(src, dest)
}

func SequenceMoveRange(dest *C.GSequenceIter, begin *C.GSequenceIter, end *C.GSequenceIter) {
	C.g_sequence_move_range(dest, begin, end)
}

func SequenceRemove(iter *C.GSequenceIter) {
	C.g_sequence_remove(iter)
}

func SequenceRemoveRange(begin *C.GSequenceIter, end *C.GSequenceIter) {
	C.g_sequence_remove_range(begin, end)
}

func SequenceSet(iter *C.GSequenceIter, data C.gpointer) {
	C.g_sequence_set(iter, data)
}

func SequenceSwap(a *C.GSequenceIter, b *C.GSequenceIter) {
	C.g_sequence_swap(a, b)
}

func SetApplicationName(application_name *C.gchar) {
	C._g_set_application_name(unsafe.Pointer(application_name))
}

//TODO varargs g_set_error

func SetErrorLiteral(err unsafe.Pointer, domain C.GQuark, code C.gint, message *C.gchar) {
	C._g_set_error_literal(unsafe.Pointer(err), domain, code, unsafe.Pointer(message))
}

func SetPrgname(prgname *C.gchar) {
	C._g_set_prgname(unsafe.Pointer(prgname))
}

func SetPrintHandler(_func C.GPrintFunc) C.GPrintFunc {
	return C.g_set_print_handler(_func)
}

func SetPrinterrHandler(_func C.GPrintFunc) C.GPrintFunc {
	return C.g_set_printerr_handler(_func)
}

func Setenv(variable *C.gchar, value *C.gchar, overwrite C.gboolean) C.gboolean {
	return C._g_setenv(unsafe.Pointer(variable), unsafe.Pointer(value), overwrite)
}

func ShellErrorQuark() C.GQuark {
	return C.g_shell_error_quark()
}

func ShellParseArgv(command_line *C.gchar, argcp *C.gint, argvp unsafe.Pointer, err unsafe.Pointer) C.gboolean {
	return C._g_shell_parse_argv(unsafe.Pointer(command_line), argcp, unsafe.Pointer(argvp), unsafe.Pointer(err))
}

func ShellQuote(unquoted_string *C.gchar) *C.gchar {
	return C._g_shell_quote(unsafe.Pointer(unquoted_string))
}

func ShellUnquote(quoted_string *C.gchar, err unsafe.Pointer) *C.gchar {
	return C._g_shell_unquote(unsafe.Pointer(quoted_string), unsafe.Pointer(err))
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

func SourceRemoveByFuncsUserData(funcs *C.GSourceFuncs, user_data C.gpointer) C.gboolean {
	return C.g_source_remove_by_funcs_user_data(funcs, user_data)
}

func SourceRemoveByUserData(user_data C.gpointer) C.gboolean {
	return C.g_source_remove_by_user_data(user_data)
}

func SourceSetNameById(tag C.guint, name *C.char) {
	C._g_source_set_name_by_id(tag, unsafe.Pointer(name))
}

func SpacedPrimesClosest(num C.guint) C.guint {
	return C.g_spaced_primes_closest(num)
}

func SpawnAsync(working_directory *C.gchar, argv unsafe.Pointer, envp unsafe.Pointer, flags C.GSpawnFlags, child_setup C.GSpawnChildSetupFunc, user_data C.gpointer, child_pid *C.GPid, err unsafe.Pointer) C.gboolean {
	return C._g_spawn_async(unsafe.Pointer(working_directory), unsafe.Pointer(argv), unsafe.Pointer(envp), flags, child_setup, user_data, child_pid, unsafe.Pointer(err))
}

func SpawnAsyncWithPipes(working_directory *C.gchar, argv unsafe.Pointer, envp unsafe.Pointer, flags C.GSpawnFlags, child_setup C.GSpawnChildSetupFunc, user_data C.gpointer, child_pid *C.GPid, standard_input *C.gint, standard_output *C.gint, standard_error *C.gint, err unsafe.Pointer) C.gboolean {
	return C._g_spawn_async_with_pipes(unsafe.Pointer(working_directory), unsafe.Pointer(argv), unsafe.Pointer(envp), flags, child_setup, user_data, child_pid, standard_input, standard_output, standard_error, unsafe.Pointer(err))
}

func SpawnCheckExitStatus(exit_status C.gint, err unsafe.Pointer) C.gboolean {
	return C._g_spawn_check_exit_status(exit_status, unsafe.Pointer(err))
}

func SpawnClosePid(pid C.GPid) {
	C.g_spawn_close_pid(pid)
}

func SpawnCommandLineAsync(command_line *C.gchar, err unsafe.Pointer) C.gboolean {
	return C._g_spawn_command_line_async(unsafe.Pointer(command_line), unsafe.Pointer(err))
}

func SpawnCommandLineSync(command_line *C.gchar, standard_output unsafe.Pointer, standard_error unsafe.Pointer, exit_status *C.gint, err unsafe.Pointer) C.gboolean {
	return C._g_spawn_command_line_sync(unsafe.Pointer(command_line), unsafe.Pointer(standard_output), unsafe.Pointer(standard_error), exit_status, unsafe.Pointer(err))
}

func SpawnErrorQuark() C.GQuark {
	return C.g_spawn_error_quark()
}

func SpawnExitErrorQuark() C.GQuark {
	return C.g_spawn_exit_error_quark()
}

func SpawnSync(working_directory *C.gchar, argv unsafe.Pointer, envp unsafe.Pointer, flags C.GSpawnFlags, child_setup C.GSpawnChildSetupFunc, user_data C.gpointer, standard_output unsafe.Pointer, standard_error unsafe.Pointer, exit_status *C.gint, err unsafe.Pointer) C.gboolean {
	return C._g_spawn_sync(unsafe.Pointer(working_directory), unsafe.Pointer(argv), unsafe.Pointer(envp), flags, child_setup, user_data, unsafe.Pointer(standard_output), unsafe.Pointer(standard_error), exit_status, unsafe.Pointer(err))
}

//TODO varargs g_sprintf

func Stpcpy(dest *C.gchar, src *C.char) *C.gchar {
	return C._g_stpcpy(dest, unsafe.Pointer(src))
}

func StrEqual(v1 C.gconstpointer, v2 C.gconstpointer) C.gboolean {
	return C.g_str_equal(v1, v2)
}

func StrHasPrefix(str *C.gchar, prefix *C.gchar) C.gboolean {
	return C._g_str_has_prefix(unsafe.Pointer(str), unsafe.Pointer(prefix))
}

func StrHasSuffix(str *C.gchar, suffix *C.gchar) C.gboolean {
	return C._g_str_has_suffix(unsafe.Pointer(str), unsafe.Pointer(suffix))
}

func StrHash(v C.gconstpointer) C.guint {
	return C.g_str_hash(v)
}

func Strcanon(string *C.gchar, valid_chars *C.gchar, substitutor C.gchar) *C.gchar {
	return C._g_strcanon(string, unsafe.Pointer(valid_chars), substitutor)
}

//Deprecated g_strcasecmp

func Strchomp(string *C.gchar) *C.gchar {
	return C.g_strchomp(string)
}

func Strchug(string *C.gchar) *C.gchar {
	return C.g_strchug(string)
}

func Strcmp0(str1 *C.char, str2 *C.char) C.int {
	return C._g_strcmp0(unsafe.Pointer(str1), unsafe.Pointer(str2))
}

func Strcompress(source *C.gchar) *C.gchar {
	return C._g_strcompress(unsafe.Pointer(source))
}

//TODO varargs g_strconcat

func Strdelimit(string *C.gchar, delimiters *C.gchar, new_delimiter C.gchar) *C.gchar {
	return C._g_strdelimit(string, unsafe.Pointer(delimiters), new_delimiter)
}

//Deprecated g_strdown

func Strdup(str *C.gchar) *C.gchar {
	return C._g_strdup(unsafe.Pointer(str))
}

//TODO varargs g_strdup_printf

//TODO va_list g_strdup_vprintf

func Strdupv(str_array unsafe.Pointer) unsafe.Pointer {
	return unsafe.Pointer(C._g_strdupv(unsafe.Pointer(str_array)))
}

func Strerror(errnum C.gint) *C.gchar {
	return C.g_strerror(errnum)
}

func Strescape(source *C.gchar, exceptions *C.gchar) *C.gchar {
	return C._g_strescape(unsafe.Pointer(source), unsafe.Pointer(exceptions))
}

func Strfreev(str_array unsafe.Pointer) {
	C._g_strfreev(unsafe.Pointer(str_array))
}

func StringNew(init *C.gchar) *C.GString {
	return C._g_string_new(unsafe.Pointer(init))
}

func StringNewLen(init *C.gchar, _len C.gssize) *C.GString {
	return C._g_string_new_len(unsafe.Pointer(init), _len)
}

func StringSizedNew(dfl_size C.gsize) *C.GString {
	return C.g_string_sized_new(dfl_size)
}

func StripContext(msgid *C.gchar, msgval *C.gchar) *C.gchar {
	return C._g_strip_context(unsafe.Pointer(msgid), unsafe.Pointer(msgval))
}

//TODO varargs g_strjoin

func Strjoinv(separator *C.gchar, str_array unsafe.Pointer) *C.gchar {
	return C._g_strjoinv(unsafe.Pointer(separator), unsafe.Pointer(str_array))
}

func Strlcat(dest *C.gchar, src *C.gchar, dest_size C.gsize) C.gsize {
	return C._g_strlcat(dest, unsafe.Pointer(src), dest_size)
}

func Strlcpy(dest *C.gchar, src *C.gchar, dest_size C.gsize) C.gsize {
	return C._g_strlcpy(dest, unsafe.Pointer(src), dest_size)
}

//Deprecated g_strncasecmp

func Strndup(str *C.gchar, n C.gsize) *C.gchar {
	return C._g_strndup(unsafe.Pointer(str), n)
}

func Strnfill(length C.gsize, fill_char C.gchar) *C.gchar {
	return C.g_strnfill(length, fill_char)
}

func Strreverse(string *C.gchar) *C.gchar {
	return C.g_strreverse(string)
}

func Strrstr(haystack *C.gchar, needle *C.gchar) *C.gchar {
	return C._g_strrstr(unsafe.Pointer(haystack), unsafe.Pointer(needle))
}

func StrrstrLen(haystack *C.gchar, haystack_len C.gssize, needle *C.gchar) *C.gchar {
	return C._g_strrstr_len(unsafe.Pointer(haystack), haystack_len, unsafe.Pointer(needle))
}

func Strsignal(signum C.gint) *C.gchar {
	return C.g_strsignal(signum)
}

func Strsplit(string *C.gchar, delimiter *C.gchar, max_tokens C.gint) unsafe.Pointer {
	return unsafe.Pointer(C._g_strsplit(unsafe.Pointer(string), unsafe.Pointer(delimiter), max_tokens))
}

func StrsplitSet(string *C.gchar, delimiters *C.gchar, max_tokens C.gint) unsafe.Pointer {
	return unsafe.Pointer(C._g_strsplit_set(unsafe.Pointer(string), unsafe.Pointer(delimiters), max_tokens))
}

func StrstrLen(haystack *C.gchar, haystack_len C.gssize, needle *C.gchar) *C.gchar {
	return C._g_strstr_len(unsafe.Pointer(haystack), haystack_len, unsafe.Pointer(needle))
}

func Strtod(nptr *C.gchar, endptr unsafe.Pointer) C.gdouble {
	return C._g_strtod(unsafe.Pointer(nptr), unsafe.Pointer(endptr))
}

//Deprecated g_strup

func StrvGetType() C.GType {
	return C.g_strv_get_type()
}

func StrvLength(str_array unsafe.Pointer) C.guint {
	return C._g_strv_length(unsafe.Pointer(str_array))
}

func TestAddDataFunc(testpath *C.char, test_data C.gconstpointer, test_func C.GTestDataFunc) {
	C._g_test_add_data_func(unsafe.Pointer(testpath), test_data, test_func)
}

func TestAddDataFuncFull(testpath *C.char, test_data C.gpointer, test_func C.GTestDataFunc, data_free_func C.GDestroyNotify) {
	C._g_test_add_data_func_full(unsafe.Pointer(testpath), test_data, test_func, data_free_func)
}

func TestAddFunc(testpath *C.char, test_func C.GTestFunc) {
	C._g_test_add_func(unsafe.Pointer(testpath), test_func)
}

func TestAddVtable(testpath *C.char, data_size C.gsize, test_data C.gconstpointer, data_setup C.GTestFixtureFunc, data_test C.GTestFixtureFunc, data_teardown C.GTestFixtureFunc) {
	C._g_test_add_vtable(unsafe.Pointer(testpath), data_size, test_data, data_setup, data_test, data_teardown)
}

func TestAssertExpectedMessagesInternal(domain *C.char, file *C.char, line C.int, _func *C.char) {
	C._g_test_assert_expected_messages_internal(unsafe.Pointer(domain), unsafe.Pointer(file), line, unsafe.Pointer(_func))
}

func TestBug(bug_uri_snippet *C.char) {
	C._g_test_bug(unsafe.Pointer(bug_uri_snippet))
}

func TestBugBase(uri_pattern *C.char) {
	C._g_test_bug_base(unsafe.Pointer(uri_pattern))
}

func TestCreateCase(test_name *C.char, data_size C.gsize, test_data C.gconstpointer, data_setup C.GTestFixtureFunc, data_test C.GTestFixtureFunc, data_teardown C.GTestFixtureFunc) *C.GTestCase {
	return C._g_test_create_case(unsafe.Pointer(test_name), data_size, test_data, data_setup, data_test, data_teardown)
}

func TestCreateSuite(suite_name *C.char) *C.GTestSuite {
	return C._g_test_create_suite(unsafe.Pointer(suite_name))
}

func TestExpectMessage(log_domain *C.gchar, log_level C.GLogLevelFlags, pattern *C.gchar) {
	C._g_test_expect_message(unsafe.Pointer(log_domain), log_level, unsafe.Pointer(pattern))
}

func TestFail() {
	C.g_test_fail()
}

func TestGetRoot() *C.GTestSuite {
	return C.g_test_get_root()
}

//TODO varargs g_test_init

func TestLogSetFatalHandler(log_func C.GTestLogFatalFunc, user_data C.gpointer) {
	C.g_test_log_set_fatal_handler(log_func, user_data)
}

func TestLogTypeName(log_type C.GTestLogType) *C.char {
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

func TestRunSuite(suite *C.GTestSuite) C.int {
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

func TestTrapAssertions(domain *C.char, file *C.char, line C.int, _func *C.char, assertion_flags C.guint64, pattern *C.char) {
	C._g_test_trap_assertions(unsafe.Pointer(domain), unsafe.Pointer(file), line, unsafe.Pointer(_func), assertion_flags, unsafe.Pointer(pattern))
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

func ThreadSelf() *C.GThread {
	return C.g_thread_self()
}

func ThreadYield() {
	C.g_thread_yield()
}

func TimeValFromIso8601(iso_date *C.gchar, time_ *C.GTimeVal) C.gboolean {
	return C._g_time_val_from_iso8601(unsafe.Pointer(iso_date), time_)
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

func TimeoutSourceNew(interval C.guint) *C.GSource {
	return C.g_timeout_source_new(interval)
}

func TimeoutSourceNewSeconds(interval C.guint) *C.GSource {
	return C.g_timeout_source_new_seconds(interval)
}

func TrashStackHeight(stack_p unsafe.Pointer) C.guint {
	return C._g_trash_stack_height(unsafe.Pointer(stack_p))
}

func TrashStackPush(stack_p unsafe.Pointer, data_p C.gpointer) {
	C._g_trash_stack_push(unsafe.Pointer(stack_p), data_p)
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

func Ucs4ToUtf16(str *C.gunichar, _len C.glong, items_read *C.glong, items_written *C.glong, err unsafe.Pointer) *C.gunichar2 {
	return C._g_ucs4_to_utf16(unsafe.Pointer(str), _len, items_read, items_written, unsafe.Pointer(err))
}

func Ucs4ToUtf8(str *C.gunichar, _len C.glong, items_read *C.glong, items_written *C.glong, err unsafe.Pointer) *C.gchar {
	return C._g_ucs4_to_utf8(unsafe.Pointer(str), _len, items_read, items_written, unsafe.Pointer(err))
}

func UnicharBreakType(c C.gunichar) C.GUnicodeBreakType {
	return C.g_unichar_break_type(c)
}

func UnicharCombiningClass(uc C.gunichar) C.gint {
	return C.g_unichar_combining_class(uc)
}

func UnicharCompose(a C.gunichar, b C.gunichar, ch *C.gunichar) C.gboolean {
	return C.g_unichar_compose(a, b, ch)
}

func UnicharDecompose(ch C.gunichar, a *C.gunichar, b *C.gunichar) C.gboolean {
	return C.g_unichar_decompose(ch, a, b)
}

func UnicharDigitValue(c C.gunichar) C.gint {
	return C.g_unichar_digit_value(c)
}

func UnicharFullyDecompose(ch C.gunichar, compat C.gboolean, result *C.gunichar, result_len C.gsize) C.gsize {
	return C.g_unichar_fully_decompose(ch, compat, result, result_len)
}

func UnicharGetMirrorChar(ch C.gunichar, mirrored_ch *C.gunichar) C.gboolean {
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

func UnicharToUtf8(c C.gunichar, outbuf *C.gchar) C.gint {
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

func UnicodeCanonicalOrdering(string *C.gunichar, _len C.gsize) {
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

func UnixOpenPipe(fds *C.gint, flags C.gint, err unsafe.Pointer) C.gboolean {
	return C._g_unix_open_pipe(fds, flags, unsafe.Pointer(err))
}

func UnixSetFdNonblocking(fd C.gint, nonblock C.gboolean, err unsafe.Pointer) C.gboolean {
	return C._g_unix_set_fd_nonblocking(fd, nonblock, unsafe.Pointer(err))
}

func UnixSignalAdd(signum C.gint, handler C.GSourceFunc, user_data C.gpointer) C.guint {
	return C.g_unix_signal_add(signum, handler, user_data)
}

func UnixSignalAddFull(priority C.gint, signum C.gint, handler C.GSourceFunc, user_data C.gpointer, notify C.GDestroyNotify) C.guint {
	return C.g_unix_signal_add_full(priority, signum, handler, user_data, notify)
}

func UnixSignalSourceNew(signum C.gint) *C.GSource {
	return C.g_unix_signal_source_new(signum)
}

func Unlink(filename *C.gchar) C.int {
	return C._g_unlink(unsafe.Pointer(filename))
}

func Unsetenv(variable *C.gchar) {
	C._g_unsetenv(unsafe.Pointer(variable))
}

func UriEscapeString(unescaped *C.char, reserved_chars_allowed *C.char, allow_utf8 C.gboolean) *C.char {
	return C._g_uri_escape_string(unsafe.Pointer(unescaped), unsafe.Pointer(reserved_chars_allowed), allow_utf8)
}

func UriListExtractUris(uri_list *C.gchar) unsafe.Pointer {
	return unsafe.Pointer(C._g_uri_list_extract_uris(unsafe.Pointer(uri_list)))
}

func UriParseScheme(uri *C.char) *C.char {
	return C._g_uri_parse_scheme(unsafe.Pointer(uri))
}

func UriUnescapeSegment(escaped_string *C.char, escaped_string_end *C.char, illegal_characters *C.char) *C.char {
	return C._g_uri_unescape_segment(unsafe.Pointer(escaped_string), unsafe.Pointer(escaped_string_end), unsafe.Pointer(illegal_characters))
}

func UriUnescapeString(escaped_string *C.char, illegal_characters *C.char) *C.char {
	return C._g_uri_unescape_string(unsafe.Pointer(escaped_string), unsafe.Pointer(illegal_characters))
}

func Usleep(microseconds C.gulong) {
	C.g_usleep(microseconds)
}

func Utf16ToUcs4(str *C.gunichar2, _len C.glong, items_read *C.glong, items_written *C.glong, err unsafe.Pointer) *C.gunichar {
	return C._g_utf16_to_ucs4(unsafe.Pointer(str), _len, items_read, items_written, unsafe.Pointer(err))
}

func Utf16ToUtf8(str *C.gunichar2, _len C.glong, items_read *C.glong, items_written *C.glong, err unsafe.Pointer) *C.gchar {
	return C._g_utf16_to_utf8(unsafe.Pointer(str), _len, items_read, items_written, unsafe.Pointer(err))
}

func Utf8Casefold(str *C.gchar, _len C.gssize) *C.gchar {
	return C._g_utf8_casefold(unsafe.Pointer(str), _len)
}

func Utf8Collate(str1 *C.gchar, str2 *C.gchar) C.gint {
	return C._g_utf8_collate(unsafe.Pointer(str1), unsafe.Pointer(str2))
}

func Utf8CollateKey(str *C.gchar, _len C.gssize) *C.gchar {
	return C._g_utf8_collate_key(unsafe.Pointer(str), _len)
}

func Utf8CollateKeyForFilename(str *C.gchar, _len C.gssize) *C.gchar {
	return C._g_utf8_collate_key_for_filename(unsafe.Pointer(str), _len)
}

func Utf8FindNextChar(p *C.gchar, end *C.gchar) *C.gchar {
	return C._g_utf8_find_next_char(unsafe.Pointer(p), unsafe.Pointer(end))
}

func Utf8FindPrevChar(str *C.gchar, p *C.gchar) *C.gchar {
	return C._g_utf8_find_prev_char(unsafe.Pointer(str), unsafe.Pointer(p))
}

func Utf8GetChar(p *C.gchar) C.gunichar {
	return C._g_utf8_get_char(unsafe.Pointer(p))
}

func Utf8GetCharValidated(p *C.gchar, max_len C.gssize) C.gunichar {
	return C._g_utf8_get_char_validated(unsafe.Pointer(p), max_len)
}

func Utf8Normalize(str *C.gchar, _len C.gssize, mode C.GNormalizeMode) *C.gchar {
	return C._g_utf8_normalize(unsafe.Pointer(str), _len, mode)
}

func Utf8OffsetToPointer(str *C.gchar, offset C.glong) *C.gchar {
	return C._g_utf8_offset_to_pointer(unsafe.Pointer(str), offset)
}

func Utf8PointerToOffset(str *C.gchar, pos *C.gchar) C.glong {
	return C._g_utf8_pointer_to_offset(unsafe.Pointer(str), unsafe.Pointer(pos))
}

func Utf8PrevChar(p *C.gchar) *C.gchar {
	return C._g_utf8_prev_char(unsafe.Pointer(p))
}

func Utf8Strchr(p *C.gchar, _len C.gssize, c C.gunichar) *C.gchar {
	return C._g_utf8_strchr(unsafe.Pointer(p), _len, c)
}

func Utf8Strdown(str *C.gchar, _len C.gssize) *C.gchar {
	return C._g_utf8_strdown(unsafe.Pointer(str), _len)
}

func Utf8Strlen(p *C.gchar, max C.gssize) C.glong {
	return C._g_utf8_strlen(unsafe.Pointer(p), max)
}

func Utf8Strncpy(dest *C.gchar, src *C.gchar, n C.gsize) *C.gchar {
	return C._g_utf8_strncpy(dest, unsafe.Pointer(src), n)
}

func Utf8Strrchr(p *C.gchar, _len C.gssize, c C.gunichar) *C.gchar {
	return C._g_utf8_strrchr(unsafe.Pointer(p), _len, c)
}

func Utf8Strreverse(str *C.gchar, _len C.gssize) *C.gchar {
	return C._g_utf8_strreverse(unsafe.Pointer(str), _len)
}

func Utf8Strup(str *C.gchar, _len C.gssize) *C.gchar {
	return C._g_utf8_strup(unsafe.Pointer(str), _len)
}

func Utf8Substring(str *C.gchar, start_pos C.glong, end_pos C.glong) *C.gchar {
	return C._g_utf8_substring(unsafe.Pointer(str), start_pos, end_pos)
}

func Utf8ToUcs4(str *C.gchar, _len C.glong, items_read *C.glong, items_written *C.glong, err unsafe.Pointer) *C.gunichar {
	return C._g_utf8_to_ucs4(unsafe.Pointer(str), _len, items_read, items_written, unsafe.Pointer(err))
}

func Utf8ToUcs4Fast(str *C.gchar, _len C.glong, items_written *C.glong) *C.gunichar {
	return C._g_utf8_to_ucs4_fast(unsafe.Pointer(str), _len, items_written)
}

func Utf8ToUtf16(str *C.gchar, _len C.glong, items_read *C.glong, items_written *C.glong, err unsafe.Pointer) *C.gunichar2 {
	return C._g_utf8_to_utf16(unsafe.Pointer(str), _len, items_read, items_written, unsafe.Pointer(err))
}

func Utf8Validate(str *C.gchar, max_len C.gssize, end unsafe.Pointer) C.gboolean {
	return C._g_utf8_validate(str, max_len, unsafe.Pointer(end))
}

//Skipped g_variant_get_gtype

func VariantIsObjectPath(string *C.gchar) C.gboolean {
	return C._g_variant_is_object_path(unsafe.Pointer(string))
}

func VariantIsSignature(string *C.gchar) C.gboolean {
	return C._g_variant_is_signature(unsafe.Pointer(string))
}

func VariantParse(_type *C.GVariantType, text *C.gchar, limit *C.gchar, endptr unsafe.Pointer, err unsafe.Pointer) *C.GVariant {
	return C._g_variant_parse(unsafe.Pointer(_type), unsafe.Pointer(text), unsafe.Pointer(limit), unsafe.Pointer(endptr), unsafe.Pointer(err))
}

func VariantParserGetErrorQuark() C.GQuark {
	return C.g_variant_parser_get_error_quark()
}

func VariantTypeChecked(arg_0 *C.gchar) *C.GVariantType {
	return C._g_variant_type_checked_(unsafe.Pointer(arg_0))
}

func VariantTypeStringIsValid(type_string *C.gchar) C.gboolean {
	return C._g_variant_type_string_is_valid(unsafe.Pointer(type_string))
}

func VariantTypeStringScan(string *C.gchar, limit *C.gchar, endptr unsafe.Pointer) C.gboolean {
	return C._g_variant_type_string_scan(unsafe.Pointer(string), unsafe.Pointer(limit), unsafe.Pointer(endptr))
}

//TODO va_list g_vasprintf

//TODO va_list g_vfprintf

//TODO va_list g_vprintf

//TODO va_list g_vsnprintf

//TODO va_list g_vsprintf

func WarnMessage(domain *C.char, file *C.char, line C.int, _func *C.char, warnexpr *C.char) {
	C._g_warn_message(unsafe.Pointer(domain), unsafe.Pointer(file), line, unsafe.Pointer(_func), unsafe.Pointer(warnexpr))
}

const G_BOOKMARK_FILE_ERROR_INVALID_URI = C.G_BOOKMARK_FILE_ERROR_INVALID_URI
const G_BOOKMARK_FILE_ERROR_INVALID_VALUE = C.G_BOOKMARK_FILE_ERROR_INVALID_VALUE
const G_BOOKMARK_FILE_ERROR_APP_NOT_REGISTERED = C.G_BOOKMARK_FILE_ERROR_APP_NOT_REGISTERED
const G_BOOKMARK_FILE_ERROR_URI_NOT_FOUND = C.G_BOOKMARK_FILE_ERROR_URI_NOT_FOUND
const G_BOOKMARK_FILE_ERROR_READ = C.G_BOOKMARK_FILE_ERROR_READ
const G_BOOKMARK_FILE_ERROR_UNKNOWN_ENCODING = C.G_BOOKMARK_FILE_ERROR_UNKNOWN_ENCODING
const G_BOOKMARK_FILE_ERROR_WRITE = C.G_BOOKMARK_FILE_ERROR_WRITE
const G_BOOKMARK_FILE_ERROR_FILE_NOT_FOUND = C.G_BOOKMARK_FILE_ERROR_FILE_NOT_FOUND
const G_CHECKSUM_MD5 = C.G_CHECKSUM_MD5
const G_CHECKSUM_SHA1 = C.G_CHECKSUM_SHA1
const G_CHECKSUM_SHA256 = C.G_CHECKSUM_SHA256
const G_CHECKSUM_SHA512 = C.G_CHECKSUM_SHA512
const G_CONVERT_ERROR_NO_CONVERSION = C.G_CONVERT_ERROR_NO_CONVERSION
const G_CONVERT_ERROR_ILLEGAL_SEQUENCE = C.G_CONVERT_ERROR_ILLEGAL_SEQUENCE
const G_CONVERT_ERROR_FAILED = C.G_CONVERT_ERROR_FAILED
const G_CONVERT_ERROR_PARTIAL_INPUT = C.G_CONVERT_ERROR_PARTIAL_INPUT
const G_CONVERT_ERROR_BAD_URI = C.G_CONVERT_ERROR_BAD_URI
const G_CONVERT_ERROR_NOT_ABSOLUTE_PATH = C.G_CONVERT_ERROR_NOT_ABSOLUTE_PATH
const G_DATE_DAY = C.G_DATE_DAY
const G_DATE_MONTH = C.G_DATE_MONTH
const G_DATE_YEAR = C.G_DATE_YEAR
const G_DATE_BAD_MONTH = C.G_DATE_BAD_MONTH
const G_DATE_JANUARY = C.G_DATE_JANUARY
const G_DATE_FEBRUARY = C.G_DATE_FEBRUARY
const G_DATE_MARCH = C.G_DATE_MARCH
const G_DATE_APRIL = C.G_DATE_APRIL
const G_DATE_MAY = C.G_DATE_MAY
const G_DATE_JUNE = C.G_DATE_JUNE
const G_DATE_JULY = C.G_DATE_JULY
const G_DATE_AUGUST = C.G_DATE_AUGUST
const G_DATE_SEPTEMBER = C.G_DATE_SEPTEMBER
const G_DATE_OCTOBER = C.G_DATE_OCTOBER
const G_DATE_NOVEMBER = C.G_DATE_NOVEMBER
const G_DATE_DECEMBER = C.G_DATE_DECEMBER
const G_DATE_BAD_WEEKDAY = C.G_DATE_BAD_WEEKDAY
const G_DATE_MONDAY = C.G_DATE_MONDAY
const G_DATE_TUESDAY = C.G_DATE_TUESDAY
const G_DATE_WEDNESDAY = C.G_DATE_WEDNESDAY
const G_DATE_THURSDAY = C.G_DATE_THURSDAY
const G_DATE_FRIDAY = C.G_DATE_FRIDAY
const G_DATE_SATURDAY = C.G_DATE_SATURDAY
const G_DATE_SUNDAY = C.G_DATE_SUNDAY
const G_ERR_UNKNOWN = C.G_ERR_UNKNOWN
const G_ERR_UNEXP_EOF = C.G_ERR_UNEXP_EOF
const G_ERR_UNEXP_EOF_IN_STRING = C.G_ERR_UNEXP_EOF_IN_STRING
const G_ERR_UNEXP_EOF_IN_COMMENT = C.G_ERR_UNEXP_EOF_IN_COMMENT
const G_ERR_NON_DIGIT_IN_CONST = C.G_ERR_NON_DIGIT_IN_CONST
const G_ERR_DIGIT_RADIX = C.G_ERR_DIGIT_RADIX
const G_ERR_FLOAT_RADIX = C.G_ERR_FLOAT_RADIX
const G_ERR_FLOAT_MALFORMED = C.G_ERR_FLOAT_MALFORMED
const G_FILE_ERROR_EXIST = C.G_FILE_ERROR_EXIST
const G_FILE_ERROR_ISDIR = C.G_FILE_ERROR_ISDIR
const G_FILE_ERROR_ACCES = C.G_FILE_ERROR_ACCES
const G_FILE_ERROR_NAMETOOLONG = C.G_FILE_ERROR_NAMETOOLONG
const G_FILE_ERROR_NOENT = C.G_FILE_ERROR_NOENT
const G_FILE_ERROR_NOTDIR = C.G_FILE_ERROR_NOTDIR
const G_FILE_ERROR_NXIO = C.G_FILE_ERROR_NXIO
const G_FILE_ERROR_NODEV = C.G_FILE_ERROR_NODEV
const G_FILE_ERROR_ROFS = C.G_FILE_ERROR_ROFS
const G_FILE_ERROR_TXTBSY = C.G_FILE_ERROR_TXTBSY
const G_FILE_ERROR_FAULT = C.G_FILE_ERROR_FAULT
const G_FILE_ERROR_LOOP = C.G_FILE_ERROR_LOOP
const G_FILE_ERROR_NOSPC = C.G_FILE_ERROR_NOSPC
const G_FILE_ERROR_NOMEM = C.G_FILE_ERROR_NOMEM
const G_FILE_ERROR_MFILE = C.G_FILE_ERROR_MFILE
const G_FILE_ERROR_NFILE = C.G_FILE_ERROR_NFILE
const G_FILE_ERROR_BADF = C.G_FILE_ERROR_BADF
const G_FILE_ERROR_INVAL = C.G_FILE_ERROR_INVAL
const G_FILE_ERROR_PIPE = C.G_FILE_ERROR_PIPE
const G_FILE_ERROR_AGAIN = C.G_FILE_ERROR_AGAIN
const G_FILE_ERROR_INTR = C.G_FILE_ERROR_INTR
const G_FILE_ERROR_IO = C.G_FILE_ERROR_IO
const G_FILE_ERROR_PERM = C.G_FILE_ERROR_PERM
const G_FILE_ERROR_NOSYS = C.G_FILE_ERROR_NOSYS
const G_FILE_ERROR_FAILED = C.G_FILE_ERROR_FAILED
const G_IO_CHANNEL_ERROR_FBIG = C.G_IO_CHANNEL_ERROR_FBIG
const G_IO_CHANNEL_ERROR_INVAL = C.G_IO_CHANNEL_ERROR_INVAL
const G_IO_CHANNEL_ERROR_IO = C.G_IO_CHANNEL_ERROR_IO
const G_IO_CHANNEL_ERROR_ISDIR = C.G_IO_CHANNEL_ERROR_ISDIR
const G_IO_CHANNEL_ERROR_NOSPC = C.G_IO_CHANNEL_ERROR_NOSPC
const G_IO_CHANNEL_ERROR_NXIO = C.G_IO_CHANNEL_ERROR_NXIO
const G_IO_CHANNEL_ERROR_OVERFLOW = C.G_IO_CHANNEL_ERROR_OVERFLOW
const G_IO_CHANNEL_ERROR_PIPE = C.G_IO_CHANNEL_ERROR_PIPE
const G_IO_CHANNEL_ERROR_FAILED = C.G_IO_CHANNEL_ERROR_FAILED
const G_IO_ERROR_NONE = C.G_IO_ERROR_NONE
const G_IO_ERROR_AGAIN = C.G_IO_ERROR_AGAIN
const G_IO_ERROR_INVAL = C.G_IO_ERROR_INVAL
const G_IO_ERROR_UNKNOWN = C.G_IO_ERROR_UNKNOWN
const G_IO_STATUS_ERROR = C.G_IO_STATUS_ERROR
const G_IO_STATUS_NORMAL = C.G_IO_STATUS_NORMAL
const G_IO_STATUS_EOF = C.G_IO_STATUS_EOF
const G_IO_STATUS_AGAIN = C.G_IO_STATUS_AGAIN
const G_KEY_FILE_ERROR_UNKNOWN_ENCODING = C.G_KEY_FILE_ERROR_UNKNOWN_ENCODING
const G_KEY_FILE_ERROR_PARSE = C.G_KEY_FILE_ERROR_PARSE
const G_KEY_FILE_ERROR_NOT_FOUND = C.G_KEY_FILE_ERROR_NOT_FOUND
const G_KEY_FILE_ERROR_KEY_NOT_FOUND = C.G_KEY_FILE_ERROR_KEY_NOT_FOUND
const G_KEY_FILE_ERROR_GROUP_NOT_FOUND = C.G_KEY_FILE_ERROR_GROUP_NOT_FOUND
const G_KEY_FILE_ERROR_INVALID_VALUE = C.G_KEY_FILE_ERROR_INVALID_VALUE
const G_MARKUP_ERROR_BAD_UTF8 = C.G_MARKUP_ERROR_BAD_UTF8
const G_MARKUP_ERROR_EMPTY = C.G_MARKUP_ERROR_EMPTY
const G_MARKUP_ERROR_PARSE = C.G_MARKUP_ERROR_PARSE
const G_MARKUP_ERROR_UNKNOWN_ELEMENT = C.G_MARKUP_ERROR_UNKNOWN_ELEMENT
const G_MARKUP_ERROR_UNKNOWN_ATTRIBUTE = C.G_MARKUP_ERROR_UNKNOWN_ATTRIBUTE
const G_MARKUP_ERROR_INVALID_CONTENT = C.G_MARKUP_ERROR_INVALID_CONTENT
const G_MARKUP_ERROR_MISSING_ATTRIBUTE = C.G_MARKUP_ERROR_MISSING_ATTRIBUTE
const G_NORMALIZE_DEFAULT = C.G_NORMALIZE_DEFAULT
const G_NORMALIZE_NFD = C.G_NORMALIZE_NFD
const G_NORMALIZE_DEFAULT_COMPOSE = C.G_NORMALIZE_DEFAULT_COMPOSE
const G_NORMALIZE_NFC = C.G_NORMALIZE_NFC
const G_NORMALIZE_ALL = C.G_NORMALIZE_ALL
const G_NORMALIZE_NFKD = C.G_NORMALIZE_NFKD
const G_NORMALIZE_ALL_COMPOSE = C.G_NORMALIZE_ALL_COMPOSE
const G_NORMALIZE_NFKC = C.G_NORMALIZE_NFKC
const G_ONCE_STATUS_NOTCALLED = C.G_ONCE_STATUS_NOTCALLED
const G_ONCE_STATUS_PROGRESS = C.G_ONCE_STATUS_PROGRESS
const G_ONCE_STATUS_READY = C.G_ONCE_STATUS_READY
const G_OPTION_ARG_NONE = C.G_OPTION_ARG_NONE
const G_OPTION_ARG_STRING = C.G_OPTION_ARG_STRING
const G_OPTION_ARG_INT = C.G_OPTION_ARG_INT
const G_OPTION_ARG_CALLBACK = C.G_OPTION_ARG_CALLBACK
const G_OPTION_ARG_FILENAME = C.G_OPTION_ARG_FILENAME
const G_OPTION_ARG_STRING_ARRAY = C.G_OPTION_ARG_STRING_ARRAY
const G_OPTION_ARG_FILENAME_ARRAY = C.G_OPTION_ARG_FILENAME_ARRAY
const G_OPTION_ARG_DOUBLE = C.G_OPTION_ARG_DOUBLE
const G_OPTION_ARG_INT64 = C.G_OPTION_ARG_INT64
const G_OPTION_ERROR_UNKNOWN_OPTION = C.G_OPTION_ERROR_UNKNOWN_OPTION
const G_OPTION_ERROR_BAD_VALUE = C.G_OPTION_ERROR_BAD_VALUE
const G_OPTION_ERROR_FAILED = C.G_OPTION_ERROR_FAILED
const G_REGEX_ERROR_COMPILE = C.G_REGEX_ERROR_COMPILE
const G_REGEX_ERROR_OPTIMIZE = C.G_REGEX_ERROR_OPTIMIZE
const G_REGEX_ERROR_REPLACE = C.G_REGEX_ERROR_REPLACE
const G_REGEX_ERROR_MATCH = C.G_REGEX_ERROR_MATCH
const G_REGEX_ERROR_INTERNAL = C.G_REGEX_ERROR_INTERNAL
const G_REGEX_ERROR_STRAY_BACKSLASH = C.G_REGEX_ERROR_STRAY_BACKSLASH
const G_REGEX_ERROR_MISSING_CONTROL_CHAR = C.G_REGEX_ERROR_MISSING_CONTROL_CHAR
const G_REGEX_ERROR_UNRECOGNIZED_ESCAPE = C.G_REGEX_ERROR_UNRECOGNIZED_ESCAPE
const G_REGEX_ERROR_QUANTIFIERS_OUT_OF_ORDER = C.G_REGEX_ERROR_QUANTIFIERS_OUT_OF_ORDER
const G_REGEX_ERROR_QUANTIFIER_TOO_BIG = C.G_REGEX_ERROR_QUANTIFIER_TOO_BIG
const G_REGEX_ERROR_UNTERMINATED_CHARACTER_CLASS = C.G_REGEX_ERROR_UNTERMINATED_CHARACTER_CLASS
const G_REGEX_ERROR_INVALID_ESCAPE_IN_CHARACTER_CLASS = C.G_REGEX_ERROR_INVALID_ESCAPE_IN_CHARACTER_CLASS
const G_REGEX_ERROR_RANGE_OUT_OF_ORDER = C.G_REGEX_ERROR_RANGE_OUT_OF_ORDER
const G_REGEX_ERROR_NOTHING_TO_REPEAT = C.G_REGEX_ERROR_NOTHING_TO_REPEAT
const G_REGEX_ERROR_UNRECOGNIZED_CHARACTER = C.G_REGEX_ERROR_UNRECOGNIZED_CHARACTER
const G_REGEX_ERROR_POSIX_NAMED_CLASS_OUTSIDE_CLASS = C.G_REGEX_ERROR_POSIX_NAMED_CLASS_OUTSIDE_CLASS
const G_REGEX_ERROR_UNMATCHED_PARENTHESIS = C.G_REGEX_ERROR_UNMATCHED_PARENTHESIS
const G_REGEX_ERROR_INEXISTENT_SUBPATTERN_REFERENCE = C.G_REGEX_ERROR_INEXISTENT_SUBPATTERN_REFERENCE
const G_REGEX_ERROR_UNTERMINATED_COMMENT = C.G_REGEX_ERROR_UNTERMINATED_COMMENT
const G_REGEX_ERROR_EXPRESSION_TOO_LARGE = C.G_REGEX_ERROR_EXPRESSION_TOO_LARGE
const G_REGEX_ERROR_MEMORY_ERROR = C.G_REGEX_ERROR_MEMORY_ERROR
const G_REGEX_ERROR_VARIABLE_LENGTH_LOOKBEHIND = C.G_REGEX_ERROR_VARIABLE_LENGTH_LOOKBEHIND
const G_REGEX_ERROR_MALFORMED_CONDITION = C.G_REGEX_ERROR_MALFORMED_CONDITION
const G_REGEX_ERROR_TOO_MANY_CONDITIONAL_BRANCHES = C.G_REGEX_ERROR_TOO_MANY_CONDITIONAL_BRANCHES
const G_REGEX_ERROR_ASSERTION_EXPECTED = C.G_REGEX_ERROR_ASSERTION_EXPECTED
const G_REGEX_ERROR_UNKNOWN_POSIX_CLASS_NAME = C.G_REGEX_ERROR_UNKNOWN_POSIX_CLASS_NAME
const G_REGEX_ERROR_POSIX_COLLATING_ELEMENTS_NOT_SUPPORTED = C.G_REGEX_ERROR_POSIX_COLLATING_ELEMENTS_NOT_SUPPORTED
const G_REGEX_ERROR_HEX_CODE_TOO_LARGE = C.G_REGEX_ERROR_HEX_CODE_TOO_LARGE
const G_REGEX_ERROR_INVALID_CONDITION = C.G_REGEX_ERROR_INVALID_CONDITION
const G_REGEX_ERROR_SINGLE_BYTE_MATCH_IN_LOOKBEHIND = C.G_REGEX_ERROR_SINGLE_BYTE_MATCH_IN_LOOKBEHIND
const G_REGEX_ERROR_INFINITE_LOOP = C.G_REGEX_ERROR_INFINITE_LOOP
const G_REGEX_ERROR_MISSING_SUBPATTERN_NAME_TERMINATOR = C.G_REGEX_ERROR_MISSING_SUBPATTERN_NAME_TERMINATOR
const G_REGEX_ERROR_DUPLICATE_SUBPATTERN_NAME = C.G_REGEX_ERROR_DUPLICATE_SUBPATTERN_NAME
const G_REGEX_ERROR_MALFORMED_PROPERTY = C.G_REGEX_ERROR_MALFORMED_PROPERTY
const G_REGEX_ERROR_UNKNOWN_PROPERTY = C.G_REGEX_ERROR_UNKNOWN_PROPERTY
const G_REGEX_ERROR_SUBPATTERN_NAME_TOO_LONG = C.G_REGEX_ERROR_SUBPATTERN_NAME_TOO_LONG
const G_REGEX_ERROR_TOO_MANY_SUBPATTERNS = C.G_REGEX_ERROR_TOO_MANY_SUBPATTERNS
const G_REGEX_ERROR_INVALID_OCTAL_VALUE = C.G_REGEX_ERROR_INVALID_OCTAL_VALUE
const G_REGEX_ERROR_TOO_MANY_BRANCHES_IN_DEFINE = C.G_REGEX_ERROR_TOO_MANY_BRANCHES_IN_DEFINE
const G_REGEX_ERROR_DEFINE_REPETION = C.G_REGEX_ERROR_DEFINE_REPETION
const G_REGEX_ERROR_INCONSISTENT_NEWLINE_OPTIONS = C.G_REGEX_ERROR_INCONSISTENT_NEWLINE_OPTIONS
const G_REGEX_ERROR_MISSING_BACK_REFERENCE = C.G_REGEX_ERROR_MISSING_BACK_REFERENCE
const G_REGEX_ERROR_INVALID_RELATIVE_REFERENCE = C.G_REGEX_ERROR_INVALID_RELATIVE_REFERENCE
const G_REGEX_ERROR_BACKTRACKING_CONTROL_VERB_ARGUMENT_FORBIDDEN = C.G_REGEX_ERROR_BACKTRACKING_CONTROL_VERB_ARGUMENT_FORBIDDEN
const G_REGEX_ERROR_UNKNOWN_BACKTRACKING_CONTROL_VERB = C.G_REGEX_ERROR_UNKNOWN_BACKTRACKING_CONTROL_VERB
const G_REGEX_ERROR_NUMBER_TOO_BIG = C.G_REGEX_ERROR_NUMBER_TOO_BIG
const G_REGEX_ERROR_MISSING_SUBPATTERN_NAME = C.G_REGEX_ERROR_MISSING_SUBPATTERN_NAME
const G_REGEX_ERROR_MISSING_DIGIT = C.G_REGEX_ERROR_MISSING_DIGIT
const G_REGEX_ERROR_INVALID_DATA_CHARACTER = C.G_REGEX_ERROR_INVALID_DATA_CHARACTER
const G_REGEX_ERROR_EXTRA_SUBPATTERN_NAME = C.G_REGEX_ERROR_EXTRA_SUBPATTERN_NAME
const G_REGEX_ERROR_BACKTRACKING_CONTROL_VERB_ARGUMENT_REQUIRED = C.G_REGEX_ERROR_BACKTRACKING_CONTROL_VERB_ARGUMENT_REQUIRED
const G_REGEX_ERROR_INVALID_CONTROL_CHAR = C.G_REGEX_ERROR_INVALID_CONTROL_CHAR
const G_REGEX_ERROR_MISSING_NAME = C.G_REGEX_ERROR_MISSING_NAME
const G_REGEX_ERROR_NOT_SUPPORTED_IN_CLASS = C.G_REGEX_ERROR_NOT_SUPPORTED_IN_CLASS
const G_REGEX_ERROR_TOO_MANY_FORWARD_REFERENCES = C.G_REGEX_ERROR_TOO_MANY_FORWARD_REFERENCES
const G_REGEX_ERROR_NAME_TOO_LONG = C.G_REGEX_ERROR_NAME_TOO_LONG
const G_REGEX_ERROR_CHARACTER_VALUE_TOO_LARGE = C.G_REGEX_ERROR_CHARACTER_VALUE_TOO_LARGE
const G_SEEK_CUR = C.G_SEEK_CUR
const G_SEEK_SET = C.G_SEEK_SET
const G_SEEK_END = C.G_SEEK_END
const G_SHELL_ERROR_BAD_QUOTING = C.G_SHELL_ERROR_BAD_QUOTING
const G_SHELL_ERROR_EMPTY_STRING = C.G_SHELL_ERROR_EMPTY_STRING
const G_SHELL_ERROR_FAILED = C.G_SHELL_ERROR_FAILED
const G_SLICE_CONFIG_ALWAYS_MALLOC = C.G_SLICE_CONFIG_ALWAYS_MALLOC
const G_SLICE_CONFIG_BYPASS_MAGAZINES = C.G_SLICE_CONFIG_BYPASS_MAGAZINES
const G_SLICE_CONFIG_WORKING_SET_MSECS = C.G_SLICE_CONFIG_WORKING_SET_MSECS
const G_SLICE_CONFIG_COLOR_INCREMENT = C.G_SLICE_CONFIG_COLOR_INCREMENT
const G_SLICE_CONFIG_CHUNK_SIZES = C.G_SLICE_CONFIG_CHUNK_SIZES
const G_SLICE_CONFIG_CONTENTION_COUNTER = C.G_SLICE_CONFIG_CONTENTION_COUNTER
const G_SPAWN_ERROR_FORK = C.G_SPAWN_ERROR_FORK
const G_SPAWN_ERROR_READ = C.G_SPAWN_ERROR_READ
const G_SPAWN_ERROR_CHDIR = C.G_SPAWN_ERROR_CHDIR
const G_SPAWN_ERROR_ACCES = C.G_SPAWN_ERROR_ACCES
const G_SPAWN_ERROR_PERM = C.G_SPAWN_ERROR_PERM
const G_SPAWN_ERROR_TOO_BIG = C.G_SPAWN_ERROR_TOO_BIG
const G_SPAWN_ERROR_2BIG = C.G_SPAWN_ERROR_2BIG
const G_SPAWN_ERROR_NOEXEC = C.G_SPAWN_ERROR_NOEXEC
const G_SPAWN_ERROR_NAMETOOLONG = C.G_SPAWN_ERROR_NAMETOOLONG
const G_SPAWN_ERROR_NOENT = C.G_SPAWN_ERROR_NOENT
const G_SPAWN_ERROR_NOMEM = C.G_SPAWN_ERROR_NOMEM
const G_SPAWN_ERROR_NOTDIR = C.G_SPAWN_ERROR_NOTDIR
const G_SPAWN_ERROR_LOOP = C.G_SPAWN_ERROR_LOOP
const G_SPAWN_ERROR_TXTBUSY = C.G_SPAWN_ERROR_TXTBUSY
const G_SPAWN_ERROR_IO = C.G_SPAWN_ERROR_IO
const G_SPAWN_ERROR_NFILE = C.G_SPAWN_ERROR_NFILE
const G_SPAWN_ERROR_MFILE = C.G_SPAWN_ERROR_MFILE
const G_SPAWN_ERROR_INVAL = C.G_SPAWN_ERROR_INVAL
const G_SPAWN_ERROR_ISDIR = C.G_SPAWN_ERROR_ISDIR
const G_SPAWN_ERROR_LIBBAD = C.G_SPAWN_ERROR_LIBBAD
const G_SPAWN_ERROR_FAILED = C.G_SPAWN_ERROR_FAILED
const G_TEST_LOG_NONE = C.G_TEST_LOG_NONE
const G_TEST_LOG_ERROR = C.G_TEST_LOG_ERROR
const G_TEST_LOG_START_BINARY = C.G_TEST_LOG_START_BINARY
const G_TEST_LOG_LIST_CASE = C.G_TEST_LOG_LIST_CASE
const G_TEST_LOG_SKIP_CASE = C.G_TEST_LOG_SKIP_CASE
const G_TEST_LOG_START_CASE = C.G_TEST_LOG_START_CASE
const G_TEST_LOG_STOP_CASE = C.G_TEST_LOG_STOP_CASE
const G_TEST_LOG_MIN_RESULT = C.G_TEST_LOG_MIN_RESULT
const G_TEST_LOG_MAX_RESULT = C.G_TEST_LOG_MAX_RESULT
const G_TEST_LOG_MESSAGE = C.G_TEST_LOG_MESSAGE
const G_THREAD_ERROR_AGAIN = C.G_THREAD_ERROR_AGAIN
const G_TIME_TYPE_STANDARD = C.G_TIME_TYPE_STANDARD
const G_TIME_TYPE_DAYLIGHT = C.G_TIME_TYPE_DAYLIGHT
const G_TIME_TYPE_UNIVERSAL = C.G_TIME_TYPE_UNIVERSAL
const G_TOKEN_EOF = C.G_TOKEN_EOF
const G_TOKEN_LEFT_PAREN = C.G_TOKEN_LEFT_PAREN
const G_TOKEN_RIGHT_PAREN = C.G_TOKEN_RIGHT_PAREN
const G_TOKEN_LEFT_CURLY = C.G_TOKEN_LEFT_CURLY
const G_TOKEN_RIGHT_CURLY = C.G_TOKEN_RIGHT_CURLY
const G_TOKEN_LEFT_BRACE = C.G_TOKEN_LEFT_BRACE
const G_TOKEN_RIGHT_BRACE = C.G_TOKEN_RIGHT_BRACE
const G_TOKEN_EQUAL_SIGN = C.G_TOKEN_EQUAL_SIGN
const G_TOKEN_COMMA = C.G_TOKEN_COMMA
const G_TOKEN_NONE = C.G_TOKEN_NONE
const G_TOKEN_ERROR = C.G_TOKEN_ERROR
const G_TOKEN_CHAR = C.G_TOKEN_CHAR
const G_TOKEN_BINARY = C.G_TOKEN_BINARY
const G_TOKEN_OCTAL = C.G_TOKEN_OCTAL
const G_TOKEN_INT = C.G_TOKEN_INT
const G_TOKEN_HEX = C.G_TOKEN_HEX
const G_TOKEN_FLOAT = C.G_TOKEN_FLOAT
const G_TOKEN_STRING = C.G_TOKEN_STRING
const G_TOKEN_SYMBOL = C.G_TOKEN_SYMBOL
const G_TOKEN_IDENTIFIER = C.G_TOKEN_IDENTIFIER
const G_TOKEN_IDENTIFIER_NULL = C.G_TOKEN_IDENTIFIER_NULL
const G_TOKEN_COMMENT_SINGLE = C.G_TOKEN_COMMENT_SINGLE
const G_TOKEN_COMMENT_MULTI = C.G_TOKEN_COMMENT_MULTI
const G_IN_ORDER = C.G_IN_ORDER
const G_PRE_ORDER = C.G_PRE_ORDER
const G_POST_ORDER = C.G_POST_ORDER
const G_LEVEL_ORDER = C.G_LEVEL_ORDER
const G_UNICODE_BREAK_MANDATORY = C.G_UNICODE_BREAK_MANDATORY
const G_UNICODE_BREAK_CARRIAGE_RETURN = C.G_UNICODE_BREAK_CARRIAGE_RETURN
const G_UNICODE_BREAK_LINE_FEED = C.G_UNICODE_BREAK_LINE_FEED
const G_UNICODE_BREAK_COMBINING_MARK = C.G_UNICODE_BREAK_COMBINING_MARK
const G_UNICODE_BREAK_SURROGATE = C.G_UNICODE_BREAK_SURROGATE
const G_UNICODE_BREAK_ZERO_WIDTH_SPACE = C.G_UNICODE_BREAK_ZERO_WIDTH_SPACE
const G_UNICODE_BREAK_INSEPARABLE = C.G_UNICODE_BREAK_INSEPARABLE
const G_UNICODE_BREAK_NON_BREAKING_GLUE = C.G_UNICODE_BREAK_NON_BREAKING_GLUE
const G_UNICODE_BREAK_CONTINGENT = C.G_UNICODE_BREAK_CONTINGENT
const G_UNICODE_BREAK_SPACE = C.G_UNICODE_BREAK_SPACE
const G_UNICODE_BREAK_AFTER = C.G_UNICODE_BREAK_AFTER
const G_UNICODE_BREAK_BEFORE = C.G_UNICODE_BREAK_BEFORE
const G_UNICODE_BREAK_BEFORE_AND_AFTER = C.G_UNICODE_BREAK_BEFORE_AND_AFTER
const G_UNICODE_BREAK_HYPHEN = C.G_UNICODE_BREAK_HYPHEN
const G_UNICODE_BREAK_NON_STARTER = C.G_UNICODE_BREAK_NON_STARTER
const G_UNICODE_BREAK_OPEN_PUNCTUATION = C.G_UNICODE_BREAK_OPEN_PUNCTUATION
const G_UNICODE_BREAK_CLOSE_PUNCTUATION = C.G_UNICODE_BREAK_CLOSE_PUNCTUATION
const G_UNICODE_BREAK_QUOTATION = C.G_UNICODE_BREAK_QUOTATION
const G_UNICODE_BREAK_EXCLAMATION = C.G_UNICODE_BREAK_EXCLAMATION
const G_UNICODE_BREAK_IDEOGRAPHIC = C.G_UNICODE_BREAK_IDEOGRAPHIC
const G_UNICODE_BREAK_NUMERIC = C.G_UNICODE_BREAK_NUMERIC
const G_UNICODE_BREAK_INFIX_SEPARATOR = C.G_UNICODE_BREAK_INFIX_SEPARATOR
const G_UNICODE_BREAK_SYMBOL = C.G_UNICODE_BREAK_SYMBOL
const G_UNICODE_BREAK_ALPHABETIC = C.G_UNICODE_BREAK_ALPHABETIC
const G_UNICODE_BREAK_PREFIX = C.G_UNICODE_BREAK_PREFIX
const G_UNICODE_BREAK_POSTFIX = C.G_UNICODE_BREAK_POSTFIX
const G_UNICODE_BREAK_COMPLEX_CONTEXT = C.G_UNICODE_BREAK_COMPLEX_CONTEXT
const G_UNICODE_BREAK_AMBIGUOUS = C.G_UNICODE_BREAK_AMBIGUOUS
const G_UNICODE_BREAK_UNKNOWN = C.G_UNICODE_BREAK_UNKNOWN
const G_UNICODE_BREAK_NEXT_LINE = C.G_UNICODE_BREAK_NEXT_LINE
const G_UNICODE_BREAK_WORD_JOINER = C.G_UNICODE_BREAK_WORD_JOINER
const G_UNICODE_BREAK_HANGUL_L_JAMO = C.G_UNICODE_BREAK_HANGUL_L_JAMO
const G_UNICODE_BREAK_HANGUL_V_JAMO = C.G_UNICODE_BREAK_HANGUL_V_JAMO
const G_UNICODE_BREAK_HANGUL_T_JAMO = C.G_UNICODE_BREAK_HANGUL_T_JAMO
const G_UNICODE_BREAK_HANGUL_LV_SYLLABLE = C.G_UNICODE_BREAK_HANGUL_LV_SYLLABLE
const G_UNICODE_BREAK_HANGUL_LVT_SYLLABLE = C.G_UNICODE_BREAK_HANGUL_LVT_SYLLABLE
const G_UNICODE_BREAK_CLOSE_PARANTHESIS = C.G_UNICODE_BREAK_CLOSE_PARANTHESIS
const G_UNICODE_BREAK_CONDITIONAL_JAPANESE_STARTER = C.G_UNICODE_BREAK_CONDITIONAL_JAPANESE_STARTER
const G_UNICODE_BREAK_HEBREW_LETTER = C.G_UNICODE_BREAK_HEBREW_LETTER
const G_UNICODE_BREAK_REGIONAL_INDICATOR = C.G_UNICODE_BREAK_REGIONAL_INDICATOR
const G_UNICODE_SCRIPT_INVALID_CODE = C.G_UNICODE_SCRIPT_INVALID_CODE
const G_UNICODE_SCRIPT_COMMON = C.G_UNICODE_SCRIPT_COMMON
const G_UNICODE_SCRIPT_INHERITED = C.G_UNICODE_SCRIPT_INHERITED
const G_UNICODE_SCRIPT_ARABIC = C.G_UNICODE_SCRIPT_ARABIC
const G_UNICODE_SCRIPT_ARMENIAN = C.G_UNICODE_SCRIPT_ARMENIAN
const G_UNICODE_SCRIPT_BENGALI = C.G_UNICODE_SCRIPT_BENGALI
const G_UNICODE_SCRIPT_BOPOMOFO = C.G_UNICODE_SCRIPT_BOPOMOFO
const G_UNICODE_SCRIPT_CHEROKEE = C.G_UNICODE_SCRIPT_CHEROKEE
const G_UNICODE_SCRIPT_COPTIC = C.G_UNICODE_SCRIPT_COPTIC
const G_UNICODE_SCRIPT_CYRILLIC = C.G_UNICODE_SCRIPT_CYRILLIC
const G_UNICODE_SCRIPT_DESERET = C.G_UNICODE_SCRIPT_DESERET
const G_UNICODE_SCRIPT_DEVANAGARI = C.G_UNICODE_SCRIPT_DEVANAGARI
const G_UNICODE_SCRIPT_ETHIOPIC = C.G_UNICODE_SCRIPT_ETHIOPIC
const G_UNICODE_SCRIPT_GEORGIAN = C.G_UNICODE_SCRIPT_GEORGIAN
const G_UNICODE_SCRIPT_GOTHIC = C.G_UNICODE_SCRIPT_GOTHIC
const G_UNICODE_SCRIPT_GREEK = C.G_UNICODE_SCRIPT_GREEK
const G_UNICODE_SCRIPT_GUJARATI = C.G_UNICODE_SCRIPT_GUJARATI
const G_UNICODE_SCRIPT_GURMUKHI = C.G_UNICODE_SCRIPT_GURMUKHI
const G_UNICODE_SCRIPT_HAN = C.G_UNICODE_SCRIPT_HAN
const G_UNICODE_SCRIPT_HANGUL = C.G_UNICODE_SCRIPT_HANGUL
const G_UNICODE_SCRIPT_HEBREW = C.G_UNICODE_SCRIPT_HEBREW
const G_UNICODE_SCRIPT_HIRAGANA = C.G_UNICODE_SCRIPT_HIRAGANA
const G_UNICODE_SCRIPT_KANNADA = C.G_UNICODE_SCRIPT_KANNADA
const G_UNICODE_SCRIPT_KATAKANA = C.G_UNICODE_SCRIPT_KATAKANA
const G_UNICODE_SCRIPT_KHMER = C.G_UNICODE_SCRIPT_KHMER
const G_UNICODE_SCRIPT_LAO = C.G_UNICODE_SCRIPT_LAO
const G_UNICODE_SCRIPT_LATIN = C.G_UNICODE_SCRIPT_LATIN
const G_UNICODE_SCRIPT_MALAYALAM = C.G_UNICODE_SCRIPT_MALAYALAM
const G_UNICODE_SCRIPT_MONGOLIAN = C.G_UNICODE_SCRIPT_MONGOLIAN
const G_UNICODE_SCRIPT_MYANMAR = C.G_UNICODE_SCRIPT_MYANMAR
const G_UNICODE_SCRIPT_OGHAM = C.G_UNICODE_SCRIPT_OGHAM
const G_UNICODE_SCRIPT_OLD_ITALIC = C.G_UNICODE_SCRIPT_OLD_ITALIC
const G_UNICODE_SCRIPT_ORIYA = C.G_UNICODE_SCRIPT_ORIYA
const G_UNICODE_SCRIPT_RUNIC = C.G_UNICODE_SCRIPT_RUNIC
const G_UNICODE_SCRIPT_SINHALA = C.G_UNICODE_SCRIPT_SINHALA
const G_UNICODE_SCRIPT_SYRIAC = C.G_UNICODE_SCRIPT_SYRIAC
const G_UNICODE_SCRIPT_TAMIL = C.G_UNICODE_SCRIPT_TAMIL
const G_UNICODE_SCRIPT_TELUGU = C.G_UNICODE_SCRIPT_TELUGU
const G_UNICODE_SCRIPT_THAANA = C.G_UNICODE_SCRIPT_THAANA
const G_UNICODE_SCRIPT_THAI = C.G_UNICODE_SCRIPT_THAI
const G_UNICODE_SCRIPT_TIBETAN = C.G_UNICODE_SCRIPT_TIBETAN
const G_UNICODE_SCRIPT_CANADIAN_ABORIGINAL = C.G_UNICODE_SCRIPT_CANADIAN_ABORIGINAL
const G_UNICODE_SCRIPT_YI = C.G_UNICODE_SCRIPT_YI
const G_UNICODE_SCRIPT_TAGALOG = C.G_UNICODE_SCRIPT_TAGALOG
const G_UNICODE_SCRIPT_HANUNOO = C.G_UNICODE_SCRIPT_HANUNOO
const G_UNICODE_SCRIPT_BUHID = C.G_UNICODE_SCRIPT_BUHID
const G_UNICODE_SCRIPT_TAGBANWA = C.G_UNICODE_SCRIPT_TAGBANWA
const G_UNICODE_SCRIPT_BRAILLE = C.G_UNICODE_SCRIPT_BRAILLE
const G_UNICODE_SCRIPT_CYPRIOT = C.G_UNICODE_SCRIPT_CYPRIOT
const G_UNICODE_SCRIPT_LIMBU = C.G_UNICODE_SCRIPT_LIMBU
const G_UNICODE_SCRIPT_OSMANYA = C.G_UNICODE_SCRIPT_OSMANYA
const G_UNICODE_SCRIPT_SHAVIAN = C.G_UNICODE_SCRIPT_SHAVIAN
const G_UNICODE_SCRIPT_LINEAR_B = C.G_UNICODE_SCRIPT_LINEAR_B
const G_UNICODE_SCRIPT_TAI_LE = C.G_UNICODE_SCRIPT_TAI_LE
const G_UNICODE_SCRIPT_UGARITIC = C.G_UNICODE_SCRIPT_UGARITIC
const G_UNICODE_SCRIPT_NEW_TAI_LUE = C.G_UNICODE_SCRIPT_NEW_TAI_LUE
const G_UNICODE_SCRIPT_BUGINESE = C.G_UNICODE_SCRIPT_BUGINESE
const G_UNICODE_SCRIPT_GLAGOLITIC = C.G_UNICODE_SCRIPT_GLAGOLITIC
const G_UNICODE_SCRIPT_TIFINAGH = C.G_UNICODE_SCRIPT_TIFINAGH
const G_UNICODE_SCRIPT_SYLOTI_NAGRI = C.G_UNICODE_SCRIPT_SYLOTI_NAGRI
const G_UNICODE_SCRIPT_OLD_PERSIAN = C.G_UNICODE_SCRIPT_OLD_PERSIAN
const G_UNICODE_SCRIPT_KHAROSHTHI = C.G_UNICODE_SCRIPT_KHAROSHTHI
const G_UNICODE_SCRIPT_UNKNOWN = C.G_UNICODE_SCRIPT_UNKNOWN
const G_UNICODE_SCRIPT_BALINESE = C.G_UNICODE_SCRIPT_BALINESE
const G_UNICODE_SCRIPT_CUNEIFORM = C.G_UNICODE_SCRIPT_CUNEIFORM
const G_UNICODE_SCRIPT_PHOENICIAN = C.G_UNICODE_SCRIPT_PHOENICIAN
const G_UNICODE_SCRIPT_PHAGS_PA = C.G_UNICODE_SCRIPT_PHAGS_PA
const G_UNICODE_SCRIPT_NKO = C.G_UNICODE_SCRIPT_NKO
const G_UNICODE_SCRIPT_KAYAH_LI = C.G_UNICODE_SCRIPT_KAYAH_LI
const G_UNICODE_SCRIPT_LEPCHA = C.G_UNICODE_SCRIPT_LEPCHA
const G_UNICODE_SCRIPT_REJANG = C.G_UNICODE_SCRIPT_REJANG
const G_UNICODE_SCRIPT_SUNDANESE = C.G_UNICODE_SCRIPT_SUNDANESE
const G_UNICODE_SCRIPT_SAURASHTRA = C.G_UNICODE_SCRIPT_SAURASHTRA
const G_UNICODE_SCRIPT_CHAM = C.G_UNICODE_SCRIPT_CHAM
const G_UNICODE_SCRIPT_OL_CHIKI = C.G_UNICODE_SCRIPT_OL_CHIKI
const G_UNICODE_SCRIPT_VAI = C.G_UNICODE_SCRIPT_VAI
const G_UNICODE_SCRIPT_CARIAN = C.G_UNICODE_SCRIPT_CARIAN
const G_UNICODE_SCRIPT_LYCIAN = C.G_UNICODE_SCRIPT_LYCIAN
const G_UNICODE_SCRIPT_LYDIAN = C.G_UNICODE_SCRIPT_LYDIAN
const G_UNICODE_SCRIPT_AVESTAN = C.G_UNICODE_SCRIPT_AVESTAN
const G_UNICODE_SCRIPT_BAMUM = C.G_UNICODE_SCRIPT_BAMUM
const G_UNICODE_SCRIPT_EGYPTIAN_HIEROGLYPHS = C.G_UNICODE_SCRIPT_EGYPTIAN_HIEROGLYPHS
const G_UNICODE_SCRIPT_IMPERIAL_ARAMAIC = C.G_UNICODE_SCRIPT_IMPERIAL_ARAMAIC
const G_UNICODE_SCRIPT_INSCRIPTIONAL_PAHLAVI = C.G_UNICODE_SCRIPT_INSCRIPTIONAL_PAHLAVI
const G_UNICODE_SCRIPT_INSCRIPTIONAL_PARTHIAN = C.G_UNICODE_SCRIPT_INSCRIPTIONAL_PARTHIAN
const G_UNICODE_SCRIPT_JAVANESE = C.G_UNICODE_SCRIPT_JAVANESE
const G_UNICODE_SCRIPT_KAITHI = C.G_UNICODE_SCRIPT_KAITHI
const G_UNICODE_SCRIPT_LISU = C.G_UNICODE_SCRIPT_LISU
const G_UNICODE_SCRIPT_MEETEI_MAYEK = C.G_UNICODE_SCRIPT_MEETEI_MAYEK
const G_UNICODE_SCRIPT_OLD_SOUTH_ARABIAN = C.G_UNICODE_SCRIPT_OLD_SOUTH_ARABIAN
const G_UNICODE_SCRIPT_OLD_TURKIC = C.G_UNICODE_SCRIPT_OLD_TURKIC
const G_UNICODE_SCRIPT_SAMARITAN = C.G_UNICODE_SCRIPT_SAMARITAN
const G_UNICODE_SCRIPT_TAI_THAM = C.G_UNICODE_SCRIPT_TAI_THAM
const G_UNICODE_SCRIPT_TAI_VIET = C.G_UNICODE_SCRIPT_TAI_VIET
const G_UNICODE_SCRIPT_BATAK = C.G_UNICODE_SCRIPT_BATAK
const G_UNICODE_SCRIPT_BRAHMI = C.G_UNICODE_SCRIPT_BRAHMI
const G_UNICODE_SCRIPT_MANDAIC = C.G_UNICODE_SCRIPT_MANDAIC
const G_UNICODE_SCRIPT_CHAKMA = C.G_UNICODE_SCRIPT_CHAKMA
const G_UNICODE_SCRIPT_MEROITIC_CURSIVE = C.G_UNICODE_SCRIPT_MEROITIC_CURSIVE
const G_UNICODE_SCRIPT_MEROITIC_HIEROGLYPHS = C.G_UNICODE_SCRIPT_MEROITIC_HIEROGLYPHS
const G_UNICODE_SCRIPT_MIAO = C.G_UNICODE_SCRIPT_MIAO
const G_UNICODE_SCRIPT_SHARADA = C.G_UNICODE_SCRIPT_SHARADA
const G_UNICODE_SCRIPT_SORA_SOMPENG = C.G_UNICODE_SCRIPT_SORA_SOMPENG
const G_UNICODE_SCRIPT_TAKRI = C.G_UNICODE_SCRIPT_TAKRI
const G_UNICODE_CONTROL = C.G_UNICODE_CONTROL
const G_UNICODE_FORMAT = C.G_UNICODE_FORMAT
const G_UNICODE_UNASSIGNED = C.G_UNICODE_UNASSIGNED
const G_UNICODE_PRIVATE_USE = C.G_UNICODE_PRIVATE_USE
const G_UNICODE_SURROGATE = C.G_UNICODE_SURROGATE
const G_UNICODE_LOWERCASE_LETTER = C.G_UNICODE_LOWERCASE_LETTER
const G_UNICODE_MODIFIER_LETTER = C.G_UNICODE_MODIFIER_LETTER
const G_UNICODE_OTHER_LETTER = C.G_UNICODE_OTHER_LETTER
const G_UNICODE_TITLECASE_LETTER = C.G_UNICODE_TITLECASE_LETTER
const G_UNICODE_UPPERCASE_LETTER = C.G_UNICODE_UPPERCASE_LETTER
const G_UNICODE_SPACING_MARK = C.G_UNICODE_SPACING_MARK
const G_UNICODE_ENCLOSING_MARK = C.G_UNICODE_ENCLOSING_MARK
const G_UNICODE_NON_SPACING_MARK = C.G_UNICODE_NON_SPACING_MARK
const G_UNICODE_DECIMAL_NUMBER = C.G_UNICODE_DECIMAL_NUMBER
const G_UNICODE_LETTER_NUMBER = C.G_UNICODE_LETTER_NUMBER
const G_UNICODE_OTHER_NUMBER = C.G_UNICODE_OTHER_NUMBER
const G_UNICODE_CONNECT_PUNCTUATION = C.G_UNICODE_CONNECT_PUNCTUATION
const G_UNICODE_DASH_PUNCTUATION = C.G_UNICODE_DASH_PUNCTUATION
const G_UNICODE_CLOSE_PUNCTUATION = C.G_UNICODE_CLOSE_PUNCTUATION
const G_UNICODE_FINAL_PUNCTUATION = C.G_UNICODE_FINAL_PUNCTUATION
const G_UNICODE_INITIAL_PUNCTUATION = C.G_UNICODE_INITIAL_PUNCTUATION
const G_UNICODE_OTHER_PUNCTUATION = C.G_UNICODE_OTHER_PUNCTUATION
const G_UNICODE_OPEN_PUNCTUATION = C.G_UNICODE_OPEN_PUNCTUATION
const G_UNICODE_CURRENCY_SYMBOL = C.G_UNICODE_CURRENCY_SYMBOL
const G_UNICODE_MODIFIER_SYMBOL = C.G_UNICODE_MODIFIER_SYMBOL
const G_UNICODE_MATH_SYMBOL = C.G_UNICODE_MATH_SYMBOL
const G_UNICODE_OTHER_SYMBOL = C.G_UNICODE_OTHER_SYMBOL
const G_UNICODE_LINE_SEPARATOR = C.G_UNICODE_LINE_SEPARATOR
const G_UNICODE_PARAGRAPH_SEPARATOR = C.G_UNICODE_PARAGRAPH_SEPARATOR
const G_UNICODE_SPACE_SEPARATOR = C.G_UNICODE_SPACE_SEPARATOR
const G_USER_DIRECTORY_DESKTOP = C.G_USER_DIRECTORY_DESKTOP
const G_USER_DIRECTORY_DOCUMENTS = C.G_USER_DIRECTORY_DOCUMENTS
const G_USER_DIRECTORY_DOWNLOAD = C.G_USER_DIRECTORY_DOWNLOAD
const G_USER_DIRECTORY_MUSIC = C.G_USER_DIRECTORY_MUSIC
const G_USER_DIRECTORY_PICTURES = C.G_USER_DIRECTORY_PICTURES
const G_USER_DIRECTORY_PUBLIC_SHARE = C.G_USER_DIRECTORY_PUBLIC_SHARE
const G_USER_DIRECTORY_TEMPLATES = C.G_USER_DIRECTORY_TEMPLATES
const G_USER_DIRECTORY_VIDEOS = C.G_USER_DIRECTORY_VIDEOS
const G_USER_N_DIRECTORIES = C.G_USER_N_DIRECTORIES
const G_VARIANT_CLASS_BOOLEAN = C.G_VARIANT_CLASS_BOOLEAN
const G_VARIANT_CLASS_BYTE = C.G_VARIANT_CLASS_BYTE
const G_VARIANT_CLASS_INT16 = C.G_VARIANT_CLASS_INT16
const G_VARIANT_CLASS_UINT16 = C.G_VARIANT_CLASS_UINT16
const G_VARIANT_CLASS_INT32 = C.G_VARIANT_CLASS_INT32
const G_VARIANT_CLASS_UINT32 = C.G_VARIANT_CLASS_UINT32
const G_VARIANT_CLASS_INT64 = C.G_VARIANT_CLASS_INT64
const G_VARIANT_CLASS_UINT64 = C.G_VARIANT_CLASS_UINT64
const G_VARIANT_CLASS_HANDLE = C.G_VARIANT_CLASS_HANDLE
const G_VARIANT_CLASS_DOUBLE = C.G_VARIANT_CLASS_DOUBLE
const G_VARIANT_CLASS_STRING = C.G_VARIANT_CLASS_STRING
const G_VARIANT_CLASS_OBJECT_PATH = C.G_VARIANT_CLASS_OBJECT_PATH
const G_VARIANT_CLASS_SIGNATURE = C.G_VARIANT_CLASS_SIGNATURE
const G_VARIANT_CLASS_VARIANT = C.G_VARIANT_CLASS_VARIANT
const G_VARIANT_CLASS_MAYBE = C.G_VARIANT_CLASS_MAYBE
const G_VARIANT_CLASS_ARRAY = C.G_VARIANT_CLASS_ARRAY
const G_VARIANT_CLASS_TUPLE = C.G_VARIANT_CLASS_TUPLE
const G_VARIANT_CLASS_DICT_ENTRY = C.G_VARIANT_CLASS_DICT_ENTRY
const G_VARIANT_PARSE_ERROR_FAILED = C.G_VARIANT_PARSE_ERROR_FAILED
const G_VARIANT_PARSE_ERROR_BASIC_TYPE_EXPECTED = C.G_VARIANT_PARSE_ERROR_BASIC_TYPE_EXPECTED
const G_VARIANT_PARSE_ERROR_CANNOT_INFER_TYPE = C.G_VARIANT_PARSE_ERROR_CANNOT_INFER_TYPE
const G_VARIANT_PARSE_ERROR_DEFINITE_TYPE_EXPECTED = C.G_VARIANT_PARSE_ERROR_DEFINITE_TYPE_EXPECTED
const G_VARIANT_PARSE_ERROR_INPUT_NOT_AT_END = C.G_VARIANT_PARSE_ERROR_INPUT_NOT_AT_END
const G_VARIANT_PARSE_ERROR_INVALID_CHARACTER = C.G_VARIANT_PARSE_ERROR_INVALID_CHARACTER
const G_VARIANT_PARSE_ERROR_INVALID_FORMAT_STRING = C.G_VARIANT_PARSE_ERROR_INVALID_FORMAT_STRING
const G_VARIANT_PARSE_ERROR_INVALID_OBJECT_PATH = C.G_VARIANT_PARSE_ERROR_INVALID_OBJECT_PATH
const G_VARIANT_PARSE_ERROR_INVALID_SIGNATURE = C.G_VARIANT_PARSE_ERROR_INVALID_SIGNATURE
const G_VARIANT_PARSE_ERROR_INVALID_TYPE_STRING = C.G_VARIANT_PARSE_ERROR_INVALID_TYPE_STRING
const G_VARIANT_PARSE_ERROR_NO_COMMON_TYPE = C.G_VARIANT_PARSE_ERROR_NO_COMMON_TYPE
const G_VARIANT_PARSE_ERROR_NUMBER_OUT_OF_RANGE = C.G_VARIANT_PARSE_ERROR_NUMBER_OUT_OF_RANGE
const G_VARIANT_PARSE_ERROR_NUMBER_TOO_BIG = C.G_VARIANT_PARSE_ERROR_NUMBER_TOO_BIG
const G_VARIANT_PARSE_ERROR_TYPE_ERROR = C.G_VARIANT_PARSE_ERROR_TYPE_ERROR
const G_VARIANT_PARSE_ERROR_UNEXPECTED_TOKEN = C.G_VARIANT_PARSE_ERROR_UNEXPECTED_TOKEN
const G_VARIANT_PARSE_ERROR_UNKNOWN_KEYWORD = C.G_VARIANT_PARSE_ERROR_UNKNOWN_KEYWORD
const G_VARIANT_PARSE_ERROR_UNTERMINATED_STRING_CONSTANT = C.G_VARIANT_PARSE_ERROR_UNTERMINATED_STRING_CONSTANT
const G_VARIANT_PARSE_ERROR_VALUE_EXPECTED = C.G_VARIANT_PARSE_ERROR_VALUE_EXPECTED
const G_ASCII_DTOSTR_BUF_SIZE = C.G_ASCII_DTOSTR_BUF_SIZE
const G_BIG_ENDIAN = C.G_BIG_ENDIAN
const G_CAN_INLINE = C.G_CAN_INLINE
const G_CSET_A_2_Z = C.G_CSET_A_2_Z
const G_CSET_DIGITS = C.G_CSET_DIGITS
const G_CSET_a_2_z = C.G_CSET_a_2_z
const G_DATALIST_FLAGS_MASK = C.G_DATALIST_FLAGS_MASK
const G_DATE_BAD_DAY = C.G_DATE_BAD_DAY
const G_DATE_BAD_JULIAN = C.G_DATE_BAD_JULIAN
const G_DATE_BAD_YEAR = C.G_DATE_BAD_YEAR
const G_DIR_SEPARATOR = C.G_DIR_SEPARATOR
const G_DIR_SEPARATOR_S = C.G_DIR_SEPARATOR_S
const G_GINT16_FORMAT = C.G_GINT16_FORMAT
const G_GINT16_MODIFIER = C.G_GINT16_MODIFIER
const G_GINT32_FORMAT = C.G_GINT32_FORMAT
const G_GINT32_MODIFIER = C.G_GINT32_MODIFIER
const G_GINT64_FORMAT = C.G_GINT64_FORMAT
const G_GINT64_MODIFIER = C.G_GINT64_MODIFIER
const G_GINTPTR_FORMAT = C.G_GINTPTR_FORMAT
const G_GINTPTR_MODIFIER = C.G_GINTPTR_MODIFIER
const G_GNUC_FUNCTION = C.G_GNUC_FUNCTION
const G_GNUC_PRETTY_FUNCTION = C.G_GNUC_PRETTY_FUNCTION
const G_GSIZE_FORMAT = C.G_GSIZE_FORMAT
const G_GSIZE_MODIFIER = C.G_GSIZE_MODIFIER
const G_GSSIZE_FORMAT = C.G_GSSIZE_FORMAT
const G_GUINT16_FORMAT = C.G_GUINT16_FORMAT
const G_GUINT32_FORMAT = C.G_GUINT32_FORMAT
const G_GUINT64_FORMAT = C.G_GUINT64_FORMAT
const G_GUINTPTR_FORMAT = C.G_GUINTPTR_FORMAT
const G_HAVE_GINT64 = C.G_HAVE_GINT64
const G_HAVE_GNUC_VARARGS = C.G_HAVE_GNUC_VARARGS
const G_HAVE_GNUC_VISIBILITY = C.G_HAVE_GNUC_VISIBILITY
const G_HAVE_GROWING_STACK = C.G_HAVE_GROWING_STACK
const G_HAVE_INLINE = C.G_HAVE_INLINE
const G_HAVE_ISO_VARARGS = C.G_HAVE_ISO_VARARGS
const G_HAVE___INLINE = C.G_HAVE___INLINE
const G_HAVE___INLINE__ = C.G_HAVE___INLINE__
const G_HOOK_FLAG_USER_SHIFT = C.G_HOOK_FLAG_USER_SHIFT
const G_IEEE754_DOUBLE_BIAS = C.G_IEEE754_DOUBLE_BIAS
const G_IEEE754_FLOAT_BIAS = C.G_IEEE754_FLOAT_BIAS
const G_KEY_FILE_DESKTOP_GROUP = C.G_KEY_FILE_DESKTOP_GROUP
const G_KEY_FILE_DESKTOP_KEY_CATEGORIES = C.G_KEY_FILE_DESKTOP_KEY_CATEGORIES
const G_KEY_FILE_DESKTOP_KEY_COMMENT = C.G_KEY_FILE_DESKTOP_KEY_COMMENT
const G_KEY_FILE_DESKTOP_KEY_EXEC = C.G_KEY_FILE_DESKTOP_KEY_EXEC
const G_KEY_FILE_DESKTOP_KEY_GENERIC_NAME = C.G_KEY_FILE_DESKTOP_KEY_GENERIC_NAME
const G_KEY_FILE_DESKTOP_KEY_HIDDEN = C.G_KEY_FILE_DESKTOP_KEY_HIDDEN
const G_KEY_FILE_DESKTOP_KEY_ICON = C.G_KEY_FILE_DESKTOP_KEY_ICON
const G_KEY_FILE_DESKTOP_KEY_MIME_TYPE = C.G_KEY_FILE_DESKTOP_KEY_MIME_TYPE
const G_KEY_FILE_DESKTOP_KEY_NAME = C.G_KEY_FILE_DESKTOP_KEY_NAME
const G_KEY_FILE_DESKTOP_KEY_NOT_SHOW_IN = C.G_KEY_FILE_DESKTOP_KEY_NOT_SHOW_IN
const G_KEY_FILE_DESKTOP_KEY_NO_DISPLAY = C.G_KEY_FILE_DESKTOP_KEY_NO_DISPLAY
const G_KEY_FILE_DESKTOP_KEY_ONLY_SHOW_IN = C.G_KEY_FILE_DESKTOP_KEY_ONLY_SHOW_IN
const G_KEY_FILE_DESKTOP_KEY_PATH = C.G_KEY_FILE_DESKTOP_KEY_PATH
const G_KEY_FILE_DESKTOP_KEY_STARTUP_NOTIFY = C.G_KEY_FILE_DESKTOP_KEY_STARTUP_NOTIFY
const G_KEY_FILE_DESKTOP_KEY_STARTUP_WM_CLASS = C.G_KEY_FILE_DESKTOP_KEY_STARTUP_WM_CLASS
const G_KEY_FILE_DESKTOP_KEY_TERMINAL = C.G_KEY_FILE_DESKTOP_KEY_TERMINAL
const G_KEY_FILE_DESKTOP_KEY_TRY_EXEC = C.G_KEY_FILE_DESKTOP_KEY_TRY_EXEC
const G_KEY_FILE_DESKTOP_KEY_TYPE = C.G_KEY_FILE_DESKTOP_KEY_TYPE
const G_KEY_FILE_DESKTOP_KEY_URL = C.G_KEY_FILE_DESKTOP_KEY_URL
const G_KEY_FILE_DESKTOP_KEY_VERSION = C.G_KEY_FILE_DESKTOP_KEY_VERSION
const G_KEY_FILE_DESKTOP_TYPE_APPLICATION = C.G_KEY_FILE_DESKTOP_TYPE_APPLICATION
const G_KEY_FILE_DESKTOP_TYPE_DIRECTORY = C.G_KEY_FILE_DESKTOP_TYPE_DIRECTORY
const G_KEY_FILE_DESKTOP_TYPE_LINK = C.G_KEY_FILE_DESKTOP_TYPE_LINK
const G_LITTLE_ENDIAN = C.G_LITTLE_ENDIAN
const G_LOG_FATAL_MASK = C.G_LOG_FATAL_MASK
const G_LOG_LEVEL_USER_SHIFT = C.G_LOG_LEVEL_USER_SHIFT
const GLIB_MAJOR_VERSION = C.GLIB_MAJOR_VERSION
const G_MAXINT16 = C.G_MAXINT16
const G_MAXINT32 = C.G_MAXINT32
const G_MAXINT64 = C.G_MAXINT64
const G_MAXINT8 = C.G_MAXINT8
const G_MAXUINT16 = C.G_MAXUINT16
const G_MAXUINT32 = C.G_MAXUINT32
const G_MAXUINT64 = C.G_MAXUINT64
const G_MAXUINT8 = C.G_MAXUINT8
const GLIB_MICRO_VERSION = C.GLIB_MICRO_VERSION
const G_MININT16 = C.G_MININT16
const G_MININT32 = C.G_MININT32
const G_MININT64 = C.G_MININT64
const G_MININT8 = C.G_MININT8
const GLIB_MINOR_VERSION = C.GLIB_MINOR_VERSION
const G_MODULE_SUFFIX = C.G_MODULE_SUFFIX
const G_OPTION_REMAINING = C.G_OPTION_REMAINING
const G_PDP_ENDIAN = C.G_PDP_ENDIAN
const G_POLLFD_FORMAT = C.G_POLLFD_FORMAT
const G_PRIORITY_DEFAULT = C.G_PRIORITY_DEFAULT
const G_PRIORITY_DEFAULT_IDLE = C.G_PRIORITY_DEFAULT_IDLE
const G_PRIORITY_HIGH = C.G_PRIORITY_HIGH
const G_PRIORITY_HIGH_IDLE = C.G_PRIORITY_HIGH_IDLE
const G_PRIORITY_LOW = C.G_PRIORITY_LOW
const G_SEARCHPATH_SEPARATOR = C.G_SEARCHPATH_SEPARATOR
const G_SEARCHPATH_SEPARATOR_S = C.G_SEARCHPATH_SEPARATOR_S
const GLIB_SIZEOF_LONG = C.GLIB_SIZEOF_LONG
const GLIB_SIZEOF_SIZE_T = C.GLIB_SIZEOF_SIZE_T
const GLIB_SIZEOF_VOID_P = C.GLIB_SIZEOF_VOID_P
const G_STR_DELIMITERS = C.G_STR_DELIMITERS
const GLIB_SYSDEF_AF_INET = C.GLIB_SYSDEF_AF_INET
const GLIB_SYSDEF_AF_INET6 = C.GLIB_SYSDEF_AF_INET6
const GLIB_SYSDEF_AF_UNIX = C.GLIB_SYSDEF_AF_UNIX
const GLIB_SYSDEF_MSG_DONTROUTE = C.GLIB_SYSDEF_MSG_DONTROUTE
const GLIB_SYSDEF_MSG_OOB = C.GLIB_SYSDEF_MSG_OOB
const GLIB_SYSDEF_MSG_PEEK = C.GLIB_SYSDEF_MSG_PEEK
const G_TIME_SPAN_DAY = C.G_TIME_SPAN_DAY
const G_TIME_SPAN_HOUR = C.G_TIME_SPAN_HOUR
const G_TIME_SPAN_MILLISECOND = C.G_TIME_SPAN_MILLISECOND
const G_TIME_SPAN_MINUTE = C.G_TIME_SPAN_MINUTE
const G_TIME_SPAN_SECOND = C.G_TIME_SPAN_SECOND
const G_UNICHAR_MAX_DECOMPOSITION_LENGTH = C.G_UNICHAR_MAX_DECOMPOSITION_LENGTH
const G_URI_RESERVED_CHARS_GENERIC_DELIMITERS = C.G_URI_RESERVED_CHARS_GENERIC_DELIMITERS
const G_URI_RESERVED_CHARS_SUBCOMPONENT_DELIMITERS = C.G_URI_RESERVED_CHARS_SUBCOMPONENT_DELIMITERS
const G_USEC_PER_SEC = C.G_USEC_PER_SEC
const G_VA_COPY_AS_ARRAY = C.G_VA_COPY_AS_ARRAY
const GLIB_VERSION_MIN_REQUIRED = C.GLIB_VERSION_MIN_REQUIRED
