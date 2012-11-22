package gtk

// #cgo pkg-config: gtk+-3.0 gobject-2.0
// #include <glib-object.h>
// #include <glib/gstdio.h>
// #include <glib-unix.h>
// #include <gtk/gtkx.h>
/*
typedef long double longdouble;
void _gtk_accelerator_parse(void* accelerator, guint* accelerator_key, GdkModifierType* accelerator_mods) {
	gtk_accelerator_parse((const gchar*)(accelerator), accelerator_key, accelerator_mods);
}
void _gtk_accelerator_parse_with_keycode(void* accelerator, guint* accelerator_key, void* accelerator_codes, GdkModifierType* accelerator_mods) {
	gtk_accelerator_parse_with_keycode((const gchar*)(accelerator), accelerator_key, (guint**)(accelerator_codes), accelerator_mods);
}
GTokenType _gtk_binding_entry_add_signal_from_string(GtkBindingSet* binding_set, void* signal_desc) {
	return gtk_binding_entry_add_signal_from_string(binding_set, (const gchar*)(signal_desc));
}
void _gtk_binding_entry_add_signall(GtkBindingSet* binding_set, guint keyval, GdkModifierType modifiers, void* signal_name, GSList* binding_args) {
	gtk_binding_entry_add_signall(binding_set, keyval, modifiers, (const gchar*)(signal_name), binding_args);
}
GtkBindingSet* _gtk_binding_set_find(void* set_name) {
	return gtk_binding_set_find((const gchar*)(set_name));
}
GtkBindingSet* _gtk_binding_set_new(void* set_name) {
	return gtk_binding_set_new((const gchar*)(set_name));
}
void _gtk_drag_set_icon_name(GdkDragContext* context, void* icon_name, gint hot_x, gint hot_y) {
	gtk_drag_set_icon_name(context, (const gchar*)(icon_name), hot_x, hot_y);
}
void _gtk_drag_set_icon_stock(GdkDragContext* context, void* stock_id, gint hot_x, gint hot_y) {
	gtk_drag_set_icon_stock(context, (const gchar*)(stock_id), hot_x, hot_y);
}
GtkIconSize _gtk_icon_size_from_name(void* name) {
	return gtk_icon_size_from_name((const gchar*)(name));
}
GtkIconSize _gtk_icon_size_register(void* name, gint width, gint height) {
	return gtk_icon_size_register((const gchar*)(name), width, height);
}
void _gtk_icon_size_register_alias(void* alias, GtkIconSize target) {
	gtk_icon_size_register_alias((const gchar*)(alias), target);
}
void _gtk_init(int* argc, void* argv) {
	gtk_init(argc, (char***)(argv));
}
gboolean _gtk_init_check(int* argc, void* argv) {
	return gtk_init_check(argc, (char***)(argv));
}
gboolean _gtk_init_with_args(gint* argc, void* argv, void* parameter_string, GOptionEntry* entries, void* translation_domain, void* err) {
	return gtk_init_with_args(argc, (gchar***)(argv), (const gchar*)(parameter_string), entries, (const gchar*)(translation_domain), (GError**)(err));
}
gboolean _gtk_parse_args(int* argc, void* argv) {
	return gtk_parse_args(argc, (char***)(argv));
}
gboolean _gtk_rc_property_parse_border(void* pspec, void* gstring, GValue* property_value) {
	return gtk_rc_property_parse_border((const GParamSpec*)(pspec), (const GString*)(gstring), property_value);
}
gboolean _gtk_rc_property_parse_color(void* pspec, void* gstring, GValue* property_value) {
	return gtk_rc_property_parse_color((const GParamSpec*)(pspec), (const GString*)(gstring), property_value);
}
gboolean _gtk_rc_property_parse_enum(void* pspec, void* gstring, GValue* property_value) {
	return gtk_rc_property_parse_enum((const GParamSpec*)(pspec), (const GString*)(gstring), property_value);
}
gboolean _gtk_rc_property_parse_flags(void* pspec, void* gstring, GValue* property_value) {
	return gtk_rc_property_parse_flags((const GParamSpec*)(pspec), (const GString*)(gstring), property_value);
}
gboolean _gtk_rc_property_parse_requisition(void* pspec, void* gstring, GValue* property_value) {
	return gtk_rc_property_parse_requisition((const GParamSpec*)(pspec), (const GString*)(gstring), property_value);
}
GdkPixbuf* _gtk_render_icon_pixbuf(GtkStyleContext* context, void* source, GtkIconSize size) {
	return gtk_render_icon_pixbuf(context, (const GtkIconSource*)(source), size);
}
gboolean _gtk_show_uri(GdkScreen* screen, void* uri, guint32 timestamp, void* err) {
	return gtk_show_uri(screen, (const gchar*)(uri), timestamp, (GError**)(err));
}
gboolean _gtk_stock_lookup(void* stock_id, GtkStockItem* item) {
	return gtk_stock_lookup((const gchar*)(stock_id), item);
}
void _gtk_stock_set_translate_func(void* domain, GtkTranslateFunc _func, gpointer data, GDestroyNotify notify) {
	gtk_stock_set_translate_func((const gchar*)(domain), _func, data, notify);
}
GtkWidget* _gtk_test_create_simple_window(void* window_title, void* dialog_text) {
	return gtk_test_create_simple_window((const gchar*)(window_title), (const gchar*)(dialog_text));
}
GtkWidget* _gtk_test_find_label(GtkWidget* widget, void* label_pattern) {
	return gtk_test_find_label(widget, (const gchar*)(label_pattern));
}
GtkWidget* _gtk_test_find_widget(GtkWidget* widget, void* label_pattern, GType widget_type) {
	return gtk_test_find_widget(widget, (const gchar*)(label_pattern), widget_type);
}
void _gtk_test_text_set(GtkWidget* widget, void* string) {
	gtk_test_text_set(widget, (const gchar*)(string));
}
gboolean _gtk_tree_get_row_drag_data(GtkSelectionData* selection_data, void* tree_model, void* path) {
	return gtk_tree_get_row_drag_data(selection_data, (GtkTreeModel**)(tree_model), (GtkTreePath**)(path));
}
*/
import "C"
import (
	"unsafe"
)

func AccelGroupsActivate(object *C.GObject, accel_key C.guint, accel_mods C.GdkModifierType) C.gboolean {
	return C.gtk_accel_groups_activate(object, accel_key, accel_mods)
}

func AccelGroupsFromObject(object *C.GObject) *C.GSList {
	return C.gtk_accel_groups_from_object(object)
}

func AcceleratorGetDefaultModMask() C.GdkModifierType {
	return C.gtk_accelerator_get_default_mod_mask()
}

func AcceleratorGetLabel(accelerator_key C.guint, accelerator_mods C.GdkModifierType) *C.gchar {
	return C.gtk_accelerator_get_label(accelerator_key, accelerator_mods)
}

func AcceleratorGetLabelWithKeycode(display *C.GdkDisplay, accelerator_key C.guint, keycode C.guint, accelerator_mods C.GdkModifierType) *C.gchar {
	return C.gtk_accelerator_get_label_with_keycode(display, accelerator_key, keycode, accelerator_mods)
}

func AcceleratorName(accelerator_key C.guint, accelerator_mods C.GdkModifierType) *C.gchar {
	return C.gtk_accelerator_name(accelerator_key, accelerator_mods)
}

func AcceleratorNameWithKeycode(display *C.GdkDisplay, accelerator_key C.guint, keycode C.guint, accelerator_mods C.GdkModifierType) *C.gchar {
	return C.gtk_accelerator_name_with_keycode(display, accelerator_key, keycode, accelerator_mods)
}

func AcceleratorParse(accelerator *C.gchar, accelerator_key *C.guint, accelerator_mods *C.GdkModifierType) {
	C._gtk_accelerator_parse(unsafe.Pointer(accelerator), accelerator_key, accelerator_mods)
}

func AcceleratorParseWithKeycode(accelerator *C.gchar, accelerator_key *C.guint, accelerator_codes unsafe.Pointer, accelerator_mods *C.GdkModifierType) {
	C._gtk_accelerator_parse_with_keycode(unsafe.Pointer(accelerator), accelerator_key, unsafe.Pointer(accelerator_codes), accelerator_mods)
}

func AcceleratorSetDefaultModMask(default_mod_mask C.GdkModifierType) {
	C.gtk_accelerator_set_default_mod_mask(default_mod_mask)
}

func AcceleratorValid(keyval C.guint, modifiers C.GdkModifierType) C.gboolean {
	return C.gtk_accelerator_valid(keyval, modifiers)
}

func AlternativeDialogButtonOrder(screen *C.GdkScreen) C.gboolean {
	return C.gtk_alternative_dialog_button_order(screen)
}

func BindingEntryAddSignalFromString(binding_set *C.GtkBindingSet, signal_desc *C.gchar) C.GTokenType {
	return C._gtk_binding_entry_add_signal_from_string(binding_set, unsafe.Pointer(signal_desc))
}

func BindingEntryAddSignall(binding_set *C.GtkBindingSet, keyval C.guint, modifiers C.GdkModifierType, signal_name *C.gchar, binding_args *C.GSList) {
	C._gtk_binding_entry_add_signall(binding_set, keyval, modifiers, unsafe.Pointer(signal_name), binding_args)
}

func BindingEntryRemove(binding_set *C.GtkBindingSet, keyval C.guint, modifiers C.GdkModifierType) {
	C.gtk_binding_entry_remove(binding_set, keyval, modifiers)
}

func BindingEntrySkip(binding_set *C.GtkBindingSet, keyval C.guint, modifiers C.GdkModifierType) {
	C.gtk_binding_entry_skip(binding_set, keyval, modifiers)
}

func BindingSetByClass(object_class C.gpointer) *C.GtkBindingSet {
	return C.gtk_binding_set_by_class(object_class)
}

func BindingSetFind(set_name *C.gchar) *C.GtkBindingSet {
	return C._gtk_binding_set_find(unsafe.Pointer(set_name))
}

func BindingSetNew(set_name *C.gchar) *C.GtkBindingSet {
	return C._gtk_binding_set_new(unsafe.Pointer(set_name))
}

func BindingsActivate(object *C.GObject, keyval C.guint, modifiers C.GdkModifierType) C.gboolean {
	return C.gtk_bindings_activate(object, keyval, modifiers)
}

func BindingsActivateEvent(object *C.GObject, event *C.GdkEventKey) C.gboolean {
	return C.gtk_bindings_activate_event(object, event)
}

func BuilderErrorQuark() C.GQuark {
	return C.gtk_builder_error_quark()
}

func CairoShouldDrawWindow(cr *C.cairo_t, window *C.GdkWindow) C.gboolean {
	return C.gtk_cairo_should_draw_window(cr, window)
}

func CairoTransformToWindow(cr *C.cairo_t, widget *C.GtkWidget, window *C.GdkWindow) {
	C.gtk_cairo_transform_to_window(cr, widget, window)
}

func CheckVersion(required_major C.guint, required_minor C.guint, required_micro C.guint) *C.gchar {
	return C.gtk_check_version(required_major, required_minor, required_micro)
}

func CssProviderErrorQuark() C.GQuark {
	return C.gtk_css_provider_error_quark()
}

func DeviceGrabAdd(widget *C.GtkWidget, device *C.GdkDevice, block_others C.gboolean) {
	C.gtk_device_grab_add(widget, device, block_others)
}

func DeviceGrabRemove(widget *C.GtkWidget, device *C.GdkDevice) {
	C.gtk_device_grab_remove(widget, device)
}

func DisableSetlocale() {
	C.gtk_disable_setlocale()
}

func DistributeNaturalAllocation(extra_space C.gint, n_requested_sizes C.guint, sizes *C.GtkRequestedSize) C.gint {
	return C.gtk_distribute_natural_allocation(extra_space, n_requested_sizes, sizes)
}

func DragFinish(context *C.GdkDragContext, success C.gboolean, del C.gboolean, time_ C.guint32) {
	C.gtk_drag_finish(context, success, del, time_)
}

func DragGetSourceWidget(context *C.GdkDragContext) *C.GtkWidget {
	return C.gtk_drag_get_source_widget(context)
}

func DragSetIconDefault(context *C.GdkDragContext) {
	C.gtk_drag_set_icon_default(context)
}

func DragSetIconGicon(context *C.GdkDragContext, icon *C.GIcon, hot_x C.gint, hot_y C.gint) {
	C.gtk_drag_set_icon_gicon(context, icon, hot_x, hot_y)
}

func DragSetIconName(context *C.GdkDragContext, icon_name *C.gchar, hot_x C.gint, hot_y C.gint) {
	C._gtk_drag_set_icon_name(context, unsafe.Pointer(icon_name), hot_x, hot_y)
}

func DragSetIconPixbuf(context *C.GdkDragContext, pixbuf *C.GdkPixbuf, hot_x C.gint, hot_y C.gint) {
	C.gtk_drag_set_icon_pixbuf(context, pixbuf, hot_x, hot_y)
}

func DragSetIconStock(context *C.GdkDragContext, stock_id *C.gchar, hot_x C.gint, hot_y C.gint) {
	C._gtk_drag_set_icon_stock(context, unsafe.Pointer(stock_id), hot_x, hot_y)
}

func DragSetIconSurface(context *C.GdkDragContext, surface *C.cairo_surface_t) {
	C.gtk_drag_set_icon_surface(context, surface)
}

func DragSetIconWidget(context *C.GdkDragContext, widget *C.GtkWidget, hot_x C.gint, hot_y C.gint) {
	C.gtk_drag_set_icon_widget(context, widget, hot_x, hot_y)
}

//Deprecated gtk_draw_insertion_cursor

func EventsPending() C.gboolean {
	return C.gtk_events_pending()
}

func False() C.gboolean {
	return C.gtk_false()
}

func FileChooserErrorQuark() C.GQuark {
	return C.gtk_file_chooser_error_quark()
}

func GetBinaryAge() C.guint {
	return C.gtk_get_binary_age()
}

func GetCurrentEvent() *C.GdkEvent {
	return C.gtk_get_current_event()
}

func GetCurrentEventDevice() *C.GdkDevice {
	return C.gtk_get_current_event_device()
}

func GetCurrentEventState(state *C.GdkModifierType) C.gboolean {
	return C.gtk_get_current_event_state(state)
}

func GetCurrentEventTime() C.guint32 {
	return C.gtk_get_current_event_time()
}

func GetDebugFlags() C.guint {
	return C.gtk_get_debug_flags()
}

func GetDefaultLanguage() *C.PangoLanguage {
	return C.gtk_get_default_language()
}

func GetEventWidget(event *C.GdkEvent) *C.GtkWidget {
	return C.gtk_get_event_widget(event)
}

func GetInterfaceAge() C.guint {
	return C.gtk_get_interface_age()
}

func GetMajorVersion() C.guint {
	return C.gtk_get_major_version()
}

func GetMicroVersion() C.guint {
	return C.gtk_get_micro_version()
}

func GetMinorVersion() C.guint {
	return C.gtk_get_minor_version()
}

func GetOptionGroup(open_default_display C.gboolean) *C.GOptionGroup {
	return C.gtk_get_option_group(open_default_display)
}

func GrabGetCurrent() *C.GtkWidget {
	return C.gtk_grab_get_current()
}

func IconSizeFromName(name *C.gchar) C.GtkIconSize {
	return C._gtk_icon_size_from_name(unsafe.Pointer(name))
}

func IconSizeGetName(size C.GtkIconSize) *C.gchar {
	return C.gtk_icon_size_get_name(size)
}

func IconSizeLookup(size C.GtkIconSize, width *C.gint, height *C.gint) C.gboolean {
	return C.gtk_icon_size_lookup(size, width, height)
}

func IconSizeLookupForSettings(settings *C.GtkSettings, size C.GtkIconSize, width *C.gint, height *C.gint) C.gboolean {
	return C.gtk_icon_size_lookup_for_settings(settings, size, width, height)
}

func IconSizeRegister(name *C.gchar, width C.gint, height C.gint) C.GtkIconSize {
	return C._gtk_icon_size_register(unsafe.Pointer(name), width, height)
}

func IconSizeRegisterAlias(alias *C.gchar, target C.GtkIconSize) {
	C._gtk_icon_size_register_alias(unsafe.Pointer(alias), target)
}

func IconThemeErrorQuark() C.GQuark {
	return C.gtk_icon_theme_error_quark()
}

func Init(argc *C.int, argv unsafe.Pointer) {
	C._gtk_init(argc, unsafe.Pointer(argv))
}

func InitCheck(argc *C.int, argv unsafe.Pointer) C.gboolean {
	return C._gtk_init_check(argc, unsafe.Pointer(argv))
}

func InitWithArgs(argc *C.gint, argv unsafe.Pointer, parameter_string *C.gchar, entries *C.GOptionEntry, translation_domain *C.gchar, err unsafe.Pointer) C.gboolean {
	return C._gtk_init_with_args(argc, unsafe.Pointer(argv), unsafe.Pointer(parameter_string), entries, unsafe.Pointer(translation_domain), unsafe.Pointer(err))
}

//Deprecated gtk_key_snooper_install

//Deprecated gtk_key_snooper_remove

func Main() {
	C.gtk_main()
}

func MainDoEvent(event *C.GdkEvent) {
	C.gtk_main_do_event(event)
}

func MainIteration() C.gboolean {
	return C.gtk_main_iteration()
}

func MainIterationDo(blocking C.gboolean) C.gboolean {
	return C.gtk_main_iteration_do(blocking)
}

func MainLevel() C.guint {
	return C.gtk_main_level()
}

func MainQuit() {
	C.gtk_main_quit()
}

//Deprecated gtk_paint_arrow

//Deprecated gtk_paint_box

//Deprecated gtk_paint_box_gap

//Deprecated gtk_paint_check

//Deprecated gtk_paint_diamond

//Deprecated gtk_paint_expander

//Deprecated gtk_paint_extension

//Deprecated gtk_paint_flat_box

//Deprecated gtk_paint_focus

//Deprecated gtk_paint_handle

//Deprecated gtk_paint_hline

//Deprecated gtk_paint_layout

//Deprecated gtk_paint_option

//Deprecated gtk_paint_resize_grip

//Deprecated gtk_paint_shadow

//Deprecated gtk_paint_shadow_gap

//Deprecated gtk_paint_slider

//Deprecated gtk_paint_spinner

//Deprecated gtk_paint_tab

//Deprecated gtk_paint_vline

func PaperSizeGetDefault() *C.gchar {
	return C.gtk_paper_size_get_default()
}

func PaperSizeGetPaperSizes(include_custom C.gboolean) *C.GList {
	return C.gtk_paper_size_get_paper_sizes(include_custom)
}

func ParseArgs(argc *C.int, argv unsafe.Pointer) C.gboolean {
	return C._gtk_parse_args(argc, unsafe.Pointer(argv))
}

func PrintErrorQuark() C.GQuark {
	return C.gtk_print_error_quark()
}

func PrintRunPageSetupDialog(parent *C.GtkWindow, page_setup *C.GtkPageSetup, settings *C.GtkPrintSettings) *C.GtkPageSetup {
	return C.gtk_print_run_page_setup_dialog(parent, page_setup, settings)
}

func PrintRunPageSetupDialogAsync(parent *C.GtkWindow, page_setup *C.GtkPageSetup, settings *C.GtkPrintSettings, done_cb C.GtkPageSetupDoneFunc, data C.gpointer) {
	C.gtk_print_run_page_setup_dialog_async(parent, page_setup, settings, done_cb, data)
}

func PropagateEvent(widget *C.GtkWidget, event *C.GdkEvent) {
	C.gtk_propagate_event(widget, event)
}

//Deprecated gtk_rc_add_default_file

//Deprecated gtk_rc_find_module_in_path

//Deprecated gtk_rc_find_pixmap_in_path

//Deprecated gtk_rc_get_default_files

//Deprecated gtk_rc_get_im_module_file

//Deprecated gtk_rc_get_im_module_path

//Deprecated gtk_rc_get_module_dir

//Deprecated gtk_rc_get_style

//Deprecated gtk_rc_get_style_by_paths

//Deprecated gtk_rc_get_theme_dir

//Deprecated gtk_rc_parse

//Deprecated gtk_rc_parse_color

//Deprecated gtk_rc_parse_color_full

//Deprecated gtk_rc_parse_priority

//Deprecated gtk_rc_parse_state

//Deprecated gtk_rc_parse_string

func RcPropertyParseBorder(pspec *C.GParamSpec, gstring *C.GString, property_value *C.GValue) C.gboolean {
	return C._gtk_rc_property_parse_border(unsafe.Pointer(pspec), unsafe.Pointer(gstring), property_value)
}

func RcPropertyParseColor(pspec *C.GParamSpec, gstring *C.GString, property_value *C.GValue) C.gboolean {
	return C._gtk_rc_property_parse_color(unsafe.Pointer(pspec), unsafe.Pointer(gstring), property_value)
}

func RcPropertyParseEnum(pspec *C.GParamSpec, gstring *C.GString, property_value *C.GValue) C.gboolean {
	return C._gtk_rc_property_parse_enum(unsafe.Pointer(pspec), unsafe.Pointer(gstring), property_value)
}

func RcPropertyParseFlags(pspec *C.GParamSpec, gstring *C.GString, property_value *C.GValue) C.gboolean {
	return C._gtk_rc_property_parse_flags(unsafe.Pointer(pspec), unsafe.Pointer(gstring), property_value)
}

func RcPropertyParseRequisition(pspec *C.GParamSpec, gstring *C.GString, property_value *C.GValue) C.gboolean {
	return C._gtk_rc_property_parse_requisition(unsafe.Pointer(pspec), unsafe.Pointer(gstring), property_value)
}

//Deprecated gtk_rc_reparse_all

//Deprecated gtk_rc_reparse_all_for_settings

//Deprecated gtk_rc_reset_styles

//Deprecated gtk_rc_scanner_new

//Deprecated gtk_rc_set_default_files

func RecentChooserErrorQuark() C.GQuark {
	return C.gtk_recent_chooser_error_quark()
}

func RecentManagerErrorQuark() C.GQuark {
	return C.gtk_recent_manager_error_quark()
}

func RenderActivity(context *C.GtkStyleContext, cr *C.cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_activity(context, cr, x, y, width, height)
}

func RenderArrow(context *C.GtkStyleContext, cr *C.cairo_t, angle C.gdouble, x C.gdouble, y C.gdouble, size C.gdouble) {
	C.gtk_render_arrow(context, cr, angle, x, y, size)
}

func RenderBackground(context *C.GtkStyleContext, cr *C.cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_background(context, cr, x, y, width, height)
}

func RenderCheck(context *C.GtkStyleContext, cr *C.cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_check(context, cr, x, y, width, height)
}

func RenderExpander(context *C.GtkStyleContext, cr *C.cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_expander(context, cr, x, y, width, height)
}

func RenderExtension(context *C.GtkStyleContext, cr *C.cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble, gap_side C.GtkPositionType) {
	C.gtk_render_extension(context, cr, x, y, width, height, gap_side)
}

func RenderFocus(context *C.GtkStyleContext, cr *C.cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_focus(context, cr, x, y, width, height)
}

func RenderFrame(context *C.GtkStyleContext, cr *C.cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_frame(context, cr, x, y, width, height)
}

func RenderFrameGap(context *C.GtkStyleContext, cr *C.cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble, gap_side C.GtkPositionType, xy0_gap C.gdouble, xy1_gap C.gdouble) {
	C.gtk_render_frame_gap(context, cr, x, y, width, height, gap_side, xy0_gap, xy1_gap)
}

func RenderHandle(context *C.GtkStyleContext, cr *C.cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_handle(context, cr, x, y, width, height)
}

func RenderIcon(context *C.GtkStyleContext, cr *C.cairo_t, pixbuf *C.GdkPixbuf, x C.gdouble, y C.gdouble) {
	C.gtk_render_icon(context, cr, pixbuf, x, y)
}

func RenderIconPixbuf(context *C.GtkStyleContext, source *C.GtkIconSource, size C.GtkIconSize) *C.GdkPixbuf {
	return C._gtk_render_icon_pixbuf(context, unsafe.Pointer(source), size)
}

func RenderInsertionCursor(context *C.GtkStyleContext, cr *C.cairo_t, x C.gdouble, y C.gdouble, layout *C.PangoLayout, index C.int, direction C.PangoDirection) {
	C.gtk_render_insertion_cursor(context, cr, x, y, layout, index, direction)
}

func RenderLayout(context *C.GtkStyleContext, cr *C.cairo_t, x C.gdouble, y C.gdouble, layout *C.PangoLayout) {
	C.gtk_render_layout(context, cr, x, y, layout)
}

func RenderLine(context *C.GtkStyleContext, cr *C.cairo_t, x0 C.gdouble, y0 C.gdouble, x1 C.gdouble, y1 C.gdouble) {
	C.gtk_render_line(context, cr, x0, y0, x1, y1)
}

func RenderOption(context *C.GtkStyleContext, cr *C.cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_option(context, cr, x, y, width, height)
}

func RenderSlider(context *C.GtkStyleContext, cr *C.cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble, orientation C.GtkOrientation) {
	C.gtk_render_slider(context, cr, x, y, width, height, orientation)
}

func RgbToHsv(r C.gdouble, g C.gdouble, b C.gdouble, h *C.gdouble, s *C.gdouble, v *C.gdouble) {
	C.gtk_rgb_to_hsv(r, g, b, h, s, v)
}

func SelectionAddTarget(widget *C.GtkWidget, selection C.GdkAtom, target C.GdkAtom, info C.guint) {
	C.gtk_selection_add_target(widget, selection, target, info)
}

func SelectionAddTargets(widget *C.GtkWidget, selection C.GdkAtom, targets *C.GtkTargetEntry, ntargets C.guint) {
	C.gtk_selection_add_targets(widget, selection, targets, ntargets)
}

func SelectionClearTargets(widget *C.GtkWidget, selection C.GdkAtom) {
	C.gtk_selection_clear_targets(widget, selection)
}

func SelectionConvert(widget *C.GtkWidget, selection C.GdkAtom, target C.GdkAtom, time_ C.guint32) C.gboolean {
	return C.gtk_selection_convert(widget, selection, target, time_)
}

func SelectionOwnerSet(widget *C.GtkWidget, selection C.GdkAtom, time_ C.guint32) C.gboolean {
	return C.gtk_selection_owner_set(widget, selection, time_)
}

func SelectionOwnerSetForDisplay(display *C.GdkDisplay, widget *C.GtkWidget, selection C.GdkAtom, time_ C.guint32) C.gboolean {
	return C.gtk_selection_owner_set_for_display(display, widget, selection, time_)
}

func SelectionRemoveAll(widget *C.GtkWidget) {
	C.gtk_selection_remove_all(widget)
}

func SetDebugFlags(flags C.guint) {
	C.gtk_set_debug_flags(flags)
}

//TODO varargs gtk_show_about_dialog

func ShowUri(screen *C.GdkScreen, uri *C.gchar, timestamp C.guint32, err unsafe.Pointer) C.gboolean {
	return C._gtk_show_uri(screen, unsafe.Pointer(uri), timestamp, unsafe.Pointer(err))
}

func StockAdd(items *C.GtkStockItem, n_items C.guint) {
	C.gtk_stock_add(items, n_items)
}

func StockAddStatic(items *C.GtkStockItem, n_items C.guint) {
	C.gtk_stock_add_static(items, n_items)
}

func StockListIds() *C.GSList {
	return C.gtk_stock_list_ids()
}

func StockLookup(stock_id *C.gchar, item *C.GtkStockItem) C.gboolean {
	return C._gtk_stock_lookup(unsafe.Pointer(stock_id), item)
}

func StockSetTranslateFunc(domain *C.gchar, _func C.GtkTranslateFunc, data C.gpointer, notify C.GDestroyNotify) {
	C._gtk_stock_set_translate_func(unsafe.Pointer(domain), _func, data, notify)
}

func TargetTableFree(targets *C.GtkTargetEntry, n_targets C.gint) {
	C.gtk_target_table_free(targets, n_targets)
}

func TargetTableNewFromList(list *C.GtkTargetList, n_targets *C.gint) *C.GtkTargetEntry {
	return C.gtk_target_table_new_from_list(list, n_targets)
}

func TargetsIncludeImage(targets *C.GdkAtom, n_targets C.gint, writable C.gboolean) C.gboolean {
	return C.gtk_targets_include_image(targets, n_targets, writable)
}

func TargetsIncludeRichText(targets *C.GdkAtom, n_targets C.gint, buffer *C.GtkTextBuffer) C.gboolean {
	return C.gtk_targets_include_rich_text(targets, n_targets, buffer)
}

func TargetsIncludeText(targets *C.GdkAtom, n_targets C.gint) C.gboolean {
	return C.gtk_targets_include_text(targets, n_targets)
}

func TargetsIncludeUri(targets *C.GdkAtom, n_targets C.gint) C.gboolean {
	return C.gtk_targets_include_uri(targets, n_targets)
}

func TestCreateSimpleWindow(window_title *C.gchar, dialog_text *C.gchar) *C.GtkWidget {
	return C._gtk_test_create_simple_window(unsafe.Pointer(window_title), unsafe.Pointer(dialog_text))
}

//TODO varargs gtk_test_create_widget

//TODO varargs gtk_test_display_button_window

func TestFindLabel(widget *C.GtkWidget, label_pattern *C.gchar) *C.GtkWidget {
	return C._gtk_test_find_label(widget, unsafe.Pointer(label_pattern))
}

func TestFindSibling(base_widget *C.GtkWidget, widget_type C.GType) *C.GtkWidget {
	return C.gtk_test_find_sibling(base_widget, widget_type)
}

func TestFindWidget(widget *C.GtkWidget, label_pattern *C.gchar, widget_type C.GType) *C.GtkWidget {
	return C._gtk_test_find_widget(widget, unsafe.Pointer(label_pattern), widget_type)
}

//TODO varargs gtk_test_init

func TestListAllTypes(n_types *C.guint) *C.GType {
	return C.gtk_test_list_all_types(n_types)
}

func TestRegisterAllTypes() {
	C.gtk_test_register_all_types()
}

func TestSliderGetValue(widget *C.GtkWidget) C.double {
	return C.gtk_test_slider_get_value(widget)
}

func TestSliderSetPerc(widget *C.GtkWidget, percentage C.double) {
	C.gtk_test_slider_set_perc(widget, percentage)
}

func TestSpinButtonClick(spinner *C.GtkSpinButton, button C.guint, upwards C.gboolean) C.gboolean {
	return C.gtk_test_spin_button_click(spinner, button, upwards)
}

func TestTextGet(widget *C.GtkWidget) *C.gchar {
	return C.gtk_test_text_get(widget)
}

func TestTextSet(widget *C.GtkWidget, string *C.gchar) {
	C._gtk_test_text_set(widget, unsafe.Pointer(string))
}

func TestWidgetClick(widget *C.GtkWidget, button C.guint, modifiers C.GdkModifierType) C.gboolean {
	return C.gtk_test_widget_click(widget, button, modifiers)
}

func TestWidgetSendKey(widget *C.GtkWidget, keyval C.guint, modifiers C.GdkModifierType) C.gboolean {
	return C.gtk_test_widget_send_key(widget, keyval, modifiers)
}

func TreeGetRowDragData(selection_data *C.GtkSelectionData, tree_model unsafe.Pointer, path unsafe.Pointer) C.gboolean {
	return C._gtk_tree_get_row_drag_data(selection_data, unsafe.Pointer(tree_model), unsafe.Pointer(path))
}

func TreeRowReferenceDeleted(proxy *C.GObject, path *C.GtkTreePath) {
	C.gtk_tree_row_reference_deleted(proxy, path)
}

func TreeRowReferenceInserted(proxy *C.GObject, path *C.GtkTreePath) {
	C.gtk_tree_row_reference_inserted(proxy, path)
}

func TreeRowReferenceReordered(proxy *C.GObject, path *C.GtkTreePath, iter *C.GtkTreeIter, new_order *C.gint) {
	C.gtk_tree_row_reference_reordered(proxy, path, iter, new_order)
}

func TreeSetRowDragData(selection_data *C.GtkSelectionData, tree_model *C.GtkTreeModel, path *C.GtkTreePath) C.gboolean {
	return C.gtk_tree_set_row_drag_data(selection_data, tree_model, path)
}

func True() C.gboolean {
	return C.gtk_true()
}
