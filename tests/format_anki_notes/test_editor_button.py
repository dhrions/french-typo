# # tests/test_editor_button.py
# from unittest.mock import MagicMock, patch
# from format_anki_notes.editor.button import add_format_button_to_editor
# from format_anki_notes.logger import get_logger

# def test_add_format_button_to_editor_already_exists(mocker):
#     mock_editor = MagicMock()
#     mock_editor._links = [{'cmd': 'format_note'}]
#     mocker.patch('format_anki_notes.editor.button.get_logger')
#     add_format_button_to_editor(mock_editor)
#     assert 'déjà présent' in str(get_logger().debug.call_args[0][0])
