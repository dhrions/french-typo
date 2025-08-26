# format_anki_notes/format_anki_notes.py
from aqt import mw, gui_hooks
from .logger import get_logger
from .editor.button import add_format_button_to_editor
from .browser.menu import add_format_menu_to_browser

def initialize_addon():
    """Initialise l'add-on en enregistrant les hooks."""
    logger = get_logger()
    logger.info("Initialisation de l'add-on...")
    gui_hooks.editor_did_init.append(add_format_button_to_editor)
    gui_hooks.browser_will_show.append(add_format_menu_to_browser)
    logger.info("Hooks enregistrés.")
