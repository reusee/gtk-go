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

const ALIGN_FILL = C.GTK_ALIGN_FILL
const ALIGN_START = C.GTK_ALIGN_START
const ALIGN_END = C.GTK_ALIGN_END
const ALIGN_CENTER = C.GTK_ALIGN_CENTER
const ARROWS_BOTH = C.GTK_ARROWS_BOTH
const ARROWS_START = C.GTK_ARROWS_START
const ARROWS_END = C.GTK_ARROWS_END
const ARROW_UP = C.GTK_ARROW_UP
const ARROW_DOWN = C.GTK_ARROW_DOWN
const ARROW_LEFT = C.GTK_ARROW_LEFT
const ARROW_RIGHT = C.GTK_ARROW_RIGHT
const ARROW_NONE = C.GTK_ARROW_NONE
const ASSISTANT_PAGE_CONTENT = C.GTK_ASSISTANT_PAGE_CONTENT
const ASSISTANT_PAGE_INTRO = C.GTK_ASSISTANT_PAGE_INTRO
const ASSISTANT_PAGE_CONFIRM = C.GTK_ASSISTANT_PAGE_CONFIRM
const ASSISTANT_PAGE_SUMMARY = C.GTK_ASSISTANT_PAGE_SUMMARY
const ASSISTANT_PAGE_PROGRESS = C.GTK_ASSISTANT_PAGE_PROGRESS
const ASSISTANT_PAGE_CUSTOM = C.GTK_ASSISTANT_PAGE_CUSTOM
const BORDER_STYLE_NONE = C.GTK_BORDER_STYLE_NONE
const BORDER_STYLE_SOLID = C.GTK_BORDER_STYLE_SOLID
const BORDER_STYLE_INSET = C.GTK_BORDER_STYLE_INSET
const BORDER_STYLE_OUTSET = C.GTK_BORDER_STYLE_OUTSET
const BORDER_STYLE_HIDDEN = C.GTK_BORDER_STYLE_HIDDEN
const BORDER_STYLE_DOTTED = C.GTK_BORDER_STYLE_DOTTED
const BORDER_STYLE_DASHED = C.GTK_BORDER_STYLE_DASHED
const BORDER_STYLE_DOUBLE = C.GTK_BORDER_STYLE_DOUBLE
const BORDER_STYLE_GROOVE = C.GTK_BORDER_STYLE_GROOVE
const BORDER_STYLE_RIDGE = C.GTK_BORDER_STYLE_RIDGE
const BUILDER_ERROR_INVALID_TYPE_FUNCTION = C.GTK_BUILDER_ERROR_INVALID_TYPE_FUNCTION
const BUILDER_ERROR_UNHANDLED_TAG = C.GTK_BUILDER_ERROR_UNHANDLED_TAG
const BUILDER_ERROR_MISSING_ATTRIBUTE = C.GTK_BUILDER_ERROR_MISSING_ATTRIBUTE
const BUILDER_ERROR_INVALID_ATTRIBUTE = C.GTK_BUILDER_ERROR_INVALID_ATTRIBUTE
const BUILDER_ERROR_INVALID_TAG = C.GTK_BUILDER_ERROR_INVALID_TAG
const BUILDER_ERROR_MISSING_PROPERTY_VALUE = C.GTK_BUILDER_ERROR_MISSING_PROPERTY_VALUE
const BUILDER_ERROR_INVALID_VALUE = C.GTK_BUILDER_ERROR_INVALID_VALUE
const BUILDER_ERROR_VERSION_MISMATCH = C.GTK_BUILDER_ERROR_VERSION_MISMATCH
const BUILDER_ERROR_DUPLICATE_ID = C.GTK_BUILDER_ERROR_DUPLICATE_ID
const BUTTONBOX_SPREAD = C.GTK_BUTTONBOX_SPREAD
const BUTTONBOX_EDGE = C.GTK_BUTTONBOX_EDGE
const BUTTONBOX_START = C.GTK_BUTTONBOX_START
const BUTTONBOX_END = C.GTK_BUTTONBOX_END
const BUTTONBOX_CENTER = C.GTK_BUTTONBOX_CENTER
const BUTTONS_NONE = C.GTK_BUTTONS_NONE
const BUTTONS_OK = C.GTK_BUTTONS_OK
const BUTTONS_CLOSE = C.GTK_BUTTONS_CLOSE
const BUTTONS_CANCEL = C.GTK_BUTTONS_CANCEL
const BUTTONS_YES_NO = C.GTK_BUTTONS_YES_NO
const BUTTONS_OK_CANCEL = C.GTK_BUTTONS_OK_CANCEL
const CELL_RENDERER_ACCEL_MODE_GTK = C.GTK_CELL_RENDERER_ACCEL_MODE_GTK
const CELL_RENDERER_ACCEL_MODE_OTHER = C.GTK_CELL_RENDERER_ACCEL_MODE_OTHER
const CELL_RENDERER_MODE_INERT = C.GTK_CELL_RENDERER_MODE_INERT
const CELL_RENDERER_MODE_ACTIVATABLE = C.GTK_CELL_RENDERER_MODE_ACTIVATABLE
const CELL_RENDERER_MODE_EDITABLE = C.GTK_CELL_RENDERER_MODE_EDITABLE
const CORNER_TOP_LEFT = C.GTK_CORNER_TOP_LEFT
const CORNER_BOTTOM_LEFT = C.GTK_CORNER_BOTTOM_LEFT
const CORNER_TOP_RIGHT = C.GTK_CORNER_TOP_RIGHT
const CORNER_BOTTOM_RIGHT = C.GTK_CORNER_BOTTOM_RIGHT
const CSS_PROVIDER_ERROR_FAILED = C.GTK_CSS_PROVIDER_ERROR_FAILED
const CSS_PROVIDER_ERROR_SYNTAX = C.GTK_CSS_PROVIDER_ERROR_SYNTAX
const CSS_PROVIDER_ERROR_IMPORT = C.GTK_CSS_PROVIDER_ERROR_IMPORT
const CSS_PROVIDER_ERROR_NAME = C.GTK_CSS_PROVIDER_ERROR_NAME
const CSS_PROVIDER_ERROR_DEPRECATED = C.GTK_CSS_PROVIDER_ERROR_DEPRECATED
const CSS_PROVIDER_ERROR_UNKNOWN_VALUE = C.GTK_CSS_PROVIDER_ERROR_UNKNOWN_VALUE
const CSS_SECTION_DOCUMENT = C.GTK_CSS_SECTION_DOCUMENT
const CSS_SECTION_IMPORT = C.GTK_CSS_SECTION_IMPORT
const CSS_SECTION_COLOR_DEFINITION = C.GTK_CSS_SECTION_COLOR_DEFINITION
const CSS_SECTION_BINDING_SET = C.GTK_CSS_SECTION_BINDING_SET
const CSS_SECTION_RULESET = C.GTK_CSS_SECTION_RULESET
const CSS_SECTION_SELECTOR = C.GTK_CSS_SECTION_SELECTOR
const CSS_SECTION_DECLARATION = C.GTK_CSS_SECTION_DECLARATION
const CSS_SECTION_VALUE = C.GTK_CSS_SECTION_VALUE
const CSS_SECTION_KEYFRAMES = C.GTK_CSS_SECTION_KEYFRAMES
const DELETE_CHARS = C.GTK_DELETE_CHARS
const DELETE_WORD_ENDS = C.GTK_DELETE_WORD_ENDS
const DELETE_WORDS = C.GTK_DELETE_WORDS
const DELETE_DISPLAY_LINES = C.GTK_DELETE_DISPLAY_LINES
const DELETE_DISPLAY_LINE_ENDS = C.GTK_DELETE_DISPLAY_LINE_ENDS
const DELETE_PARAGRAPH_ENDS = C.GTK_DELETE_PARAGRAPH_ENDS
const DELETE_PARAGRAPHS = C.GTK_DELETE_PARAGRAPHS
const DELETE_WHITESPACE = C.GTK_DELETE_WHITESPACE
const DIR_TAB_FORWARD = C.GTK_DIR_TAB_FORWARD
const DIR_TAB_BACKWARD = C.GTK_DIR_TAB_BACKWARD
const DIR_UP = C.GTK_DIR_UP
const DIR_DOWN = C.GTK_DIR_DOWN
const DIR_LEFT = C.GTK_DIR_LEFT
const DIR_RIGHT = C.GTK_DIR_RIGHT
const DRAG_RESULT_SUCCESS = C.GTK_DRAG_RESULT_SUCCESS
const DRAG_RESULT_NO_TARGET = C.GTK_DRAG_RESULT_NO_TARGET
const DRAG_RESULT_USER_CANCELLED = C.GTK_DRAG_RESULT_USER_CANCELLED
const DRAG_RESULT_TIMEOUT_EXPIRED = C.GTK_DRAG_RESULT_TIMEOUT_EXPIRED
const DRAG_RESULT_GRAB_BROKEN = C.GTK_DRAG_RESULT_GRAB_BROKEN
const DRAG_RESULT_ERROR = C.GTK_DRAG_RESULT_ERROR
const ENTRY_ICON_PRIMARY = C.GTK_ENTRY_ICON_PRIMARY
const ENTRY_ICON_SECONDARY = C.GTK_ENTRY_ICON_SECONDARY
const EXPANDER_COLLAPSED = C.GTK_EXPANDER_COLLAPSED
const EXPANDER_SEMI_COLLAPSED = C.GTK_EXPANDER_SEMI_COLLAPSED
const EXPANDER_SEMI_EXPANDED = C.GTK_EXPANDER_SEMI_EXPANDED
const EXPANDER_EXPANDED = C.GTK_EXPANDER_EXPANDED
const FILE_CHOOSER_ACTION_OPEN = C.GTK_FILE_CHOOSER_ACTION_OPEN
const FILE_CHOOSER_ACTION_SAVE = C.GTK_FILE_CHOOSER_ACTION_SAVE
const FILE_CHOOSER_ACTION_SELECT_FOLDER = C.GTK_FILE_CHOOSER_ACTION_SELECT_FOLDER
const FILE_CHOOSER_ACTION_CREATE_FOLDER = C.GTK_FILE_CHOOSER_ACTION_CREATE_FOLDER
const FILE_CHOOSER_CONFIRMATION_CONFIRM = C.GTK_FILE_CHOOSER_CONFIRMATION_CONFIRM
const FILE_CHOOSER_CONFIRMATION_ACCEPT_FILENAME = C.GTK_FILE_CHOOSER_CONFIRMATION_ACCEPT_FILENAME
const FILE_CHOOSER_CONFIRMATION_SELECT_AGAIN = C.GTK_FILE_CHOOSER_CONFIRMATION_SELECT_AGAIN
const FILE_CHOOSER_ERROR_NONEXISTENT = C.GTK_FILE_CHOOSER_ERROR_NONEXISTENT
const FILE_CHOOSER_ERROR_BAD_FILENAME = C.GTK_FILE_CHOOSER_ERROR_BAD_FILENAME
const FILE_CHOOSER_ERROR_ALREADY_EXISTS = C.GTK_FILE_CHOOSER_ERROR_ALREADY_EXISTS
const FILE_CHOOSER_ERROR_INCOMPLETE_HOSTNAME = C.GTK_FILE_CHOOSER_ERROR_INCOMPLETE_HOSTNAME
const IM_PREEDIT_NOTHING = C.GTK_IM_PREEDIT_NOTHING
const IM_PREEDIT_CALLBACK = C.GTK_IM_PREEDIT_CALLBACK
const IM_PREEDIT_NONE = C.GTK_IM_PREEDIT_NONE
const IM_STATUS_NOTHING = C.GTK_IM_STATUS_NOTHING
const IM_STATUS_CALLBACK = C.GTK_IM_STATUS_CALLBACK
const IM_STATUS_NONE = C.GTK_IM_STATUS_NONE
const ICON_SIZE_INVALID = C.GTK_ICON_SIZE_INVALID
const ICON_SIZE_MENU = C.GTK_ICON_SIZE_MENU
const ICON_SIZE_SMALL_TOOLBAR = C.GTK_ICON_SIZE_SMALL_TOOLBAR
const ICON_SIZE_LARGE_TOOLBAR = C.GTK_ICON_SIZE_LARGE_TOOLBAR
const ICON_SIZE_BUTTON = C.GTK_ICON_SIZE_BUTTON
const ICON_SIZE_DND = C.GTK_ICON_SIZE_DND
const ICON_SIZE_DIALOG = C.GTK_ICON_SIZE_DIALOG
const ICON_THEME_NOT_FOUND = C.GTK_ICON_THEME_NOT_FOUND
const ICON_THEME_FAILED = C.GTK_ICON_THEME_FAILED
const ICON_VIEW_NO_DROP = C.GTK_ICON_VIEW_NO_DROP
const ICON_VIEW_DROP_INTO = C.GTK_ICON_VIEW_DROP_INTO
const ICON_VIEW_DROP_LEFT = C.GTK_ICON_VIEW_DROP_LEFT
const ICON_VIEW_DROP_RIGHT = C.GTK_ICON_VIEW_DROP_RIGHT
const ICON_VIEW_DROP_ABOVE = C.GTK_ICON_VIEW_DROP_ABOVE
const ICON_VIEW_DROP_BELOW = C.GTK_ICON_VIEW_DROP_BELOW
const IMAGE_EMPTY = C.GTK_IMAGE_EMPTY
const IMAGE_PIXBUF = C.GTK_IMAGE_PIXBUF
const IMAGE_STOCK = C.GTK_IMAGE_STOCK
const IMAGE_ICON_SET = C.GTK_IMAGE_ICON_SET
const IMAGE_ANIMATION = C.GTK_IMAGE_ANIMATION
const IMAGE_ICON_NAME = C.GTK_IMAGE_ICON_NAME
const IMAGE_GICON = C.GTK_IMAGE_GICON
const INPUT_PURPOSE_FREE_FORM = C.GTK_INPUT_PURPOSE_FREE_FORM
const INPUT_PURPOSE_ALPHA = C.GTK_INPUT_PURPOSE_ALPHA
const INPUT_PURPOSE_DIGITS = C.GTK_INPUT_PURPOSE_DIGITS
const INPUT_PURPOSE_NUMBER = C.GTK_INPUT_PURPOSE_NUMBER
const INPUT_PURPOSE_PHONE = C.GTK_INPUT_PURPOSE_PHONE
const INPUT_PURPOSE_URL = C.GTK_INPUT_PURPOSE_URL
const INPUT_PURPOSE_EMAIL = C.GTK_INPUT_PURPOSE_EMAIL
const INPUT_PURPOSE_NAME = C.GTK_INPUT_PURPOSE_NAME
const INPUT_PURPOSE_PASSWORD = C.GTK_INPUT_PURPOSE_PASSWORD
const INPUT_PURPOSE_PIN = C.GTK_INPUT_PURPOSE_PIN
const JUSTIFY_LEFT = C.GTK_JUSTIFY_LEFT
const JUSTIFY_RIGHT = C.GTK_JUSTIFY_RIGHT
const JUSTIFY_CENTER = C.GTK_JUSTIFY_CENTER
const JUSTIFY_FILL = C.GTK_JUSTIFY_FILL
const LEVEL_BAR_MODE_CONTINUOUS = C.GTK_LEVEL_BAR_MODE_CONTINUOUS
const LEVEL_BAR_MODE_DISCRETE = C.GTK_LEVEL_BAR_MODE_DISCRETE
const LICENSE_UNKNOWN = C.GTK_LICENSE_UNKNOWN
const LICENSE_CUSTOM = C.GTK_LICENSE_CUSTOM
const LICENSE_GPL_2_0 = C.GTK_LICENSE_GPL_2_0
const LICENSE_GPL_3_0 = C.GTK_LICENSE_GPL_3_0
const LICENSE_LGPL_2_1 = C.GTK_LICENSE_LGPL_2_1
const LICENSE_LGPL_3_0 = C.GTK_LICENSE_LGPL_3_0
const LICENSE_BSD = C.GTK_LICENSE_BSD
const LICENSE_MIT_X11 = C.GTK_LICENSE_MIT_X11
const LICENSE_ARTISTIC = C.GTK_LICENSE_ARTISTIC
const MENU_DIR_PARENT = C.GTK_MENU_DIR_PARENT
const MENU_DIR_CHILD = C.GTK_MENU_DIR_CHILD
const MENU_DIR_NEXT = C.GTK_MENU_DIR_NEXT
const MENU_DIR_PREV = C.GTK_MENU_DIR_PREV
const MESSAGE_INFO = C.GTK_MESSAGE_INFO
const MESSAGE_WARNING = C.GTK_MESSAGE_WARNING
const MESSAGE_QUESTION = C.GTK_MESSAGE_QUESTION
const MESSAGE_ERROR = C.GTK_MESSAGE_ERROR
const MESSAGE_OTHER = C.GTK_MESSAGE_OTHER
const MOVEMENT_LOGICAL_POSITIONS = C.GTK_MOVEMENT_LOGICAL_POSITIONS
const MOVEMENT_VISUAL_POSITIONS = C.GTK_MOVEMENT_VISUAL_POSITIONS
const MOVEMENT_WORDS = C.GTK_MOVEMENT_WORDS
const MOVEMENT_DISPLAY_LINES = C.GTK_MOVEMENT_DISPLAY_LINES
const MOVEMENT_DISPLAY_LINE_ENDS = C.GTK_MOVEMENT_DISPLAY_LINE_ENDS
const MOVEMENT_PARAGRAPHS = C.GTK_MOVEMENT_PARAGRAPHS
const MOVEMENT_PARAGRAPH_ENDS = C.GTK_MOVEMENT_PARAGRAPH_ENDS
const MOVEMENT_PAGES = C.GTK_MOVEMENT_PAGES
const MOVEMENT_BUFFER_ENDS = C.GTK_MOVEMENT_BUFFER_ENDS
const MOVEMENT_HORIZONTAL_PAGES = C.GTK_MOVEMENT_HORIZONTAL_PAGES
const NOTEBOOK_TAB_FIRST = C.GTK_NOTEBOOK_TAB_FIRST
const NOTEBOOK_TAB_LAST = C.GTK_NOTEBOOK_TAB_LAST
const NUMBER_UP_LAYOUT_LEFT_TO_RIGHT_TOP_TO_BOTTOM = C.GTK_NUMBER_UP_LAYOUT_LEFT_TO_RIGHT_TOP_TO_BOTTOM
const NUMBER_UP_LAYOUT_LEFT_TO_RIGHT_BOTTOM_TO_TOP = C.GTK_NUMBER_UP_LAYOUT_LEFT_TO_RIGHT_BOTTOM_TO_TOP
const NUMBER_UP_LAYOUT_RIGHT_TO_LEFT_TOP_TO_BOTTOM = C.GTK_NUMBER_UP_LAYOUT_RIGHT_TO_LEFT_TOP_TO_BOTTOM
const NUMBER_UP_LAYOUT_RIGHT_TO_LEFT_BOTTOM_TO_TOP = C.GTK_NUMBER_UP_LAYOUT_RIGHT_TO_LEFT_BOTTOM_TO_TOP
const NUMBER_UP_LAYOUT_TOP_TO_BOTTOM_LEFT_TO_RIGHT = C.GTK_NUMBER_UP_LAYOUT_TOP_TO_BOTTOM_LEFT_TO_RIGHT
const NUMBER_UP_LAYOUT_TOP_TO_BOTTOM_RIGHT_TO_LEFT = C.GTK_NUMBER_UP_LAYOUT_TOP_TO_BOTTOM_RIGHT_TO_LEFT
const NUMBER_UP_LAYOUT_BOTTOM_TO_TOP_LEFT_TO_RIGHT = C.GTK_NUMBER_UP_LAYOUT_BOTTOM_TO_TOP_LEFT_TO_RIGHT
const NUMBER_UP_LAYOUT_BOTTOM_TO_TOP_RIGHT_TO_LEFT = C.GTK_NUMBER_UP_LAYOUT_BOTTOM_TO_TOP_RIGHT_TO_LEFT
const ORIENTATION_HORIZONTAL = C.GTK_ORIENTATION_HORIZONTAL
const ORIENTATION_VERTICAL = C.GTK_ORIENTATION_VERTICAL
const PACK_DIRECTION_LTR = C.GTK_PACK_DIRECTION_LTR
const PACK_DIRECTION_RTL = C.GTK_PACK_DIRECTION_RTL
const PACK_DIRECTION_TTB = C.GTK_PACK_DIRECTION_TTB
const PACK_DIRECTION_BTT = C.GTK_PACK_DIRECTION_BTT
const PACK_START = C.GTK_PACK_START
const PACK_END = C.GTK_PACK_END
const PAGE_ORIENTATION_PORTRAIT = C.GTK_PAGE_ORIENTATION_PORTRAIT
const PAGE_ORIENTATION_LANDSCAPE = C.GTK_PAGE_ORIENTATION_LANDSCAPE
const PAGE_ORIENTATION_REVERSE_PORTRAIT = C.GTK_PAGE_ORIENTATION_REVERSE_PORTRAIT
const PAGE_ORIENTATION_REVERSE_LANDSCAPE = C.GTK_PAGE_ORIENTATION_REVERSE_LANDSCAPE
const PAGE_SET_ALL = C.GTK_PAGE_SET_ALL
const PAGE_SET_EVEN = C.GTK_PAGE_SET_EVEN
const PAGE_SET_ODD = C.GTK_PAGE_SET_ODD
const PATH_PRIO_LOWEST = C.GTK_PATH_PRIO_LOWEST
const PATH_PRIO_GTK = C.GTK_PATH_PRIO_GTK
const PATH_PRIO_APPLICATION = C.GTK_PATH_PRIO_APPLICATION
const PATH_PRIO_THEME = C.GTK_PATH_PRIO_THEME
const PATH_PRIO_RC = C.GTK_PATH_PRIO_RC
const PATH_PRIO_HIGHEST = C.GTK_PATH_PRIO_HIGHEST
const PATH_WIDGET = C.GTK_PATH_WIDGET
const PATH_WIDGET_CLASS = C.GTK_PATH_WIDGET_CLASS
const PATH_CLASS = C.GTK_PATH_CLASS
const POLICY_ALWAYS = C.GTK_POLICY_ALWAYS
const POLICY_AUTOMATIC = C.GTK_POLICY_AUTOMATIC
const POLICY_NEVER = C.GTK_POLICY_NEVER
const POS_LEFT = C.GTK_POS_LEFT
const POS_RIGHT = C.GTK_POS_RIGHT
const POS_TOP = C.GTK_POS_TOP
const POS_BOTTOM = C.GTK_POS_BOTTOM
const PRINT_DUPLEX_SIMPLEX = C.GTK_PRINT_DUPLEX_SIMPLEX
const PRINT_DUPLEX_HORIZONTAL = C.GTK_PRINT_DUPLEX_HORIZONTAL
const PRINT_DUPLEX_VERTICAL = C.GTK_PRINT_DUPLEX_VERTICAL
const PRINT_ERROR_GENERAL = C.GTK_PRINT_ERROR_GENERAL
const PRINT_ERROR_INTERNAL_ERROR = C.GTK_PRINT_ERROR_INTERNAL_ERROR
const PRINT_ERROR_NOMEM = C.GTK_PRINT_ERROR_NOMEM
const PRINT_ERROR_INVALID_FILE = C.GTK_PRINT_ERROR_INVALID_FILE
const PRINT_OPERATION_ACTION_PRINT_DIALOG = C.GTK_PRINT_OPERATION_ACTION_PRINT_DIALOG
const PRINT_OPERATION_ACTION_PRINT = C.GTK_PRINT_OPERATION_ACTION_PRINT
const PRINT_OPERATION_ACTION_PREVIEW = C.GTK_PRINT_OPERATION_ACTION_PREVIEW
const PRINT_OPERATION_ACTION_EXPORT = C.GTK_PRINT_OPERATION_ACTION_EXPORT
const PRINT_OPERATION_RESULT_ERROR = C.GTK_PRINT_OPERATION_RESULT_ERROR
const PRINT_OPERATION_RESULT_APPLY = C.GTK_PRINT_OPERATION_RESULT_APPLY
const PRINT_OPERATION_RESULT_CANCEL = C.GTK_PRINT_OPERATION_RESULT_CANCEL
const PRINT_OPERATION_RESULT_IN_PROGRESS = C.GTK_PRINT_OPERATION_RESULT_IN_PROGRESS
const PRINT_PAGES_ALL = C.GTK_PRINT_PAGES_ALL
const PRINT_PAGES_CURRENT = C.GTK_PRINT_PAGES_CURRENT
const PRINT_PAGES_RANGES = C.GTK_PRINT_PAGES_RANGES
const PRINT_PAGES_SELECTION = C.GTK_PRINT_PAGES_SELECTION
const PRINT_QUALITY_LOW = C.GTK_PRINT_QUALITY_LOW
const PRINT_QUALITY_NORMAL = C.GTK_PRINT_QUALITY_NORMAL
const PRINT_QUALITY_HIGH = C.GTK_PRINT_QUALITY_HIGH
const PRINT_QUALITY_DRAFT = C.GTK_PRINT_QUALITY_DRAFT
const PRINT_STATUS_INITIAL = C.GTK_PRINT_STATUS_INITIAL
const PRINT_STATUS_PREPARING = C.GTK_PRINT_STATUS_PREPARING
const PRINT_STATUS_GENERATING_DATA = C.GTK_PRINT_STATUS_GENERATING_DATA
const PRINT_STATUS_SENDING_DATA = C.GTK_PRINT_STATUS_SENDING_DATA
const PRINT_STATUS_PENDING = C.GTK_PRINT_STATUS_PENDING
const PRINT_STATUS_PENDING_ISSUE = C.GTK_PRINT_STATUS_PENDING_ISSUE
const PRINT_STATUS_PRINTING = C.GTK_PRINT_STATUS_PRINTING
const PRINT_STATUS_FINISHED = C.GTK_PRINT_STATUS_FINISHED
const PRINT_STATUS_FINISHED_ABORTED = C.GTK_PRINT_STATUS_FINISHED_ABORTED
const RC_TOKEN_INVALID = C.GTK_RC_TOKEN_INVALID
const RC_TOKEN_INCLUDE = C.GTK_RC_TOKEN_INCLUDE
const RC_TOKEN_NORMAL = C.GTK_RC_TOKEN_NORMAL
const RC_TOKEN_ACTIVE = C.GTK_RC_TOKEN_ACTIVE
const RC_TOKEN_PRELIGHT = C.GTK_RC_TOKEN_PRELIGHT
const RC_TOKEN_SELECTED = C.GTK_RC_TOKEN_SELECTED
const RC_TOKEN_INSENSITIVE = C.GTK_RC_TOKEN_INSENSITIVE
const RC_TOKEN_FG = C.GTK_RC_TOKEN_FG
const RC_TOKEN_BG = C.GTK_RC_TOKEN_BG
const RC_TOKEN_TEXT = C.GTK_RC_TOKEN_TEXT
const RC_TOKEN_BASE = C.GTK_RC_TOKEN_BASE
const RC_TOKEN_XTHICKNESS = C.GTK_RC_TOKEN_XTHICKNESS
const RC_TOKEN_YTHICKNESS = C.GTK_RC_TOKEN_YTHICKNESS
const RC_TOKEN_FONT = C.GTK_RC_TOKEN_FONT
const RC_TOKEN_FONTSET = C.GTK_RC_TOKEN_FONTSET
const RC_TOKEN_FONT_NAME = C.GTK_RC_TOKEN_FONT_NAME
const RC_TOKEN_BG_PIXMAP = C.GTK_RC_TOKEN_BG_PIXMAP
const RC_TOKEN_PIXMAP_PATH = C.GTK_RC_TOKEN_PIXMAP_PATH
const RC_TOKEN_STYLE = C.GTK_RC_TOKEN_STYLE
const RC_TOKEN_BINDING = C.GTK_RC_TOKEN_BINDING
const RC_TOKEN_BIND = C.GTK_RC_TOKEN_BIND
const RC_TOKEN_WIDGET = C.GTK_RC_TOKEN_WIDGET
const RC_TOKEN_WIDGET_CLASS = C.GTK_RC_TOKEN_WIDGET_CLASS
const RC_TOKEN_CLASS = C.GTK_RC_TOKEN_CLASS
const RC_TOKEN_LOWEST = C.GTK_RC_TOKEN_LOWEST
const RC_TOKEN_GTK = C.GTK_RC_TOKEN_GTK
const RC_TOKEN_APPLICATION = C.GTK_RC_TOKEN_APPLICATION
const RC_TOKEN_THEME = C.GTK_RC_TOKEN_THEME
const RC_TOKEN_RC = C.GTK_RC_TOKEN_RC
const RC_TOKEN_HIGHEST = C.GTK_RC_TOKEN_HIGHEST
const RC_TOKEN_ENGINE = C.GTK_RC_TOKEN_ENGINE
const RC_TOKEN_MODULE_PATH = C.GTK_RC_TOKEN_MODULE_PATH
const RC_TOKEN_IM_MODULE_PATH = C.GTK_RC_TOKEN_IM_MODULE_PATH
const RC_TOKEN_IM_MODULE_FILE = C.GTK_RC_TOKEN_IM_MODULE_FILE
const RC_TOKEN_STOCK = C.GTK_RC_TOKEN_STOCK
const RC_TOKEN_LTR = C.GTK_RC_TOKEN_LTR
const RC_TOKEN_RTL = C.GTK_RC_TOKEN_RTL
const RC_TOKEN_COLOR = C.GTK_RC_TOKEN_COLOR
const RC_TOKEN_UNBIND = C.GTK_RC_TOKEN_UNBIND
const RC_TOKEN_LAST = C.GTK_RC_TOKEN_LAST
const RECENT_CHOOSER_ERROR_NOT_FOUND = C.GTK_RECENT_CHOOSER_ERROR_NOT_FOUND
const RECENT_CHOOSER_ERROR_INVALID_URI = C.GTK_RECENT_CHOOSER_ERROR_INVALID_URI
const RECENT_MANAGER_ERROR_NOT_FOUND = C.GTK_RECENT_MANAGER_ERROR_NOT_FOUND
const RECENT_MANAGER_ERROR_INVALID_URI = C.GTK_RECENT_MANAGER_ERROR_INVALID_URI
const RECENT_MANAGER_ERROR_INVALID_ENCODING = C.GTK_RECENT_MANAGER_ERROR_INVALID_ENCODING
const RECENT_MANAGER_ERROR_NOT_REGISTERED = C.GTK_RECENT_MANAGER_ERROR_NOT_REGISTERED
const RECENT_MANAGER_ERROR_READ = C.GTK_RECENT_MANAGER_ERROR_READ
const RECENT_MANAGER_ERROR_WRITE = C.GTK_RECENT_MANAGER_ERROR_WRITE
const RECENT_MANAGER_ERROR_UNKNOWN = C.GTK_RECENT_MANAGER_ERROR_UNKNOWN
const RECENT_SORT_NONE = C.GTK_RECENT_SORT_NONE
const RECENT_SORT_MRU = C.GTK_RECENT_SORT_MRU
const RECENT_SORT_LRU = C.GTK_RECENT_SORT_LRU
const RECENT_SORT_CUSTOM = C.GTK_RECENT_SORT_CUSTOM
const RELIEF_NORMAL = C.GTK_RELIEF_NORMAL
const RELIEF_HALF = C.GTK_RELIEF_HALF
const RELIEF_NONE = C.GTK_RELIEF_NONE
const RESIZE_PARENT = C.GTK_RESIZE_PARENT
const RESIZE_QUEUE = C.GTK_RESIZE_QUEUE
const RESIZE_IMMEDIATE = C.GTK_RESIZE_IMMEDIATE
const RESPONSE_NONE = C.GTK_RESPONSE_NONE
const RESPONSE_REJECT = C.GTK_RESPONSE_REJECT
const RESPONSE_ACCEPT = C.GTK_RESPONSE_ACCEPT
const RESPONSE_DELETE_EVENT = C.GTK_RESPONSE_DELETE_EVENT
const RESPONSE_OK = C.GTK_RESPONSE_OK
const RESPONSE_CANCEL = C.GTK_RESPONSE_CANCEL
const RESPONSE_CLOSE = C.GTK_RESPONSE_CLOSE
const RESPONSE_YES = C.GTK_RESPONSE_YES
const RESPONSE_NO = C.GTK_RESPONSE_NO
const RESPONSE_APPLY = C.GTK_RESPONSE_APPLY
const RESPONSE_HELP = C.GTK_RESPONSE_HELP
const SCROLL_STEPS = C.GTK_SCROLL_STEPS
const SCROLL_PAGES = C.GTK_SCROLL_PAGES
const SCROLL_ENDS = C.GTK_SCROLL_ENDS
const SCROLL_HORIZONTAL_STEPS = C.GTK_SCROLL_HORIZONTAL_STEPS
const SCROLL_HORIZONTAL_PAGES = C.GTK_SCROLL_HORIZONTAL_PAGES
const SCROLL_HORIZONTAL_ENDS = C.GTK_SCROLL_HORIZONTAL_ENDS
const SCROLL_NONE = C.GTK_SCROLL_NONE
const SCROLL_JUMP = C.GTK_SCROLL_JUMP
const SCROLL_STEP_BACKWARD = C.GTK_SCROLL_STEP_BACKWARD
const SCROLL_STEP_FORWARD = C.GTK_SCROLL_STEP_FORWARD
const SCROLL_PAGE_BACKWARD = C.GTK_SCROLL_PAGE_BACKWARD
const SCROLL_PAGE_FORWARD = C.GTK_SCROLL_PAGE_FORWARD
const SCROLL_STEP_UP = C.GTK_SCROLL_STEP_UP
const SCROLL_STEP_DOWN = C.GTK_SCROLL_STEP_DOWN
const SCROLL_PAGE_UP = C.GTK_SCROLL_PAGE_UP
const SCROLL_PAGE_DOWN = C.GTK_SCROLL_PAGE_DOWN
const SCROLL_STEP_LEFT = C.GTK_SCROLL_STEP_LEFT
const SCROLL_STEP_RIGHT = C.GTK_SCROLL_STEP_RIGHT
const SCROLL_PAGE_LEFT = C.GTK_SCROLL_PAGE_LEFT
const SCROLL_PAGE_RIGHT = C.GTK_SCROLL_PAGE_RIGHT
const SCROLL_START = C.GTK_SCROLL_START
const SCROLL_END = C.GTK_SCROLL_END
const SCROLL_MINIMUM = C.GTK_SCROLL_MINIMUM
const SCROLL_NATURAL = C.GTK_SCROLL_NATURAL
const SELECTION_NONE = C.GTK_SELECTION_NONE
const SELECTION_SINGLE = C.GTK_SELECTION_SINGLE
const SELECTION_BROWSE = C.GTK_SELECTION_BROWSE
const SELECTION_MULTIPLE = C.GTK_SELECTION_MULTIPLE
const SENSITIVITY_AUTO = C.GTK_SENSITIVITY_AUTO
const SENSITIVITY_ON = C.GTK_SENSITIVITY_ON
const SENSITIVITY_OFF = C.GTK_SENSITIVITY_OFF
const SHADOW_NONE = C.GTK_SHADOW_NONE
const SHADOW_IN = C.GTK_SHADOW_IN
const SHADOW_OUT = C.GTK_SHADOW_OUT
const SHADOW_ETCHED_IN = C.GTK_SHADOW_ETCHED_IN
const SHADOW_ETCHED_OUT = C.GTK_SHADOW_ETCHED_OUT
const SIZE_GROUP_NONE = C.GTK_SIZE_GROUP_NONE
const SIZE_GROUP_HORIZONTAL = C.GTK_SIZE_GROUP_HORIZONTAL
const SIZE_GROUP_VERTICAL = C.GTK_SIZE_GROUP_VERTICAL
const SIZE_GROUP_BOTH = C.GTK_SIZE_GROUP_BOTH
const SIZE_REQUEST_HEIGHT_FOR_WIDTH = C.GTK_SIZE_REQUEST_HEIGHT_FOR_WIDTH
const SIZE_REQUEST_WIDTH_FOR_HEIGHT = C.GTK_SIZE_REQUEST_WIDTH_FOR_HEIGHT
const SIZE_REQUEST_CONSTANT_SIZE = C.GTK_SIZE_REQUEST_CONSTANT_SIZE
const SORT_ASCENDING = C.GTK_SORT_ASCENDING
const SORT_DESCENDING = C.GTK_SORT_DESCENDING
const UPDATE_ALWAYS = C.GTK_UPDATE_ALWAYS
const UPDATE_IF_VALID = C.GTK_UPDATE_IF_VALID
const SPIN_STEP_FORWARD = C.GTK_SPIN_STEP_FORWARD
const SPIN_STEP_BACKWARD = C.GTK_SPIN_STEP_BACKWARD
const SPIN_PAGE_FORWARD = C.GTK_SPIN_PAGE_FORWARD
const SPIN_PAGE_BACKWARD = C.GTK_SPIN_PAGE_BACKWARD
const SPIN_HOME = C.GTK_SPIN_HOME
const SPIN_END = C.GTK_SPIN_END
const SPIN_USER_DEFINED = C.GTK_SPIN_USER_DEFINED
const STATE_NORMAL = C.GTK_STATE_NORMAL
const STATE_ACTIVE = C.GTK_STATE_ACTIVE
const STATE_PRELIGHT = C.GTK_STATE_PRELIGHT
const STATE_SELECTED = C.GTK_STATE_SELECTED
const STATE_INSENSITIVE = C.GTK_STATE_INSENSITIVE
const STATE_INCONSISTENT = C.GTK_STATE_INCONSISTENT
const STATE_FOCUSED = C.GTK_STATE_FOCUSED
const TEXT_BUFFER_TARGET_INFO_BUFFER_CONTENTS = C.GTK_TEXT_BUFFER_TARGET_INFO_BUFFER_CONTENTS
const TEXT_BUFFER_TARGET_INFO_RICH_TEXT = C.GTK_TEXT_BUFFER_TARGET_INFO_RICH_TEXT
const TEXT_BUFFER_TARGET_INFO_TEXT = C.GTK_TEXT_BUFFER_TARGET_INFO_TEXT
const TEXT_DIR_NONE = C.GTK_TEXT_DIR_NONE
const TEXT_DIR_LTR = C.GTK_TEXT_DIR_LTR
const TEXT_DIR_RTL = C.GTK_TEXT_DIR_RTL
const TEXT_WINDOW_PRIVATE = C.GTK_TEXT_WINDOW_PRIVATE
const TEXT_WINDOW_WIDGET = C.GTK_TEXT_WINDOW_WIDGET
const TEXT_WINDOW_TEXT = C.GTK_TEXT_WINDOW_TEXT
const TEXT_WINDOW_LEFT = C.GTK_TEXT_WINDOW_LEFT
const TEXT_WINDOW_RIGHT = C.GTK_TEXT_WINDOW_RIGHT
const TEXT_WINDOW_TOP = C.GTK_TEXT_WINDOW_TOP
const TEXT_WINDOW_BOTTOM = C.GTK_TEXT_WINDOW_BOTTOM
const TOOLBAR_SPACE_EMPTY = C.GTK_TOOLBAR_SPACE_EMPTY
const TOOLBAR_SPACE_LINE = C.GTK_TOOLBAR_SPACE_LINE
const TOOLBAR_ICONS = C.GTK_TOOLBAR_ICONS
const TOOLBAR_TEXT = C.GTK_TOOLBAR_TEXT
const TOOLBAR_BOTH = C.GTK_TOOLBAR_BOTH
const TOOLBAR_BOTH_HORIZ = C.GTK_TOOLBAR_BOTH_HORIZ
const TREE_VIEW_COLUMN_GROW_ONLY = C.GTK_TREE_VIEW_COLUMN_GROW_ONLY
const TREE_VIEW_COLUMN_AUTOSIZE = C.GTK_TREE_VIEW_COLUMN_AUTOSIZE
const TREE_VIEW_COLUMN_FIXED = C.GTK_TREE_VIEW_COLUMN_FIXED
const TREE_VIEW_DROP_BEFORE = C.GTK_TREE_VIEW_DROP_BEFORE
const TREE_VIEW_DROP_AFTER = C.GTK_TREE_VIEW_DROP_AFTER
const TREE_VIEW_DROP_INTO_OR_BEFORE = C.GTK_TREE_VIEW_DROP_INTO_OR_BEFORE
const TREE_VIEW_DROP_INTO_OR_AFTER = C.GTK_TREE_VIEW_DROP_INTO_OR_AFTER
const TREE_VIEW_GRID_LINES_NONE = C.GTK_TREE_VIEW_GRID_LINES_NONE
const TREE_VIEW_GRID_LINES_HORIZONTAL = C.GTK_TREE_VIEW_GRID_LINES_HORIZONTAL
const TREE_VIEW_GRID_LINES_VERTICAL = C.GTK_TREE_VIEW_GRID_LINES_VERTICAL
const TREE_VIEW_GRID_LINES_BOTH = C.GTK_TREE_VIEW_GRID_LINES_BOTH
const UNIT_NONE = C.GTK_UNIT_NONE
const UNIT_POINTS = C.GTK_UNIT_POINTS
const UNIT_INCH = C.GTK_UNIT_INCH
const UNIT_MM = C.GTK_UNIT_MM
const WIDGET_HELP_TOOLTIP = C.GTK_WIDGET_HELP_TOOLTIP
const WIDGET_HELP_WHATS_THIS = C.GTK_WIDGET_HELP_WHATS_THIS
const WIN_POS_NONE = C.GTK_WIN_POS_NONE
const WIN_POS_CENTER = C.GTK_WIN_POS_CENTER
const WIN_POS_MOUSE = C.GTK_WIN_POS_MOUSE
const WIN_POS_CENTER_ALWAYS = C.GTK_WIN_POS_CENTER_ALWAYS
const WIN_POS_CENTER_ON_PARENT = C.GTK_WIN_POS_CENTER_ON_PARENT
const WINDOW_TOPLEVEL = C.GTK_WINDOW_TOPLEVEL
const WINDOW_POPUP = C.GTK_WINDOW_POPUP
const WRAP_NONE = C.GTK_WRAP_NONE
const WRAP_CHAR = C.GTK_WRAP_CHAR
const WRAP_WORD = C.GTK_WRAP_WORD
const WRAP_WORD_CHAR = C.GTK_WRAP_WORD_CHAR
const BINARY_AGE = C.GTK_BINARY_AGE
const INPUT_ERROR = C.GTK_INPUT_ERROR
const INTERFACE_AGE = C.GTK_INTERFACE_AGE
const LEVEL_BAR_OFFSET_HIGH = C.GTK_LEVEL_BAR_OFFSET_HIGH
const LEVEL_BAR_OFFSET_LOW = C.GTK_LEVEL_BAR_OFFSET_LOW
const MAJOR_VERSION = C.GTK_MAJOR_VERSION
const MAX_COMPOSE_LEN = C.GTK_MAX_COMPOSE_LEN
const MICRO_VERSION = C.GTK_MICRO_VERSION
const MINOR_VERSION = C.GTK_MINOR_VERSION
const PAPER_NAME_A3 = C.GTK_PAPER_NAME_A3
const PAPER_NAME_A4 = C.GTK_PAPER_NAME_A4
const PAPER_NAME_A5 = C.GTK_PAPER_NAME_A5
const PAPER_NAME_B5 = C.GTK_PAPER_NAME_B5
const PAPER_NAME_EXECUTIVE = C.GTK_PAPER_NAME_EXECUTIVE
const PAPER_NAME_LEGAL = C.GTK_PAPER_NAME_LEGAL
const PAPER_NAME_LETTER = C.GTK_PAPER_NAME_LETTER
const PATH_PRIO_MASK = C.GTK_PATH_PRIO_MASK
const PRINT_SETTINGS_COLLATE = C.GTK_PRINT_SETTINGS_COLLATE
const PRINT_SETTINGS_DEFAULT_SOURCE = C.GTK_PRINT_SETTINGS_DEFAULT_SOURCE
const PRINT_SETTINGS_DITHER = C.GTK_PRINT_SETTINGS_DITHER
const PRINT_SETTINGS_DUPLEX = C.GTK_PRINT_SETTINGS_DUPLEX
const PRINT_SETTINGS_FINISHINGS = C.GTK_PRINT_SETTINGS_FINISHINGS
const PRINT_SETTINGS_MEDIA_TYPE = C.GTK_PRINT_SETTINGS_MEDIA_TYPE
const PRINT_SETTINGS_NUMBER_UP = C.GTK_PRINT_SETTINGS_NUMBER_UP
const PRINT_SETTINGS_NUMBER_UP_LAYOUT = C.GTK_PRINT_SETTINGS_NUMBER_UP_LAYOUT
const PRINT_SETTINGS_N_COPIES = C.GTK_PRINT_SETTINGS_N_COPIES
const PRINT_SETTINGS_ORIENTATION = C.GTK_PRINT_SETTINGS_ORIENTATION
const PRINT_SETTINGS_OUTPUT_BASENAME = C.GTK_PRINT_SETTINGS_OUTPUT_BASENAME
const PRINT_SETTINGS_OUTPUT_BIN = C.GTK_PRINT_SETTINGS_OUTPUT_BIN
const PRINT_SETTINGS_OUTPUT_DIR = C.GTK_PRINT_SETTINGS_OUTPUT_DIR
const PRINT_SETTINGS_OUTPUT_FILE_FORMAT = C.GTK_PRINT_SETTINGS_OUTPUT_FILE_FORMAT
const PRINT_SETTINGS_OUTPUT_URI = C.GTK_PRINT_SETTINGS_OUTPUT_URI
const PRINT_SETTINGS_PAGE_RANGES = C.GTK_PRINT_SETTINGS_PAGE_RANGES
const PRINT_SETTINGS_PAGE_SET = C.GTK_PRINT_SETTINGS_PAGE_SET
const PRINT_SETTINGS_PAPER_FORMAT = C.GTK_PRINT_SETTINGS_PAPER_FORMAT
const PRINT_SETTINGS_PAPER_HEIGHT = C.GTK_PRINT_SETTINGS_PAPER_HEIGHT
const PRINT_SETTINGS_PAPER_WIDTH = C.GTK_PRINT_SETTINGS_PAPER_WIDTH
const PRINT_SETTINGS_PRINTER = C.GTK_PRINT_SETTINGS_PRINTER
const PRINT_SETTINGS_PRINTER_LPI = C.GTK_PRINT_SETTINGS_PRINTER_LPI
const PRINT_SETTINGS_PRINT_PAGES = C.GTK_PRINT_SETTINGS_PRINT_PAGES
const PRINT_SETTINGS_QUALITY = C.GTK_PRINT_SETTINGS_QUALITY
const PRINT_SETTINGS_RESOLUTION = C.GTK_PRINT_SETTINGS_RESOLUTION
const PRINT_SETTINGS_RESOLUTION_X = C.GTK_PRINT_SETTINGS_RESOLUTION_X
const PRINT_SETTINGS_RESOLUTION_Y = C.GTK_PRINT_SETTINGS_RESOLUTION_Y
const PRINT_SETTINGS_REVERSE = C.GTK_PRINT_SETTINGS_REVERSE
const PRINT_SETTINGS_SCALE = C.GTK_PRINT_SETTINGS_SCALE
const PRINT_SETTINGS_USE_COLOR = C.GTK_PRINT_SETTINGS_USE_COLOR
const PRINT_SETTINGS_WIN32_DRIVER_EXTRA = C.GTK_PRINT_SETTINGS_WIN32_DRIVER_EXTRA
const PRINT_SETTINGS_WIN32_DRIVER_VERSION = C.GTK_PRINT_SETTINGS_WIN32_DRIVER_VERSION
const PRIORITY_RESIZE = C.GTK_PRIORITY_RESIZE
const STOCK_ABOUT = C.GTK_STOCK_ABOUT
const STOCK_ADD = C.GTK_STOCK_ADD
const STOCK_APPLY = C.GTK_STOCK_APPLY
const STOCK_BOLD = C.GTK_STOCK_BOLD
const STOCK_CANCEL = C.GTK_STOCK_CANCEL
const STOCK_CAPS_LOCK_WARNING = C.GTK_STOCK_CAPS_LOCK_WARNING
const STOCK_CDROM = C.GTK_STOCK_CDROM
const STOCK_CLEAR = C.GTK_STOCK_CLEAR
const STOCK_CLOSE = C.GTK_STOCK_CLOSE
const STOCK_COLOR_PICKER = C.GTK_STOCK_COLOR_PICKER
const STOCK_CONNECT = C.GTK_STOCK_CONNECT
const STOCK_CONVERT = C.GTK_STOCK_CONVERT
const STOCK_COPY = C.GTK_STOCK_COPY
const STOCK_CUT = C.GTK_STOCK_CUT
const STOCK_DELETE = C.GTK_STOCK_DELETE
const STOCK_DIALOG_AUTHENTICATION = C.GTK_STOCK_DIALOG_AUTHENTICATION
const STOCK_DIALOG_ERROR = C.GTK_STOCK_DIALOG_ERROR
const STOCK_DIALOG_INFO = C.GTK_STOCK_DIALOG_INFO
const STOCK_DIALOG_QUESTION = C.GTK_STOCK_DIALOG_QUESTION
const STOCK_DIALOG_WARNING = C.GTK_STOCK_DIALOG_WARNING
const STOCK_DIRECTORY = C.GTK_STOCK_DIRECTORY
const STOCK_DISCARD = C.GTK_STOCK_DISCARD
const STOCK_DISCONNECT = C.GTK_STOCK_DISCONNECT
const STOCK_DND = C.GTK_STOCK_DND
const STOCK_DND_MULTIPLE = C.GTK_STOCK_DND_MULTIPLE
const STOCK_EDIT = C.GTK_STOCK_EDIT
const STOCK_EXECUTE = C.GTK_STOCK_EXECUTE
const STOCK_FILE = C.GTK_STOCK_FILE
const STOCK_FIND = C.GTK_STOCK_FIND
const STOCK_FIND_AND_REPLACE = C.GTK_STOCK_FIND_AND_REPLACE
const STOCK_FLOPPY = C.GTK_STOCK_FLOPPY
const STOCK_FULLSCREEN = C.GTK_STOCK_FULLSCREEN
const STOCK_GOTO_BOTTOM = C.GTK_STOCK_GOTO_BOTTOM
const STOCK_GOTO_FIRST = C.GTK_STOCK_GOTO_FIRST
const STOCK_GOTO_LAST = C.GTK_STOCK_GOTO_LAST
const STOCK_GOTO_TOP = C.GTK_STOCK_GOTO_TOP
const STOCK_GO_BACK = C.GTK_STOCK_GO_BACK
const STOCK_GO_DOWN = C.GTK_STOCK_GO_DOWN
const STOCK_GO_FORWARD = C.GTK_STOCK_GO_FORWARD
const STOCK_GO_UP = C.GTK_STOCK_GO_UP
const STOCK_HARDDISK = C.GTK_STOCK_HARDDISK
const STOCK_HELP = C.GTK_STOCK_HELP
const STOCK_HOME = C.GTK_STOCK_HOME
const STOCK_INDENT = C.GTK_STOCK_INDENT
const STOCK_INDEX = C.GTK_STOCK_INDEX
const STOCK_INFO = C.GTK_STOCK_INFO
const STOCK_ITALIC = C.GTK_STOCK_ITALIC
const STOCK_JUMP_TO = C.GTK_STOCK_JUMP_TO
const STOCK_JUSTIFY_CENTER = C.GTK_STOCK_JUSTIFY_CENTER
const STOCK_JUSTIFY_FILL = C.GTK_STOCK_JUSTIFY_FILL
const STOCK_JUSTIFY_LEFT = C.GTK_STOCK_JUSTIFY_LEFT
const STOCK_JUSTIFY_RIGHT = C.GTK_STOCK_JUSTIFY_RIGHT
const STOCK_LEAVE_FULLSCREEN = C.GTK_STOCK_LEAVE_FULLSCREEN
const STOCK_MEDIA_FORWARD = C.GTK_STOCK_MEDIA_FORWARD
const STOCK_MEDIA_NEXT = C.GTK_STOCK_MEDIA_NEXT
const STOCK_MEDIA_PAUSE = C.GTK_STOCK_MEDIA_PAUSE
const STOCK_MEDIA_PLAY = C.GTK_STOCK_MEDIA_PLAY
const STOCK_MEDIA_PREVIOUS = C.GTK_STOCK_MEDIA_PREVIOUS
const STOCK_MEDIA_RECORD = C.GTK_STOCK_MEDIA_RECORD
const STOCK_MEDIA_REWIND = C.GTK_STOCK_MEDIA_REWIND
const STOCK_MEDIA_STOP = C.GTK_STOCK_MEDIA_STOP
const STOCK_MISSING_IMAGE = C.GTK_STOCK_MISSING_IMAGE
const STOCK_NETWORK = C.GTK_STOCK_NETWORK
const STOCK_NEW = C.GTK_STOCK_NEW
const STOCK_NO = C.GTK_STOCK_NO
const STOCK_OK = C.GTK_STOCK_OK
const STOCK_OPEN = C.GTK_STOCK_OPEN
const STOCK_ORIENTATION_LANDSCAPE = C.GTK_STOCK_ORIENTATION_LANDSCAPE
const STOCK_ORIENTATION_PORTRAIT = C.GTK_STOCK_ORIENTATION_PORTRAIT
const STOCK_ORIENTATION_REVERSE_LANDSCAPE = C.GTK_STOCK_ORIENTATION_REVERSE_LANDSCAPE
const STOCK_ORIENTATION_REVERSE_PORTRAIT = C.GTK_STOCK_ORIENTATION_REVERSE_PORTRAIT
const STOCK_PAGE_SETUP = C.GTK_STOCK_PAGE_SETUP
const STOCK_PASTE = C.GTK_STOCK_PASTE
const STOCK_PREFERENCES = C.GTK_STOCK_PREFERENCES
const STOCK_PRINT = C.GTK_STOCK_PRINT
const STOCK_PRINT_ERROR = C.GTK_STOCK_PRINT_ERROR
const STOCK_PRINT_PAUSED = C.GTK_STOCK_PRINT_PAUSED
const STOCK_PRINT_PREVIEW = C.GTK_STOCK_PRINT_PREVIEW
const STOCK_PRINT_REPORT = C.GTK_STOCK_PRINT_REPORT
const STOCK_PRINT_WARNING = C.GTK_STOCK_PRINT_WARNING
const STOCK_PROPERTIES = C.GTK_STOCK_PROPERTIES
const STOCK_QUIT = C.GTK_STOCK_QUIT
const STOCK_REDO = C.GTK_STOCK_REDO
const STOCK_REFRESH = C.GTK_STOCK_REFRESH
const STOCK_REMOVE = C.GTK_STOCK_REMOVE
const STOCK_REVERT_TO_SAVED = C.GTK_STOCK_REVERT_TO_SAVED
const STOCK_SAVE = C.GTK_STOCK_SAVE
const STOCK_SAVE_AS = C.GTK_STOCK_SAVE_AS
const STOCK_SELECT_ALL = C.GTK_STOCK_SELECT_ALL
const STOCK_SELECT_COLOR = C.GTK_STOCK_SELECT_COLOR
const STOCK_SELECT_FONT = C.GTK_STOCK_SELECT_FONT
const STOCK_SORT_ASCENDING = C.GTK_STOCK_SORT_ASCENDING
const STOCK_SORT_DESCENDING = C.GTK_STOCK_SORT_DESCENDING
const STOCK_SPELL_CHECK = C.GTK_STOCK_SPELL_CHECK
const STOCK_STOP = C.GTK_STOCK_STOP
const STOCK_STRIKETHROUGH = C.GTK_STOCK_STRIKETHROUGH
const STOCK_UNDELETE = C.GTK_STOCK_UNDELETE
const STOCK_UNDERLINE = C.GTK_STOCK_UNDERLINE
const STOCK_UNDO = C.GTK_STOCK_UNDO
const STOCK_UNINDENT = C.GTK_STOCK_UNINDENT
const STOCK_YES = C.GTK_STOCK_YES
const STOCK_ZOOM_100 = C.GTK_STOCK_ZOOM_100
const STOCK_ZOOM_FIT = C.GTK_STOCK_ZOOM_FIT
const STOCK_ZOOM_IN = C.GTK_STOCK_ZOOM_IN
const STOCK_ZOOM_OUT = C.GTK_STOCK_ZOOM_OUT
const STYLE_CLASS_ACCELERATOR = C.GTK_STYLE_CLASS_ACCELERATOR
const STYLE_CLASS_ARROW = C.GTK_STYLE_CLASS_ARROW
const STYLE_CLASS_BACKGROUND = C.GTK_STYLE_CLASS_BACKGROUND
const STYLE_CLASS_BOTTOM = C.GTK_STYLE_CLASS_BOTTOM
const STYLE_CLASS_BUTTON = C.GTK_STYLE_CLASS_BUTTON
const STYLE_CLASS_CALENDAR = C.GTK_STYLE_CLASS_CALENDAR
const STYLE_CLASS_CELL = C.GTK_STYLE_CLASS_CELL
const STYLE_CLASS_CHECK = C.GTK_STYLE_CLASS_CHECK
const STYLE_CLASS_COMBOBOX_ENTRY = C.GTK_STYLE_CLASS_COMBOBOX_ENTRY
const STYLE_CLASS_CURSOR_HANDLE = C.GTK_STYLE_CLASS_CURSOR_HANDLE
const STYLE_CLASS_DEFAULT = C.GTK_STYLE_CLASS_DEFAULT
const STYLE_CLASS_DIM_LABEL = C.GTK_STYLE_CLASS_DIM_LABEL
const STYLE_CLASS_DND = C.GTK_STYLE_CLASS_DND
const STYLE_CLASS_DOCK = C.GTK_STYLE_CLASS_DOCK
const STYLE_CLASS_ENTRY = C.GTK_STYLE_CLASS_ENTRY
const STYLE_CLASS_ERROR = C.GTK_STYLE_CLASS_ERROR
const STYLE_CLASS_EXPANDER = C.GTK_STYLE_CLASS_EXPANDER
const STYLE_CLASS_FRAME = C.GTK_STYLE_CLASS_FRAME
const STYLE_CLASS_GRIP = C.GTK_STYLE_CLASS_GRIP
const STYLE_CLASS_HEADER = C.GTK_STYLE_CLASS_HEADER
const STYLE_CLASS_HIGHLIGHT = C.GTK_STYLE_CLASS_HIGHLIGHT
const STYLE_CLASS_HORIZONTAL = C.GTK_STYLE_CLASS_HORIZONTAL
const STYLE_CLASS_IMAGE = C.GTK_STYLE_CLASS_IMAGE
const STYLE_CLASS_INFO = C.GTK_STYLE_CLASS_INFO
const STYLE_CLASS_INLINE_TOOLBAR = C.GTK_STYLE_CLASS_INLINE_TOOLBAR
const STYLE_CLASS_LEFT = C.GTK_STYLE_CLASS_LEFT
const STYLE_CLASS_LEVEL_BAR = C.GTK_STYLE_CLASS_LEVEL_BAR
const STYLE_CLASS_LINKED = C.GTK_STYLE_CLASS_LINKED
const STYLE_CLASS_MARK = C.GTK_STYLE_CLASS_MARK
const STYLE_CLASS_MENU = C.GTK_STYLE_CLASS_MENU
const STYLE_CLASS_MENUBAR = C.GTK_STYLE_CLASS_MENUBAR
const STYLE_CLASS_MENUITEM = C.GTK_STYLE_CLASS_MENUITEM
const STYLE_CLASS_NOTEBOOK = C.GTK_STYLE_CLASS_NOTEBOOK
const STYLE_CLASS_OSD = C.GTK_STYLE_CLASS_OSD
const STYLE_CLASS_PANE_SEPARATOR = C.GTK_STYLE_CLASS_PANE_SEPARATOR
const STYLE_CLASS_PRIMARY_TOOLBAR = C.GTK_STYLE_CLASS_PRIMARY_TOOLBAR
const STYLE_CLASS_PROGRESSBAR = C.GTK_STYLE_CLASS_PROGRESSBAR
const STYLE_CLASS_PULSE = C.GTK_STYLE_CLASS_PULSE
const STYLE_CLASS_QUESTION = C.GTK_STYLE_CLASS_QUESTION
const STYLE_CLASS_RADIO = C.GTK_STYLE_CLASS_RADIO
const STYLE_CLASS_RAISED = C.GTK_STYLE_CLASS_RAISED
const STYLE_CLASS_RIGHT = C.GTK_STYLE_CLASS_RIGHT
const STYLE_CLASS_RUBBERBAND = C.GTK_STYLE_CLASS_RUBBERBAND
const STYLE_CLASS_SCALE = C.GTK_STYLE_CLASS_SCALE
const STYLE_CLASS_SCALE_HAS_MARKS_ABOVE = C.GTK_STYLE_CLASS_SCALE_HAS_MARKS_ABOVE
const STYLE_CLASS_SCALE_HAS_MARKS_BELOW = C.GTK_STYLE_CLASS_SCALE_HAS_MARKS_BELOW
const STYLE_CLASS_SCROLLBAR = C.GTK_STYLE_CLASS_SCROLLBAR
const STYLE_CLASS_SCROLLBARS_JUNCTION = C.GTK_STYLE_CLASS_SCROLLBARS_JUNCTION
const STYLE_CLASS_SEPARATOR = C.GTK_STYLE_CLASS_SEPARATOR
const STYLE_CLASS_SIDEBAR = C.GTK_STYLE_CLASS_SIDEBAR
const STYLE_CLASS_SLIDER = C.GTK_STYLE_CLASS_SLIDER
const STYLE_CLASS_SPINBUTTON = C.GTK_STYLE_CLASS_SPINBUTTON
const STYLE_CLASS_SPINNER = C.GTK_STYLE_CLASS_SPINNER
const STYLE_CLASS_TOOLBAR = C.GTK_STYLE_CLASS_TOOLBAR
const STYLE_CLASS_TOOLTIP = C.GTK_STYLE_CLASS_TOOLTIP
const STYLE_CLASS_TOP = C.GTK_STYLE_CLASS_TOP
const STYLE_CLASS_TROUGH = C.GTK_STYLE_CLASS_TROUGH
const STYLE_CLASS_VERTICAL = C.GTK_STYLE_CLASS_VERTICAL
const STYLE_CLASS_VIEW = C.GTK_STYLE_CLASS_VIEW
const STYLE_CLASS_WARNING = C.GTK_STYLE_CLASS_WARNING
const STYLE_PROPERTY_BACKGROUND_COLOR = C.GTK_STYLE_PROPERTY_BACKGROUND_COLOR
const STYLE_PROPERTY_BACKGROUND_IMAGE = C.GTK_STYLE_PROPERTY_BACKGROUND_IMAGE
const STYLE_PROPERTY_BORDER_COLOR = C.GTK_STYLE_PROPERTY_BORDER_COLOR
const STYLE_PROPERTY_BORDER_RADIUS = C.GTK_STYLE_PROPERTY_BORDER_RADIUS
const STYLE_PROPERTY_BORDER_STYLE = C.GTK_STYLE_PROPERTY_BORDER_STYLE
const STYLE_PROPERTY_BORDER_WIDTH = C.GTK_STYLE_PROPERTY_BORDER_WIDTH
const STYLE_PROPERTY_COLOR = C.GTK_STYLE_PROPERTY_COLOR
const STYLE_PROPERTY_FONT = C.GTK_STYLE_PROPERTY_FONT
const STYLE_PROPERTY_MARGIN = C.GTK_STYLE_PROPERTY_MARGIN
const STYLE_PROPERTY_PADDING = C.GTK_STYLE_PROPERTY_PADDING
const STYLE_PROVIDER_PRIORITY_APPLICATION = C.GTK_STYLE_PROVIDER_PRIORITY_APPLICATION
const STYLE_PROVIDER_PRIORITY_FALLBACK = C.GTK_STYLE_PROVIDER_PRIORITY_FALLBACK
const STYLE_PROVIDER_PRIORITY_SETTINGS = C.GTK_STYLE_PROVIDER_PRIORITY_SETTINGS
const STYLE_PROVIDER_PRIORITY_THEME = C.GTK_STYLE_PROVIDER_PRIORITY_THEME
const STYLE_PROVIDER_PRIORITY_USER = C.GTK_STYLE_PROVIDER_PRIORITY_USER
const STYLE_REGION_COLUMN = C.GTK_STYLE_REGION_COLUMN
const STYLE_REGION_COLUMN_HEADER = C.GTK_STYLE_REGION_COLUMN_HEADER
const STYLE_REGION_ROW = C.GTK_STYLE_REGION_ROW
const STYLE_REGION_TAB = C.GTK_STYLE_REGION_TAB
const TEXT_VIEW_PRIORITY_VALIDATE = C.GTK_TEXT_VIEW_PRIORITY_VALIDATE
