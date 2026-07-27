from format_anki_notes.editor.format import format_current_note


def test_format_current_note_no_modification(mocker):
    mock_editor = mocker.MagicMock()
    mocker.patch("format_anki_notes.editor.format.format_note", return_value=False)
    mock_show_info = mocker.patch("format_anki_notes.editor.format.showInfo")

    format_current_note(mock_editor)

    mock_show_info.assert_called_once_with("Aucune modification nécessaire.")
    mock_editor.loadNote.assert_not_called()


def test_format_current_note_modified(mocker):
    mock_editor = mocker.MagicMock()
    mocker.patch("format_anki_notes.editor.format.format_note", return_value=True)
    mock_mw = mocker.patch("format_anki_notes.editor.format.mw")
    mock_show_info = mocker.patch("format_anki_notes.editor.format.showInfo")

    format_current_note(mock_editor)

    mock_mw.col.update_note.assert_called_once_with(mock_editor.note)
    mock_editor.loadNote.assert_called_once()
    mock_show_info.assert_called_once_with("Note formatée avec succès.")


def test_format_current_note_error(mocker):
    mock_editor = mocker.MagicMock()
    mocker.patch(
        "format_anki_notes.editor.format.format_note",
        side_effect=Exception("Erreur de mise à jour"),
    )
    mock_logger = mocker.MagicMock()
    mocker.patch("format_anki_notes.editor.format.get_logger", return_value=mock_logger)
    mock_show_info = mocker.patch("format_anki_notes.editor.format.showInfo")

    format_current_note(mock_editor)

    mock_logger.error.assert_called_once_with(
        "Erreur lors du formatage de la note : Erreur de mise à jour",
        exc_info=True,
    )
    mock_show_info.assert_called_once_with("Erreur lors du formatage : Erreur de mise à jour")
