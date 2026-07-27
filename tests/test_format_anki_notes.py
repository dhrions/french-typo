from format_anki_notes.format_anki_notes import initialize_addon


def test_initialize_addon_registers_hooks(mocker):
    mocker.patch("format_anki_notes.format_anki_notes.get_logger", return_value=mocker.MagicMock())
    mock_gui_hooks = mocker.patch("format_anki_notes.format_anki_notes.gui_hooks")

    initialize_addon()

    from format_anki_notes.editor.button import add_format_button_to_editor
    from format_anki_notes.browser.menu import add_format_menu_to_browser

    mock_gui_hooks.editor_did_init.append.assert_called_once_with(add_format_button_to_editor)
    mock_gui_hooks.browser_will_show.append.assert_called_once_with(add_format_menu_to_browser)
