# Copyright 2019, Rasmus Sorensen <rasmusscholer@gmail.com>

"""

Module for testing the mock_api module.


The TEST_ARGS below is easily initialized by running this in the Sublime Text console:

>>> import sublime_api, pprint
>>> TEST_ARGS_2 = [(attr, inspect.getfullargspec(getattr(mock_api, attr)).args, [], None)
                   for attr in dir(sublime_api) if callable(getattr(mock_api, attr))]
>>> pprint(TEST_ARGS, indent=4, width=140)



"""


TEST_ARGS = [
    # (function-name, arg-names, example_arg_values, example_return_value)
    ('active_window', [], [], None),
    ('architecture', [], [], None),
    ('cache_path', [], [], None),
    ('can_accept_input', ['name', 'args'], [], None),
    ('channel', [], [], None),
    ('decode_value', ['data'], [], None),
    ('encode_value', ['val', 'pretty'], [], None),
    ('error_message', ['msg'], [], None),
    ('executable_path', [], [], None),
    ('expand_variables', ['val', 'variables'], [], None),
    ('find_resources', ['pattern'], [], None),
    ('get_clipboard', ['size_limit'], [], None),
    ('get_macro', [], [], []),
    ('incompatible_syntax_patterns', [], [], None),
    ('installed_packages_path', [], [], None),
    ('load_binary_resource', ['name'], [], None),
    ('load_resource', ['name'], [], None),
    ('load_settings', ['base_name'], [], None),
    ('log_build_systems', ['flag'], [], None),
    ('log_commands', ['flag'], [], None),
    ('log_indexing', ['flag'], [], None),
    ('log_input', ['flag'], [], None),
    ('log_message', ['s'], [], None),
    ('log_result_regex', ['flag'], [], None),
    ('message_dialog', ['msg'], [], 0),
    ('notify_application_commands', ['cmds'], [], None),
    ('ok_cancel_dialog', ['msg', 'ok_title'], [], None),
    ('packages_path', [], [], None),
    ('platform', [], [], None),
    ('plugin_host_loaded_plugins', [], [], None),
    ('plugin_host_ready', [], [], None),
    ('profile_syntax_definition', [], [], None),
    ('run_command', ['cmd', 'args'], [], None),
    ('run_syntax_test', [], [], None),
    ('save_settings', ['base_name'], [], None),
    ('score_selector', ['scope_name', 'selector'], [], None),
    ('set_clipboard', ['text'], [], None),
    ('set_timeout', ['f', 'timeout_ms'], [], None),
    ('set_timeout_async', ['f', 'timeout_ms'], [], None),
    ('settings_add_on_change', ['settings_id', 'tag', 'callback'], [], None),
    ('settings_clear_on_change', ['settings_id', 'tag'], [], None),
    ('settings_erase', ['settings_id', 'key'], [], None),
    ('settings_get', ['settings_id', 'key'], [], None),
    ('settings_get_default', ['settings_id', 'key', 'default'], [], None),
    ('settings_has', ['settings_id', 'key'], [], None),
    ('settings_set', ['settings_id', 'key', 'value'], [], None),
    ('sheet_view', ['sheet_id'], [], None),
    ('sheet_window', ['sheet_id'], [], None),
    ('status_message', ['msg'], [], None),
    ('verify_pc_signature', [], [], None),
    ('version', [], [], None),
    ('view_add_phantom', ['view_id', 'key', 'region', 'content', 'layout', 'on_navigate'], [], None),
    ('view_add_regions', ['view_id', 'key', 'regions', 'scope', 'icon', 'flags'], [], None),
    ('view_assign_syntax', ['view_id', 'syntax_file'], [], None),
    ('view_begin_edit', ['view_id', 'edit_token', 'cmd', 'args'], [], None),
    ('view_buffer_id', ['view_id'], [], None),
    ('view_cached_substr', ['view_id', 'a', 'b'], [], None),
    ('view_can_accept_input', ['view_id', 'name', 'args'], [], None),
    ('view_change_count', ['view_id'], [], None),
    ('view_classify', ['view_id', 'pt'], [], None),
    ('view_command_history', ['view_id', 'delta', 'modifying_only'], [], None),
    ('view_em_width', ['view_id'], [], None),
    ('view_encoding', ['view_id'], [], None),
    ('view_end_edit', ['view_id', 'edit_token'], [], None),
    ('view_erase', ['view_id', 'edit_token', 'r'], [], None),
    ('view_erase_phantom', ['view_id', 'key'], [], None),
    ('view_erase_phantoms', ['view_id', 'key'], [], None),
    ('view_erase_regions', ['view_id', 'key'], [], None),
    ('view_erase_status', ['view_id', 'key'], [], None),
    ('view_expand_by_class', ['view_id', 'pt', 'forward', 'classes', 'separators'], [], None),
    ('view_extract_completions', ['view_id', 'prefix', 'tp'], [], None),
    ('view_extract_scope', ['view_id', 'pt'], [], None),
    ('view_extract_tokens_with_scopes', ['view_id', 'begin', 'end'], [], None),
    ('view_file_name', ['view_id'], [], None),
    ('view_find', ['view_id', 'pattern', 'start_pt', 'flags'], [], None),
    ('view_find_all', ['view_id', 'pattern', 'flags'], [], None),
    ('view_find_all_results', ['view_id'], [], None),
    ('view_find_all_results_with_text', ['view_id'], [], None),
    ('view_find_all_with_contents', ['view_id', 'pattern', 'flags', 'fmt'], [], None),
    ('view_find_by_class', ['view_id', 'pt', 'forward', 'classes', 'separators'], [], None),
    ('view_find_by_selector', ['view_id', 'selector'], [], None),
    ('view_fold_region', ['view_id', 'x'], [], None),
    ('view_fold_regions', ['view_id', 'x'], [], None),
    ('view_folded_regions', ['view_id'], [], None),
    ('view_full_line_from_point', ['view_id', 'x'], [], None),
    ('view_full_line_from_region', ['view_id', 'x'], [], None),
    ('view_get_name', ['view_id'], [], None),
    ('view_get_overwrite_status', ['view_id'], [], None),
    ('view_get_regions', ['view_id', 'key'], [], None),
    ('view_get_status', ['view_id', 'key'], [], None),
    ('view_has_non_empty_selection_region', ['view_id'], [], None),
    ('view_hide_popup', ['view_id'], [], None),
    ('view_indentation_level', ['view_id', 'pt'], [], None),
    ('view_indented_region', ['view_id', 'pt'], [], None),
    ('view_indexed_references', ['view_id'], [], None),
    ('view_indexed_symbols', ['view_id'], [], None),
    ('view_insert', ['view_id', 'edit_token', 'pt', 'text'], [], None),
    ('view_is_auto_complete_visible', ['view_id'], [], None),
    ('view_is_dirty', ['view_id'], [], None),
    ('view_is_folded', ['view_id', 'sr'], [], None),
    ('view_is_in_edit', ['view_id'], [], None),
    ('view_is_loading', ['view_id'], [], None),
    ('view_is_popup_visible', ['view_id'], [], None),
    ('view_is_primary', ['view_id'], [], None),
    ('view_is_read_only', ['view_id'], [], None),
    ('view_is_scratch', ['view_id'], [], None),
    ('view_layout_extents', ['view_id'], [], None),
    ('view_layout_to_text', ['view_id', 'tp'], [], None),
    ('view_layout_to_window', ['view_id', 'tp'], [], None),
    ('view_line_endings', ['view_id'], [], None),
    ('view_line_from_point', ['view_id', 'x'], [], None),
    ('view_line_from_region', ['view_id', 'x'], [], None),
    ('view_line_height', ['view_id'], [], None),
    ('view_lines', ['view_id', 'r'], [], None),
    ('view_match_selector', ['view_id', 'pt', 'selector'], [], None),
    ('view_meta_info', ['view_id', 'key', 'pt'], [], None),
    ('view_query_phantoms', ['view_id', 'pids'], [], None),
    ('view_replace', ['view_id', 'edit_token', 'r', 'text'], [], None),
    ('view_reset_reference_document', ['view_id'], [], None),
    ('view_retarget', ['view_id', 'new_fname'], [], None),
    ('view_row_col', ['view_id', 'tp'], [], None),
    ('view_run_command', ['view_id', 'cmd', 'args'], [], None),
    ('view_scope_name', ['view_id', 'pt'], [], None),
    ('view_score_selector', ['view_id', 'pt', 'selector'], [], None),
    ('view_selection_add_point', ['view_id', 'x'], [], None),
    ('view_selection_add_region', ['view_id', 'a', 'b', 'pos'], [], None),
    ('view_selection_clear', ['view_id'], [], None),
    ('view_selection_contains', ['view_id', 'a', 'b'], [], None),
    ('view_selection_erase', ['view_id', 'index'], [], None),
    ('view_selection_get', ['view_id', 'index'], [], None),
    ('view_selection_size', ['view_id'], [], None),
    ('view_selection_subtract_region', ['view_id', 'a', 'b'], [], None),
    ('view_set_encoding', ['view_id', 'encoding_name'], [], None),
    ('view_set_line_endings', ['view_id', 'line_ending_name'], [], None),
    ('view_set_name', ['view_id', 'name'], [], None),
    ('view_set_overwrite_status', ['view_id', 'value'], [], None),
    ('view_set_read_only', ['view_id', 'read_only'], [], None),
    ('view_set_reference_document', ['view_id', 'reference'], [], None),
    ('view_set_scratch', ['view_id', 'scratch'], [], None),
    ('view_set_status', ['view_id', 'key', 'value'], [], None),
    ('view_set_viewport_position', ['view_id', 'xy', 'animate'], [], None),
    ('view_settings', ['view_id'], [], None),
    ('view_show_point', ['view_id', 'x', 'show_surrounds'], [], None),
    ('view_show_point_at_center', ['view_id', 'x'], [], None),
    ('view_show_popup',
     ['view_id', 'location', 'content', 'flags', 'max_width', 'max_height', 'on_navigate', 'on_hide'],
     [],
     None),
    ('view_show_popup_table', ['view_id', 'items', 'on_select', 'flags', 'sel'], [], None),
    ('view_show_region', ['view_id', 'x', 'show_surrounds'], [], None),
    ('view_show_region_at_center', ['view_id', 'x'], [], None),
    ('view_size', ['view_id'], [], None),
    ('view_split_by_newlines', ['view_id', 'r'], [], None),
    ('view_style', ['view_id'], [], None),
    ('view_style_for_scope', ['view_id', 'scope'], [], None),
    ('view_substr', [], [], None),
    ('view_symbols', ['view_id'], [], None),
    ('view_text_point', ['view_id', 'row', 'col'], [], None),
    ('view_text_to_layout', ['view_id', 'tp'], [], None),
    ('view_unfold_region', ['view_id', 'x'], [], None),
    ('view_unfold_regions', ['view_id', 'x'], [], None),
    ('view_update_popup_content', ['view_id', 'content'], [], None),
    ('view_viewport_extents', ['view_id'], [], None),
    ('view_viewport_position', ['view_id'], [], None),
    ('view_visible_region', ['view_id'], [], None),
    ('view_window', ['view_id'], [], None),
    ('view_window_to_layout', ['view_id', 'tp'], [], None),
    ('view_word_from_point', ['view_id', 'x'], [], None),
    ('view_word_from_region', ['view_id', 'x'], [], None),
    ('window_active_group', ['window_id'], [], None),
    ('window_active_panel', ['window_id'], [], None),
    ('window_active_sheet', ['window_id'], [], None),
    ('window_active_sheet_in_group', ['window_id', 'group'], [], None),
    ('window_active_view', ['window_id'], [], None),
    ('window_active_view_in_group', ['window_id', 'group'], [], None),
    ('window_can_accept_input', ['window_id', 'name', 'args'], [], None),
    ('window_close_file', ['window_id', 'view_id'], [], None),
    ('window_create_output_panel', ['window_id', 'name', 'unlisted'], [], None),
    ('window_destroy_output_panel', ['window_id', 'name'], [], None),
    ('window_extract_variables', ['window_id'], [], None),
    ('window_find_open_file', ['window_id', 'fname'], [], None),
    ('window_find_output_panel', ['window_id', 'name'], [], None),
    ('window_focus_group', ['window_id', 'idx'], [], None),
    ('window_focus_sheet', ['window_id', 'sheet_id'], [], None),
    ('window_focus_view', ['window_id', 'view_id'], [], None),
    ('window_folders', ['window_id'], [], None),
    ('window_get_layout', ['window_id'], [], None),
    ('window_get_project_data', ['window_id'], [], None),
    ('window_get_sheet_index', ['window_id', 'sheet_id'], [], None),
    ('window_get_view_index', ['window_id', 'view_id'], [], None),
    ('window_is_dragging', [], [], None),
    ('window_is_ui_element_visible', ['window_id', 'val'], [], None),
    ('window_lookup_references', ['window_id', 'sym'], [], None),
    ('window_lookup_references_in_open_files', ['window_id', 'sym'], [], None),
    ('window_lookup_symbol', ['window_id', 'sym'], [], None),
    ('window_lookup_symbol_in_open_files', ['window_id', 'sym'], [], None),
    ('window_new_file', ['window_id', 'flags', 'syntax'], [], None),
    ('window_num_groups', ['window_id'], [], None),
    ('window_open_file', ['window_id', 'fname', 'flags', 'group'], [], None),
    ('window_panels', ['window_id'], [], None),
    ('window_project_file_name', ['window_id'], [], None),
    ('window_run_command', ['window_id', 'cmd', 'args'], [], None),
    ('window_set_layout', ['window_id', 'layout'], [], None),
    ('window_set_project_data', ['window_id', 'v'], [], None),
    ('window_set_sheet_index', ['window_id', 'sheet_id', 'group', 'idx'], [], None),
    ('window_set_ui_element_visible', ['window_id', 'val', 'flag'], [], None),
    ('window_set_view_index', ['window_id', 'view_id', 'group', 'idx'], [], None),
    ('window_settings', ['window_id'], [], None),
    ('window_sheets', ['window_id'], [], None),
    ('window_sheets_in_group', ['window_id', 'group'], [], None),
    ('window_show_input_panel',
     ['window_id', 'caption', 'initial_text', 'on_done', 'on_change', 'on_cancel'],
     [],
     None),
    ('window_show_quick_panel',
     ['window_id', 'flat_items', 'items_per_row', 'on_select', 'on_highlight', 'flags', 'selected_index'],
     [],
     None),
    ('window_status_message', ['window_id', 'msg'], [], None),
    ('window_system_handle', ['window_id'], [], None),
    ('window_template_settings', ['window_id'], [], None),
    ('window_transient_sheet_in_group', ['window_id', 'group'], [], None),
    ('window_transient_view_in_group', ['window_id', 'group'], [], None),
    ('window_views', ['window_id'], [], None),
    ('window_views_in_group', ['window_id', 'group'], [], None),
    ('windows', [], [], None),
    ('yes_no_cancel_dialog', ['msg', 'yes_title', 'no_title'], [], None)
]


