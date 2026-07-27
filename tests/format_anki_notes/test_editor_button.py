from format_anki_notes.editor.button import add_format_button_to_editor


def test_add_format_button_to_editor_already_exists(mocker):
    mock_logger = mocker.MagicMock()
    mocker.patch("format_anki_notes.editor.button.get_logger", return_value=mock_logger)

    mock_editor = mocker.MagicMock()
    mock_editor._links = [{"cmd": "format_note"}]

    add_format_button_to_editor(mock_editor)

    mock_logger.debug.assert_called_once_with("Bouton 'Formater' déjà présent dans l'éditeur.")
    mock_editor.addButton.assert_not_called()


def test_add_format_button_to_editor_adds_button(mocker):
    mock_logger = mocker.MagicMock()
    mocker.patch("format_anki_notes.editor.button.get_logger", return_value=mock_logger)

    mock_editor = mocker.MagicMock()
    mock_editor._links = []

    add_format_button_to_editor(mock_editor)

    mock_editor.addButton.assert_called_once()
    _, kwargs = mock_editor.addButton.call_args
    assert kwargs["cmd"] == "format_note"
    assert kwargs["label"] == "Formater"
    mock_logger.info.assert_called_once_with("Bouton 'Formater' ajouté à l'éditeur.")
