# # tests/test_browser_menu.py
# from unittest.mock import MagicMock, patch
# from format_anki_notes.browser.menu import add_format_menu_to_browser
# from format_anki_notes.logger import get_logger

# def test_add_format_menu_to_browser_menu_not_found(mocker):
#     mock_browser = MagicMock()
#     mock_browser.menuBar.return_value.actions.return_value = []
#     mocker.patch('format_anki_notes.browser.menu.get_logger')
#     add_format_menu_to_browser(mock_browser)
#     assert 'Menu "Notes" introuvable' in str(get_logger().error.call_args[0][0])

# def test_add_format_menu_to_browser_action_exists(mocker):
#     mock_browser = MagicMock()
#     mock_menu = MagicMock()
#     mock_action = MagicMock()
#     mock_action.text.return_value = "&Notes"
#     mock_action.menu.return_value = mock_menu
#     mock_existing_action = MagicMock()
#     mock_existing_action.text.return_value = "Formater les notes sélectionnées"
#     mock_menu.actions.return_value = [mock_existing_action]
#     mock_browser.menuBar.return_value.actions.return_value = [mock_action]
#     mocker.patch('format_anki_notes.browser.menu.get_logger')
#     add_format_menu_to_browser(mock_browser)
#     assert 'existe déjà' in str(get_logger().info.call_args[0][0])
