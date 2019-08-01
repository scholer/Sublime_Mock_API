# Copyright 2019, Rasmus Sorensen <rasmusscholer@gmail.com>

"""

Mocks the sublime_api functions provided by Sublime Text execution environment.

This currently only provides function interfaces, but no actual functionality.
That is, the functions when called, will not do anything, and will just return a dummy value,
typically simply 1.


The API functions are provided in this file
to make it easier to import the mocked `sublime_api` module
from within Sublime Text, without being overshadowed by the built-in modules
provided by the execution environment in Sublime Text.

Example usage:

* From within the Sublime Text console, update `sys.path`, appending the folder containing
    this file to the end of the `sys.path` list:

    >>> import sys
    >>> sys.path.append("<path-to-folder-containing-this-file>")
    >>> import sublime_api  # This will get you the original sublime_api module.
    >>> from sublime_mock_api import mock_api  # This will get you the mocked API.

You can easily determine if you are importing the mocked or original module by doing:

    hasattr(sublime_api, 'THIS_IS_THE_MOCKED_MODULE')

If the above is True, then you have the mocked module, otherwise you have the original.

"""

# Is it possible to do relative imports from a module that is not within a package?
# No, that will give an error:
# SystemError: Parent module '' not loaded, cannot perform relative import.
# But if we are inside Sublime Text console, and we don't want to shadow the original `sublime_api`
# module provided by the execution environment, then we have to do something else.
# from .sublime_api import *
# Instead, we have all the mock API functions in here, and then we import them
# in the `sublime_api.py` module provided outside this package.


import sys
from pprint import pformat
import json
import string

_settings_base_dir = ""


# Flag to make it easy to determine if you are using the mocked module:
THIS_IS_THE_MOCKED_MODULE = True


def log_message(s):
    print(s)


def version():
    return '3207'


def platform():
    return 'windows'


def architecture():
    return "Mock"


def channel():
    return "Mock"


def executable_path():
    return "Mock"


def packages_path():
    return "Mock"


def installed_packages_path():
    return "Mock"


def cache_path():
    return "Mock"


def status_message(msg):
    print(msg)


def error_message(msg):
    print(msg, file=sys.stderr)


def message_dialog(msg):
    print(msg)


def ok_cancel_dialog(msg, ok_title=""):
    print(ok_title)
    print(msg)


def yes_no_cancel_dialog(msg, yes_title="", no_title=""):
    print(msg)
    print("Yes =", yes_title)
    print("No  =", no_title)


def run_command(cmd, args=None):
    print("MOCK API: Running command", cmd, "with args:", args)


def get_clipboard(size_limit=16777216):
    try:
        import pyperclip
        return pyperclip.paste()
    except ImportError:
        pass
    try:
        import xerox
        return xerox.paste()
    except ImportError:
        pass
    return "Could not get clipboard data; required packages not available."


def set_clipboard(text):
    try:
        import pyperclip
        return pyperclip.copy(text)
    except ImportError:
        pass
    try:
        import xerox
        return xerox.copy(text)
    except ImportError:
        pass
    print("Could not set clipboard data; required packages not available.", file=sys.stderr)


def log_commands(flag):
    print("log_commands:", flag)


LOG_INPUT_ACTIVE = False


def log_input(flag):
    print("log_input:", flag)
    global LOG_INPUT_ACTIVE
    LOG_INPUT_ACTIVE = flag


def log_result_regex(flag):
    print("log_result_regex:", flag)


def log_indexing(flag):
    print("log_indexing:", flag)


def log_build_systems(flag):
    print("log_build_systems:", flag)


def score_selector(scope_name, selector):
    print("score_selector:", scope_name, selector)


def load_resource(name):
    pass


def load_binary_resource(name):
    pass


def find_resources(pattern):
    pass


def encode_value(val, pretty=False):
    return json.dumps(val, indent=4 if pretty else None)


def decode_value(data):
    try:
        val = json.loads(data)
    except Exception:
        return "", 1
    else:
        return val, 0


def expand_variables(val, variables):
    return string.Template(val).substitute(variables)


def load_settings(base_name):
    # settings_id = sublime_api.load_settings(base_name)
    # return Settings(settings_id)
    # Not really sure what the right approach is here...
    # However, because the Sublime Text settings can include non-JSON-complient things like
    # comments, we will certainly have to e.g. pass the settings file through jsmin or similar.
    return 0


def save_settings(base_name):
    pass


def set_timeout(f, timeout_ms=0):
    """
    Schedules a function to be called in the future. Sublime Text will block
    while the function is running
    """
    # sublime_api.set_timeout(f, timeout_ms)
    # Not supported right now?
    return f()


def set_timeout_async(f, timeout_ms=0):
    """
    Schedules a function to be called in the future. The function will be
    called in a worker thread, and Sublime Text will not block while the
    function is running
    """
    return f()


def active_window():
    # Should return a window_id:
    return 1


def windows():
    # Should return a list of windows IDs.
    return [1]


def get_macro():
    """ Returns a list of the commands and args that compromise the currently recorded macro.
    Each dict will contain the keys command and args.
    """
    return {}


def window_num_groups(window_id):
    return 1


def window_system_handle(window_id):
    """ Platform specific window handle, only returns a meaningful result under Windows """
    return 1


def window_active_sheet(window_id):
    """ Returns sheet_id """
    return 1


def window_active_view(window_id):
    """ Returns view_id specifying the active view for the given window. """
    return 1


def window_run_command(window_id, cmd, args):
    print("Running Window Command {cmd} with args {args} in window with id {window_id}".format(
        window_id=window_id, cmd=cmd, args=args
    ))


def window_new_file(window_id, flags, syntax):
    print("Creating new file with flags {flags} and syntax {syntax} in window with id {window_id}".format(
        window_id=window_id, flags=flags, syntax=syntax
    ))


def window_open_file(window_id, fname, flags, group):
    print("Opening file {fname} with flags {flags} in group {group} in window with id {window_id}".format(
        window_id=window_id, flags=flags, group=group, fname=fname
    ))


def window_find_open_file(window_id, fname):
    """ Return view_id for open file `fname`. """
    return 1


def window_close_file(window_id, view_id):
    pass


def window_active_group(window_id):
    return 1


def window_focus_group(window_id, idx):
    return 1


def window_focus_sheet(window_id, sheet_id):
    return 1


def window_focus_view(window_id, view_id):
    return 1


def window_get_sheet_index(window_id, sheet_id):
    return 1


def window_get_view_index(window_id, view_id):
    return 1


def window_set_sheet_index(window_id, sheet_id, group, idx):
    return 1


def window_set_view_index(window_id, view_id, group, idx):
    return 1


def window_sheets(window_id):
    return 1


def window_views(window_id):
    return 1


def window_active_sheet_in_group(window_id, group):
    return 1


def window_active_view_in_group(window_id, group):
    return 1


def window_sheets_in_group(window_id, group):
    return [1]


def window_views_in_group(window_id, group):
    return [1]


def window_transient_sheet_in_group(window_id, group):
    return 1


def window_transient_view_in_group(window_id, group):
    return 1


def window_get_layout(window_id):
    return 1


def window_set_layout(window_id, layout):
    return 1


def window_create_output_panel(window_id, name, unlisted):
    return 1


def window_find_output_panel(window_id, name):
    return 1


def window_destroy_output_panel(window_id, name):
    return 1


def window_active_panel(window_id):
    return ""


def window_panels(window_id):
    return [1]


def window_show_input_panel(window_id, caption, initial_text, on_done, on_change, on_cancel):
    return 1


def window_show_quick_panel(
        window_id, flat_items, items_per_row, on_select, on_highlight,
        flags, selected_index):
    return 1


def window_is_ui_element_visible(window_id, val):
    return 1


def window_set_ui_element_visible(window_id, val, flag):
    return 1


def is_minimap_visible(window_id, UI_ELEMENT_MINIMAP):
    return 1


def set_minimap_visible(window_id, UI_ELEMENT_MINIMAP, flag):
    return 1


def is_status_bar_visible(window_id, UI_ELEMENT_STATUS_BAR):
    return 1


def set_status_bar_visible(flag):
    return 1


def window_folders(window_id):
    return []


def window_project_file_name(window_id):
    return 1


def window_get_project_data(window_id):
    return 1


def window_set_project_data(window_id, v):
    return 1


def window_settings(window_id):
    return 1


def window_template_settings(window_id):
    return 1


def window_lookup_symbol(window_id, sym):
    return 1


def window_lookup_symbol_in_open_files(window_id, sym):
    return 1


def window_lookup_references(window_id, sym):
    return 1


def window_lookup_references_in_open_files(window_id, sym):
    return 1


def window_extract_variables(window_id):
    return 1


def window_status_message(window_id, msg):
    return 1


def sheet_window(sheet_id):
    return 1


def sheet_view(sheet_id):
    return 1


def view_selection_size(view_id):
    return 1


def view_selection_get(view_id, index):
    return 1


def view_selection_erase(view_id, index):
    return 1


def view_buffer_id(view_id):
    return 1


def view_selection_clear(view_id):
    return 1


def view_selection_add_region(view_id, a, b, pos):
    return 1


def view_selection_add_point(view_id, x):
    return 1


def view_selection_subtract_region(view_id, a, b):
    return 1


def view_selection_contains(view_id, a, b):
    return 1


def view_is_primary(view_id):
    return 1


def view_window(view_id):
    return 1


def view_file_name(view_id):
    return 1


def view_retarget(view_id, new_fname):
    return 1


def view_get_name(view_id):
    return 1


def view_set_name(view_id, name):
    return 1


def view_reset_reference_document(view_id):
    return 1


def view_set_reference_document(view_id, reference):
    return 1


def view_is_loading(view_id):
    return 1


def view_is_dirty(view_id):
    return 1


def view_is_read_only(view_id):
    return 1


def view_set_read_only(view_id, read_only):
    return 1


def view_is_scratch(view_id):
    return 1


def view_set_scratch(view_id, scratch):
    return 1


def view_encoding(view_id):
    return 1


def view_set_encoding(view_id, encoding_name):
    return 1


def view_line_endings(view_id):
    return 1


def view_set_line_endings(view_id, line_ending_name):
    return 1


def view_size(view_id):
    return 1


def view_begin_edit(view_id, edit_token, cmd, args):
    return 1


def view_end_edit(view_id, edit_token):
    return 1


def view_is_in_edit(view_id):
    return 0


def view_insert(view_id, edit_token, pt, text):
    return 1


def view_erase(view_id, edit_token, r):
    return 1


def view_replace(view_id, edit_token, r, text):
    return 1


def view_change_count(view_id):
    return 1


def view_run_command(view_id, cmd, args):
    return 1


def view_cached_substr(view_id, a, b):
    return 1


def view_find(view_id, pattern, start_pt, flags):
    return 1


def view_find_all(view_id, pattern, flags):
    return 1


def view_find_all_with_contents(view_id, pattern, flags, fmt):
    return 1


def view_settings(view_id):
    return 1


def view_meta_info(view_id, key, pt):
    return 1


def view_extract_tokens_with_scopes(view_id, begin, end):
    return 1


def view_extract_scope(view_id, pt):
    return 1


def view_scope_name(view_id, pt):
    return 1


def view_match_selector(view_id, pt, selector):
    return 1


def view_score_selector(view_id, pt, selector):
    return 1


def view_find_by_selector(view_id, selector):
    return 1


def view_style(view_id):
    return 1


def view_style_for_scope(view_id, scope):
    return 1


def view_indented_region(view_id, pt):
    return 1


def view_indentation_level(view_id, pt):
    return 1


def view_has_non_empty_selection_region(view_id):
    return 1


def view_lines(view_id, r):
    return 1


def view_split_by_newlines(view_id, r):
    return 1


def view_line_from_region(view_id, x):
    return 1


def view_line_from_point(view_id, x):
    return 1


def view_full_line_from_region(view_id, x):
    return 1


def view_full_line_from_point(view_id, x):
    return 1


def view_word_from_region(view_id, x):
    return 1


def view_word_from_point(view_id, x):
    return 1


def view_classify(view_id, pt):
    return 1


def view_find_by_class(view_id, pt, forward, classes, separators):
    return 1


def view_expand_by_class(view_id, pt, forward, classes, separators):
    return 1


def view_row_col(view_id, tp):
    return 1


def view_text_point(view_id, row, col):
    return 1


def view_visible_region(view_id):
    return 1


def view_show_region(view_id, x, show_surrounds):
    return 1


def view_show_point(view_id, x, show_surrounds):
    return 1


def view_show_region_at_center(view_id, x):
    return 1


def view_show_point_at_center(view_id, x):
    return 1


def view_viewport_position(view_id):
    return 1


def view_set_viewport_position(view_id, xy, animate):
    return 1


def view_viewport_extents(view_id):
    return 1


def view_layout_extents(view_id):
    return 1


def view_text_to_layout(view_id, tp):
    return 1


def view_layout_to_text(view_id, tp):
    return 1


def view_layout_to_window(view_id, tp):
    return 1


def view_window_to_layout(view_id, tp):
    return 1


def view_line_height(view_id):
    return 1


def view_em_width(view_id):
    return 1


def view_is_folded(view_id, sr):
    return 1


def view_folded_regions(view_id):
    return 1


def view_fold_region(view_id, x):
    return 1


def view_fold_regions(view_id, x):
    return 1


def view_unfold_region(view_id, x):
    return 1


def view_unfold_regions(view_id, x):
    return 1


def view_add_regions(view_id, key, regions, scope, icon, flags):
    return 1


def view_get_regions(view_id, key):
    return 1


def view_erase_regions(view_id, key):
    return 1


def view_add_phantom(view_id, key, region, content, layout, on_navigate):
    return 1


def view_erase_phantoms(view_id, key):
    return 1


def view_erase_phantom(view_id, key):
    return 1


def view_query_phantoms(view_id, pids):
    return 1


def view_assign_syntax(view_id, syntax_file):
    return 1


def view_symbols(view_id):
    return 1


def view_indexed_symbols(view_id):
    return 1


def view_indexed_references(view_id):
    return 1


def view_set_status(view_id, key, value):
    return 1


def view_get_status(view_id, key):
    return 1


def view_erase_status(view_id, key):
    return 1


def view_extract_completions(view_id, prefix, tp):
    return 1


def view_find_all_results(view_id):
    return 1


def view_find_all_results_with_text(view_id):
    return 1


def view_command_history(view_id, delta, modifying_only):
    return 1


def view_get_overwrite_status(view_id):
    return 1


def view_set_overwrite_status(view_id, value):
    return 1


def view_show_popup_table(view_id, items, on_select, flags, sel):
    return 1


def view_show_popup(
        view_id, location, content, flags, max_width, max_height,
        on_navigate, on_hide):
    return 1


def view_update_popup_content(view_id, content):
    return 1


def view_is_popup_visible(view_id):
    return 1


def view_hide_popup(view_id):
    return 1


def view_is_auto_complete_visible(view_id):
    return 1


def settings_get_default(settings_id, key, default):
    return default


def settings_get(settings_id, key):
    return 1


def settings_has(settings_id, key):
    return 1


def settings_set(settings_id, key, value):
    return 1


def settings_erase(settings_id, key):
    return 1


def settings_add_on_change(settings_id, tag, callback):
    return 1


def settings_clear_on_change(settings_id, tag):
    return 1


def notify_application_commands(cmds):
    pass


def can_accept_input(name, args):
    pass


def window_can_accept_input(window_id, name, args):
    pass


def view_can_accept_input(view_id, name, args):
    pass


def incompatible_syntax_patterns(**args):
    pass


def plugin_host_loaded_plugins(**args):
    pass


def plugin_host_ready(**args):
    pass


def profile_syntax_definition(**args):
    pass


def run_syntax_test(**args):
    pass


def verify_pc_signature(**args):
    pass


def view_substr(**args):
    pass


def window_is_dragging(**args):
    pass


print("sublime_mock_api.mock_api module imported.")
print("version():", version())
