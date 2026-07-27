from format_anki_notes.browser.menu import add_format_menu_to_browser


def test_add_format_menu_to_browser_menu_not_found(mocker):
    mock_logger = mocker.MagicMock()
    mocker.patch("format_anki_notes.browser.menu.get_logger", return_value=mock_logger)

    mock_browser = mocker.MagicMock()
    mock_browser.menuBar.return_value.actions.return_value = []

    add_format_menu_to_browser(mock_browser)

    mock_logger.error.assert_called_once_with("Menu 'Notes' introuvable dans le navigateur.")


def test_add_format_menu_to_browser_action_exists(mocker):
    mock_logger = mocker.MagicMock()
    mocker.patch("format_anki_notes.browser.menu.get_logger", return_value=mock_logger)

    mock_menu = mocker.MagicMock()
    mock_existing_action = mocker.MagicMock()
    mock_existing_action.text.return_value = "Formater les notes sélectionnées"
    mock_menu.actions.return_value = [mock_existing_action]

    mock_action = mocker.MagicMock()
    mock_action.text.return_value = "&Notes"
    mock_action.menu.return_value = mock_menu

    mock_browser = mocker.MagicMock()
    mock_browser.menuBar.return_value.actions.return_value = [mock_action]

    add_format_menu_to_browser(mock_browser)

    mock_logger.info.assert_any_call("L'action 'Formater les notes sélectionnées' existe déjà.")
    mock_menu.addAction.assert_not_called()


def test_add_format_menu_to_browser_adds_action(mocker):
    mock_logger = mocker.MagicMock()
    mocker.patch("format_anki_notes.browser.menu.get_logger", return_value=mock_logger)
    # QAction est mocké : avec le vrai PyQt6 (env/ local), construire un QAction
    # avec un `mw` mocké comme parent segfault côté C++ sip/PyQt.
    mock_action_cls = mocker.patch("format_anki_notes.browser.menu.QAction")

    mock_menu = mocker.MagicMock()
    mock_menu.actions.return_value = []

    mock_action = mocker.MagicMock()
    mock_action.text.return_value = "&Notes"
    mock_action.menu.return_value = mock_menu

    mock_browser = mocker.MagicMock()
    mock_browser.menuBar.return_value.actions.return_value = [mock_action]

    add_format_menu_to_browser(mock_browser)

    mock_menu.addAction.assert_called_once()
    mock_logger.info.assert_any_call("Action 'Formater les notes sélectionnées' ajoutée avec succès.")
