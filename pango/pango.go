// this file is auto-generated by go-gi

package pango

// #cgo pkg-config: pango gobject-2.0
// #include <string.h>
// #include <glib-object.h>
// #include <glib/gstdio.h>
// #include <glib-unix.h>
// #include <pango/pango.h>
/*
typedef long double longdouble;
gboolean _true() { return TRUE; }
gboolean _false() { return FALSE; }
PangoAttribute* _pango_attr_font_desc_new(void* desc) {
	return pango_attr_font_desc_new((const PangoFontDescription*)(desc));
}
PangoAttribute* _pango_attr_shape_new(void* ink_rect, void* logical_rect) {
	return pango_attr_shape_new((const PangoRectangle*)(ink_rect), (const PangoRectangle*)(logical_rect));
}
PangoAttribute* _pango_attr_shape_new_with_data(void* ink_rect, void* logical_rect, gpointer data, PangoAttrDataCopyFunc copy_func, GDestroyNotify destroy_func) {
	return pango_attr_shape_new_with_data((const PangoRectangle*)(ink_rect), (const PangoRectangle*)(logical_rect), data, copy_func, destroy_func);
}
PangoFontDescription* _pango_font_description_from_string(void* str) {
	return pango_font_description_from_string((const char*)(str));
}
PangoLanguage* _pango_language_from_string(void* language) {
	return pango_language_from_string((const char*)(language));
}
PangoScriptIter* _pango_script_iter_new(void* text, int length) {
	return pango_script_iter_new((const char*)(text), length);
}
PangoAttribute* _pango_attr_family_new(void* family) {
	return pango_attr_family_new((const char*)(family));
}
PangoAttrType _pango_attr_type_register(void* name) {
	return pango_attr_type_register((const gchar*)(name));
}
void _pango_break(void* text, int length, PangoAnalysis* analysis, PangoLogAttr* attrs, int attrs_len) {
	pango_break((const gchar*)(text), length, analysis, attrs, attrs_len);
}
PangoDirection _pango_find_base_dir(void* text, gint length) {
	return pango_find_base_dir((const gchar*)(text), length);
}
void _pango_find_paragraph_boundary(void* text, gint length, gint* paragraph_delimiter_index, gint* next_paragraph_start) {
	pango_find_paragraph_boundary((const gchar*)(text), length, paragraph_delimiter_index, next_paragraph_start);
}
void _pango_get_log_attrs(void* text, int length, int level, PangoLanguage* language, PangoLogAttr* log_attrs, int attrs_len) {
	pango_get_log_attrs((const char*)(text), length, level, language, log_attrs, attrs_len);
}
PangoGravity _pango_gravity_get_for_matrix(void* matrix) {
	return pango_gravity_get_for_matrix((const PangoMatrix*)(matrix));
}
GList* _pango_itemize(PangoContext* context, void* text, int start_index, int length, PangoAttrList* attrs, PangoAttrIterator* cached_iter) {
	return pango_itemize(context, (const char*)(text), start_index, length, attrs, cached_iter);
}
GList* _pango_itemize_with_base_dir(PangoContext* context, PangoDirection base_dir, void* text, int start_index, int length, PangoAttrList* attrs, PangoAttrIterator* cached_iter) {
	return pango_itemize_with_base_dir(context, base_dir, (const char*)(text), start_index, length, attrs, cached_iter);
}
guint8* _pango_log2vis_get_embedding_levels(void* text, int length, PangoDirection* pbase_dir) {
	return pango_log2vis_get_embedding_levels((const gchar*)(text), length, pbase_dir);
}
gboolean _pango_parse_enum(GType type_, void* str, int* value, gboolean warn, void* possible_values) {
	return pango_parse_enum(type_, (const char*)(str), value, warn, (char**)(possible_values));
}
gboolean _pango_parse_markup(void* markup_text, int length, gunichar accel_marker, void* attr_list, void* text, gunichar* accel_char, void* err) {
	return pango_parse_markup((const char*)(markup_text), length, accel_marker, (PangoAttrList**)(attr_list), (char**)(text), accel_char, (GError**)(err));
}
gboolean _pango_parse_stretch(void* str, PangoStretch* stretch, gboolean warn) {
	return pango_parse_stretch((const char*)(str), stretch, warn);
}
gboolean _pango_parse_style(void* str, PangoStyle* style, gboolean warn) {
	return pango_parse_style((const char*)(str), style, warn);
}
gboolean _pango_parse_variant(void* str, PangoVariant* variant, gboolean warn) {
	return pango_parse_variant((const char*)(str), variant, warn);
}
gboolean _pango_parse_weight(void* str, PangoWeight* weight, gboolean warn) {
	return pango_parse_weight((const char*)(str), weight, warn);
}
gboolean _pango_scan_int(void* pos, int* out) {
	return pango_scan_int((const char**)(pos), out);
}
gboolean _pango_scan_string(void* pos, GString* out) {
	return pango_scan_string((const char**)(pos), out);
}
gboolean _pango_scan_word(void* pos, GString* out) {
	return pango_scan_word((const char**)(pos), out);
}
void _pango_shape(void* text, gint length, void* analysis, PangoGlyphString* glyphs) {
	pango_shape((const gchar*)(text), length, (const PangoAnalysis*)(analysis), glyphs);
}
void _pango_shape_full(void* item_text, gint item_length, void* paragraph_text, gint paragraph_length, void* analysis, PangoGlyphString* glyphs) {
	pango_shape_full((const gchar*)(item_text), item_length, (const gchar*)(paragraph_text), paragraph_length, (const PangoAnalysis*)(analysis), glyphs);
}
gboolean _pango_skip_space(void* pos) {
	return pango_skip_space((const char**)(pos));
}
char** _pango_split_file_list(void* str) {
	return pango_split_file_list((const char*)(str));
}
char* _pango_trim_string(void* str) {
	return pango_trim_string((const char*)(str));
}
*/
import "C"
import (
	"unsafe"
	"runtime"
)

func AttrFontDescNew(desc *FontDescription) *Attribute {
	_cp_desc_ := (*C.PangoFontDescription)(desc)
	_c_return_ := C._pango_attr_font_desc_new(unsafe.Pointer(_cp_desc_))
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrLanguageNew(language *Language) *Attribute {
	_cp_language_ := (*C.PangoLanguage)(language)
	_c_return_ := C.pango_attr_language_new(_cp_language_)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrListNew() *AttrList {
	_c_return_ := C.pango_attr_list_new()
	_go_return_ := (*AttrList)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **AttrList) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrShapeNew(ink_rect *Rectangle, logical_rect *Rectangle) *Attribute {
	_cp_ink_rect_ := (*C.PangoRectangle)(ink_rect)
	_cp_logical_rect_ := (*C.PangoRectangle)(logical_rect)
	_c_return_ := C._pango_attr_shape_new(unsafe.Pointer(_cp_ink_rect_), unsafe.Pointer(_cp_logical_rect_))
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrShapeNewWithData(ink_rect *Rectangle, logical_rect *Rectangle, data unsafe.Pointer, copy_func C.PangoAttrDataCopyFunc, destroy_func C.GDestroyNotify) *Attribute {
	_cp_ink_rect_ := (*C.PangoRectangle)(ink_rect)
	_cp_logical_rect_ := (*C.PangoRectangle)(logical_rect)
	_gpointer_data := (C.gpointer)(data)
	_c_return_ := C._pango_attr_shape_new_with_data(unsafe.Pointer(_cp_ink_rect_), unsafe.Pointer(_cp_logical_rect_), _gpointer_data, copy_func, destroy_func)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrSizeNew(size C.int) *Attribute {
	_c_return_ := C.pango_attr_size_new(size)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrSizeNewAbsolute(size C.int) *Attribute {
	_c_return_ := C.pango_attr_size_new_absolute(size)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func CoverageFromBytes(bytes []byte, n_bytes C.int) *Coverage {
	_custr_bytes := unsafe.Pointer(C.CString(string(bytes)))
	defer C.free(_custr_bytes)
	_gustr_bytes := (*C.guchar)(unsafe.Pointer(_custr_bytes))
	_c_return_ := C.pango_coverage_from_bytes(_gustr_bytes, n_bytes)
	_go_return_ := (*Coverage)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Coverage) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func CoverageNew() *Coverage {
	_c_return_ := C.pango_coverage_new()
	_go_return_ := (*Coverage)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Coverage) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func FontDescriptionNew() *FontDescription {
	_c_return_ := C.pango_font_description_new()
	_go_return_ := (*FontDescription)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **FontDescription) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func FontDescriptionFromString(str *C.char) *FontDescription {
	_c_return_ := C._pango_font_description_from_string(unsafe.Pointer(str))
	_go_return_ := (*FontDescription)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **FontDescription) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func GlyphStringNew() *GlyphString {
	_c_return_ := C.pango_glyph_string_new()
	_go_return_ := (*GlyphString)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **GlyphString) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func ItemNew() *Item {
	_c_return_ := C.pango_item_new()
	_go_return_ := (*Item)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Item) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func LanguageFromString(language *C.char) *Language {
	_c_return_ := C._pango_language_from_string(unsafe.Pointer(language))
	_go_return_ := (*Language)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Language) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func LanguageGetDefault() *Language {
	_c_return_ := C.pango_language_get_default()
	_go_return_ := (*Language)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Language) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func ScriptIterNew(text *C.char, length C.int) *ScriptIter {
	_c_return_ := C._pango_script_iter_new(unsafe.Pointer(text), length)
	_go_return_ := (*ScriptIter)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **ScriptIter) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func TabArrayNew(initial_size int, positions_in_pixels bool) *TabArray {
	_gint_initial_size := C.gint(initial_size)
	_gbool_positions_in_pixels := C._false()
	if positions_in_pixels { _gbool_positions_in_pixels = C._true() }
	_c_return_ := C.pango_tab_array_new(_gint_initial_size, _gbool_positions_in_pixels)
	_go_return_ := (*TabArray)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **TabArray) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

//TODO pango_tab_array_new_with_positions

func AttrBackgroundNew(red uint16, green uint16, blue uint16) *Attribute {
	_guint16_red := C.guint16(red)
	_guint16_green := C.guint16(green)
	_guint16_blue := C.guint16(blue)
	_c_return_ := C.pango_attr_background_new(_guint16_red, _guint16_green, _guint16_blue)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrFallbackNew(enable_fallback bool) *Attribute {
	_gbool_enable_fallback := C._false()
	if enable_fallback { _gbool_enable_fallback = C._true() }
	_c_return_ := C.pango_attr_fallback_new(_gbool_enable_fallback)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrFamilyNew(family *C.char) *Attribute {
	_c_return_ := C._pango_attr_family_new(unsafe.Pointer(family))
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrForegroundNew(red uint16, green uint16, blue uint16) *Attribute {
	_guint16_red := C.guint16(red)
	_guint16_green := C.guint16(green)
	_guint16_blue := C.guint16(blue)
	_c_return_ := C.pango_attr_foreground_new(_guint16_red, _guint16_green, _guint16_blue)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrGravityHintNew(hint C.PangoGravityHint) *Attribute {
	_c_return_ := C.pango_attr_gravity_hint_new(hint)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrGravityNew(gravity C.PangoGravity) *Attribute {
	_c_return_ := C.pango_attr_gravity_new(gravity)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrLetterSpacingNew(letter_spacing C.int) *Attribute {
	_c_return_ := C.pango_attr_letter_spacing_new(letter_spacing)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrRiseNew(rise C.int) *Attribute {
	_c_return_ := C.pango_attr_rise_new(rise)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrScaleNew(scale_factor C.double) *Attribute {
	_c_return_ := C.pango_attr_scale_new(scale_factor)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrStretchNew(stretch C.PangoStretch) *Attribute {
	_c_return_ := C.pango_attr_stretch_new(stretch)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrStrikethroughColorNew(red uint16, green uint16, blue uint16) *Attribute {
	_guint16_red := C.guint16(red)
	_guint16_green := C.guint16(green)
	_guint16_blue := C.guint16(blue)
	_c_return_ := C.pango_attr_strikethrough_color_new(_guint16_red, _guint16_green, _guint16_blue)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrStrikethroughNew(strikethrough bool) *Attribute {
	_gbool_strikethrough := C._false()
	if strikethrough { _gbool_strikethrough = C._true() }
	_c_return_ := C.pango_attr_strikethrough_new(_gbool_strikethrough)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrStyleNew(style C.PangoStyle) *Attribute {
	_c_return_ := C.pango_attr_style_new(style)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrTypeGetName(type_ C.PangoAttrType) *C.char {
	return C.pango_attr_type_get_name(type_)
}

func AttrTypeRegister(name string) C.PangoAttrType {
	_cstr_name := unsafe.Pointer(C.CString(name))
	defer C.free(_cstr_name)
	_gstr_name := (*C.gchar)(unsafe.Pointer(_cstr_name))
	return C._pango_attr_type_register(unsafe.Pointer(_gstr_name))
}

func AttrUnderlineColorNew(red uint16, green uint16, blue uint16) *Attribute {
	_guint16_red := C.guint16(red)
	_guint16_green := C.guint16(green)
	_guint16_blue := C.guint16(blue)
	_c_return_ := C.pango_attr_underline_color_new(_guint16_red, _guint16_green, _guint16_blue)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrUnderlineNew(underline C.PangoUnderline) *Attribute {
	_c_return_ := C.pango_attr_underline_new(underline)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrVariantNew(variant C.PangoVariant) *Attribute {
	_c_return_ := C.pango_attr_variant_new(variant)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func AttrWeightNew(weight C.PangoWeight) *Attribute {
	_c_return_ := C.pango_attr_weight_new(weight)
	_go_return_ := (*Attribute)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Attribute) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func BidiTypeForUnichar(ch C.gunichar) C.PangoBidiType {
	return C.pango_bidi_type_for_unichar(ch)
}

func Break(text string, length C.int, analysis *Analysis, attrs *LogAttr, attrs_len C.int) {
	_cstr_text := unsafe.Pointer(C.CString(text))
	defer C.free(_cstr_text)
	_gstr_text := (*C.gchar)(unsafe.Pointer(_cstr_text))
	_cp_analysis_ := (*C.PangoAnalysis)(analysis)
	_cp_attrs_ := (*C.PangoLogAttr)(attrs)
	C._pango_break(unsafe.Pointer(_gstr_text), length, _cp_analysis_, _cp_attrs_, attrs_len)
}

func ExtentsToPixels(inclusive *Rectangle, nearest *Rectangle) {
	_cp_inclusive_ := (*C.PangoRectangle)(inclusive)
	_cp_nearest_ := (*C.PangoRectangle)(nearest)
	C.pango_extents_to_pixels(_cp_inclusive_, _cp_nearest_)
}

func FindBaseDir(text string, length int) C.PangoDirection {
	_cstr_text := unsafe.Pointer(C.CString(text))
	defer C.free(_cstr_text)
	_gstr_text := (*C.gchar)(unsafe.Pointer(_cstr_text))
	_gint_length := C.gint(length)
	return C._pango_find_base_dir(unsafe.Pointer(_gstr_text), _gint_length)
}

func FindParagraphBoundary(text string, length int, paragraph_delimiter_index *int, next_paragraph_start *int) {
	_cstr_text := unsafe.Pointer(C.CString(text))
	defer C.free(_cstr_text)
	_gstr_text := (*C.gchar)(unsafe.Pointer(_cstr_text))
	_gint_length := C.gint(length)
	_c_gint_paragraph_delimiter_index := C.gint(*paragraph_delimiter_index)
	_cp_gint_paragraph_delimiter_index := (*C.gint)(&_c_gint_paragraph_delimiter_index)
	_c_gint_next_paragraph_start := C.gint(*next_paragraph_start)
	_cp_gint_next_paragraph_start := (*C.gint)(&_c_gint_next_paragraph_start)
	C._pango_find_paragraph_boundary(unsafe.Pointer(_gstr_text), _gint_length, _cp_gint_paragraph_delimiter_index, _cp_gint_next_paragraph_start)
}

func GetLogAttrs(text *C.char, length C.int, level C.int, language *Language, log_attrs *LogAttr, attrs_len C.int) {
	_cp_language_ := (*C.PangoLanguage)(language)
	_cp_log_attrs_ := (*C.PangoLogAttr)(log_attrs)
	C._pango_get_log_attrs(unsafe.Pointer(text), length, level, _cp_language_, _cp_log_attrs_, attrs_len)
}

func GetMirrorChar(ch C.gunichar, mirrored_ch *C.gunichar) bool {
	return gboolean2bool(C.pango_get_mirror_char(ch, mirrored_ch))
}

func GravityGetForMatrix(matrix *Matrix) C.PangoGravity {
	_cp_matrix_ := (*C.PangoMatrix)(matrix)
	return C._pango_gravity_get_for_matrix(unsafe.Pointer(_cp_matrix_))
}

func GravityGetForScript(script C.PangoScript, base_gravity C.PangoGravity, hint C.PangoGravityHint) C.PangoGravity {
	return C.pango_gravity_get_for_script(script, base_gravity, hint)
}

func GravityGetForScriptAndWidth(script C.PangoScript, wide bool, base_gravity C.PangoGravity, hint C.PangoGravityHint) C.PangoGravity {
	_gbool_wide := C._false()
	if wide { _gbool_wide = C._true() }
	return C.pango_gravity_get_for_script_and_width(script, _gbool_wide, base_gravity, hint)
}

func GravityToRotation(gravity C.PangoGravity) C.double {
	return C.pango_gravity_to_rotation(gravity)
}

func IsZeroWidth(ch C.gunichar) bool {
	return gboolean2bool(C.pango_is_zero_width(ch))
}

func Itemize(context *C.PangoContext, text *C.char, start_index C.int, length C.int, attrs *AttrList, cached_iter *AttrIterator) *C.GList {
	_cp_attrs_ := (*C.PangoAttrList)(attrs)
	_cp_cached_iter_ := (*C.PangoAttrIterator)(cached_iter)
	return C._pango_itemize(context, unsafe.Pointer(text), start_index, length, _cp_attrs_, _cp_cached_iter_)
}

func ItemizeWithBaseDir(context *C.PangoContext, base_dir C.PangoDirection, text *C.char, start_index C.int, length C.int, attrs *AttrList, cached_iter *AttrIterator) *C.GList {
	_cp_attrs_ := (*C.PangoAttrList)(attrs)
	_cp_cached_iter_ := (*C.PangoAttrIterator)(cached_iter)
	return C._pango_itemize_with_base_dir(context, base_dir, unsafe.Pointer(text), start_index, length, _cp_attrs_, _cp_cached_iter_)
}

func Log2visGetEmbeddingLevels(text string, length C.int, pbase_dir *C.PangoDirection) *uint8 {
	_cstr_text := unsafe.Pointer(C.CString(text))
	defer C.free(_cstr_text)
	_gstr_text := (*C.gchar)(unsafe.Pointer(_cstr_text))
	return guint8p2uint8p(C._pango_log2vis_get_embedding_levels(unsafe.Pointer(_gstr_text), length, pbase_dir))
}

func ParseEnum(type_ C.GType, str *C.char, value *C.int, warn bool, possible_values unsafe.Pointer) bool {
	_gbool_warn := C._false()
	if warn { _gbool_warn = C._true() }
	return gboolean2bool(C._pango_parse_enum(type_, unsafe.Pointer(str), value, _gbool_warn, unsafe.Pointer(possible_values)))
}

func ParseMarkup(markup_text *C.char, length C.int, accel_marker C.gunichar, attr_list unsafe.Pointer, text unsafe.Pointer, accel_char *C.gunichar, err unsafe.Pointer) bool {
	return gboolean2bool(C._pango_parse_markup(unsafe.Pointer(markup_text), length, accel_marker, unsafe.Pointer(attr_list), unsafe.Pointer(text), accel_char, unsafe.Pointer(err)))
}

func ParseStretch(str *C.char, stretch *C.PangoStretch, warn bool) bool {
	_gbool_warn := C._false()
	if warn { _gbool_warn = C._true() }
	return gboolean2bool(C._pango_parse_stretch(unsafe.Pointer(str), stretch, _gbool_warn))
}

func ParseStyle(str *C.char, style *C.PangoStyle, warn bool) bool {
	_gbool_warn := C._false()
	if warn { _gbool_warn = C._true() }
	return gboolean2bool(C._pango_parse_style(unsafe.Pointer(str), style, _gbool_warn))
}

func ParseVariant(str *C.char, variant *C.PangoVariant, warn bool) bool {
	_gbool_warn := C._false()
	if warn { _gbool_warn = C._true() }
	return gboolean2bool(C._pango_parse_variant(unsafe.Pointer(str), variant, _gbool_warn))
}

func ParseWeight(str *C.char, weight *C.PangoWeight, warn bool) bool {
	_gbool_warn := C._false()
	if warn { _gbool_warn = C._true() }
	return gboolean2bool(C._pango_parse_weight(unsafe.Pointer(str), weight, _gbool_warn))
}

func QuantizeLineGeometry(thickness *C.int, position *C.int) {
	C.pango_quantize_line_geometry(thickness, position)
}

func ReadLine(stream *C.FILE, str *C.GString) int {
	return gint2int(C.pango_read_line(stream, str))
}

func ReorderItems(logical_items *C.GList) *C.GList {
	return C.pango_reorder_items(logical_items)
}

func ScanInt(pos unsafe.Pointer, out *C.int) bool {
	return gboolean2bool(C._pango_scan_int(unsafe.Pointer(pos), out))
}

func ScanString(pos unsafe.Pointer, out *C.GString) bool {
	return gboolean2bool(C._pango_scan_string(unsafe.Pointer(pos), out))
}

func ScanWord(pos unsafe.Pointer, out *C.GString) bool {
	return gboolean2bool(C._pango_scan_word(unsafe.Pointer(pos), out))
}

func ScriptForUnichar(ch C.gunichar) C.PangoScript {
	return C.pango_script_for_unichar(ch)
}

func ScriptGetSampleLanguage(script C.PangoScript) *Language {
	_c_return_ := C.pango_script_get_sample_language(script)
	_go_return_ := (*Language)(_c_return_)
	runtime.SetFinalizer(&_go_return_, func (x **Language) {
		C.g_object_unref(C.gpointer(_c_return_))
	})
	return _go_return_
}

func Shape(text string, length int, analysis *Analysis, glyphs *GlyphString) {
	_cstr_text := unsafe.Pointer(C.CString(text))
	defer C.free(_cstr_text)
	_gstr_text := (*C.gchar)(unsafe.Pointer(_cstr_text))
	_gint_length := C.gint(length)
	_cp_analysis_ := (*C.PangoAnalysis)(analysis)
	_cp_glyphs_ := (*C.PangoGlyphString)(glyphs)
	C._pango_shape(unsafe.Pointer(_gstr_text), _gint_length, unsafe.Pointer(_cp_analysis_), _cp_glyphs_)
}

func ShapeFull(item_text string, item_length int, paragraph_text string, paragraph_length int, analysis *Analysis, glyphs *GlyphString) {
	_cstr_item_text := unsafe.Pointer(C.CString(item_text))
	defer C.free(_cstr_item_text)
	_gstr_item_text := (*C.gchar)(unsafe.Pointer(_cstr_item_text))
	_gint_item_length := C.gint(item_length)
	_cstr_paragraph_text := unsafe.Pointer(C.CString(paragraph_text))
	defer C.free(_cstr_paragraph_text)
	_gstr_paragraph_text := (*C.gchar)(unsafe.Pointer(_cstr_paragraph_text))
	_gint_paragraph_length := C.gint(paragraph_length)
	_cp_analysis_ := (*C.PangoAnalysis)(analysis)
	_cp_glyphs_ := (*C.PangoGlyphString)(glyphs)
	C._pango_shape_full(unsafe.Pointer(_gstr_item_text), _gint_item_length, unsafe.Pointer(_gstr_paragraph_text), _gint_paragraph_length, unsafe.Pointer(_cp_analysis_), _cp_glyphs_)
}

func SkipSpace(pos unsafe.Pointer) bool {
	return gboolean2bool(C._pango_skip_space(unsafe.Pointer(pos)))
}

func SplitFileList(str *C.char) unsafe.Pointer {
	return unsafe.Pointer(C._pango_split_file_list(unsafe.Pointer(str)))
}

func TrimString(str *C.char) *C.char {
	return C._pango_trim_string(unsafe.Pointer(str))
}

func UnicharDirection(ch C.gunichar) C.PangoDirection {
	return C.pango_unichar_direction(ch)
}

func UnitsFromDouble(d C.double) C.int {
	return C.pango_units_from_double(d)
}

func UnitsToDouble(i C.int) C.double {
	return C.pango_units_to_double(i)
}

func Version() C.int {
	return C.pango_version()
}

func VersionCheck(required_major C.int, required_minor C.int, required_micro C.int) *C.char {
	return C.pango_version_check(required_major, required_minor, required_micro)
}

func VersionString() *C.char {
	return C.pango_version_string()
}

const ALIGN_LEFT = C.PANGO_ALIGN_LEFT
const ALIGN_CENTER = C.PANGO_ALIGN_CENTER
const ALIGN_RIGHT = C.PANGO_ALIGN_RIGHT
const ATTR_INVALID = C.PANGO_ATTR_INVALID
const ATTR_LANGUAGE = C.PANGO_ATTR_LANGUAGE
const ATTR_FAMILY = C.PANGO_ATTR_FAMILY
const ATTR_STYLE = C.PANGO_ATTR_STYLE
const ATTR_WEIGHT = C.PANGO_ATTR_WEIGHT
const ATTR_VARIANT = C.PANGO_ATTR_VARIANT
const ATTR_STRETCH = C.PANGO_ATTR_STRETCH
const ATTR_SIZE = C.PANGO_ATTR_SIZE
const ATTR_FONT_DESC = C.PANGO_ATTR_FONT_DESC
const ATTR_FOREGROUND = C.PANGO_ATTR_FOREGROUND
const ATTR_BACKGROUND = C.PANGO_ATTR_BACKGROUND
const ATTR_UNDERLINE = C.PANGO_ATTR_UNDERLINE
const ATTR_STRIKETHROUGH = C.PANGO_ATTR_STRIKETHROUGH
const ATTR_RISE = C.PANGO_ATTR_RISE
const ATTR_SHAPE = C.PANGO_ATTR_SHAPE
const ATTR_SCALE = C.PANGO_ATTR_SCALE
const ATTR_FALLBACK = C.PANGO_ATTR_FALLBACK
const ATTR_LETTER_SPACING = C.PANGO_ATTR_LETTER_SPACING
const ATTR_UNDERLINE_COLOR = C.PANGO_ATTR_UNDERLINE_COLOR
const ATTR_STRIKETHROUGH_COLOR = C.PANGO_ATTR_STRIKETHROUGH_COLOR
const ATTR_ABSOLUTE_SIZE = C.PANGO_ATTR_ABSOLUTE_SIZE
const ATTR_GRAVITY = C.PANGO_ATTR_GRAVITY
const ATTR_GRAVITY_HINT = C.PANGO_ATTR_GRAVITY_HINT
const BIDI_TYPE_L = C.PANGO_BIDI_TYPE_L
const BIDI_TYPE_LRE = C.PANGO_BIDI_TYPE_LRE
const BIDI_TYPE_LRO = C.PANGO_BIDI_TYPE_LRO
const BIDI_TYPE_R = C.PANGO_BIDI_TYPE_R
const BIDI_TYPE_AL = C.PANGO_BIDI_TYPE_AL
const BIDI_TYPE_RLE = C.PANGO_BIDI_TYPE_RLE
const BIDI_TYPE_RLO = C.PANGO_BIDI_TYPE_RLO
const BIDI_TYPE_PDF = C.PANGO_BIDI_TYPE_PDF
const BIDI_TYPE_EN = C.PANGO_BIDI_TYPE_EN
const BIDI_TYPE_ES = C.PANGO_BIDI_TYPE_ES
const BIDI_TYPE_ET = C.PANGO_BIDI_TYPE_ET
const BIDI_TYPE_AN = C.PANGO_BIDI_TYPE_AN
const BIDI_TYPE_CS = C.PANGO_BIDI_TYPE_CS
const BIDI_TYPE_NSM = C.PANGO_BIDI_TYPE_NSM
const BIDI_TYPE_BN = C.PANGO_BIDI_TYPE_BN
const BIDI_TYPE_B = C.PANGO_BIDI_TYPE_B
const BIDI_TYPE_S = C.PANGO_BIDI_TYPE_S
const BIDI_TYPE_WS = C.PANGO_BIDI_TYPE_WS
const BIDI_TYPE_ON = C.PANGO_BIDI_TYPE_ON
const COVERAGE_NONE = C.PANGO_COVERAGE_NONE
const COVERAGE_FALLBACK = C.PANGO_COVERAGE_FALLBACK
const COVERAGE_APPROXIMATE = C.PANGO_COVERAGE_APPROXIMATE
const COVERAGE_EXACT = C.PANGO_COVERAGE_EXACT
const DIRECTION_LTR = C.PANGO_DIRECTION_LTR
const DIRECTION_RTL = C.PANGO_DIRECTION_RTL
const DIRECTION_TTB_LTR = C.PANGO_DIRECTION_TTB_LTR
const DIRECTION_TTB_RTL = C.PANGO_DIRECTION_TTB_RTL
const DIRECTION_WEAK_LTR = C.PANGO_DIRECTION_WEAK_LTR
const DIRECTION_WEAK_RTL = C.PANGO_DIRECTION_WEAK_RTL
const DIRECTION_NEUTRAL = C.PANGO_DIRECTION_NEUTRAL
const ELLIPSIZE_NONE = C.PANGO_ELLIPSIZE_NONE
const ELLIPSIZE_START = C.PANGO_ELLIPSIZE_START
const ELLIPSIZE_MIDDLE = C.PANGO_ELLIPSIZE_MIDDLE
const ELLIPSIZE_END = C.PANGO_ELLIPSIZE_END
const GRAVITY_SOUTH = C.PANGO_GRAVITY_SOUTH
const GRAVITY_EAST = C.PANGO_GRAVITY_EAST
const GRAVITY_NORTH = C.PANGO_GRAVITY_NORTH
const GRAVITY_WEST = C.PANGO_GRAVITY_WEST
const GRAVITY_AUTO = C.PANGO_GRAVITY_AUTO
const GRAVITY_HINT_NATURAL = C.PANGO_GRAVITY_HINT_NATURAL
const GRAVITY_HINT_STRONG = C.PANGO_GRAVITY_HINT_STRONG
const GRAVITY_HINT_LINE = C.PANGO_GRAVITY_HINT_LINE
const RENDER_PART_FOREGROUND = C.PANGO_RENDER_PART_FOREGROUND
const RENDER_PART_BACKGROUND = C.PANGO_RENDER_PART_BACKGROUND
const RENDER_PART_UNDERLINE = C.PANGO_RENDER_PART_UNDERLINE
const RENDER_PART_STRIKETHROUGH = C.PANGO_RENDER_PART_STRIKETHROUGH
const SCRIPT_INVALID_CODE = C.PANGO_SCRIPT_INVALID_CODE
const SCRIPT_COMMON = C.PANGO_SCRIPT_COMMON
const SCRIPT_INHERITED = C.PANGO_SCRIPT_INHERITED
const SCRIPT_ARABIC = C.PANGO_SCRIPT_ARABIC
const SCRIPT_ARMENIAN = C.PANGO_SCRIPT_ARMENIAN
const SCRIPT_BENGALI = C.PANGO_SCRIPT_BENGALI
const SCRIPT_BOPOMOFO = C.PANGO_SCRIPT_BOPOMOFO
const SCRIPT_CHEROKEE = C.PANGO_SCRIPT_CHEROKEE
const SCRIPT_COPTIC = C.PANGO_SCRIPT_COPTIC
const SCRIPT_CYRILLIC = C.PANGO_SCRIPT_CYRILLIC
const SCRIPT_DESERET = C.PANGO_SCRIPT_DESERET
const SCRIPT_DEVANAGARI = C.PANGO_SCRIPT_DEVANAGARI
const SCRIPT_ETHIOPIC = C.PANGO_SCRIPT_ETHIOPIC
const SCRIPT_GEORGIAN = C.PANGO_SCRIPT_GEORGIAN
const SCRIPT_GOTHIC = C.PANGO_SCRIPT_GOTHIC
const SCRIPT_GREEK = C.PANGO_SCRIPT_GREEK
const SCRIPT_GUJARATI = C.PANGO_SCRIPT_GUJARATI
const SCRIPT_GURMUKHI = C.PANGO_SCRIPT_GURMUKHI
const SCRIPT_HAN = C.PANGO_SCRIPT_HAN
const SCRIPT_HANGUL = C.PANGO_SCRIPT_HANGUL
const SCRIPT_HEBREW = C.PANGO_SCRIPT_HEBREW
const SCRIPT_HIRAGANA = C.PANGO_SCRIPT_HIRAGANA
const SCRIPT_KANNADA = C.PANGO_SCRIPT_KANNADA
const SCRIPT_KATAKANA = C.PANGO_SCRIPT_KATAKANA
const SCRIPT_KHMER = C.PANGO_SCRIPT_KHMER
const SCRIPT_LAO = C.PANGO_SCRIPT_LAO
const SCRIPT_LATIN = C.PANGO_SCRIPT_LATIN
const SCRIPT_MALAYALAM = C.PANGO_SCRIPT_MALAYALAM
const SCRIPT_MONGOLIAN = C.PANGO_SCRIPT_MONGOLIAN
const SCRIPT_MYANMAR = C.PANGO_SCRIPT_MYANMAR
const SCRIPT_OGHAM = C.PANGO_SCRIPT_OGHAM
const SCRIPT_OLD_ITALIC = C.PANGO_SCRIPT_OLD_ITALIC
const SCRIPT_ORIYA = C.PANGO_SCRIPT_ORIYA
const SCRIPT_RUNIC = C.PANGO_SCRIPT_RUNIC
const SCRIPT_SINHALA = C.PANGO_SCRIPT_SINHALA
const SCRIPT_SYRIAC = C.PANGO_SCRIPT_SYRIAC
const SCRIPT_TAMIL = C.PANGO_SCRIPT_TAMIL
const SCRIPT_TELUGU = C.PANGO_SCRIPT_TELUGU
const SCRIPT_THAANA = C.PANGO_SCRIPT_THAANA
const SCRIPT_THAI = C.PANGO_SCRIPT_THAI
const SCRIPT_TIBETAN = C.PANGO_SCRIPT_TIBETAN
const SCRIPT_CANADIAN_ABORIGINAL = C.PANGO_SCRIPT_CANADIAN_ABORIGINAL
const SCRIPT_YI = C.PANGO_SCRIPT_YI
const SCRIPT_TAGALOG = C.PANGO_SCRIPT_TAGALOG
const SCRIPT_HANUNOO = C.PANGO_SCRIPT_HANUNOO
const SCRIPT_BUHID = C.PANGO_SCRIPT_BUHID
const SCRIPT_TAGBANWA = C.PANGO_SCRIPT_TAGBANWA
const SCRIPT_BRAILLE = C.PANGO_SCRIPT_BRAILLE
const SCRIPT_CYPRIOT = C.PANGO_SCRIPT_CYPRIOT
const SCRIPT_LIMBU = C.PANGO_SCRIPT_LIMBU
const SCRIPT_OSMANYA = C.PANGO_SCRIPT_OSMANYA
const SCRIPT_SHAVIAN = C.PANGO_SCRIPT_SHAVIAN
const SCRIPT_LINEAR_B = C.PANGO_SCRIPT_LINEAR_B
const SCRIPT_TAI_LE = C.PANGO_SCRIPT_TAI_LE
const SCRIPT_UGARITIC = C.PANGO_SCRIPT_UGARITIC
const SCRIPT_NEW_TAI_LUE = C.PANGO_SCRIPT_NEW_TAI_LUE
const SCRIPT_BUGINESE = C.PANGO_SCRIPT_BUGINESE
const SCRIPT_GLAGOLITIC = C.PANGO_SCRIPT_GLAGOLITIC
const SCRIPT_TIFINAGH = C.PANGO_SCRIPT_TIFINAGH
const SCRIPT_SYLOTI_NAGRI = C.PANGO_SCRIPT_SYLOTI_NAGRI
const SCRIPT_OLD_PERSIAN = C.PANGO_SCRIPT_OLD_PERSIAN
const SCRIPT_KHAROSHTHI = C.PANGO_SCRIPT_KHAROSHTHI
const SCRIPT_UNKNOWN = C.PANGO_SCRIPT_UNKNOWN
const SCRIPT_BALINESE = C.PANGO_SCRIPT_BALINESE
const SCRIPT_CUNEIFORM = C.PANGO_SCRIPT_CUNEIFORM
const SCRIPT_PHOENICIAN = C.PANGO_SCRIPT_PHOENICIAN
const SCRIPT_PHAGS_PA = C.PANGO_SCRIPT_PHAGS_PA
const SCRIPT_NKO = C.PANGO_SCRIPT_NKO
const SCRIPT_KAYAH_LI = C.PANGO_SCRIPT_KAYAH_LI
const SCRIPT_LEPCHA = C.PANGO_SCRIPT_LEPCHA
const SCRIPT_REJANG = C.PANGO_SCRIPT_REJANG
const SCRIPT_SUNDANESE = C.PANGO_SCRIPT_SUNDANESE
const SCRIPT_SAURASHTRA = C.PANGO_SCRIPT_SAURASHTRA
const SCRIPT_CHAM = C.PANGO_SCRIPT_CHAM
const SCRIPT_OL_CHIKI = C.PANGO_SCRIPT_OL_CHIKI
const SCRIPT_VAI = C.PANGO_SCRIPT_VAI
const SCRIPT_CARIAN = C.PANGO_SCRIPT_CARIAN
const SCRIPT_LYCIAN = C.PANGO_SCRIPT_LYCIAN
const SCRIPT_LYDIAN = C.PANGO_SCRIPT_LYDIAN
const SCRIPT_BATAK = C.PANGO_SCRIPT_BATAK
const SCRIPT_BRAHMI = C.PANGO_SCRIPT_BRAHMI
const SCRIPT_MANDAIC = C.PANGO_SCRIPT_MANDAIC
const SCRIPT_CHAKMA = C.PANGO_SCRIPT_CHAKMA
const SCRIPT_MEROITIC_CURSIVE = C.PANGO_SCRIPT_MEROITIC_CURSIVE
const SCRIPT_MEROITIC_HIEROGLYPHS = C.PANGO_SCRIPT_MEROITIC_HIEROGLYPHS
const SCRIPT_MIAO = C.PANGO_SCRIPT_MIAO
const SCRIPT_SHARADA = C.PANGO_SCRIPT_SHARADA
const SCRIPT_SORA_SOMPENG = C.PANGO_SCRIPT_SORA_SOMPENG
const SCRIPT_TAKRI = C.PANGO_SCRIPT_TAKRI
const STRETCH_ULTRA_CONDENSED = C.PANGO_STRETCH_ULTRA_CONDENSED
const STRETCH_EXTRA_CONDENSED = C.PANGO_STRETCH_EXTRA_CONDENSED
const STRETCH_CONDENSED = C.PANGO_STRETCH_CONDENSED
const STRETCH_SEMI_CONDENSED = C.PANGO_STRETCH_SEMI_CONDENSED
const STRETCH_NORMAL = C.PANGO_STRETCH_NORMAL
const STRETCH_SEMI_EXPANDED = C.PANGO_STRETCH_SEMI_EXPANDED
const STRETCH_EXPANDED = C.PANGO_STRETCH_EXPANDED
const STRETCH_EXTRA_EXPANDED = C.PANGO_STRETCH_EXTRA_EXPANDED
const STRETCH_ULTRA_EXPANDED = C.PANGO_STRETCH_ULTRA_EXPANDED
const STYLE_NORMAL = C.PANGO_STYLE_NORMAL
const STYLE_OBLIQUE = C.PANGO_STYLE_OBLIQUE
const STYLE_ITALIC = C.PANGO_STYLE_ITALIC
const TAB_LEFT = C.PANGO_TAB_LEFT
const UNDERLINE_NONE = C.PANGO_UNDERLINE_NONE
const UNDERLINE_SINGLE = C.PANGO_UNDERLINE_SINGLE
const UNDERLINE_DOUBLE = C.PANGO_UNDERLINE_DOUBLE
const UNDERLINE_LOW = C.PANGO_UNDERLINE_LOW
const UNDERLINE_ERROR = C.PANGO_UNDERLINE_ERROR
const VARIANT_NORMAL = C.PANGO_VARIANT_NORMAL
const VARIANT_SMALL_CAPS = C.PANGO_VARIANT_SMALL_CAPS
const WEIGHT_THIN = C.PANGO_WEIGHT_THIN
const WEIGHT_ULTRALIGHT = C.PANGO_WEIGHT_ULTRALIGHT
const WEIGHT_LIGHT = C.PANGO_WEIGHT_LIGHT
const WEIGHT_BOOK = C.PANGO_WEIGHT_BOOK
const WEIGHT_NORMAL = C.PANGO_WEIGHT_NORMAL
const WEIGHT_MEDIUM = C.PANGO_WEIGHT_MEDIUM
const WEIGHT_SEMIBOLD = C.PANGO_WEIGHT_SEMIBOLD
const WEIGHT_BOLD = C.PANGO_WEIGHT_BOLD
const WEIGHT_ULTRABOLD = C.PANGO_WEIGHT_ULTRABOLD
const WEIGHT_HEAVY = C.PANGO_WEIGHT_HEAVY
const WEIGHT_ULTRAHEAVY = C.PANGO_WEIGHT_ULTRAHEAVY
const WRAP_WORD = C.PANGO_WRAP_WORD
const WRAP_CHAR = C.PANGO_WRAP_CHAR
const WRAP_WORD_CHAR = C.PANGO_WRAP_WORD_CHAR
const ANALYSIS_FLAG_CENTERED_BASELINE = C.PANGO_ANALYSIS_FLAG_CENTERED_BASELINE
const ATTR_INDEX_FROM_TEXT_BEGINNING = C.PANGO_ATTR_INDEX_FROM_TEXT_BEGINNING
const ENGINE_TYPE_LANG = C.PANGO_ENGINE_TYPE_LANG
const ENGINE_TYPE_SHAPE = C.PANGO_ENGINE_TYPE_SHAPE
const GLYPH_EMPTY = C.PANGO_GLYPH_EMPTY
const GLYPH_INVALID_INPUT = C.PANGO_GLYPH_INVALID_INPUT
const GLYPH_UNKNOWN_FLAG = C.PANGO_GLYPH_UNKNOWN_FLAG
const RENDER_TYPE_NONE = C.PANGO_RENDER_TYPE_NONE
const SCALE = C.PANGO_SCALE
const UNKNOWN_GLYPH_HEIGHT = C.PANGO_UNKNOWN_GLYPH_HEIGHT
const UNKNOWN_GLYPH_WIDTH = C.PANGO_UNKNOWN_GLYPH_WIDTH
func gboolean2bool(b C.gboolean) bool {
  return b == C._true()
}
func gint2int(i C.gint) int {
  return int(i)
}
func guint8p2uint8p(p *C.guint8) *uint8 {
  i := uint8(*p)
  return &i
}
type AttrString C.PangoAttrString
type Matrix C.PangoMatrix
type LayoutIter C.PangoLayoutIter
type Coverage C.PangoCoverage
type LayoutClass C.PangoLayoutClass
type EngineLang C.PangoEngineLang
type RendererClass C.PangoRendererClass
type GlyphGeometry C.PangoGlyphGeometry
type EngineShape C.PangoEngineShape
type GlyphString C.PangoGlyphString
type AttrLanguage C.PangoAttrLanguage
type LayoutLine C.PangoLayoutLine
type FontMetrics C.PangoFontMetrics
type TabArray C.PangoTabArray
type Analysis C.PangoAnalysis
type GlyphInfo C.PangoGlyphInfo
type GlyphVisAttr C.PangoGlyphVisAttr
type GlyphItem C.PangoGlyphItem
type LogAttr C.PangoLogAttr
type FontDescription C.PangoFontDescription
type AttrColor C.PangoAttrColor
type AttrList C.PangoAttrList
type ScriptIter C.PangoScriptIter
type RendererPrivate C.PangoRendererPrivate
type AttrFloat C.PangoAttrFloat
type _ScriptForLang C._PangoScriptForLang
type AttrShape C.PangoAttrShape
type Color C.PangoColor
type Rectangle C.PangoRectangle
type Item C.PangoItem
type GlyphItemIter C.PangoGlyphItemIter
type AttrInt C.PangoAttrInt
type Language C.PangoLanguage
type AttrFontDesc C.PangoAttrFontDesc
type AttrSize C.PangoAttrSize
type AttrClass C.PangoAttrClass
type ContextClass C.PangoContextClass
type Attribute C.PangoAttribute
type AttrIterator C.PangoAttrIterator
