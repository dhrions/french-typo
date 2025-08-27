# import pytest
# from unittest.mock import MagicMock, patch
# from aqt.qt import QMessageBox
# from format_anki_notes.browser.format import format_selected_notes_in_browser

# @patch('aqt.utils.showInfo')
# @patch('format_anki_notes.browser.format.get_logger')
# @patch('aqt.mw')
# def test_format_selected_notes_in_browser_no_selection(mock_mw, mock_get_logger, mock_showInfo):
#     # Mock du logger
#     mock_logger = MagicMock()
#     mock_get_logger.return_value = mock_logger

#     # Mock du browser
#     mock_browser = MagicMock()
#     mock_browser.selectedNotes.return_value = []

#     # Exécution
#     format_selected_notes_in_browser(mock_browser)

#     # Vérifications
#     mock_logger.warning.assert_called_with("browser.selectedNotes non disponible.")
#     mock_showInfo.assert_called_with("Veuillez sélectionner des notes dans le navigateur.")

# @patch('aqt.qt.QMessageBox.question')
# @patch('aqt.utils.showInfo')
# @patch('format_anki_notes.browser.format.get_logger')
# @patch('aqt.mw')
# def test_format_selected_notes_in_browser_user_cancel(mock_mw, mock_get_logger, mock_showInfo, mock_question):
#     # Mock du logger
#     mock_logger = MagicMock()
#     mock_get_logger.return_value = mock_logger

#     # Mock de QMessageBox.question pour retourner "No"
#     mock_question.return_value = QMessageBox.StandardButton.No

#     # Mock du browser
#     mock_browser = MagicMock()
#     mock_browser.selectedNotes.return_value = [123]

#     # Exécution
#     format_selected_notes_in_browser(mock_browser)

#     # Vérifications
#     mock_logger.info.assert_called_with("Formatage annulé par l'utilisateur.")

# @patch('aqt.qt.QMessageBox.question')
# @patch('aqt.utils.showInfo')
# @patch('format_anki_notes.browser.format.get_logger')
# @patch('aqt.mw')
# def test_format_selected_notes_in_browser_note_error(mock_mw, mock_get_logger, mock_showInfo, mock_question):
#     # Mock du logger
#     mock_logger = MagicMock()
#     mock_get_logger.return_value = mock_logger

#     # Mock de mw.col
#     mock_col = MagicMock()
#     mock_mw.col = mock_col
#     mock_col.get_note.side_effect = Exception("Note introuvable")

#     # Mock de QMessageBox.question pour retourner "Yes"
#     mock_question.return_value = QMessageBox.StandardButton.Yes

#     # Mock du browser
#     mock_browser = MagicMock()
#     mock_browser.selectedNotes.return_value = [123]

#     # Exécution
#     format_selected_notes_in_browser(mock_browser)

#     # Vérifications
#     mock_logger.error.assert_called_with("Erreur pour la note 123 : Note introuvable", exc_info=True)
#     mock_showInfo.assert_called_with("Erreur inattendue : Note introuvable")
