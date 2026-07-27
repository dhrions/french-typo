from format_anki_notes.browser.format import format_selected_notes_in_browser


def test_format_selected_notes_no_selection_method(mocker):
    mock_logger = mocker.MagicMock()
    mocker.patch("format_anki_notes.browser.format.get_logger", return_value=mock_logger)
    mock_show_info = mocker.patch("format_anki_notes.browser.format.showInfo")

    mock_browser = mocker.MagicMock(spec=[])

    format_selected_notes_in_browser(mock_browser)

    mock_logger.warning.assert_called_once_with("browser.selectedNotes non disponible.")
    mock_show_info.assert_called_once_with("Veuillez sélectionner des notes dans le navigateur.")


def test_format_selected_notes_empty_selection(mocker):
    mocker.patch("format_anki_notes.browser.format.get_logger", return_value=mocker.MagicMock())
    mock_show_info = mocker.patch("format_anki_notes.browser.format.showInfo")

    mock_browser = mocker.MagicMock()
    mock_browser.selectedNotes.return_value = []

    format_selected_notes_in_browser(mock_browser)

    mock_show_info.assert_called_once_with("Aucune note sélectionnée.")


def test_format_selected_notes_user_cancels(mocker):
    mock_logger = mocker.MagicMock()
    mocker.patch("format_anki_notes.browser.format.get_logger", return_value=mock_logger)

    from format_anki_notes.browser.format import QMessageBox

    mocker.patch.object(QMessageBox, "question", return_value=QMessageBox.StandardButton.No)

    mock_browser = mocker.MagicMock()
    mock_browser.selectedNotes.return_value = [123]

    format_selected_notes_in_browser(mock_browser)

    mock_logger.info.assert_any_call("Formatage annulé par l'utilisateur.")


def test_format_selected_notes_success(mocker):
    mocker.patch("format_anki_notes.browser.format.get_logger", return_value=mocker.MagicMock())
    mock_show_info = mocker.patch("format_anki_notes.browser.format.showInfo")
    mock_mw = mocker.patch("format_anki_notes.browser.format.mw")
    mocker.patch("format_anki_notes.browser.format.format_note", return_value=True)

    from format_anki_notes.browser.format import QMessageBox

    mocker.patch.object(QMessageBox, "question", return_value=QMessageBox.StandardButton.Yes)

    mock_browser = mocker.MagicMock()
    mock_browser.selectedNotes.return_value = [123, 456]

    format_selected_notes_in_browser(mock_browser)

    assert mock_mw.col.update_note.call_count == 2
    mock_show_info.assert_called_once_with("2 notes formatées avec succès.")


def test_format_selected_notes_note_error(mocker):
    mock_logger = mocker.MagicMock()
    mocker.patch("format_anki_notes.browser.format.get_logger", return_value=mock_logger)
    mocker.patch("format_anki_notes.browser.format.showInfo")
    mock_mw = mocker.patch("format_anki_notes.browser.format.mw")
    mock_mw.col.get_note.side_effect = Exception("Note introuvable")

    from format_anki_notes.browser.format import QMessageBox

    mocker.patch.object(QMessageBox, "question", return_value=QMessageBox.StandardButton.Yes)

    mock_browser = mocker.MagicMock()
    mock_browser.selectedNotes.return_value = [123]

    format_selected_notes_in_browser(mock_browser)

    mock_logger.error.assert_called_once_with(
        "Erreur lors du formatage de la note 123 : Note introuvable",
        exc_info=True,
    )
