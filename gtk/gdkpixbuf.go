// this file is auto-generated by gtk-go

package gtk

// #cgo pkg-config: gdk-pixbuf-2.0 gobject-2.0 gtk+-3.0
// #include <string.h>
// #include <glib-object.h>
// #include <glib/gstdio.h>
// #include <glib-unix.h>
// #include <gdk-pixbuf/gdk-pixbuf.h>
/*
GdkPixbuf * _gdk_pixbuf_new_from_file(char * filename, void * error) {
	return (GdkPixbuf *)gdk_pixbuf_new_from_file((const char *)(filename), (GError **)(error));
}
GdkPixbuf * _gdk_pixbuf_new_from_file_at_scale(char * filename, int width, int height, gboolean preserve_aspect_ratio, void * error) {
	return (GdkPixbuf *)gdk_pixbuf_new_from_file_at_scale((const char *)(filename), width, height, preserve_aspect_ratio, (GError **)(error));
}
GdkPixbuf * _gdk_pixbuf_new_from_file_at_size(char * filename, int width, int height, void * error) {
	return (GdkPixbuf *)gdk_pixbuf_new_from_file_at_size((const char *)(filename), width, height, (GError **)(error));
}
GdkPixbuf * _gdk_pixbuf_new_from_resource(char * resource_path, void * error) {
	return (GdkPixbuf *)gdk_pixbuf_new_from_resource((const char *)(resource_path), (GError **)(error));
}
GdkPixbuf * _gdk_pixbuf_new_from_resource_at_scale(char * resource_path, int width, int height, gboolean preserve_aspect_ratio, void * error) {
	return (GdkPixbuf *)gdk_pixbuf_new_from_resource_at_scale((const char *)(resource_path), width, height, preserve_aspect_ratio, (GError **)(error));
}
GdkPixbuf * _gdk_pixbuf_new_from_stream(GInputStream * stream, GCancellable * cancellable, void * error) {
	return (GdkPixbuf *)gdk_pixbuf_new_from_stream(stream, cancellable, (GError **)(error));
}
GdkPixbuf * _gdk_pixbuf_new_from_stream_at_scale(GInputStream * stream, gint width, gint height, gboolean preserve_aspect_ratio, GCancellable * cancellable, void * error) {
	return (GdkPixbuf *)gdk_pixbuf_new_from_stream_at_scale(stream, width, height, preserve_aspect_ratio, cancellable, (GError **)(error));
}
GdkPixbuf * _gdk_pixbuf_new_from_stream_finish(GAsyncResult * async_result, void * error) {
	return (GdkPixbuf *)gdk_pixbuf_new_from_stream_finish(async_result, (GError **)(error));
}
GdkPixbufFormat * _gdk_pixbuf_get_file_info(gchar * filename, gint * width, gint * height) {
	return (GdkPixbufFormat *)gdk_pixbuf_get_file_info((const gchar *)(filename), width, height);
}
gboolean _gdk_pixbuf_save_to_stream_finish(GAsyncResult * async_result, void * error) {
	return (gboolean)gdk_pixbuf_save_to_stream_finish(async_result, (GError **)(error));
}
GdkPixbuf * _gdk_pixbuf_add_alpha(GdkPixbuf * _self_, gboolean substitute_color, guchar r, guchar g, guchar b) {
	return (GdkPixbuf *)gdk_pixbuf_add_alpha((const GdkPixbuf *)(_self_), substitute_color, r, g, b);
}
void _gdk_pixbuf_composite(GdkPixbuf * _self_, GdkPixbuf * dest, int dest_x, int dest_y, int dest_width, int dest_height, double offset_x, double offset_y, double scale_x, double scale_y, GdkInterpType interp_type, int overall_alpha) {
	(void)gdk_pixbuf_composite((const GdkPixbuf *)(_self_), dest, dest_x, dest_y, dest_width, dest_height, offset_x, offset_y, scale_x, scale_y, interp_type, overall_alpha);
}
void _gdk_pixbuf_composite_color(GdkPixbuf * _self_, GdkPixbuf * dest, int dest_x, int dest_y, int dest_width, int dest_height, double offset_x, double offset_y, double scale_x, double scale_y, GdkInterpType interp_type, int overall_alpha, int check_x, int check_y, int check_size, guint32 color1, guint32 color2) {
	(void)gdk_pixbuf_composite_color((const GdkPixbuf *)(_self_), dest, dest_x, dest_y, dest_width, dest_height, offset_x, offset_y, scale_x, scale_y, interp_type, overall_alpha, check_x, check_y, check_size, color1, color2);
}
GdkPixbuf * _gdk_pixbuf_composite_color_simple(GdkPixbuf * _self_, int dest_width, int dest_height, GdkInterpType interp_type, int overall_alpha, int check_size, guint32 color1, guint32 color2) {
	return (GdkPixbuf *)gdk_pixbuf_composite_color_simple((const GdkPixbuf *)(_self_), dest_width, dest_height, interp_type, overall_alpha, check_size, color1, color2);
}
GdkPixbuf * _gdk_pixbuf_copy(GdkPixbuf * _self_) {
	return (GdkPixbuf *)gdk_pixbuf_copy((const GdkPixbuf *)(_self_));
}
void _gdk_pixbuf_copy_area(GdkPixbuf * _self_, int src_x, int src_y, int width, int height, GdkPixbuf * dest_pixbuf, int dest_x, int dest_y) {
	(void)gdk_pixbuf_copy_area((const GdkPixbuf *)(_self_), src_x, src_y, width, height, dest_pixbuf, dest_x, dest_y);
}
GdkPixbuf * _gdk_pixbuf_flip(GdkPixbuf * _self_, gboolean horizontal) {
	return (GdkPixbuf *)gdk_pixbuf_flip((const GdkPixbuf *)(_self_), horizontal);
}
int _gdk_pixbuf_get_bits_per_sample(GdkPixbuf * _self_) {
	return (int)gdk_pixbuf_get_bits_per_sample((const GdkPixbuf *)(_self_));
}
gsize _gdk_pixbuf_get_byte_length(GdkPixbuf * _self_) {
	return (gsize)gdk_pixbuf_get_byte_length((const GdkPixbuf *)(_self_));
}
GdkColorspace _gdk_pixbuf_get_colorspace(GdkPixbuf * _self_) {
	return (GdkColorspace)gdk_pixbuf_get_colorspace((const GdkPixbuf *)(_self_));
}
gboolean _gdk_pixbuf_get_has_alpha(GdkPixbuf * _self_) {
	return (gboolean)gdk_pixbuf_get_has_alpha((const GdkPixbuf *)(_self_));
}
int _gdk_pixbuf_get_height(GdkPixbuf * _self_) {
	return (int)gdk_pixbuf_get_height((const GdkPixbuf *)(_self_));
}
int _gdk_pixbuf_get_n_channels(GdkPixbuf * _self_) {
	return (int)gdk_pixbuf_get_n_channels((const GdkPixbuf *)(_self_));
}
gchar * _gdk_pixbuf_get_option(GdkPixbuf * _self_, gchar * key) {
	return (gchar *)gdk_pixbuf_get_option(_self_, (const gchar *)(key));
}
guchar * _gdk_pixbuf_get_pixels(GdkPixbuf * _self_) {
	return (guchar *)gdk_pixbuf_get_pixels((const GdkPixbuf *)(_self_));
}
guchar * _gdk_pixbuf_get_pixels_with_length(GdkPixbuf * _self_, guint * length) {
	return (guchar *)gdk_pixbuf_get_pixels_with_length((const GdkPixbuf *)(_self_), length);
}
int _gdk_pixbuf_get_rowstride(GdkPixbuf * _self_) {
	return (int)gdk_pixbuf_get_rowstride((const GdkPixbuf *)(_self_));
}
int _gdk_pixbuf_get_width(GdkPixbuf * _self_) {
	return (int)gdk_pixbuf_get_width((const GdkPixbuf *)(_self_));
}
GdkPixbuf * _gdk_pixbuf_rotate_simple(GdkPixbuf * _self_, GdkPixbufRotation angle) {
	return (GdkPixbuf *)gdk_pixbuf_rotate_simple((const GdkPixbuf *)(_self_), angle);
}
void _gdk_pixbuf_saturate_and_pixelate(GdkPixbuf * _self_, GdkPixbuf * dest, gfloat saturation, gboolean pixelate) {
	(void)gdk_pixbuf_saturate_and_pixelate((const GdkPixbuf *)(_self_), dest, saturation, pixelate);
}
void _gdk_pixbuf_scale(GdkPixbuf * _self_, GdkPixbuf * dest, int dest_x, int dest_y, int dest_width, int dest_height, double offset_x, double offset_y, double scale_x, double scale_y, GdkInterpType interp_type) {
	(void)gdk_pixbuf_scale((const GdkPixbuf *)(_self_), dest, dest_x, dest_y, dest_width, dest_height, offset_x, offset_y, scale_x, scale_y, interp_type);
}
GdkPixbuf * _gdk_pixbuf_scale_simple(GdkPixbuf * _self_, int dest_width, int dest_height, GdkInterpType interp_type) {
	return (GdkPixbuf *)gdk_pixbuf_scale_simple((const GdkPixbuf *)(_self_), dest_width, dest_height, interp_type);
}
GdkPixbufAnimation * _gdk_pixbuf_animation_new_from_file(char * filename, void * error) {
	return (GdkPixbufAnimation *)gdk_pixbuf_animation_new_from_file((const char *)(filename), (GError **)(error));
}
GdkPixbufAnimationIter * _gdk_pixbuf_animation_get_iter(GdkPixbufAnimation * _self_, GTimeVal * start_time) {
	return (GdkPixbufAnimationIter *)gdk_pixbuf_animation_get_iter(_self_, (const GTimeVal *)(start_time));
}
gboolean _gdk_pixbuf_animation_iter_advance(GdkPixbufAnimationIter * _self_, GTimeVal * current_time) {
	return (gboolean)gdk_pixbuf_animation_iter_advance(_self_, (const GTimeVal *)(current_time));
}
GdkPixbufLoader * _gdk_pixbuf_loader_new_with_mime_type(char * mime_type, void * error) {
	return (GdkPixbufLoader *)gdk_pixbuf_loader_new_with_mime_type((const char *)(mime_type), (GError **)(error));
}
GdkPixbufLoader * _gdk_pixbuf_loader_new_with_type(char * image_type, void * error) {
	return (GdkPixbufLoader *)gdk_pixbuf_loader_new_with_type((const char *)(image_type), (GError **)(error));
}
gboolean _gdk_pixbuf_loader_close(GdkPixbufLoader * _self_, void * error) {
	return (gboolean)gdk_pixbuf_loader_close(_self_, (GError **)(error));
}
GdkPixbufFormat * _gdk_pixbuf_format_copy(GdkPixbufFormat * _self_) {
	return (GdkPixbufFormat *)gdk_pixbuf_format_copy((const GdkPixbufFormat *)(_self_));
}
void * _gdk_pixbuf_format_get_extensions(GdkPixbufFormat * _self_) {
	return (void *)gdk_pixbuf_format_get_extensions(_self_);
}
void * _gdk_pixbuf_format_get_mime_types(GdkPixbufFormat * _self_) {
	return (void *)gdk_pixbuf_format_get_mime_types(_self_);
}
*/
import "C"
import (
	"unsafe"
)

type PixbufLoaderClass C.GdkPixbufLoaderClass
type PixbufFormat C.GdkPixbufFormat
type PixbufSimpleAnimClass C.GdkPixbufSimpleAnimClass
type PixbufSimpleAnim struct {
	PixbufAnimation
	_value_ unsafe.Pointer
}
type PixbufSimpleAnimKind interface {
  _IsPixbufSimpleAnim()
  GetGObject() unsafe.Pointer
}
func (self PixbufSimpleAnim) _IsPixbufSimpleAnim() {}
func (self PixbufSimpleAnim) GetGObject() unsafe.Pointer { return self._value_ }
func ToPixbufSimpleAnim(value unsafe.Pointer) PixbufSimpleAnim {
	return PixbufSimpleAnim{
		ToPixbufAnimation(value),
		value,
	}
}
type PixbufAnimation struct {
	GObjectObject
	_value_ unsafe.Pointer
}
type PixbufAnimationKind interface {
  _IsPixbufAnimation()
  GetGObject() unsafe.Pointer
}
func (self PixbufAnimation) _IsPixbufAnimation() {}
func (self PixbufAnimation) GetGObject() unsafe.Pointer { return self._value_ }
func ToPixbufAnimation(value unsafe.Pointer) PixbufAnimation {
	return PixbufAnimation{
		ToGObjectObject(value),
		value,
	}
}
type Pixbuf struct {
	GObjectObject
	Icon
	_value_ unsafe.Pointer
}
type PixbufKind interface {
  _IsPixbuf()
  GetGObject() unsafe.Pointer
}
func (self Pixbuf) _IsPixbuf() {}
func (self Pixbuf) GetGObject() unsafe.Pointer { return self._value_ }
func ToPixbuf(value unsafe.Pointer) Pixbuf {
	return Pixbuf{
		ToGObjectObject(value),
		ToIcon(value),
		value,
	}
}
func (self Pixbuf) _IsIcon () {}
type PixbufAnimationIter struct {
	GObjectObject
	_value_ unsafe.Pointer
}
type PixbufAnimationIterKind interface {
  _IsPixbufAnimationIter()
  GetGObject() unsafe.Pointer
}
func (self PixbufAnimationIter) _IsPixbufAnimationIter() {}
func (self PixbufAnimationIter) GetGObject() unsafe.Pointer { return self._value_ }
func ToPixbufAnimationIter(value unsafe.Pointer) PixbufAnimationIter {
	return PixbufAnimationIter{
		ToGObjectObject(value),
		value,
	}
}
type PixbufSimpleAnimIter struct {
	PixbufAnimationIter
	_value_ unsafe.Pointer
}
type PixbufSimpleAnimIterKind interface {
  _IsPixbufSimpleAnimIter()
  GetGObject() unsafe.Pointer
}
func (self PixbufSimpleAnimIter) _IsPixbufSimpleAnimIter() {}
func (self PixbufSimpleAnimIter) GetGObject() unsafe.Pointer { return self._value_ }
func ToPixbufSimpleAnimIter(value unsafe.Pointer) PixbufSimpleAnimIter {
	return PixbufSimpleAnimIter{
		ToPixbufAnimationIter(value),
		value,
	}
}
type PixbufLoader struct {
	GObjectObject
	_value_ unsafe.Pointer
}
type PixbufLoaderKind interface {
  _IsPixbufLoader()
  GetGObject() unsafe.Pointer
}
func (self PixbufLoader) _IsPixbufLoader() {}
func (self PixbufLoader) GetGObject() unsafe.Pointer { return self._value_ }
func ToPixbufLoader(value unsafe.Pointer) PixbufLoader {
	return PixbufLoader{
		ToGObjectObject(value),
		value,
	}
}
func PixbufErrorQuark() (_return_ C.GQuark) {
	_return_ = C.gdk_pixbuf_error_quark()
	return
}

func PixbufNew(colorspace C.GdkColorspace, has_alpha bool, bits_per_sample C.int, width C.int, height C.int) (_go__return__ Pixbuf) {
	var _return_ *C.GdkPixbuf
	_cgo_has_alpha_ := (C.gboolean)(C.FALSE)
	if has_alpha { _cgo_has_alpha_ = (C.gboolean)(C.TRUE) }
	_return_ = C.gdk_pixbuf_new(colorspace, _cgo_has_alpha_, bits_per_sample, width, height)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func PixbufNewFromFile(filename string) (_go__return__ Pixbuf, _error_ unsafe.Pointer) {
	var _return_ *C.GdkPixbuf
	_cstring_filename_ := C.CString(filename)
	_cgo_filename_ := (*C.char)(unsafe.Pointer(_cstring_filename_))
	defer C.free(unsafe.Pointer(_cstring_filename_))
	_return_ = C._gdk_pixbuf_new_from_file(_cgo_filename_, _error_)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func PixbufNewFromFileAtScale(filename string, width C.int, height C.int, preserve_aspect_ratio bool) (_go__return__ Pixbuf, _error_ unsafe.Pointer) {
	var _return_ *C.GdkPixbuf
	_cstring_filename_ := C.CString(filename)
	_cgo_filename_ := (*C.char)(unsafe.Pointer(_cstring_filename_))
	defer C.free(unsafe.Pointer(_cstring_filename_))
	_cgo_preserve_aspect_ratio_ := (C.gboolean)(C.FALSE)
	if preserve_aspect_ratio { _cgo_preserve_aspect_ratio_ = (C.gboolean)(C.TRUE) }
	_return_ = C._gdk_pixbuf_new_from_file_at_scale(_cgo_filename_, width, height, _cgo_preserve_aspect_ratio_, _error_)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func PixbufNewFromFileAtSize(filename string, width C.int, height C.int) (_go__return__ Pixbuf, _error_ unsafe.Pointer) {
	var _return_ *C.GdkPixbuf
	_cstring_filename_ := C.CString(filename)
	_cgo_filename_ := (*C.char)(unsafe.Pointer(_cstring_filename_))
	defer C.free(unsafe.Pointer(_cstring_filename_))
	_return_ = C._gdk_pixbuf_new_from_file_at_size(_cgo_filename_, width, height, _error_)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func PixbufNewFromResource(resource_path string) (_go__return__ Pixbuf, _error_ unsafe.Pointer) {
	var _return_ *C.GdkPixbuf
	_cstring_resource_path_ := C.CString(resource_path)
	_cgo_resource_path_ := (*C.char)(unsafe.Pointer(_cstring_resource_path_))
	defer C.free(unsafe.Pointer(_cstring_resource_path_))
	_return_ = C._gdk_pixbuf_new_from_resource(_cgo_resource_path_, _error_)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func PixbufNewFromResourceAtScale(resource_path string, width C.int, height C.int, preserve_aspect_ratio bool) (_go__return__ Pixbuf, _error_ unsafe.Pointer) {
	var _return_ *C.GdkPixbuf
	_cstring_resource_path_ := C.CString(resource_path)
	_cgo_resource_path_ := (*C.char)(unsafe.Pointer(_cstring_resource_path_))
	defer C.free(unsafe.Pointer(_cstring_resource_path_))
	_cgo_preserve_aspect_ratio_ := (C.gboolean)(C.FALSE)
	if preserve_aspect_ratio { _cgo_preserve_aspect_ratio_ = (C.gboolean)(C.TRUE) }
	_return_ = C._gdk_pixbuf_new_from_resource_at_scale(_cgo_resource_path_, width, height, _cgo_preserve_aspect_ratio_, _error_)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func PixbufNewFromStream(stream *C.GInputStream, cancellable *C.GCancellable) (_go__return__ Pixbuf, _error_ unsafe.Pointer) {
	var _return_ *C.GdkPixbuf
	_return_ = C._gdk_pixbuf_new_from_stream(stream, cancellable, _error_)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func PixbufNewFromStreamAtScale(stream *C.GInputStream, width int, height int, preserve_aspect_ratio bool, cancellable *C.GCancellable) (_go__return__ Pixbuf, _error_ unsafe.Pointer) {
	var _return_ *C.GdkPixbuf
	_cgo_width_ := (C.gint)(width)
	_cgo_height_ := (C.gint)(height)
	_cgo_preserve_aspect_ratio_ := (C.gboolean)(C.FALSE)
	if preserve_aspect_ratio { _cgo_preserve_aspect_ratio_ = (C.gboolean)(C.TRUE) }
	_return_ = C._gdk_pixbuf_new_from_stream_at_scale(stream, _cgo_width_, _cgo_height_, _cgo_preserve_aspect_ratio_, cancellable, _error_)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func PixbufNewFromStreamFinish(async_result *C.GAsyncResult) (_go__return__ Pixbuf, _error_ unsafe.Pointer) {
	var _return_ *C.GdkPixbuf
	_return_ = C._gdk_pixbuf_new_from_stream_finish(async_result, _error_)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func PixbufGetFileInfo(filename string) (_go__return__ *PixbufFormat, _go_width_ int, _go_height_ int) {
	var _return_ *C.GdkPixbufFormat
	var width C.gint
	var height C.gint
	_cstring_filename_ := C.CString(filename)
	_cgo_filename_ := (*C.gchar)(unsafe.Pointer(_cstring_filename_))
	defer C.free(unsafe.Pointer(_cstring_filename_))
	_return_ = C._gdk_pixbuf_get_file_info(_cgo_filename_, &width, &height)
	_go__return__ = (*PixbufFormat)(unsafe.Pointer(_return_))
	_go_width_ = (int)(width)
	_go_height_ = (int)(height)
	return
}

func PixbufGetFormats() (_return_ *C.GSList) {
	_return_ = C.gdk_pixbuf_get_formats()
	return
}

func PixbufNewFromStreamAsync(stream *C.GInputStream, cancellable *C.GCancellable, callback C.GAsyncReadyCallback, user_data C.gpointer) () {
	C.gdk_pixbuf_new_from_stream_async(stream, cancellable, callback, user_data)
	return
}

func PixbufNewFromStreamAtScaleAsync(stream *C.GInputStream, width int, height int, preserve_aspect_ratio bool, cancellable *C.GCancellable, callback C.GAsyncReadyCallback, user_data C.gpointer) () {
	_cgo_width_ := (C.gint)(width)
	_cgo_height_ := (C.gint)(height)
	_cgo_preserve_aspect_ratio_ := (C.gboolean)(C.FALSE)
	if preserve_aspect_ratio { _cgo_preserve_aspect_ratio_ = (C.gboolean)(C.TRUE) }
	C.gdk_pixbuf_new_from_stream_at_scale_async(stream, _cgo_width_, _cgo_height_, _cgo_preserve_aspect_ratio_, cancellable, callback, user_data)
	return
}

func PixbufSaveToStreamFinish(async_result *C.GAsyncResult) (_go__return__ bool, _error_ unsafe.Pointer) {
	var _return_ C.gboolean
	_return_ = C._gdk_pixbuf_save_to_stream_finish(async_result, _error_)
	_go__return__ = _return_ == (C.gboolean)(C.TRUE)
	return
}

func (_self_ *Pixbuf) AddAlpha(substitute_color bool, r byte, g byte, b byte) (_go__return__ Pixbuf) {
	var _return_ *C.GdkPixbuf
	_cgo_r_ := (C.guchar)(r)
	_cgo_g_ := (C.guchar)(g)
	_cgo_b_ := (C.guchar)(b)
	_cgo_substitute_color_ := (C.gboolean)(C.FALSE)
	if substitute_color { _cgo_substitute_color_ = (C.gboolean)(C.TRUE) }
	_return_ = C._gdk_pixbuf_add_alpha((*C.GdkPixbuf)(_self_._value_), _cgo_substitute_color_, _cgo_r_, _cgo_g_, _cgo_b_)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func (_self_ *Pixbuf) ApplyEmbeddedOrientation() (_go__return__ Pixbuf) {
	var _return_ *C.GdkPixbuf
	_return_ = C.gdk_pixbuf_apply_embedded_orientation((*C.GdkPixbuf)(_self_._value_))
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func (_self_ *Pixbuf) Composite(dest PixbufKind, dest_x C.int, dest_y C.int, dest_width C.int, dest_height C.int, offset_x C.double, offset_y C.double, scale_x C.double, scale_y C.double, interp_type C.GdkInterpType, overall_alpha C.int) () {
	_cgo_dest_ := (*C.GdkPixbuf)(dest.GetGObject())
	C._gdk_pixbuf_composite((*C.GdkPixbuf)(_self_._value_), _cgo_dest_, dest_x, dest_y, dest_width, dest_height, offset_x, offset_y, scale_x, scale_y, interp_type, overall_alpha)
	return
}

func (_self_ *Pixbuf) CompositeColor(dest PixbufKind, dest_x C.int, dest_y C.int, dest_width C.int, dest_height C.int, offset_x C.double, offset_y C.double, scale_x C.double, scale_y C.double, interp_type C.GdkInterpType, overall_alpha C.int, check_x C.int, check_y C.int, check_size C.int, color1 uint32, color2 uint32) () {
	_cgo_dest_ := (*C.GdkPixbuf)(dest.GetGObject())
	_cgo_color1_ := (C.guint32)(color1)
	_cgo_color2_ := (C.guint32)(color2)
	C._gdk_pixbuf_composite_color((*C.GdkPixbuf)(_self_._value_), _cgo_dest_, dest_x, dest_y, dest_width, dest_height, offset_x, offset_y, scale_x, scale_y, interp_type, overall_alpha, check_x, check_y, check_size, _cgo_color1_, _cgo_color2_)
	return
}

func (_self_ *Pixbuf) CompositeColorSimple(dest_width C.int, dest_height C.int, interp_type C.GdkInterpType, overall_alpha C.int, check_size C.int, color1 uint32, color2 uint32) (_go__return__ Pixbuf) {
	var _return_ *C.GdkPixbuf
	_cgo_color1_ := (C.guint32)(color1)
	_cgo_color2_ := (C.guint32)(color2)
	_return_ = C._gdk_pixbuf_composite_color_simple((*C.GdkPixbuf)(_self_._value_), dest_width, dest_height, interp_type, overall_alpha, check_size, _cgo_color1_, _cgo_color2_)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func (_self_ *Pixbuf) Copy() (_go__return__ Pixbuf) {
	var _return_ *C.GdkPixbuf
	_return_ = C._gdk_pixbuf_copy((*C.GdkPixbuf)(_self_._value_))
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func (_self_ *Pixbuf) CopyArea(src_x C.int, src_y C.int, width C.int, height C.int, dest_pixbuf PixbufKind, dest_x C.int, dest_y C.int) () {
	_cgo_dest_pixbuf_ := (*C.GdkPixbuf)(dest_pixbuf.GetGObject())
	C._gdk_pixbuf_copy_area((*C.GdkPixbuf)(_self_._value_), src_x, src_y, width, height, _cgo_dest_pixbuf_, dest_x, dest_y)
	return
}

func (_self_ *Pixbuf) Fill(pixel uint32) () {
	_cgo_pixel_ := (C.guint32)(pixel)
	C.gdk_pixbuf_fill((*C.GdkPixbuf)(_self_._value_), _cgo_pixel_)
	return
}

func (_self_ *Pixbuf) Flip(horizontal bool) (_go__return__ Pixbuf) {
	var _return_ *C.GdkPixbuf
	_cgo_horizontal_ := (C.gboolean)(C.FALSE)
	if horizontal { _cgo_horizontal_ = (C.gboolean)(C.TRUE) }
	_return_ = C._gdk_pixbuf_flip((*C.GdkPixbuf)(_self_._value_), _cgo_horizontal_)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func (_self_ *Pixbuf) GetBitsPerSample() (_return_ C.int) {
	_return_ = C._gdk_pixbuf_get_bits_per_sample((*C.GdkPixbuf)(_self_._value_))
	return
}

func (_self_ *Pixbuf) GetByteLength() (_go__return__ uint64) {
	var _return_ C.gsize
	_return_ = C._gdk_pixbuf_get_byte_length((*C.GdkPixbuf)(_self_._value_))
	_go__return__ = (uint64)(_return_)
	return
}

func (_self_ *Pixbuf) GetColorspace() (_return_ C.GdkColorspace) {
	_return_ = C._gdk_pixbuf_get_colorspace((*C.GdkPixbuf)(_self_._value_))
	return
}

func (_self_ *Pixbuf) GetHasAlpha() (_go__return__ bool) {
	var _return_ C.gboolean
	_return_ = C._gdk_pixbuf_get_has_alpha((*C.GdkPixbuf)(_self_._value_))
	_go__return__ = _return_ == (C.gboolean)(C.TRUE)
	return
}

func (_self_ *Pixbuf) GetHeight() (_return_ C.int) {
	_return_ = C._gdk_pixbuf_get_height((*C.GdkPixbuf)(_self_._value_))
	return
}

func (_self_ *Pixbuf) GetNChannels() (_return_ C.int) {
	_return_ = C._gdk_pixbuf_get_n_channels((*C.GdkPixbuf)(_self_._value_))
	return
}

func (_self_ *Pixbuf) GetOption(key string) (_go__return__ string) {
	_cstring_key_ := C.CString(key)
	_cgo_key_ := (*C.gchar)(unsafe.Pointer(_cstring_key_))
	defer C.free(unsafe.Pointer(_cstring_key_))
	var _return_ *C.gchar
	_return_ = C._gdk_pixbuf_get_option((*C.GdkPixbuf)(_self_._value_), _cgo_key_)
	_go__return__ = C.GoString((*C.char)(unsafe.Pointer(_return_)))
	return
}

func (_self_ *Pixbuf) GetPixels() (_return_ *C.guchar) {
	_return_ = C._gdk_pixbuf_get_pixels((*C.GdkPixbuf)(_self_._value_))
	return
}

func (_self_ *Pixbuf) GetPixelsWithLength() (_return_ *C.guchar, _go_length_ uint) {
	var length C.guint
	_return_ = C._gdk_pixbuf_get_pixels_with_length((*C.GdkPixbuf)(_self_._value_), &length)
	_go_length_ = (uint)(length)
	return
}

func (_self_ *Pixbuf) GetRowstride() (_return_ C.int) {
	_return_ = C._gdk_pixbuf_get_rowstride((*C.GdkPixbuf)(_self_._value_))
	return
}

func (_self_ *Pixbuf) GetWidth() (_return_ C.int) {
	_return_ = C._gdk_pixbuf_get_width((*C.GdkPixbuf)(_self_._value_))
	return
}

func (_self_ *Pixbuf) NewSubpixbuf(src_x C.int, src_y C.int, width C.int, height C.int) (_go__return__ Pixbuf) {
	var _return_ *C.GdkPixbuf
	_return_ = C.gdk_pixbuf_new_subpixbuf((*C.GdkPixbuf)(_self_._value_), src_x, src_y, width, height)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func (_self_ *Pixbuf) RotateSimple(angle C.GdkPixbufRotation) (_go__return__ Pixbuf) {
	var _return_ *C.GdkPixbuf
	_return_ = C._gdk_pixbuf_rotate_simple((*C.GdkPixbuf)(_self_._value_), angle)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func (_self_ *Pixbuf) SaturateAndPixelate(dest PixbufKind, saturation float64, pixelate bool) () {
	_cgo_dest_ := (*C.GdkPixbuf)(dest.GetGObject())
	_cgo_saturation_ := (C.gfloat)(saturation)
	_cgo_pixelate_ := (C.gboolean)(C.FALSE)
	if pixelate { _cgo_pixelate_ = (C.gboolean)(C.TRUE) }
	C._gdk_pixbuf_saturate_and_pixelate((*C.GdkPixbuf)(_self_._value_), _cgo_dest_, _cgo_saturation_, _cgo_pixelate_)
	return
}

func (_self_ *Pixbuf) Scale(dest PixbufKind, dest_x C.int, dest_y C.int, dest_width C.int, dest_height C.int, offset_x C.double, offset_y C.double, scale_x C.double, scale_y C.double, interp_type C.GdkInterpType) () {
	_cgo_dest_ := (*C.GdkPixbuf)(dest.GetGObject())
	C._gdk_pixbuf_scale((*C.GdkPixbuf)(_self_._value_), _cgo_dest_, dest_x, dest_y, dest_width, dest_height, offset_x, offset_y, scale_x, scale_y, interp_type)
	return
}

func (_self_ *Pixbuf) ScaleSimple(dest_width C.int, dest_height C.int, interp_type C.GdkInterpType) (_go__return__ Pixbuf) {
	var _return_ *C.GdkPixbuf
	_return_ = C._gdk_pixbuf_scale_simple((*C.GdkPixbuf)(_self_._value_), dest_width, dest_height, interp_type)
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func PixbufAnimationNewFromFile(filename string) (_go__return__ PixbufAnimation, _error_ unsafe.Pointer) {
	var _return_ *C.GdkPixbufAnimation
	_cstring_filename_ := C.CString(filename)
	_cgo_filename_ := (*C.char)(unsafe.Pointer(_cstring_filename_))
	defer C.free(unsafe.Pointer(_cstring_filename_))
	_return_ = C._gdk_pixbuf_animation_new_from_file(_cgo_filename_, _error_)
	_go__return__ = ToPixbufAnimation(unsafe.Pointer(_return_))
	return
}

func (_self_ *PixbufAnimation) GetHeight() (_return_ C.int) {
	_return_ = C.gdk_pixbuf_animation_get_height((*C.GdkPixbufAnimation)(_self_._value_))
	return
}

func (_self_ *PixbufAnimation) GetIter(start_time *C.GTimeVal) (_go__return__ PixbufAnimationIter) {
	var _return_ *C.GdkPixbufAnimationIter
	_return_ = C._gdk_pixbuf_animation_get_iter((*C.GdkPixbufAnimation)(_self_._value_), start_time)
	_go__return__ = ToPixbufAnimationIter(unsafe.Pointer(_return_))
	return
}

func (_self_ *PixbufAnimation) GetStaticImage() (_go__return__ Pixbuf) {
	var _return_ *C.GdkPixbuf
	_return_ = C.gdk_pixbuf_animation_get_static_image((*C.GdkPixbufAnimation)(_self_._value_))
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func (_self_ *PixbufAnimation) GetWidth() (_return_ C.int) {
	_return_ = C.gdk_pixbuf_animation_get_width((*C.GdkPixbufAnimation)(_self_._value_))
	return
}

func (_self_ *PixbufAnimation) IsStaticImage() (_go__return__ bool) {
	var _return_ C.gboolean
	_return_ = C.gdk_pixbuf_animation_is_static_image((*C.GdkPixbufAnimation)(_self_._value_))
	_go__return__ = _return_ == (C.gboolean)(C.TRUE)
	return
}

func (_self_ *PixbufAnimationIter) Advance(current_time *C.GTimeVal) (_go__return__ bool) {
	var _return_ C.gboolean
	_return_ = C._gdk_pixbuf_animation_iter_advance((*C.GdkPixbufAnimationIter)(_self_._value_), current_time)
	_go__return__ = _return_ == (C.gboolean)(C.TRUE)
	return
}

func (_self_ *PixbufAnimationIter) GetDelayTime() (_return_ C.int) {
	_return_ = C.gdk_pixbuf_animation_iter_get_delay_time((*C.GdkPixbufAnimationIter)(_self_._value_))
	return
}

func (_self_ *PixbufAnimationIter) GetPixbuf() (_go__return__ Pixbuf) {
	var _return_ *C.GdkPixbuf
	_return_ = C.gdk_pixbuf_animation_iter_get_pixbuf((*C.GdkPixbufAnimationIter)(_self_._value_))
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func (_self_ *PixbufAnimationIter) OnCurrentlyLoadingFrame() (_go__return__ bool) {
	var _return_ C.gboolean
	_return_ = C.gdk_pixbuf_animation_iter_on_currently_loading_frame((*C.GdkPixbufAnimationIter)(_self_._value_))
	_go__return__ = _return_ == (C.gboolean)(C.TRUE)
	return
}

func PixbufLoaderNew() (_go__return__ PixbufLoader) {
	var _return_ *C.GdkPixbufLoader
	_return_ = C.gdk_pixbuf_loader_new()
	_go__return__ = ToPixbufLoader(unsafe.Pointer(_return_))
	return
}

func PixbufLoaderNewWithMimeType(mime_type string) (_go__return__ PixbufLoader, _error_ unsafe.Pointer) {
	var _return_ *C.GdkPixbufLoader
	_cstring_mime_type_ := C.CString(mime_type)
	_cgo_mime_type_ := (*C.char)(unsafe.Pointer(_cstring_mime_type_))
	defer C.free(unsafe.Pointer(_cstring_mime_type_))
	_return_ = C._gdk_pixbuf_loader_new_with_mime_type(_cgo_mime_type_, _error_)
	_go__return__ = ToPixbufLoader(unsafe.Pointer(_return_))
	return
}

func PixbufLoaderNewWithType(image_type string) (_go__return__ PixbufLoader, _error_ unsafe.Pointer) {
	var _return_ *C.GdkPixbufLoader
	_cstring_image_type_ := C.CString(image_type)
	_cgo_image_type_ := (*C.char)(unsafe.Pointer(_cstring_image_type_))
	defer C.free(unsafe.Pointer(_cstring_image_type_))
	_return_ = C._gdk_pixbuf_loader_new_with_type(_cgo_image_type_, _error_)
	_go__return__ = ToPixbufLoader(unsafe.Pointer(_return_))
	return
}

func (_self_ *PixbufLoader) Close() (_go__return__ bool, _error_ unsafe.Pointer) {
	var _return_ C.gboolean
	_return_ = C._gdk_pixbuf_loader_close((*C.GdkPixbufLoader)(_self_._value_), _error_)
	_go__return__ = _return_ == (C.gboolean)(C.TRUE)
	return
}

func (_self_ *PixbufLoader) GetAnimation() (_go__return__ PixbufAnimation) {
	var _return_ *C.GdkPixbufAnimation
	_return_ = C.gdk_pixbuf_loader_get_animation((*C.GdkPixbufLoader)(_self_._value_))
	_go__return__ = ToPixbufAnimation(unsafe.Pointer(_return_))
	return
}

func (_self_ *PixbufLoader) GetFormat() (_go__return__ *PixbufFormat) {
	var _return_ *C.GdkPixbufFormat
	_return_ = C.gdk_pixbuf_loader_get_format((*C.GdkPixbufLoader)(_self_._value_))
	_go__return__ = (*PixbufFormat)(unsafe.Pointer(_return_))
	return
}

func (_self_ *PixbufLoader) GetPixbuf() (_go__return__ Pixbuf) {
	var _return_ *C.GdkPixbuf
	_return_ = C.gdk_pixbuf_loader_get_pixbuf((*C.GdkPixbufLoader)(_self_._value_))
	_go__return__ = ToPixbuf(unsafe.Pointer(_return_))
	return
}

func (_self_ *PixbufLoader) SetSize(width C.int, height C.int) () {
	C.gdk_pixbuf_loader_set_size((*C.GdkPixbufLoader)(_self_._value_), width, height)
	return
}

func PixbufSimpleAnimNew(width int, height int, rate float64) (_go__return__ PixbufSimpleAnim) {
	var _return_ *C.GdkPixbufSimpleAnim
	_cgo_width_ := (C.gint)(width)
	_cgo_height_ := (C.gint)(height)
	_cgo_rate_ := (C.gfloat)(rate)
	_return_ = C.gdk_pixbuf_simple_anim_new(_cgo_width_, _cgo_height_, _cgo_rate_)
	_go__return__ = ToPixbufSimpleAnim(unsafe.Pointer(_return_))
	return
}

func (_self_ *PixbufSimpleAnim) AddFrame(pixbuf PixbufKind) () {
	_cgo_pixbuf_ := (*C.GdkPixbuf)(pixbuf.GetGObject())
	C.gdk_pixbuf_simple_anim_add_frame((*C.GdkPixbufSimpleAnim)(_self_._value_), _cgo_pixbuf_)
	return
}

func (_self_ *PixbufSimpleAnim) GetLoop() (_go__return__ bool) {
	var _return_ C.gboolean
	_return_ = C.gdk_pixbuf_simple_anim_get_loop((*C.GdkPixbufSimpleAnim)(_self_._value_))
	_go__return__ = _return_ == (C.gboolean)(C.TRUE)
	return
}

func (_self_ *PixbufSimpleAnim) SetLoop(loop bool) () {
	_cgo_loop_ := (C.gboolean)(C.FALSE)
	if loop { _cgo_loop_ = (C.gboolean)(C.TRUE) }
	C.gdk_pixbuf_simple_anim_set_loop((*C.GdkPixbufSimpleAnim)(_self_._value_), _cgo_loop_)
	return
}

func (_self_ *PixbufFormat) Copy() (_go__return__ *PixbufFormat) {
	var _return_ *C.GdkPixbufFormat
	_return_ = C._gdk_pixbuf_format_copy((*C.GdkPixbufFormat)(_self_))
	_go__return__ = (*PixbufFormat)(unsafe.Pointer(_return_))
	return
}

func (_self_ *PixbufFormat) Free() () {
	C.gdk_pixbuf_format_free((*C.GdkPixbufFormat)(_self_))
	return
}

func (_self_ *PixbufFormat) GetDescription() (_go__return__ string) {
	var _return_ *C.gchar
	_return_ = C.gdk_pixbuf_format_get_description((*C.GdkPixbufFormat)(_self_))
	_go__return__ = C.GoString((*C.char)(unsafe.Pointer(_return_)))
	return
}

func (_self_ *PixbufFormat) GetExtensions() (_return_ unsafe.Pointer) {
	_return_ = C._gdk_pixbuf_format_get_extensions((*C.GdkPixbufFormat)(_self_))
	return
}

func (_self_ *PixbufFormat) GetLicense() (_go__return__ string) {
	var _return_ *C.gchar
	_return_ = C.gdk_pixbuf_format_get_license((*C.GdkPixbufFormat)(_self_))
	_go__return__ = C.GoString((*C.char)(unsafe.Pointer(_return_)))
	return
}

func (_self_ *PixbufFormat) GetMimeTypes() (_return_ unsafe.Pointer) {
	_return_ = C._gdk_pixbuf_format_get_mime_types((*C.GdkPixbufFormat)(_self_))
	return
}

func (_self_ *PixbufFormat) GetName() (_go__return__ string) {
	var _return_ *C.gchar
	_return_ = C.gdk_pixbuf_format_get_name((*C.GdkPixbufFormat)(_self_))
	_go__return__ = C.GoString((*C.char)(unsafe.Pointer(_return_)))
	return
}

func (_self_ *PixbufFormat) IsDisabled() (_go__return__ bool) {
	var _return_ C.gboolean
	_return_ = C.gdk_pixbuf_format_is_disabled((*C.GdkPixbufFormat)(_self_))
	_go__return__ = _return_ == (C.gboolean)(C.TRUE)
	return
}

func (_self_ *PixbufFormat) IsScalable() (_go__return__ bool) {
	var _return_ C.gboolean
	_return_ = C.gdk_pixbuf_format_is_scalable((*C.GdkPixbufFormat)(_self_))
	_go__return__ = _return_ == (C.gboolean)(C.TRUE)
	return
}

func (_self_ *PixbufFormat) IsWritable() (_go__return__ bool) {
	var _return_ C.gboolean
	_return_ = C.gdk_pixbuf_format_is_writable((*C.GdkPixbufFormat)(_self_))
	_go__return__ = _return_ == (C.gboolean)(C.TRUE)
	return
}

func (_self_ *PixbufFormat) SetDisabled(disabled bool) () {
	_cgo_disabled_ := (C.gboolean)(C.FALSE)
	if disabled { _cgo_disabled_ = (C.gboolean)(C.TRUE) }
	C.gdk_pixbuf_format_set_disabled((*C.GdkPixbufFormat)(_self_), _cgo_disabled_)
	return
}

const INTERP_BILINEAR = C.GDK_INTERP_BILINEAR
const INTERP_HYPER = C.GDK_INTERP_HYPER
const PIXBUF_ERROR_BAD_OPTION = C.GDK_PIXBUF_ERROR_BAD_OPTION
const PIXBUF_ROTATE_COUNTERCLOCKWISE = C.GDK_PIXBUF_ROTATE_COUNTERCLOCKWISE
const PIXBUF_ERROR_FAILED = C.GDK_PIXBUF_ERROR_FAILED
const PIXBUF_ROTATE_UPSIDEDOWN = C.GDK_PIXBUF_ROTATE_UPSIDEDOWN
const PIXBUF_MAJOR = C.GDK_PIXBUF_MAJOR
const COLORSPACE_RGB = C.GDK_COLORSPACE_RGB
const PIXBUF_ALPHA_FULL = C.GDK_PIXBUF_ALPHA_FULL
const PIXBUF_MINOR = C.GDK_PIXBUF_MINOR
const PIXBUF_MICRO = C.GDK_PIXBUF_MICRO
const INTERP_NEAREST = C.GDK_INTERP_NEAREST
const PIXBUF_ERROR_INSUFFICIENT_MEMORY = C.GDK_PIXBUF_ERROR_INSUFFICIENT_MEMORY
const PIXBUF_ERROR_UNSUPPORTED_OPERATION = C.GDK_PIXBUF_ERROR_UNSUPPORTED_OPERATION
const INTERP_TILES = C.GDK_INTERP_TILES
const PIXBUF_FEATURES_H = C.GDK_PIXBUF_FEATURES_H
const PIXBUF_ROTATE_NONE = C.GDK_PIXBUF_ROTATE_NONE
const PIXBUF_VERSION = C.GDK_PIXBUF_VERSION
const PIXBUF_ERROR_UNKNOWN_TYPE = C.GDK_PIXBUF_ERROR_UNKNOWN_TYPE
const PIXBUF_ERROR_CORRUPT_IMAGE = C.GDK_PIXBUF_ERROR_CORRUPT_IMAGE
const PIXBUF_ROTATE_CLOCKWISE = C.GDK_PIXBUF_ROTATE_CLOCKWISE
const PIXBUF_ALPHA_BILEVEL = C.GDK_PIXBUF_ALPHA_BILEVEL
