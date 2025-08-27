# # tests/test_format_anki_notes.py
# from unittest.mock import patch
# from format_anki_notes.format_anki_notes import initialize_addon
# from format_anki_notes.logger import get_logger

# def test_initialize_addon_hook_error(mocker):
#     mocker.patch('aqt.gui_hooks.editor_did_init.append', side_effect=Exception("Erreur de hook"))
#     mocker.patch('format_anki_notes.format_anki_notes.get_logger')
#     initialize_addon()
#     assert 'Erreur lors de l\'initialisation' in str(get_logger().error.call_args[0][0])
