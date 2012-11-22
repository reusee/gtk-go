package gtk

// #cgo pkg-config: gtk+-3.0 gobject-2.0
// #include <glib-object.h>
// #include <glib/gstdio.h>
// #include <glib-unix.h>
// #include <gtk/gtkx.h>
/*
typedef long double longdouble;
typedef GtkTreePath** _pp_GtkTreePath;
typedef const GtkIconSource* _const_p_GtkIconSource;
typedef GtkSettings* _p_GtkSettings;
typedef GtkWindow* _p_GtkWindow;
typedef PangoLayout* _p_PangoLayout;
typedef const gchar* _const_p_gchar;
typedef guint** _pp_guint;
typedef GtkPrintSettings* _p_GtkPrintSettings;
typedef GdkEvent* _p_GdkEvent;
typedef GdkWindow* _p_GdkWindow;
typedef char*** _ppp_char;
typedef GValue* _p_GValue;
typedef GObject* _p_GObject;
typedef gdouble* _p_gdouble;
typedef GtkTargetEntry* _p_GtkTargetEntry;
typedef GOptionGroup* _p_GOptionGroup;
typedef gchar* _p_gchar;
typedef GtkStockItem* _p_GtkStockItem;
typedef GError** _pp_GError;
typedef GdkPixbuf* _p_GdkPixbuf;
typedef GtkTreeModel** _pp_GtkTreeModel;
typedef const GString* _const_p_GString;
typedef cairo_t* _p_cairo_t;
typedef GtkTextBuffer* _p_GtkTextBuffer;
typedef GSList* _p_GSList;
typedef PangoLanguage* _p_PangoLanguage;
typedef GtkTargetList* _p_GtkTargetList;
typedef GtkBindingSet* _p_GtkBindingSet;
typedef GIcon* _p_GIcon;
typedef GtkSelectionData* _p_GtkSelectionData;
typedef gchar*** _ppp_gchar;
typedef GtkTreePath* _p_GtkTreePath;
typedef GtkPageSetup* _p_GtkPageSetup;
typedef gint* _p_gint;
typedef cairo_surface_t* _p_cairo_surface_t;
typedef GtkRequestedSize* _p_GtkRequestedSize;
typedef GdkDisplay* _p_GdkDisplay;
typedef guint* _p_guint;
typedef int* _p_int;
typedef GdkDragContext* _p_GdkDragContext;
typedef const GParamSpec* _const_p_GParamSpec;
typedef GdkModifierType* _p_GdkModifierType;
typedef GList* _p_GList;
typedef GOptionEntry* _p_GOptionEntry;
typedef GtkSpinButton* _p_GtkSpinButton;
typedef GdkAtom* _p_GdkAtom;
typedef GtkTreeModel* _p_GtkTreeModel;
typedef GType* _p_GType;
typedef GtkTreeIter* _p_GtkTreeIter;
typedef GdkEventKey* _p_GdkEventKey;
typedef GdkDevice* _p_GdkDevice;
typedef GtkWidget* _p_GtkWidget;
typedef GdkScreen* _p_GdkScreen;
typedef GtkStyleContext* _p_GtkStyleContext;
*/
import "C"

func AccelGroupsActivate(object C._p_GObject, accel_key C.guint, accel_mods C.GdkModifierType) C.gboolean {
	return C.gtk_accel_groups_activate(object, accel_key, accel_mods)
}

func AccelGroupsFromObject(object C._p_GObject) C._p_GSList {
	return C.gtk_accel_groups_from_object(object)
}

func AcceleratorGetDefaultModMask() C.GdkModifierType {
	return C.gtk_accelerator_get_default_mod_mask()
}

func AcceleratorGetLabel(accelerator_key C.guint, accelerator_mods C.GdkModifierType) C._p_gchar {
	return C.gtk_accelerator_get_label(accelerator_key, accelerator_mods)
}

func AcceleratorGetLabelWithKeycode(display C._p_GdkDisplay, accelerator_key C.guint, keycode C.guint, accelerator_mods C.GdkModifierType) C._p_gchar {
	return C.gtk_accelerator_get_label_with_keycode(display, accelerator_key, keycode, accelerator_mods)
}

func AcceleratorName(accelerator_key C.guint, accelerator_mods C.GdkModifierType) C._p_gchar {
	return C.gtk_accelerator_name(accelerator_key, accelerator_mods)
}

func AcceleratorNameWithKeycode(display C._p_GdkDisplay, accelerator_key C.guint, keycode C.guint, accelerator_mods C.GdkModifierType) C._p_gchar {
	return C.gtk_accelerator_name_with_keycode(display, accelerator_key, keycode, accelerator_mods)
}

func AcceleratorParse(accelerator C._const_p_gchar, accelerator_key C._p_guint, accelerator_mods C._p_GdkModifierType) {
	C.gtk_accelerator_parse(accelerator, accelerator_key, accelerator_mods)
}

func AcceleratorParseWithKeycode(accelerator C._const_p_gchar, accelerator_key C._p_guint, accelerator_codes C._pp_guint, accelerator_mods C._p_GdkModifierType) {
	C.gtk_accelerator_parse_with_keycode(accelerator, accelerator_key, accelerator_codes, accelerator_mods)
}

func AcceleratorSetDefaultModMask(default_mod_mask C.GdkModifierType) {
	C.gtk_accelerator_set_default_mod_mask(default_mod_mask)
}

func AcceleratorValid(keyval C.guint, modifiers C.GdkModifierType) C.gboolean {
	return C.gtk_accelerator_valid(keyval, modifiers)
}

func AlternativeDialogButtonOrder(screen C._p_GdkScreen) C.gboolean {
	return C.gtk_alternative_dialog_button_order(screen)
}

func BindingEntryAddSignalFromString(binding_set C._p_GtkBindingSet, signal_desc C._const_p_gchar) C.GTokenType {
	return C.gtk_binding_entry_add_signal_from_string(binding_set, signal_desc)
}

func BindingEntryAddSignall(binding_set C._p_GtkBindingSet, keyval C.guint, modifiers C.GdkModifierType, signal_name C._const_p_gchar, binding_args C._p_GSList) {
	C.gtk_binding_entry_add_signall(binding_set, keyval, modifiers, signal_name, binding_args)
}

func BindingEntryRemove(binding_set C._p_GtkBindingSet, keyval C.guint, modifiers C.GdkModifierType) {
	C.gtk_binding_entry_remove(binding_set, keyval, modifiers)
}

func BindingEntrySkip(binding_set C._p_GtkBindingSet, keyval C.guint, modifiers C.GdkModifierType) {
	C.gtk_binding_entry_skip(binding_set, keyval, modifiers)
}

func BindingSetByClass(object_class C.gpointer) C._p_GtkBindingSet {
	return C.gtk_binding_set_by_class(object_class)
}

func BindingSetFind(set_name C._const_p_gchar) C._p_GtkBindingSet {
	return C.gtk_binding_set_find(set_name)
}

func BindingSetNew(set_name C._const_p_gchar) C._p_GtkBindingSet {
	return C.gtk_binding_set_new(set_name)
}

func BindingsActivate(object C._p_GObject, keyval C.guint, modifiers C.GdkModifierType) C.gboolean {
	return C.gtk_bindings_activate(object, keyval, modifiers)
}

func BindingsActivateEvent(object C._p_GObject, event C._p_GdkEventKey) C.gboolean {
	return C.gtk_bindings_activate_event(object, event)
}

func BuilderErrorQuark() C.GQuark {
	return C.gtk_builder_error_quark()
}

func CairoShouldDrawWindow(cr C._p_cairo_t, window C._p_GdkWindow) C.gboolean {
	return C.gtk_cairo_should_draw_window(cr, window)
}

func CairoTransformToWindow(cr C._p_cairo_t, widget C._p_GtkWidget, window C._p_GdkWindow) {
	C.gtk_cairo_transform_to_window(cr, widget, window)
}

func CheckVersion(required_major C.guint, required_minor C.guint, required_micro C.guint) C._const_p_gchar {
	return C.gtk_check_version(required_major, required_minor, required_micro)
}

func CssProviderErrorQuark() C.GQuark {
	return C.gtk_css_provider_error_quark()
}

func DeviceGrabAdd(widget C._p_GtkWidget, device C._p_GdkDevice, block_others C.gboolean) {
	C.gtk_device_grab_add(widget, device, block_others)
}

func DeviceGrabRemove(widget C._p_GtkWidget, device C._p_GdkDevice) {
	C.gtk_device_grab_remove(widget, device)
}

func DisableSetlocale() {
	C.gtk_disable_setlocale()
}

func DistributeNaturalAllocation(extra_space C.gint, n_requested_sizes C.guint, sizes C._p_GtkRequestedSize) C.gint {
	return C.gtk_distribute_natural_allocation(extra_space, n_requested_sizes, sizes)
}

func DragFinish(context C._p_GdkDragContext, success C.gboolean, del C.gboolean, time_ C.guint32) {
	C.gtk_drag_finish(context, success, del, time_)
}

func DragGetSourceWidget(context C._p_GdkDragContext) C._p_GtkWidget {
	return C.gtk_drag_get_source_widget(context)
}

func DragSetIconDefault(context C._p_GdkDragContext) {
	C.gtk_drag_set_icon_default(context)
}

func DragSetIconGicon(context C._p_GdkDragContext, icon C._p_GIcon, hot_x C.gint, hot_y C.gint) {
	C.gtk_drag_set_icon_gicon(context, icon, hot_x, hot_y)
}

func DragSetIconName(context C._p_GdkDragContext, icon_name C._const_p_gchar, hot_x C.gint, hot_y C.gint) {
	C.gtk_drag_set_icon_name(context, icon_name, hot_x, hot_y)
}

func DragSetIconPixbuf(context C._p_GdkDragContext, pixbuf C._p_GdkPixbuf, hot_x C.gint, hot_y C.gint) {
	C.gtk_drag_set_icon_pixbuf(context, pixbuf, hot_x, hot_y)
}

func DragSetIconStock(context C._p_GdkDragContext, stock_id C._const_p_gchar, hot_x C.gint, hot_y C.gint) {
	C.gtk_drag_set_icon_stock(context, stock_id, hot_x, hot_y)
}

func DragSetIconSurface(context C._p_GdkDragContext, surface C._p_cairo_surface_t) {
	C.gtk_drag_set_icon_surface(context, surface)
}

func DragSetIconWidget(context C._p_GdkDragContext, widget C._p_GtkWidget, hot_x C.gint, hot_y C.gint) {
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

func GetCurrentEvent() C._p_GdkEvent {
	return C.gtk_get_current_event()
}

func GetCurrentEventDevice() C._p_GdkDevice {
	return C.gtk_get_current_event_device()
}

func GetCurrentEventState(state C._p_GdkModifierType) C.gboolean {
	return C.gtk_get_current_event_state(state)
}

func GetCurrentEventTime() C.guint32 {
	return C.gtk_get_current_event_time()
}

func GetDebugFlags() C.guint {
	return C.gtk_get_debug_flags()
}

func GetDefaultLanguage() C._p_PangoLanguage {
	return C.gtk_get_default_language()
}

func GetEventWidget(event C._p_GdkEvent) C._p_GtkWidget {
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

func GetOptionGroup(open_default_display C.gboolean) C._p_GOptionGroup {
	return C.gtk_get_option_group(open_default_display)
}

func GrabGetCurrent() C._p_GtkWidget {
	return C.gtk_grab_get_current()
}

func IconSizeFromName(name C._const_p_gchar) C.GtkIconSize {
	return C.gtk_icon_size_from_name(name)
}

func IconSizeGetName(size C.GtkIconSize) C._const_p_gchar {
	return C.gtk_icon_size_get_name(size)
}

func IconSizeLookup(size C.GtkIconSize, width C._p_gint, height C._p_gint) C.gboolean {
	return C.gtk_icon_size_lookup(size, width, height)
}

func IconSizeLookupForSettings(settings C._p_GtkSettings, size C.GtkIconSize, width C._p_gint, height C._p_gint) C.gboolean {
	return C.gtk_icon_size_lookup_for_settings(settings, size, width, height)
}

func IconSizeRegister(name C._const_p_gchar, width C.gint, height C.gint) C.GtkIconSize {
	return C.gtk_icon_size_register(name, width, height)
}

func IconSizeRegisterAlias(alias C._const_p_gchar, target C.GtkIconSize) {
	C.gtk_icon_size_register_alias(alias, target)
}

func IconThemeErrorQuark() C.GQuark {
	return C.gtk_icon_theme_error_quark()
}

func Init(argc C._p_int, argv C._ppp_char) {
	C.gtk_init(argc, argv)
}

func InitCheck(argc C._p_int, argv C._ppp_char) C.gboolean {
	return C.gtk_init_check(argc, argv)
}

func InitWithArgs(argc C._p_gint, argv C._ppp_gchar, parameter_string C._const_p_gchar, entries C._p_GOptionEntry, translation_domain C._const_p_gchar, err C._pp_GError) C.gboolean {
	return C.gtk_init_with_args(argc, argv, parameter_string, entries, translation_domain, err)
}

//Deprecated gtk_key_snooper_install

//Deprecated gtk_key_snooper_remove

func Main() {
	C.gtk_main()
}

func MainDoEvent(event C._p_GdkEvent) {
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

func PaperSizeGetDefault() C._const_p_gchar {
	return C.gtk_paper_size_get_default()
}

func PaperSizeGetPaperSizes(include_custom C.gboolean) C._p_GList {
	return C.gtk_paper_size_get_paper_sizes(include_custom)
}

func ParseArgs(argc C._p_int, argv C._ppp_char) C.gboolean {
	return C.gtk_parse_args(argc, argv)
}

func PrintErrorQuark() C.GQuark {
	return C.gtk_print_error_quark()
}

func PrintRunPageSetupDialog(parent C._p_GtkWindow, page_setup C._p_GtkPageSetup, settings C._p_GtkPrintSettings) C._p_GtkPageSetup {
	return C.gtk_print_run_page_setup_dialog(parent, page_setup, settings)
}

func PrintRunPageSetupDialogAsync(parent C._p_GtkWindow, page_setup C._p_GtkPageSetup, settings C._p_GtkPrintSettings, done_cb C.GtkPageSetupDoneFunc, data C.gpointer) {
	C.gtk_print_run_page_setup_dialog_async(parent, page_setup, settings, done_cb, data)
}

func PropagateEvent(widget C._p_GtkWidget, event C._p_GdkEvent) {
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

func RcPropertyParseBorder(pspec C._const_p_GParamSpec, gstring C._const_p_GString, property_value C._p_GValue) C.gboolean {
	return C.gtk_rc_property_parse_border(pspec, gstring, property_value)
}

func RcPropertyParseColor(pspec C._const_p_GParamSpec, gstring C._const_p_GString, property_value C._p_GValue) C.gboolean {
	return C.gtk_rc_property_parse_color(pspec, gstring, property_value)
}

func RcPropertyParseEnum(pspec C._const_p_GParamSpec, gstring C._const_p_GString, property_value C._p_GValue) C.gboolean {
	return C.gtk_rc_property_parse_enum(pspec, gstring, property_value)
}

func RcPropertyParseFlags(pspec C._const_p_GParamSpec, gstring C._const_p_GString, property_value C._p_GValue) C.gboolean {
	return C.gtk_rc_property_parse_flags(pspec, gstring, property_value)
}

func RcPropertyParseRequisition(pspec C._const_p_GParamSpec, gstring C._const_p_GString, property_value C._p_GValue) C.gboolean {
	return C.gtk_rc_property_parse_requisition(pspec, gstring, property_value)
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

func RenderActivity(context C._p_GtkStyleContext, cr C._p_cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_activity(context, cr, x, y, width, height)
}

func RenderArrow(context C._p_GtkStyleContext, cr C._p_cairo_t, angle C.gdouble, x C.gdouble, y C.gdouble, size C.gdouble) {
	C.gtk_render_arrow(context, cr, angle, x, y, size)
}

func RenderBackground(context C._p_GtkStyleContext, cr C._p_cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_background(context, cr, x, y, width, height)
}

func RenderCheck(context C._p_GtkStyleContext, cr C._p_cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_check(context, cr, x, y, width, height)
}

func RenderExpander(context C._p_GtkStyleContext, cr C._p_cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_expander(context, cr, x, y, width, height)
}

func RenderExtension(context C._p_GtkStyleContext, cr C._p_cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble, gap_side C.GtkPositionType) {
	C.gtk_render_extension(context, cr, x, y, width, height, gap_side)
}

func RenderFocus(context C._p_GtkStyleContext, cr C._p_cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_focus(context, cr, x, y, width, height)
}

func RenderFrame(context C._p_GtkStyleContext, cr C._p_cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_frame(context, cr, x, y, width, height)
}

func RenderFrameGap(context C._p_GtkStyleContext, cr C._p_cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble, gap_side C.GtkPositionType, xy0_gap C.gdouble, xy1_gap C.gdouble) {
	C.gtk_render_frame_gap(context, cr, x, y, width, height, gap_side, xy0_gap, xy1_gap)
}

func RenderHandle(context C._p_GtkStyleContext, cr C._p_cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_handle(context, cr, x, y, width, height)
}

func RenderIcon(context C._p_GtkStyleContext, cr C._p_cairo_t, pixbuf C._p_GdkPixbuf, x C.gdouble, y C.gdouble) {
	C.gtk_render_icon(context, cr, pixbuf, x, y)
}

func RenderIconPixbuf(context C._p_GtkStyleContext, source C._const_p_GtkIconSource, size C.GtkIconSize) C._p_GdkPixbuf {
	return C.gtk_render_icon_pixbuf(context, source, size)
}

func RenderInsertionCursor(context C._p_GtkStyleContext, cr C._p_cairo_t, x C.gdouble, y C.gdouble, layout C._p_PangoLayout, index C.int, direction C.PangoDirection) {
	C.gtk_render_insertion_cursor(context, cr, x, y, layout, index, direction)
}

func RenderLayout(context C._p_GtkStyleContext, cr C._p_cairo_t, x C.gdouble, y C.gdouble, layout C._p_PangoLayout) {
	C.gtk_render_layout(context, cr, x, y, layout)
}

func RenderLine(context C._p_GtkStyleContext, cr C._p_cairo_t, x0 C.gdouble, y0 C.gdouble, x1 C.gdouble, y1 C.gdouble) {
	C.gtk_render_line(context, cr, x0, y0, x1, y1)
}

func RenderOption(context C._p_GtkStyleContext, cr C._p_cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble) {
	C.gtk_render_option(context, cr, x, y, width, height)
}

func RenderSlider(context C._p_GtkStyleContext, cr C._p_cairo_t, x C.gdouble, y C.gdouble, width C.gdouble, height C.gdouble, orientation C.GtkOrientation) {
	C.gtk_render_slider(context, cr, x, y, width, height, orientation)
}

func RgbToHsv(r C.gdouble, g C.gdouble, b C.gdouble, h C._p_gdouble, s C._p_gdouble, v C._p_gdouble) {
	C.gtk_rgb_to_hsv(r, g, b, h, s, v)
}

func SelectionAddTarget(widget C._p_GtkWidget, selection C.GdkAtom, target C.GdkAtom, info C.guint) {
	C.gtk_selection_add_target(widget, selection, target, info)
}

func SelectionAddTargets(widget C._p_GtkWidget, selection C.GdkAtom, targets C._p_GtkTargetEntry, ntargets C.guint) {
	C.gtk_selection_add_targets(widget, selection, targets, ntargets)
}

func SelectionClearTargets(widget C._p_GtkWidget, selection C.GdkAtom) {
	C.gtk_selection_clear_targets(widget, selection)
}

func SelectionConvert(widget C._p_GtkWidget, selection C.GdkAtom, target C.GdkAtom, time_ C.guint32) C.gboolean {
	return C.gtk_selection_convert(widget, selection, target, time_)
}

func SelectionOwnerSet(widget C._p_GtkWidget, selection C.GdkAtom, time_ C.guint32) C.gboolean {
	return C.gtk_selection_owner_set(widget, selection, time_)
}

func SelectionOwnerSetForDisplay(display C._p_GdkDisplay, widget C._p_GtkWidget, selection C.GdkAtom, time_ C.guint32) C.gboolean {
	return C.gtk_selection_owner_set_for_display(display, widget, selection, time_)
}

func SelectionRemoveAll(widget C._p_GtkWidget) {
	C.gtk_selection_remove_all(widget)
}

func SetDebugFlags(flags C.guint) {
	C.gtk_set_debug_flags(flags)
}

//TODO varargs gtk_show_about_dialog

func ShowUri(screen C._p_GdkScreen, uri C._const_p_gchar, timestamp C.guint32, err C._pp_GError) C.gboolean {
	return C.gtk_show_uri(screen, uri, timestamp, err)
}

func StockAdd(items C._p_GtkStockItem, n_items C.guint) {
	C.gtk_stock_add(items, n_items)
}

func StockAddStatic(items C._p_GtkStockItem, n_items C.guint) {
	C.gtk_stock_add_static(items, n_items)
}

func StockListIds() C._p_GSList {
	return C.gtk_stock_list_ids()
}

func StockLookup(stock_id C._const_p_gchar, item C._p_GtkStockItem) C.gboolean {
	return C.gtk_stock_lookup(stock_id, item)
}

func StockSetTranslateFunc(domain C._const_p_gchar, _func C.GtkTranslateFunc, data C.gpointer, notify C.GDestroyNotify) {
	C.gtk_stock_set_translate_func(domain, _func, data, notify)
}

func TargetTableFree(targets C._p_GtkTargetEntry, n_targets C.gint) {
	C.gtk_target_table_free(targets, n_targets)
}

func TargetTableNewFromList(list C._p_GtkTargetList, n_targets C._p_gint) C._p_GtkTargetEntry {
	return C.gtk_target_table_new_from_list(list, n_targets)
}

func TargetsIncludeImage(targets C._p_GdkAtom, n_targets C.gint, writable C.gboolean) C.gboolean {
	return C.gtk_targets_include_image(targets, n_targets, writable)
}

func TargetsIncludeRichText(targets C._p_GdkAtom, n_targets C.gint, buffer C._p_GtkTextBuffer) C.gboolean {
	return C.gtk_targets_include_rich_text(targets, n_targets, buffer)
}

func TargetsIncludeText(targets C._p_GdkAtom, n_targets C.gint) C.gboolean {
	return C.gtk_targets_include_text(targets, n_targets)
}

func TargetsIncludeUri(targets C._p_GdkAtom, n_targets C.gint) C.gboolean {
	return C.gtk_targets_include_uri(targets, n_targets)
}

func TestCreateSimpleWindow(window_title C._const_p_gchar, dialog_text C._const_p_gchar) C._p_GtkWidget {
	return C.gtk_test_create_simple_window(window_title, dialog_text)
}

//TODO varargs gtk_test_create_widget

//TODO varargs gtk_test_display_button_window

func TestFindLabel(widget C._p_GtkWidget, label_pattern C._const_p_gchar) C._p_GtkWidget {
	return C.gtk_test_find_label(widget, label_pattern)
}

func TestFindSibling(base_widget C._p_GtkWidget, widget_type C.GType) C._p_GtkWidget {
	return C.gtk_test_find_sibling(base_widget, widget_type)
}

func TestFindWidget(widget C._p_GtkWidget, label_pattern C._const_p_gchar, widget_type C.GType) C._p_GtkWidget {
	return C.gtk_test_find_widget(widget, label_pattern, widget_type)
}

//TODO varargs gtk_test_init

func TestListAllTypes(n_types C._p_guint) C._p_GType {
	return C.gtk_test_list_all_types(n_types)
}

func TestRegisterAllTypes() {
	C.gtk_test_register_all_types()
}

func TestSliderGetValue(widget C._p_GtkWidget) C.double {
	return C.gtk_test_slider_get_value(widget)
}

func TestSliderSetPerc(widget C._p_GtkWidget, percentage C.double) {
	C.gtk_test_slider_set_perc(widget, percentage)
}

func TestSpinButtonClick(spinner C._p_GtkSpinButton, button C.guint, upwards C.gboolean) C.gboolean {
	return C.gtk_test_spin_button_click(spinner, button, upwards)
}

func TestTextGet(widget C._p_GtkWidget) C._p_gchar {
	return C.gtk_test_text_get(widget)
}

func TestTextSet(widget C._p_GtkWidget, string C._const_p_gchar) {
	C.gtk_test_text_set(widget, string)
}

func TestWidgetClick(widget C._p_GtkWidget, button C.guint, modifiers C.GdkModifierType) C.gboolean {
	return C.gtk_test_widget_click(widget, button, modifiers)
}

func TestWidgetSendKey(widget C._p_GtkWidget, keyval C.guint, modifiers C.GdkModifierType) C.gboolean {
	return C.gtk_test_widget_send_key(widget, keyval, modifiers)
}

func TreeGetRowDragData(selection_data C._p_GtkSelectionData, tree_model C._pp_GtkTreeModel, path C._pp_GtkTreePath) C.gboolean {
	return C.gtk_tree_get_row_drag_data(selection_data, tree_model, path)
}

func TreeRowReferenceDeleted(proxy C._p_GObject, path C._p_GtkTreePath) {
	C.gtk_tree_row_reference_deleted(proxy, path)
}

func TreeRowReferenceInserted(proxy C._p_GObject, path C._p_GtkTreePath) {
	C.gtk_tree_row_reference_inserted(proxy, path)
}

func TreeRowReferenceReordered(proxy C._p_GObject, path C._p_GtkTreePath, iter C._p_GtkTreeIter, new_order C._p_gint) {
	C.gtk_tree_row_reference_reordered(proxy, path, iter, new_order)
}

func TreeSetRowDragData(selection_data C._p_GtkSelectionData, tree_model C._p_GtkTreeModel, path C._p_GtkTreePath) C.gboolean {
	return C.gtk_tree_set_row_drag_data(selection_data, tree_model, path)
}

func True() C.gboolean {
	return C.gtk_true()
}

const (
	ALIGN_FILL = C.GTK_ALIGN_FILL
	ALIGN_START = C.GTK_ALIGN_START
	ALIGN_END = C.GTK_ALIGN_END
	ALIGN_CENTER = C.GTK_ALIGN_CENTER
	ARROWS_BOTH = C.GTK_ARROWS_BOTH
	ARROWS_START = C.GTK_ARROWS_START
	ARROWS_END = C.GTK_ARROWS_END
	ARROW_UP = C.GTK_ARROW_UP
	ARROW_DOWN = C.GTK_ARROW_DOWN
	ARROW_LEFT = C.GTK_ARROW_LEFT
	ARROW_RIGHT = C.GTK_ARROW_RIGHT
	ARROW_NONE = C.GTK_ARROW_NONE
	ASSISTANT_PAGE_CONTENT = C.GTK_ASSISTANT_PAGE_CONTENT
	ASSISTANT_PAGE_INTRO = C.GTK_ASSISTANT_PAGE_INTRO
	ASSISTANT_PAGE_CONFIRM = C.GTK_ASSISTANT_PAGE_CONFIRM
	ASSISTANT_PAGE_SUMMARY = C.GTK_ASSISTANT_PAGE_SUMMARY
	ASSISTANT_PAGE_PROGRESS = C.GTK_ASSISTANT_PAGE_PROGRESS
	ASSISTANT_PAGE_CUSTOM = C.GTK_ASSISTANT_PAGE_CUSTOM
	BORDER_STYLE_NONE = C.GTK_BORDER_STYLE_NONE
	BORDER_STYLE_SOLID = C.GTK_BORDER_STYLE_SOLID
	BORDER_STYLE_INSET = C.GTK_BORDER_STYLE_INSET
	BORDER_STYLE_OUTSET = C.GTK_BORDER_STYLE_OUTSET
	BORDER_STYLE_HIDDEN = C.GTK_BORDER_STYLE_HIDDEN
	BORDER_STYLE_DOTTED = C.GTK_BORDER_STYLE_DOTTED
	BORDER_STYLE_DASHED = C.GTK_BORDER_STYLE_DASHED
	BORDER_STYLE_DOUBLE = C.GTK_BORDER_STYLE_DOUBLE
	BORDER_STYLE_GROOVE = C.GTK_BORDER_STYLE_GROOVE
	BORDER_STYLE_RIDGE = C.GTK_BORDER_STYLE_RIDGE
	BUILDER_ERROR_INVALID_TYPE_FUNCTION = C.GTK_BUILDER_ERROR_INVALID_TYPE_FUNCTION
	BUILDER_ERROR_UNHANDLED_TAG = C.GTK_BUILDER_ERROR_UNHANDLED_TAG
	BUILDER_ERROR_MISSING_ATTRIBUTE = C.GTK_BUILDER_ERROR_MISSING_ATTRIBUTE
	BUILDER_ERROR_INVALID_ATTRIBUTE = C.GTK_BUILDER_ERROR_INVALID_ATTRIBUTE
	BUILDER_ERROR_INVALID_TAG = C.GTK_BUILDER_ERROR_INVALID_TAG
	BUILDER_ERROR_MISSING_PROPERTY_VALUE = C.GTK_BUILDER_ERROR_MISSING_PROPERTY_VALUE
	BUILDER_ERROR_INVALID_VALUE = C.GTK_BUILDER_ERROR_INVALID_VALUE
	BUILDER_ERROR_VERSION_MISMATCH = C.GTK_BUILDER_ERROR_VERSION_MISMATCH
	BUILDER_ERROR_DUPLICATE_ID = C.GTK_BUILDER_ERROR_DUPLICATE_ID
	BUTTONBOX_SPREAD = C.GTK_BUTTONBOX_SPREAD
	BUTTONBOX_EDGE = C.GTK_BUTTONBOX_EDGE
	BUTTONBOX_START = C.GTK_BUTTONBOX_START
	BUTTONBOX_END = C.GTK_BUTTONBOX_END
	BUTTONBOX_CENTER = C.GTK_BUTTONBOX_CENTER
	BUTTONS_NONE = C.GTK_BUTTONS_NONE
	BUTTONS_OK = C.GTK_BUTTONS_OK
	BUTTONS_CLOSE = C.GTK_BUTTONS_CLOSE
	BUTTONS_CANCEL = C.GTK_BUTTONS_CANCEL
	BUTTONS_YES_NO = C.GTK_BUTTONS_YES_NO
	BUTTONS_OK_CANCEL = C.GTK_BUTTONS_OK_CANCEL
	CELL_RENDERER_ACCEL_MODE_GTK = C.GTK_CELL_RENDERER_ACCEL_MODE_GTK
	CELL_RENDERER_ACCEL_MODE_OTHER = C.GTK_CELL_RENDERER_ACCEL_MODE_OTHER
	CELL_RENDERER_MODE_INERT = C.GTK_CELL_RENDERER_MODE_INERT
	CELL_RENDERER_MODE_ACTIVATABLE = C.GTK_CELL_RENDERER_MODE_ACTIVATABLE
	CELL_RENDERER_MODE_EDITABLE = C.GTK_CELL_RENDERER_MODE_EDITABLE
	CORNER_TOP_LEFT = C.GTK_CORNER_TOP_LEFT
	CORNER_BOTTOM_LEFT = C.GTK_CORNER_BOTTOM_LEFT
	CORNER_TOP_RIGHT = C.GTK_CORNER_TOP_RIGHT
	CORNER_BOTTOM_RIGHT = C.GTK_CORNER_BOTTOM_RIGHT
	CSS_PROVIDER_ERROR_FAILED = C.GTK_CSS_PROVIDER_ERROR_FAILED
	CSS_PROVIDER_ERROR_SYNTAX = C.GTK_CSS_PROVIDER_ERROR_SYNTAX
	CSS_PROVIDER_ERROR_IMPORT = C.GTK_CSS_PROVIDER_ERROR_IMPORT
	CSS_PROVIDER_ERROR_NAME = C.GTK_CSS_PROVIDER_ERROR_NAME
	CSS_PROVIDER_ERROR_DEPRECATED = C.GTK_CSS_PROVIDER_ERROR_DEPRECATED
	CSS_PROVIDER_ERROR_UNKNOWN_VALUE = C.GTK_CSS_PROVIDER_ERROR_UNKNOWN_VALUE
	CSS_SECTION_DOCUMENT = C.GTK_CSS_SECTION_DOCUMENT
	CSS_SECTION_IMPORT = C.GTK_CSS_SECTION_IMPORT
	CSS_SECTION_COLOR_DEFINITION = C.GTK_CSS_SECTION_COLOR_DEFINITION
	CSS_SECTION_BINDING_SET = C.GTK_CSS_SECTION_BINDING_SET
	CSS_SECTION_RULESET = C.GTK_CSS_SECTION_RULESET
	CSS_SECTION_SELECTOR = C.GTK_CSS_SECTION_SELECTOR
	CSS_SECTION_DECLARATION = C.GTK_CSS_SECTION_DECLARATION
	CSS_SECTION_VALUE = C.GTK_CSS_SECTION_VALUE
	CSS_SECTION_KEYFRAMES = C.GTK_CSS_SECTION_KEYFRAMES
	DELETE_CHARS = C.GTK_DELETE_CHARS
	DELETE_WORD_ENDS = C.GTK_DELETE_WORD_ENDS
	DELETE_WORDS = C.GTK_DELETE_WORDS
	DELETE_DISPLAY_LINES = C.GTK_DELETE_DISPLAY_LINES
	DELETE_DISPLAY_LINE_ENDS = C.GTK_DELETE_DISPLAY_LINE_ENDS
	DELETE_PARAGRAPH_ENDS = C.GTK_DELETE_PARAGRAPH_ENDS
	DELETE_PARAGRAPHS = C.GTK_DELETE_PARAGRAPHS
	DELETE_WHITESPACE = C.GTK_DELETE_WHITESPACE
	DIR_TAB_FORWARD = C.GTK_DIR_TAB_FORWARD
	DIR_TAB_BACKWARD = C.GTK_DIR_TAB_BACKWARD
	DIR_UP = C.GTK_DIR_UP
	DIR_DOWN = C.GTK_DIR_DOWN
	DIR_LEFT = C.GTK_DIR_LEFT
	DIR_RIGHT = C.GTK_DIR_RIGHT
	DRAG_RESULT_SUCCESS = C.GTK_DRAG_RESULT_SUCCESS
	DRAG_RESULT_NO_TARGET = C.GTK_DRAG_RESULT_NO_TARGET
	DRAG_RESULT_USER_CANCELLED = C.GTK_DRAG_RESULT_USER_CANCELLED
	DRAG_RESULT_TIMEOUT_EXPIRED = C.GTK_DRAG_RESULT_TIMEOUT_EXPIRED
	DRAG_RESULT_GRAB_BROKEN = C.GTK_DRAG_RESULT_GRAB_BROKEN
	DRAG_RESULT_ERROR = C.GTK_DRAG_RESULT_ERROR
	ENTRY_ICON_PRIMARY = C.GTK_ENTRY_ICON_PRIMARY
	ENTRY_ICON_SECONDARY = C.GTK_ENTRY_ICON_SECONDARY
	EXPANDER_COLLAPSED = C.GTK_EXPANDER_COLLAPSED
	EXPANDER_SEMI_COLLAPSED = C.GTK_EXPANDER_SEMI_COLLAPSED
	EXPANDER_SEMI_EXPANDED = C.GTK_EXPANDER_SEMI_EXPANDED
	EXPANDER_EXPANDED = C.GTK_EXPANDER_EXPANDED
	FILE_CHOOSER_ACTION_OPEN = C.GTK_FILE_CHOOSER_ACTION_OPEN
	FILE_CHOOSER_ACTION_SAVE = C.GTK_FILE_CHOOSER_ACTION_SAVE
	FILE_CHOOSER_ACTION_SELECT_FOLDER = C.GTK_FILE_CHOOSER_ACTION_SELECT_FOLDER
	FILE_CHOOSER_ACTION_CREATE_FOLDER = C.GTK_FILE_CHOOSER_ACTION_CREATE_FOLDER
	FILE_CHOOSER_CONFIRMATION_CONFIRM = C.GTK_FILE_CHOOSER_CONFIRMATION_CONFIRM
	FILE_CHOOSER_CONFIRMATION_ACCEPT_FILENAME = C.GTK_FILE_CHOOSER_CONFIRMATION_ACCEPT_FILENAME
	FILE_CHOOSER_CONFIRMATION_SELECT_AGAIN = C.GTK_FILE_CHOOSER_CONFIRMATION_SELECT_AGAIN
	FILE_CHOOSER_ERROR_NONEXISTENT = C.GTK_FILE_CHOOSER_ERROR_NONEXISTENT
	FILE_CHOOSER_ERROR_BAD_FILENAME = C.GTK_FILE_CHOOSER_ERROR_BAD_FILENAME
	FILE_CHOOSER_ERROR_ALREADY_EXISTS = C.GTK_FILE_CHOOSER_ERROR_ALREADY_EXISTS
	FILE_CHOOSER_ERROR_INCOMPLETE_HOSTNAME = C.GTK_FILE_CHOOSER_ERROR_INCOMPLETE_HOSTNAME
	IM_PREEDIT_NOTHING = C.GTK_IM_PREEDIT_NOTHING
	IM_PREEDIT_CALLBACK = C.GTK_IM_PREEDIT_CALLBACK
	IM_PREEDIT_NONE = C.GTK_IM_PREEDIT_NONE
	IM_STATUS_NOTHING = C.GTK_IM_STATUS_NOTHING
	IM_STATUS_CALLBACK = C.GTK_IM_STATUS_CALLBACK
	IM_STATUS_NONE = C.GTK_IM_STATUS_NONE
	ICON_SIZE_INVALID = C.GTK_ICON_SIZE_INVALID
	ICON_SIZE_MENU = C.GTK_ICON_SIZE_MENU
	ICON_SIZE_SMALL_TOOLBAR = C.GTK_ICON_SIZE_SMALL_TOOLBAR
	ICON_SIZE_LARGE_TOOLBAR = C.GTK_ICON_SIZE_LARGE_TOOLBAR
	ICON_SIZE_BUTTON = C.GTK_ICON_SIZE_BUTTON
	ICON_SIZE_DND = C.GTK_ICON_SIZE_DND
	ICON_SIZE_DIALOG = C.GTK_ICON_SIZE_DIALOG
	ICON_THEME_NOT_FOUND = C.GTK_ICON_THEME_NOT_FOUND
	ICON_THEME_FAILED = C.GTK_ICON_THEME_FAILED
	ICON_VIEW_NO_DROP = C.GTK_ICON_VIEW_NO_DROP
	ICON_VIEW_DROP_INTO = C.GTK_ICON_VIEW_DROP_INTO
	ICON_VIEW_DROP_LEFT = C.GTK_ICON_VIEW_DROP_LEFT
	ICON_VIEW_DROP_RIGHT = C.GTK_ICON_VIEW_DROP_RIGHT
	ICON_VIEW_DROP_ABOVE = C.GTK_ICON_VIEW_DROP_ABOVE
	ICON_VIEW_DROP_BELOW = C.GTK_ICON_VIEW_DROP_BELOW
	IMAGE_EMPTY = C.GTK_IMAGE_EMPTY
	IMAGE_PIXBUF = C.GTK_IMAGE_PIXBUF
	IMAGE_STOCK = C.GTK_IMAGE_STOCK
	IMAGE_ICON_SET = C.GTK_IMAGE_ICON_SET
	IMAGE_ANIMATION = C.GTK_IMAGE_ANIMATION
	IMAGE_ICON_NAME = C.GTK_IMAGE_ICON_NAME
	IMAGE_GICON = C.GTK_IMAGE_GICON
	INPUT_PURPOSE_FREE_FORM = C.GTK_INPUT_PURPOSE_FREE_FORM
	INPUT_PURPOSE_ALPHA = C.GTK_INPUT_PURPOSE_ALPHA
	INPUT_PURPOSE_DIGITS = C.GTK_INPUT_PURPOSE_DIGITS
	INPUT_PURPOSE_NUMBER = C.GTK_INPUT_PURPOSE_NUMBER
	INPUT_PURPOSE_PHONE = C.GTK_INPUT_PURPOSE_PHONE
	INPUT_PURPOSE_URL = C.GTK_INPUT_PURPOSE_URL
	INPUT_PURPOSE_EMAIL = C.GTK_INPUT_PURPOSE_EMAIL
	INPUT_PURPOSE_NAME = C.GTK_INPUT_PURPOSE_NAME
	INPUT_PURPOSE_PASSWORD = C.GTK_INPUT_PURPOSE_PASSWORD
	INPUT_PURPOSE_PIN = C.GTK_INPUT_PURPOSE_PIN
	JUSTIFY_LEFT = C.GTK_JUSTIFY_LEFT
	JUSTIFY_RIGHT = C.GTK_JUSTIFY_RIGHT
	JUSTIFY_CENTER = C.GTK_JUSTIFY_CENTER
	JUSTIFY_FILL = C.GTK_JUSTIFY_FILL
	LEVEL_BAR_MODE_CONTINUOUS = C.GTK_LEVEL_BAR_MODE_CONTINUOUS
	LEVEL_BAR_MODE_DISCRETE = C.GTK_LEVEL_BAR_MODE_DISCRETE
	LICENSE_UNKNOWN = C.GTK_LICENSE_UNKNOWN
	LICENSE_CUSTOM = C.GTK_LICENSE_CUSTOM
	LICENSE_GPL_2_0 = C.GTK_LICENSE_GPL_2_0
	LICENSE_GPL_3_0 = C.GTK_LICENSE_GPL_3_0
	LICENSE_LGPL_2_1 = C.GTK_LICENSE_LGPL_2_1
	LICENSE_LGPL_3_0 = C.GTK_LICENSE_LGPL_3_0
	LICENSE_BSD = C.GTK_LICENSE_BSD
	LICENSE_MIT_X11 = C.GTK_LICENSE_MIT_X11
	LICENSE_ARTISTIC = C.GTK_LICENSE_ARTISTIC
	MENU_DIR_PARENT = C.GTK_MENU_DIR_PARENT
	MENU_DIR_CHILD = C.GTK_MENU_DIR_CHILD
	MENU_DIR_NEXT = C.GTK_MENU_DIR_NEXT
	MENU_DIR_PREV = C.GTK_MENU_DIR_PREV
	MESSAGE_INFO = C.GTK_MESSAGE_INFO
	MESSAGE_WARNING = C.GTK_MESSAGE_WARNING
	MESSAGE_QUESTION = C.GTK_MESSAGE_QUESTION
	MESSAGE_ERROR = C.GTK_MESSAGE_ERROR
	MESSAGE_OTHER = C.GTK_MESSAGE_OTHER
	MOVEMENT_LOGICAL_POSITIONS = C.GTK_MOVEMENT_LOGICAL_POSITIONS
	MOVEMENT_VISUAL_POSITIONS = C.GTK_MOVEMENT_VISUAL_POSITIONS
	MOVEMENT_WORDS = C.GTK_MOVEMENT_WORDS
	MOVEMENT_DISPLAY_LINES = C.GTK_MOVEMENT_DISPLAY_LINES
	MOVEMENT_DISPLAY_LINE_ENDS = C.GTK_MOVEMENT_DISPLAY_LINE_ENDS
	MOVEMENT_PARAGRAPHS = C.GTK_MOVEMENT_PARAGRAPHS
	MOVEMENT_PARAGRAPH_ENDS = C.GTK_MOVEMENT_PARAGRAPH_ENDS
	MOVEMENT_PAGES = C.GTK_MOVEMENT_PAGES
	MOVEMENT_BUFFER_ENDS = C.GTK_MOVEMENT_BUFFER_ENDS
	MOVEMENT_HORIZONTAL_PAGES = C.GTK_MOVEMENT_HORIZONTAL_PAGES
	NOTEBOOK_TAB_FIRST = C.GTK_NOTEBOOK_TAB_FIRST
	NOTEBOOK_TAB_LAST = C.GTK_NOTEBOOK_TAB_LAST
	NUMBER_UP_LAYOUT_LEFT_TO_RIGHT_TOP_TO_BOTTOM = C.GTK_NUMBER_UP_LAYOUT_LEFT_TO_RIGHT_TOP_TO_BOTTOM
	NUMBER_UP_LAYOUT_LEFT_TO_RIGHT_BOTTOM_TO_TOP = C.GTK_NUMBER_UP_LAYOUT_LEFT_TO_RIGHT_BOTTOM_TO_TOP
	NUMBER_UP_LAYOUT_RIGHT_TO_LEFT_TOP_TO_BOTTOM = C.GTK_NUMBER_UP_LAYOUT_RIGHT_TO_LEFT_TOP_TO_BOTTOM
	NUMBER_UP_LAYOUT_RIGHT_TO_LEFT_BOTTOM_TO_TOP = C.GTK_NUMBER_UP_LAYOUT_RIGHT_TO_LEFT_BOTTOM_TO_TOP
	NUMBER_UP_LAYOUT_TOP_TO_BOTTOM_LEFT_TO_RIGHT = C.GTK_NUMBER_UP_LAYOUT_TOP_TO_BOTTOM_LEFT_TO_RIGHT
	NUMBER_UP_LAYOUT_TOP_TO_BOTTOM_RIGHT_TO_LEFT = C.GTK_NUMBER_UP_LAYOUT_TOP_TO_BOTTOM_RIGHT_TO_LEFT
	NUMBER_UP_LAYOUT_BOTTOM_TO_TOP_LEFT_TO_RIGHT = C.GTK_NUMBER_UP_LAYOUT_BOTTOM_TO_TOP_LEFT_TO_RIGHT
	NUMBER_UP_LAYOUT_BOTTOM_TO_TOP_RIGHT_TO_LEFT = C.GTK_NUMBER_UP_LAYOUT_BOTTOM_TO_TOP_RIGHT_TO_LEFT
	ORIENTATION_HORIZONTAL = C.GTK_ORIENTATION_HORIZONTAL
	ORIENTATION_VERTICAL = C.GTK_ORIENTATION_VERTICAL
	PACK_DIRECTION_LTR = C.GTK_PACK_DIRECTION_LTR
	PACK_DIRECTION_RTL = C.GTK_PACK_DIRECTION_RTL
	PACK_DIRECTION_TTB = C.GTK_PACK_DIRECTION_TTB
	PACK_DIRECTION_BTT = C.GTK_PACK_DIRECTION_BTT
	PACK_START = C.GTK_PACK_START
	PACK_END = C.GTK_PACK_END
	PAGE_ORIENTATION_PORTRAIT = C.GTK_PAGE_ORIENTATION_PORTRAIT
	PAGE_ORIENTATION_LANDSCAPE = C.GTK_PAGE_ORIENTATION_LANDSCAPE
	PAGE_ORIENTATION_REVERSE_PORTRAIT = C.GTK_PAGE_ORIENTATION_REVERSE_PORTRAIT
	PAGE_ORIENTATION_REVERSE_LANDSCAPE = C.GTK_PAGE_ORIENTATION_REVERSE_LANDSCAPE
	PAGE_SET_ALL = C.GTK_PAGE_SET_ALL
	PAGE_SET_EVEN = C.GTK_PAGE_SET_EVEN
	PAGE_SET_ODD = C.GTK_PAGE_SET_ODD
	PATH_PRIO_LOWEST = C.GTK_PATH_PRIO_LOWEST
	PATH_PRIO_GTK = C.GTK_PATH_PRIO_GTK
	PATH_PRIO_APPLICATION = C.GTK_PATH_PRIO_APPLICATION
	PATH_PRIO_THEME = C.GTK_PATH_PRIO_THEME
	PATH_PRIO_RC = C.GTK_PATH_PRIO_RC
	PATH_PRIO_HIGHEST = C.GTK_PATH_PRIO_HIGHEST
	PATH_WIDGET = C.GTK_PATH_WIDGET
	PATH_WIDGET_CLASS = C.GTK_PATH_WIDGET_CLASS
	PATH_CLASS = C.GTK_PATH_CLASS
	POLICY_ALWAYS = C.GTK_POLICY_ALWAYS
	POLICY_AUTOMATIC = C.GTK_POLICY_AUTOMATIC
	POLICY_NEVER = C.GTK_POLICY_NEVER
	POS_LEFT = C.GTK_POS_LEFT
	POS_RIGHT = C.GTK_POS_RIGHT
	POS_TOP = C.GTK_POS_TOP
	POS_BOTTOM = C.GTK_POS_BOTTOM
	PRINT_DUPLEX_SIMPLEX = C.GTK_PRINT_DUPLEX_SIMPLEX
	PRINT_DUPLEX_HORIZONTAL = C.GTK_PRINT_DUPLEX_HORIZONTAL
	PRINT_DUPLEX_VERTICAL = C.GTK_PRINT_DUPLEX_VERTICAL
	PRINT_ERROR_GENERAL = C.GTK_PRINT_ERROR_GENERAL
	PRINT_ERROR_INTERNAL_ERROR = C.GTK_PRINT_ERROR_INTERNAL_ERROR
	PRINT_ERROR_NOMEM = C.GTK_PRINT_ERROR_NOMEM
	PRINT_ERROR_INVALID_FILE = C.GTK_PRINT_ERROR_INVALID_FILE
	PRINT_OPERATION_ACTION_PRINT_DIALOG = C.GTK_PRINT_OPERATION_ACTION_PRINT_DIALOG
	PRINT_OPERATION_ACTION_PRINT = C.GTK_PRINT_OPERATION_ACTION_PRINT
	PRINT_OPERATION_ACTION_PREVIEW = C.GTK_PRINT_OPERATION_ACTION_PREVIEW
	PRINT_OPERATION_ACTION_EXPORT = C.GTK_PRINT_OPERATION_ACTION_EXPORT
	PRINT_OPERATION_RESULT_ERROR = C.GTK_PRINT_OPERATION_RESULT_ERROR
	PRINT_OPERATION_RESULT_APPLY = C.GTK_PRINT_OPERATION_RESULT_APPLY
	PRINT_OPERATION_RESULT_CANCEL = C.GTK_PRINT_OPERATION_RESULT_CANCEL
	PRINT_OPERATION_RESULT_IN_PROGRESS = C.GTK_PRINT_OPERATION_RESULT_IN_PROGRESS
	PRINT_PAGES_ALL = C.GTK_PRINT_PAGES_ALL
	PRINT_PAGES_CURRENT = C.GTK_PRINT_PAGES_CURRENT
	PRINT_PAGES_RANGES = C.GTK_PRINT_PAGES_RANGES
	PRINT_PAGES_SELECTION = C.GTK_PRINT_PAGES_SELECTION
	PRINT_QUALITY_LOW = C.GTK_PRINT_QUALITY_LOW
	PRINT_QUALITY_NORMAL = C.GTK_PRINT_QUALITY_NORMAL
	PRINT_QUALITY_HIGH = C.GTK_PRINT_QUALITY_HIGH
	PRINT_QUALITY_DRAFT = C.GTK_PRINT_QUALITY_DRAFT
	PRINT_STATUS_INITIAL = C.GTK_PRINT_STATUS_INITIAL
	PRINT_STATUS_PREPARING = C.GTK_PRINT_STATUS_PREPARING
	PRINT_STATUS_GENERATING_DATA = C.GTK_PRINT_STATUS_GENERATING_DATA
	PRINT_STATUS_SENDING_DATA = C.GTK_PRINT_STATUS_SENDING_DATA
	PRINT_STATUS_PENDING = C.GTK_PRINT_STATUS_PENDING
	PRINT_STATUS_PENDING_ISSUE = C.GTK_PRINT_STATUS_PENDING_ISSUE
	PRINT_STATUS_PRINTING = C.GTK_PRINT_STATUS_PRINTING
	PRINT_STATUS_FINISHED = C.GTK_PRINT_STATUS_FINISHED
	PRINT_STATUS_FINISHED_ABORTED = C.GTK_PRINT_STATUS_FINISHED_ABORTED
	RC_TOKEN_INVALID = C.GTK_RC_TOKEN_INVALID
	RC_TOKEN_INCLUDE = C.GTK_RC_TOKEN_INCLUDE
	RC_TOKEN_NORMAL = C.GTK_RC_TOKEN_NORMAL
	RC_TOKEN_ACTIVE = C.GTK_RC_TOKEN_ACTIVE
	RC_TOKEN_PRELIGHT = C.GTK_RC_TOKEN_PRELIGHT
	RC_TOKEN_SELECTED = C.GTK_RC_TOKEN_SELECTED
	RC_TOKEN_INSENSITIVE = C.GTK_RC_TOKEN_INSENSITIVE
	RC_TOKEN_FG = C.GTK_RC_TOKEN_FG
	RC_TOKEN_BG = C.GTK_RC_TOKEN_BG
	RC_TOKEN_TEXT = C.GTK_RC_TOKEN_TEXT
	RC_TOKEN_BASE = C.GTK_RC_TOKEN_BASE
	RC_TOKEN_XTHICKNESS = C.GTK_RC_TOKEN_XTHICKNESS
	RC_TOKEN_YTHICKNESS = C.GTK_RC_TOKEN_YTHICKNESS
	RC_TOKEN_FONT = C.GTK_RC_TOKEN_FONT
	RC_TOKEN_FONTSET = C.GTK_RC_TOKEN_FONTSET
	RC_TOKEN_FONT_NAME = C.GTK_RC_TOKEN_FONT_NAME
	RC_TOKEN_BG_PIXMAP = C.GTK_RC_TOKEN_BG_PIXMAP
	RC_TOKEN_PIXMAP_PATH = C.GTK_RC_TOKEN_PIXMAP_PATH
	RC_TOKEN_STYLE = C.GTK_RC_TOKEN_STYLE
	RC_TOKEN_BINDING = C.GTK_RC_TOKEN_BINDING
	RC_TOKEN_BIND = C.GTK_RC_TOKEN_BIND
	RC_TOKEN_WIDGET = C.GTK_RC_TOKEN_WIDGET
	RC_TOKEN_WIDGET_CLASS = C.GTK_RC_TOKEN_WIDGET_CLASS
	RC_TOKEN_CLASS = C.GTK_RC_TOKEN_CLASS
	RC_TOKEN_LOWEST = C.GTK_RC_TOKEN_LOWEST
	RC_TOKEN_GTK = C.GTK_RC_TOKEN_GTK
	RC_TOKEN_APPLICATION = C.GTK_RC_TOKEN_APPLICATION
	RC_TOKEN_THEME = C.GTK_RC_TOKEN_THEME
	RC_TOKEN_RC = C.GTK_RC_TOKEN_RC
	RC_TOKEN_HIGHEST = C.GTK_RC_TOKEN_HIGHEST
	RC_TOKEN_ENGINE = C.GTK_RC_TOKEN_ENGINE
	RC_TOKEN_MODULE_PATH = C.GTK_RC_TOKEN_MODULE_PATH
	RC_TOKEN_IM_MODULE_PATH = C.GTK_RC_TOKEN_IM_MODULE_PATH
	RC_TOKEN_IM_MODULE_FILE = C.GTK_RC_TOKEN_IM_MODULE_FILE
	RC_TOKEN_STOCK = C.GTK_RC_TOKEN_STOCK
	RC_TOKEN_LTR = C.GTK_RC_TOKEN_LTR
	RC_TOKEN_RTL = C.GTK_RC_TOKEN_RTL
	RC_TOKEN_COLOR = C.GTK_RC_TOKEN_COLOR
	RC_TOKEN_UNBIND = C.GTK_RC_TOKEN_UNBIND
	RC_TOKEN_LAST = C.GTK_RC_TOKEN_LAST
	RECENT_CHOOSER_ERROR_NOT_FOUND = C.GTK_RECENT_CHOOSER_ERROR_NOT_FOUND
	RECENT_CHOOSER_ERROR_INVALID_URI = C.GTK_RECENT_CHOOSER_ERROR_INVALID_URI
	RECENT_MANAGER_ERROR_NOT_FOUND = C.GTK_RECENT_MANAGER_ERROR_NOT_FOUND
	RECENT_MANAGER_ERROR_INVALID_URI = C.GTK_RECENT_MANAGER_ERROR_INVALID_URI
	RECENT_MANAGER_ERROR_INVALID_ENCODING = C.GTK_RECENT_MANAGER_ERROR_INVALID_ENCODING
	RECENT_MANAGER_ERROR_NOT_REGISTERED = C.GTK_RECENT_MANAGER_ERROR_NOT_REGISTERED
	RECENT_MANAGER_ERROR_READ = C.GTK_RECENT_MANAGER_ERROR_READ
	RECENT_MANAGER_ERROR_WRITE = C.GTK_RECENT_MANAGER_ERROR_WRITE
	RECENT_MANAGER_ERROR_UNKNOWN = C.GTK_RECENT_MANAGER_ERROR_UNKNOWN
	RECENT_SORT_NONE = C.GTK_RECENT_SORT_NONE
	RECENT_SORT_MRU = C.GTK_RECENT_SORT_MRU
	RECENT_SORT_LRU = C.GTK_RECENT_SORT_LRU
	RECENT_SORT_CUSTOM = C.GTK_RECENT_SORT_CUSTOM
	RELIEF_NORMAL = C.GTK_RELIEF_NORMAL
	RELIEF_HALF = C.GTK_RELIEF_HALF
	RELIEF_NONE = C.GTK_RELIEF_NONE
	RESIZE_PARENT = C.GTK_RESIZE_PARENT
	RESIZE_QUEUE = C.GTK_RESIZE_QUEUE
	RESIZE_IMMEDIATE = C.GTK_RESIZE_IMMEDIATE
	RESPONSE_NONE = C.GTK_RESPONSE_NONE
	RESPONSE_REJECT = C.GTK_RESPONSE_REJECT
	RESPONSE_ACCEPT = C.GTK_RESPONSE_ACCEPT
	RESPONSE_DELETE_EVENT = C.GTK_RESPONSE_DELETE_EVENT
	RESPONSE_OK = C.GTK_RESPONSE_OK
	RESPONSE_CANCEL = C.GTK_RESPONSE_CANCEL
	RESPONSE_CLOSE = C.GTK_RESPONSE_CLOSE
	RESPONSE_YES = C.GTK_RESPONSE_YES
	RESPONSE_NO = C.GTK_RESPONSE_NO
	RESPONSE_APPLY = C.GTK_RESPONSE_APPLY
	RESPONSE_HELP = C.GTK_RESPONSE_HELP
	SCROLL_STEPS = C.GTK_SCROLL_STEPS
	SCROLL_PAGES = C.GTK_SCROLL_PAGES
	SCROLL_ENDS = C.GTK_SCROLL_ENDS
	SCROLL_HORIZONTAL_STEPS = C.GTK_SCROLL_HORIZONTAL_STEPS
	SCROLL_HORIZONTAL_PAGES = C.GTK_SCROLL_HORIZONTAL_PAGES
	SCROLL_HORIZONTAL_ENDS = C.GTK_SCROLL_HORIZONTAL_ENDS
	SCROLL_NONE = C.GTK_SCROLL_NONE
	SCROLL_JUMP = C.GTK_SCROLL_JUMP
	SCROLL_STEP_BACKWARD = C.GTK_SCROLL_STEP_BACKWARD
	SCROLL_STEP_FORWARD = C.GTK_SCROLL_STEP_FORWARD
	SCROLL_PAGE_BACKWARD = C.GTK_SCROLL_PAGE_BACKWARD
	SCROLL_PAGE_FORWARD = C.GTK_SCROLL_PAGE_FORWARD
	SCROLL_STEP_UP = C.GTK_SCROLL_STEP_UP
	SCROLL_STEP_DOWN = C.GTK_SCROLL_STEP_DOWN
	SCROLL_PAGE_UP = C.GTK_SCROLL_PAGE_UP
	SCROLL_PAGE_DOWN = C.GTK_SCROLL_PAGE_DOWN
	SCROLL_STEP_LEFT = C.GTK_SCROLL_STEP_LEFT
	SCROLL_STEP_RIGHT = C.GTK_SCROLL_STEP_RIGHT
	SCROLL_PAGE_LEFT = C.GTK_SCROLL_PAGE_LEFT
	SCROLL_PAGE_RIGHT = C.GTK_SCROLL_PAGE_RIGHT
	SCROLL_START = C.GTK_SCROLL_START
	SCROLL_END = C.GTK_SCROLL_END
	SCROLL_MINIMUM = C.GTK_SCROLL_MINIMUM
	SCROLL_NATURAL = C.GTK_SCROLL_NATURAL
	SELECTION_NONE = C.GTK_SELECTION_NONE
	SELECTION_SINGLE = C.GTK_SELECTION_SINGLE
	SELECTION_BROWSE = C.GTK_SELECTION_BROWSE
	SELECTION_MULTIPLE = C.GTK_SELECTION_MULTIPLE
	SENSITIVITY_AUTO = C.GTK_SENSITIVITY_AUTO
	SENSITIVITY_ON = C.GTK_SENSITIVITY_ON
	SENSITIVITY_OFF = C.GTK_SENSITIVITY_OFF
	SHADOW_NONE = C.GTK_SHADOW_NONE
	SHADOW_IN = C.GTK_SHADOW_IN
	SHADOW_OUT = C.GTK_SHADOW_OUT
	SHADOW_ETCHED_IN = C.GTK_SHADOW_ETCHED_IN
	SHADOW_ETCHED_OUT = C.GTK_SHADOW_ETCHED_OUT
	SIZE_GROUP_NONE = C.GTK_SIZE_GROUP_NONE
	SIZE_GROUP_HORIZONTAL = C.GTK_SIZE_GROUP_HORIZONTAL
	SIZE_GROUP_VERTICAL = C.GTK_SIZE_GROUP_VERTICAL
	SIZE_GROUP_BOTH = C.GTK_SIZE_GROUP_BOTH
	SIZE_REQUEST_HEIGHT_FOR_WIDTH = C.GTK_SIZE_REQUEST_HEIGHT_FOR_WIDTH
	SIZE_REQUEST_WIDTH_FOR_HEIGHT = C.GTK_SIZE_REQUEST_WIDTH_FOR_HEIGHT
	SIZE_REQUEST_CONSTANT_SIZE = C.GTK_SIZE_REQUEST_CONSTANT_SIZE
	SORT_ASCENDING = C.GTK_SORT_ASCENDING
	SORT_DESCENDING = C.GTK_SORT_DESCENDING
	UPDATE_ALWAYS = C.GTK_UPDATE_ALWAYS
	UPDATE_IF_VALID = C.GTK_UPDATE_IF_VALID
	SPIN_STEP_FORWARD = C.GTK_SPIN_STEP_FORWARD
	SPIN_STEP_BACKWARD = C.GTK_SPIN_STEP_BACKWARD
	SPIN_PAGE_FORWARD = C.GTK_SPIN_PAGE_FORWARD
	SPIN_PAGE_BACKWARD = C.GTK_SPIN_PAGE_BACKWARD
	SPIN_HOME = C.GTK_SPIN_HOME
	SPIN_END = C.GTK_SPIN_END
	SPIN_USER_DEFINED = C.GTK_SPIN_USER_DEFINED
	STATE_NORMAL = C.GTK_STATE_NORMAL
	STATE_ACTIVE = C.GTK_STATE_ACTIVE
	STATE_PRELIGHT = C.GTK_STATE_PRELIGHT
	STATE_SELECTED = C.GTK_STATE_SELECTED
	STATE_INSENSITIVE = C.GTK_STATE_INSENSITIVE
	STATE_INCONSISTENT = C.GTK_STATE_INCONSISTENT
	STATE_FOCUSED = C.GTK_STATE_FOCUSED
	TEXT_BUFFER_TARGET_INFO_BUFFER_CONTENTS = C.GTK_TEXT_BUFFER_TARGET_INFO_BUFFER_CONTENTS
	TEXT_BUFFER_TARGET_INFO_RICH_TEXT = C.GTK_TEXT_BUFFER_TARGET_INFO_RICH_TEXT
	TEXT_BUFFER_TARGET_INFO_TEXT = C.GTK_TEXT_BUFFER_TARGET_INFO_TEXT
	TEXT_DIR_NONE = C.GTK_TEXT_DIR_NONE
	TEXT_DIR_LTR = C.GTK_TEXT_DIR_LTR
	TEXT_DIR_RTL = C.GTK_TEXT_DIR_RTL
	TEXT_WINDOW_PRIVATE = C.GTK_TEXT_WINDOW_PRIVATE
	TEXT_WINDOW_WIDGET = C.GTK_TEXT_WINDOW_WIDGET
	TEXT_WINDOW_TEXT = C.GTK_TEXT_WINDOW_TEXT
	TEXT_WINDOW_LEFT = C.GTK_TEXT_WINDOW_LEFT
	TEXT_WINDOW_RIGHT = C.GTK_TEXT_WINDOW_RIGHT
	TEXT_WINDOW_TOP = C.GTK_TEXT_WINDOW_TOP
	TEXT_WINDOW_BOTTOM = C.GTK_TEXT_WINDOW_BOTTOM
	TOOLBAR_SPACE_EMPTY = C.GTK_TOOLBAR_SPACE_EMPTY
	TOOLBAR_SPACE_LINE = C.GTK_TOOLBAR_SPACE_LINE
	TOOLBAR_ICONS = C.GTK_TOOLBAR_ICONS
	TOOLBAR_TEXT = C.GTK_TOOLBAR_TEXT
	TOOLBAR_BOTH = C.GTK_TOOLBAR_BOTH
	TOOLBAR_BOTH_HORIZ = C.GTK_TOOLBAR_BOTH_HORIZ
	TREE_VIEW_COLUMN_GROW_ONLY = C.GTK_TREE_VIEW_COLUMN_GROW_ONLY
	TREE_VIEW_COLUMN_AUTOSIZE = C.GTK_TREE_VIEW_COLUMN_AUTOSIZE
	TREE_VIEW_COLUMN_FIXED = C.GTK_TREE_VIEW_COLUMN_FIXED
	TREE_VIEW_DROP_BEFORE = C.GTK_TREE_VIEW_DROP_BEFORE
	TREE_VIEW_DROP_AFTER = C.GTK_TREE_VIEW_DROP_AFTER
	TREE_VIEW_DROP_INTO_OR_BEFORE = C.GTK_TREE_VIEW_DROP_INTO_OR_BEFORE
	TREE_VIEW_DROP_INTO_OR_AFTER = C.GTK_TREE_VIEW_DROP_INTO_OR_AFTER
	TREE_VIEW_GRID_LINES_NONE = C.GTK_TREE_VIEW_GRID_LINES_NONE
	TREE_VIEW_GRID_LINES_HORIZONTAL = C.GTK_TREE_VIEW_GRID_LINES_HORIZONTAL
	TREE_VIEW_GRID_LINES_VERTICAL = C.GTK_TREE_VIEW_GRID_LINES_VERTICAL
	TREE_VIEW_GRID_LINES_BOTH = C.GTK_TREE_VIEW_GRID_LINES_BOTH
	UNIT_NONE = C.GTK_UNIT_NONE
	UNIT_POINTS = C.GTK_UNIT_POINTS
	UNIT_INCH = C.GTK_UNIT_INCH
	UNIT_MM = C.GTK_UNIT_MM
	WIDGET_HELP_TOOLTIP = C.GTK_WIDGET_HELP_TOOLTIP
	WIDGET_HELP_WHATS_THIS = C.GTK_WIDGET_HELP_WHATS_THIS
	WIN_POS_NONE = C.GTK_WIN_POS_NONE
	WIN_POS_CENTER = C.GTK_WIN_POS_CENTER
	WIN_POS_MOUSE = C.GTK_WIN_POS_MOUSE
	WIN_POS_CENTER_ALWAYS = C.GTK_WIN_POS_CENTER_ALWAYS
	WIN_POS_CENTER_ON_PARENT = C.GTK_WIN_POS_CENTER_ON_PARENT
	WINDOW_TOPLEVEL = C.GTK_WINDOW_TOPLEVEL
	WINDOW_POPUP = C.GTK_WINDOW_POPUP
	WRAP_NONE = C.GTK_WRAP_NONE
	WRAP_CHAR = C.GTK_WRAP_CHAR
	WRAP_WORD = C.GTK_WRAP_WORD
	WRAP_WORD_CHAR = C.GTK_WRAP_WORD_CHAR
)
const (
	BINARY_AGE = C.GTK_BINARY_AGE
	INPUT_ERROR = C.GTK_INPUT_ERROR
	INTERFACE_AGE = C.GTK_INTERFACE_AGE
	LEVEL_BAR_OFFSET_HIGH = C.GTK_LEVEL_BAR_OFFSET_HIGH
	LEVEL_BAR_OFFSET_LOW = C.GTK_LEVEL_BAR_OFFSET_LOW
	MAJOR_VERSION = C.GTK_MAJOR_VERSION
	MAX_COMPOSE_LEN = C.GTK_MAX_COMPOSE_LEN
	MICRO_VERSION = C.GTK_MICRO_VERSION
	MINOR_VERSION = C.GTK_MINOR_VERSION
	PAPER_NAME_A3 = C.GTK_PAPER_NAME_A3
	PAPER_NAME_A4 = C.GTK_PAPER_NAME_A4
	PAPER_NAME_A5 = C.GTK_PAPER_NAME_A5
	PAPER_NAME_B5 = C.GTK_PAPER_NAME_B5
	PAPER_NAME_EXECUTIVE = C.GTK_PAPER_NAME_EXECUTIVE
	PAPER_NAME_LEGAL = C.GTK_PAPER_NAME_LEGAL
	PAPER_NAME_LETTER = C.GTK_PAPER_NAME_LETTER
	PATH_PRIO_MASK = C.GTK_PATH_PRIO_MASK
	PRINT_SETTINGS_COLLATE = C.GTK_PRINT_SETTINGS_COLLATE
	PRINT_SETTINGS_DEFAULT_SOURCE = C.GTK_PRINT_SETTINGS_DEFAULT_SOURCE
	PRINT_SETTINGS_DITHER = C.GTK_PRINT_SETTINGS_DITHER
	PRINT_SETTINGS_DUPLEX = C.GTK_PRINT_SETTINGS_DUPLEX
	PRINT_SETTINGS_FINISHINGS = C.GTK_PRINT_SETTINGS_FINISHINGS
	PRINT_SETTINGS_MEDIA_TYPE = C.GTK_PRINT_SETTINGS_MEDIA_TYPE
	PRINT_SETTINGS_NUMBER_UP = C.GTK_PRINT_SETTINGS_NUMBER_UP
	PRINT_SETTINGS_NUMBER_UP_LAYOUT = C.GTK_PRINT_SETTINGS_NUMBER_UP_LAYOUT
	PRINT_SETTINGS_N_COPIES = C.GTK_PRINT_SETTINGS_N_COPIES
	PRINT_SETTINGS_ORIENTATION = C.GTK_PRINT_SETTINGS_ORIENTATION
	PRINT_SETTINGS_OUTPUT_BASENAME = C.GTK_PRINT_SETTINGS_OUTPUT_BASENAME
	PRINT_SETTINGS_OUTPUT_BIN = C.GTK_PRINT_SETTINGS_OUTPUT_BIN
	PRINT_SETTINGS_OUTPUT_DIR = C.GTK_PRINT_SETTINGS_OUTPUT_DIR
	PRINT_SETTINGS_OUTPUT_FILE_FORMAT = C.GTK_PRINT_SETTINGS_OUTPUT_FILE_FORMAT
	PRINT_SETTINGS_OUTPUT_URI = C.GTK_PRINT_SETTINGS_OUTPUT_URI
	PRINT_SETTINGS_PAGE_RANGES = C.GTK_PRINT_SETTINGS_PAGE_RANGES
	PRINT_SETTINGS_PAGE_SET = C.GTK_PRINT_SETTINGS_PAGE_SET
	PRINT_SETTINGS_PAPER_FORMAT = C.GTK_PRINT_SETTINGS_PAPER_FORMAT
	PRINT_SETTINGS_PAPER_HEIGHT = C.GTK_PRINT_SETTINGS_PAPER_HEIGHT
	PRINT_SETTINGS_PAPER_WIDTH = C.GTK_PRINT_SETTINGS_PAPER_WIDTH
	PRINT_SETTINGS_PRINTER = C.GTK_PRINT_SETTINGS_PRINTER
	PRINT_SETTINGS_PRINTER_LPI = C.GTK_PRINT_SETTINGS_PRINTER_LPI
	PRINT_SETTINGS_PRINT_PAGES = C.GTK_PRINT_SETTINGS_PRINT_PAGES
	PRINT_SETTINGS_QUALITY = C.GTK_PRINT_SETTINGS_QUALITY
	PRINT_SETTINGS_RESOLUTION = C.GTK_PRINT_SETTINGS_RESOLUTION
	PRINT_SETTINGS_RESOLUTION_X = C.GTK_PRINT_SETTINGS_RESOLUTION_X
	PRINT_SETTINGS_RESOLUTION_Y = C.GTK_PRINT_SETTINGS_RESOLUTION_Y
	PRINT_SETTINGS_REVERSE = C.GTK_PRINT_SETTINGS_REVERSE
	PRINT_SETTINGS_SCALE = C.GTK_PRINT_SETTINGS_SCALE
	PRINT_SETTINGS_USE_COLOR = C.GTK_PRINT_SETTINGS_USE_COLOR
	PRINT_SETTINGS_WIN32_DRIVER_EXTRA = C.GTK_PRINT_SETTINGS_WIN32_DRIVER_EXTRA
	PRINT_SETTINGS_WIN32_DRIVER_VERSION = C.GTK_PRINT_SETTINGS_WIN32_DRIVER_VERSION
	PRIORITY_RESIZE = C.GTK_PRIORITY_RESIZE
	STOCK_ABOUT = C.GTK_STOCK_ABOUT
	STOCK_ADD = C.GTK_STOCK_ADD
	STOCK_APPLY = C.GTK_STOCK_APPLY
	STOCK_BOLD = C.GTK_STOCK_BOLD
	STOCK_CANCEL = C.GTK_STOCK_CANCEL
	STOCK_CAPS_LOCK_WARNING = C.GTK_STOCK_CAPS_LOCK_WARNING
	STOCK_CDROM = C.GTK_STOCK_CDROM
	STOCK_CLEAR = C.GTK_STOCK_CLEAR
	STOCK_CLOSE = C.GTK_STOCK_CLOSE
	STOCK_COLOR_PICKER = C.GTK_STOCK_COLOR_PICKER
	STOCK_CONNECT = C.GTK_STOCK_CONNECT
	STOCK_CONVERT = C.GTK_STOCK_CONVERT
	STOCK_COPY = C.GTK_STOCK_COPY
	STOCK_CUT = C.GTK_STOCK_CUT
	STOCK_DELETE = C.GTK_STOCK_DELETE
	STOCK_DIALOG_AUTHENTICATION = C.GTK_STOCK_DIALOG_AUTHENTICATION
	STOCK_DIALOG_ERROR = C.GTK_STOCK_DIALOG_ERROR
	STOCK_DIALOG_INFO = C.GTK_STOCK_DIALOG_INFO
	STOCK_DIALOG_QUESTION = C.GTK_STOCK_DIALOG_QUESTION
	STOCK_DIALOG_WARNING = C.GTK_STOCK_DIALOG_WARNING
	STOCK_DIRECTORY = C.GTK_STOCK_DIRECTORY
	STOCK_DISCARD = C.GTK_STOCK_DISCARD
	STOCK_DISCONNECT = C.GTK_STOCK_DISCONNECT
	STOCK_DND = C.GTK_STOCK_DND
	STOCK_DND_MULTIPLE = C.GTK_STOCK_DND_MULTIPLE
	STOCK_EDIT = C.GTK_STOCK_EDIT
	STOCK_EXECUTE = C.GTK_STOCK_EXECUTE
	STOCK_FILE = C.GTK_STOCK_FILE
	STOCK_FIND = C.GTK_STOCK_FIND
	STOCK_FIND_AND_REPLACE = C.GTK_STOCK_FIND_AND_REPLACE
	STOCK_FLOPPY = C.GTK_STOCK_FLOPPY
	STOCK_FULLSCREEN = C.GTK_STOCK_FULLSCREEN
	STOCK_GOTO_BOTTOM = C.GTK_STOCK_GOTO_BOTTOM
	STOCK_GOTO_FIRST = C.GTK_STOCK_GOTO_FIRST
	STOCK_GOTO_LAST = C.GTK_STOCK_GOTO_LAST
	STOCK_GOTO_TOP = C.GTK_STOCK_GOTO_TOP
	STOCK_GO_BACK = C.GTK_STOCK_GO_BACK
	STOCK_GO_DOWN = C.GTK_STOCK_GO_DOWN
	STOCK_GO_FORWARD = C.GTK_STOCK_GO_FORWARD
	STOCK_GO_UP = C.GTK_STOCK_GO_UP
	STOCK_HARDDISK = C.GTK_STOCK_HARDDISK
	STOCK_HELP = C.GTK_STOCK_HELP
	STOCK_HOME = C.GTK_STOCK_HOME
	STOCK_INDENT = C.GTK_STOCK_INDENT
	STOCK_INDEX = C.GTK_STOCK_INDEX
	STOCK_INFO = C.GTK_STOCK_INFO
	STOCK_ITALIC = C.GTK_STOCK_ITALIC
	STOCK_JUMP_TO = C.GTK_STOCK_JUMP_TO
	STOCK_JUSTIFY_CENTER = C.GTK_STOCK_JUSTIFY_CENTER
	STOCK_JUSTIFY_FILL = C.GTK_STOCK_JUSTIFY_FILL
	STOCK_JUSTIFY_LEFT = C.GTK_STOCK_JUSTIFY_LEFT
	STOCK_JUSTIFY_RIGHT = C.GTK_STOCK_JUSTIFY_RIGHT
	STOCK_LEAVE_FULLSCREEN = C.GTK_STOCK_LEAVE_FULLSCREEN
	STOCK_MEDIA_FORWARD = C.GTK_STOCK_MEDIA_FORWARD
	STOCK_MEDIA_NEXT = C.GTK_STOCK_MEDIA_NEXT
	STOCK_MEDIA_PAUSE = C.GTK_STOCK_MEDIA_PAUSE
	STOCK_MEDIA_PLAY = C.GTK_STOCK_MEDIA_PLAY
	STOCK_MEDIA_PREVIOUS = C.GTK_STOCK_MEDIA_PREVIOUS
	STOCK_MEDIA_RECORD = C.GTK_STOCK_MEDIA_RECORD
	STOCK_MEDIA_REWIND = C.GTK_STOCK_MEDIA_REWIND
	STOCK_MEDIA_STOP = C.GTK_STOCK_MEDIA_STOP
	STOCK_MISSING_IMAGE = C.GTK_STOCK_MISSING_IMAGE
	STOCK_NETWORK = C.GTK_STOCK_NETWORK
	STOCK_NEW = C.GTK_STOCK_NEW
	STOCK_NO = C.GTK_STOCK_NO
	STOCK_OK = C.GTK_STOCK_OK
	STOCK_OPEN = C.GTK_STOCK_OPEN
	STOCK_ORIENTATION_LANDSCAPE = C.GTK_STOCK_ORIENTATION_LANDSCAPE
	STOCK_ORIENTATION_PORTRAIT = C.GTK_STOCK_ORIENTATION_PORTRAIT
	STOCK_ORIENTATION_REVERSE_LANDSCAPE = C.GTK_STOCK_ORIENTATION_REVERSE_LANDSCAPE
	STOCK_ORIENTATION_REVERSE_PORTRAIT = C.GTK_STOCK_ORIENTATION_REVERSE_PORTRAIT
	STOCK_PAGE_SETUP = C.GTK_STOCK_PAGE_SETUP
	STOCK_PASTE = C.GTK_STOCK_PASTE
	STOCK_PREFERENCES = C.GTK_STOCK_PREFERENCES
	STOCK_PRINT = C.GTK_STOCK_PRINT
	STOCK_PRINT_ERROR = C.GTK_STOCK_PRINT_ERROR
	STOCK_PRINT_PAUSED = C.GTK_STOCK_PRINT_PAUSED
	STOCK_PRINT_PREVIEW = C.GTK_STOCK_PRINT_PREVIEW
	STOCK_PRINT_REPORT = C.GTK_STOCK_PRINT_REPORT
	STOCK_PRINT_WARNING = C.GTK_STOCK_PRINT_WARNING
	STOCK_PROPERTIES = C.GTK_STOCK_PROPERTIES
	STOCK_QUIT = C.GTK_STOCK_QUIT
	STOCK_REDO = C.GTK_STOCK_REDO
	STOCK_REFRESH = C.GTK_STOCK_REFRESH
	STOCK_REMOVE = C.GTK_STOCK_REMOVE
	STOCK_REVERT_TO_SAVED = C.GTK_STOCK_REVERT_TO_SAVED
	STOCK_SAVE = C.GTK_STOCK_SAVE
	STOCK_SAVE_AS = C.GTK_STOCK_SAVE_AS
	STOCK_SELECT_ALL = C.GTK_STOCK_SELECT_ALL
	STOCK_SELECT_COLOR = C.GTK_STOCK_SELECT_COLOR
	STOCK_SELECT_FONT = C.GTK_STOCK_SELECT_FONT
	STOCK_SORT_ASCENDING = C.GTK_STOCK_SORT_ASCENDING
	STOCK_SORT_DESCENDING = C.GTK_STOCK_SORT_DESCENDING
	STOCK_SPELL_CHECK = C.GTK_STOCK_SPELL_CHECK
	STOCK_STOP = C.GTK_STOCK_STOP
	STOCK_STRIKETHROUGH = C.GTK_STOCK_STRIKETHROUGH
	STOCK_UNDELETE = C.GTK_STOCK_UNDELETE
	STOCK_UNDERLINE = C.GTK_STOCK_UNDERLINE
	STOCK_UNDO = C.GTK_STOCK_UNDO
	STOCK_UNINDENT = C.GTK_STOCK_UNINDENT
	STOCK_YES = C.GTK_STOCK_YES
	STOCK_ZOOM_100 = C.GTK_STOCK_ZOOM_100
	STOCK_ZOOM_FIT = C.GTK_STOCK_ZOOM_FIT
	STOCK_ZOOM_IN = C.GTK_STOCK_ZOOM_IN
	STOCK_ZOOM_OUT = C.GTK_STOCK_ZOOM_OUT
	STYLE_CLASS_ACCELERATOR = C.GTK_STYLE_CLASS_ACCELERATOR
	STYLE_CLASS_ARROW = C.GTK_STYLE_CLASS_ARROW
	STYLE_CLASS_BACKGROUND = C.GTK_STYLE_CLASS_BACKGROUND
	STYLE_CLASS_BOTTOM = C.GTK_STYLE_CLASS_BOTTOM
	STYLE_CLASS_BUTTON = C.GTK_STYLE_CLASS_BUTTON
	STYLE_CLASS_CALENDAR = C.GTK_STYLE_CLASS_CALENDAR
	STYLE_CLASS_CELL = C.GTK_STYLE_CLASS_CELL
	STYLE_CLASS_CHECK = C.GTK_STYLE_CLASS_CHECK
	STYLE_CLASS_COMBOBOX_ENTRY = C.GTK_STYLE_CLASS_COMBOBOX_ENTRY
	STYLE_CLASS_CURSOR_HANDLE = C.GTK_STYLE_CLASS_CURSOR_HANDLE
	STYLE_CLASS_DEFAULT = C.GTK_STYLE_CLASS_DEFAULT
	STYLE_CLASS_DIM_LABEL = C.GTK_STYLE_CLASS_DIM_LABEL
	STYLE_CLASS_DND = C.GTK_STYLE_CLASS_DND
	STYLE_CLASS_DOCK = C.GTK_STYLE_CLASS_DOCK
	STYLE_CLASS_ENTRY = C.GTK_STYLE_CLASS_ENTRY
	STYLE_CLASS_ERROR = C.GTK_STYLE_CLASS_ERROR
	STYLE_CLASS_EXPANDER = C.GTK_STYLE_CLASS_EXPANDER
	STYLE_CLASS_FRAME = C.GTK_STYLE_CLASS_FRAME
	STYLE_CLASS_GRIP = C.GTK_STYLE_CLASS_GRIP
	STYLE_CLASS_HEADER = C.GTK_STYLE_CLASS_HEADER
	STYLE_CLASS_HIGHLIGHT = C.GTK_STYLE_CLASS_HIGHLIGHT
	STYLE_CLASS_HORIZONTAL = C.GTK_STYLE_CLASS_HORIZONTAL
	STYLE_CLASS_IMAGE = C.GTK_STYLE_CLASS_IMAGE
	STYLE_CLASS_INFO = C.GTK_STYLE_CLASS_INFO
	STYLE_CLASS_INLINE_TOOLBAR = C.GTK_STYLE_CLASS_INLINE_TOOLBAR
	STYLE_CLASS_LEFT = C.GTK_STYLE_CLASS_LEFT
	STYLE_CLASS_LEVEL_BAR = C.GTK_STYLE_CLASS_LEVEL_BAR
	STYLE_CLASS_LINKED = C.GTK_STYLE_CLASS_LINKED
	STYLE_CLASS_MARK = C.GTK_STYLE_CLASS_MARK
	STYLE_CLASS_MENU = C.GTK_STYLE_CLASS_MENU
	STYLE_CLASS_MENUBAR = C.GTK_STYLE_CLASS_MENUBAR
	STYLE_CLASS_MENUITEM = C.GTK_STYLE_CLASS_MENUITEM
	STYLE_CLASS_NOTEBOOK = C.GTK_STYLE_CLASS_NOTEBOOK
	STYLE_CLASS_OSD = C.GTK_STYLE_CLASS_OSD
	STYLE_CLASS_PANE_SEPARATOR = C.GTK_STYLE_CLASS_PANE_SEPARATOR
	STYLE_CLASS_PRIMARY_TOOLBAR = C.GTK_STYLE_CLASS_PRIMARY_TOOLBAR
	STYLE_CLASS_PROGRESSBAR = C.GTK_STYLE_CLASS_PROGRESSBAR
	STYLE_CLASS_PULSE = C.GTK_STYLE_CLASS_PULSE
	STYLE_CLASS_QUESTION = C.GTK_STYLE_CLASS_QUESTION
	STYLE_CLASS_RADIO = C.GTK_STYLE_CLASS_RADIO
	STYLE_CLASS_RAISED = C.GTK_STYLE_CLASS_RAISED
	STYLE_CLASS_RIGHT = C.GTK_STYLE_CLASS_RIGHT
	STYLE_CLASS_RUBBERBAND = C.GTK_STYLE_CLASS_RUBBERBAND
	STYLE_CLASS_SCALE = C.GTK_STYLE_CLASS_SCALE
	STYLE_CLASS_SCALE_HAS_MARKS_ABOVE = C.GTK_STYLE_CLASS_SCALE_HAS_MARKS_ABOVE
	STYLE_CLASS_SCALE_HAS_MARKS_BELOW = C.GTK_STYLE_CLASS_SCALE_HAS_MARKS_BELOW
	STYLE_CLASS_SCROLLBAR = C.GTK_STYLE_CLASS_SCROLLBAR
	STYLE_CLASS_SCROLLBARS_JUNCTION = C.GTK_STYLE_CLASS_SCROLLBARS_JUNCTION
	STYLE_CLASS_SEPARATOR = C.GTK_STYLE_CLASS_SEPARATOR
	STYLE_CLASS_SIDEBAR = C.GTK_STYLE_CLASS_SIDEBAR
	STYLE_CLASS_SLIDER = C.GTK_STYLE_CLASS_SLIDER
	STYLE_CLASS_SPINBUTTON = C.GTK_STYLE_CLASS_SPINBUTTON
	STYLE_CLASS_SPINNER = C.GTK_STYLE_CLASS_SPINNER
	STYLE_CLASS_TOOLBAR = C.GTK_STYLE_CLASS_TOOLBAR
	STYLE_CLASS_TOOLTIP = C.GTK_STYLE_CLASS_TOOLTIP
	STYLE_CLASS_TOP = C.GTK_STYLE_CLASS_TOP
	STYLE_CLASS_TROUGH = C.GTK_STYLE_CLASS_TROUGH
	STYLE_CLASS_VERTICAL = C.GTK_STYLE_CLASS_VERTICAL
	STYLE_CLASS_VIEW = C.GTK_STYLE_CLASS_VIEW
	STYLE_CLASS_WARNING = C.GTK_STYLE_CLASS_WARNING
	STYLE_PROPERTY_BACKGROUND_COLOR = C.GTK_STYLE_PROPERTY_BACKGROUND_COLOR
	STYLE_PROPERTY_BACKGROUND_IMAGE = C.GTK_STYLE_PROPERTY_BACKGROUND_IMAGE
	STYLE_PROPERTY_BORDER_COLOR = C.GTK_STYLE_PROPERTY_BORDER_COLOR
	STYLE_PROPERTY_BORDER_RADIUS = C.GTK_STYLE_PROPERTY_BORDER_RADIUS
	STYLE_PROPERTY_BORDER_STYLE = C.GTK_STYLE_PROPERTY_BORDER_STYLE
	STYLE_PROPERTY_BORDER_WIDTH = C.GTK_STYLE_PROPERTY_BORDER_WIDTH
	STYLE_PROPERTY_COLOR = C.GTK_STYLE_PROPERTY_COLOR
	STYLE_PROPERTY_FONT = C.GTK_STYLE_PROPERTY_FONT
	STYLE_PROPERTY_MARGIN = C.GTK_STYLE_PROPERTY_MARGIN
	STYLE_PROPERTY_PADDING = C.GTK_STYLE_PROPERTY_PADDING
	STYLE_PROVIDER_PRIORITY_APPLICATION = C.GTK_STYLE_PROVIDER_PRIORITY_APPLICATION
	STYLE_PROVIDER_PRIORITY_FALLBACK = C.GTK_STYLE_PROVIDER_PRIORITY_FALLBACK
	STYLE_PROVIDER_PRIORITY_SETTINGS = C.GTK_STYLE_PROVIDER_PRIORITY_SETTINGS
	STYLE_PROVIDER_PRIORITY_THEME = C.GTK_STYLE_PROVIDER_PRIORITY_THEME
	STYLE_PROVIDER_PRIORITY_USER = C.GTK_STYLE_PROVIDER_PRIORITY_USER
	STYLE_REGION_COLUMN = C.GTK_STYLE_REGION_COLUMN
	STYLE_REGION_COLUMN_HEADER = C.GTK_STYLE_REGION_COLUMN_HEADER
	STYLE_REGION_ROW = C.GTK_STYLE_REGION_ROW
	STYLE_REGION_TAB = C.GTK_STYLE_REGION_TAB
	TEXT_VIEW_PRIORITY_VALIDATE = C.GTK_TEXT_VIEW_PRIORITY_VALIDATE
)
