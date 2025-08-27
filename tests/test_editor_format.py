# # tests/test_editor_format.py
# from unittest.mock import MagicMock, patch
# from format_anki_notes.editor.format import format_current_note
# from aqt.utils import showInfo
# from format_anki_notes.logger import get_logger

# def test_format_current_note_no_fields(mocker):
#     mock_editor = MagicMock()
#     mock_editor.note = MagicMock()
#     mock_editor.note.keys.return_value = []
#     mocker.patch('aqt.utils.showInfo')
#     format_current_note(mock_editor)
#     assert 'Aucune modification nécessaire' in str(showInfo.call_args[0][0])

# def test_format_current_note_update_error(mocker):
#     mock_editor = MagicMock()
#     mock_editor.note = MagicMock()
#     mock_editor.note.keys.return_value = ['Front']
#     mock_editor.note.__getitem__.return_value = 'Test 1er'
#     mocker.patch('aqt.mw.col.update_note', side_effect=Exception("Erreur de mise à jour"))
#     mocker.patch('aqt.utils.showInfo')
#     format_current_note(mock_editor)
#     assert 'Erreur lors du formatage' in str(showInfo.call_args[0][0])
