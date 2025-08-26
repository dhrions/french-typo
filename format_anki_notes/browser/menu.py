# format_anki_notes/browser/menu.py
from aqt import mw
from aqt.qt import QAction, QMessageBox
from aqt.utils import showInfo
from ..logger import get_logger
from .format import format_selected_notes_in_browser

def add_format_menu_to_browser(browser):
    """Ajoute une entrée de menu 'Formater les notes sélectionnées' au navigateur."""
    logger = get_logger()
    logger.info("Hook browser_will_show déclenché !")
    try:
        menu_notes = None
        for action in browser.menuBar().actions():
            if action.text() == "&Notes":
                menu_notes = action.menu()
                logger.info("Menu 'Notes' trouvé.")
                break
        if not menu_notes:
            logger.error("Menu 'Notes' introuvable dans le navigateur.")
            return
        # Vérifie si l'action existe déjà
        for existing_action in menu_notes.actions():
            if existing_action.text() == "Formater les notes sélectionnées":
                logger.info("L'action 'Formater les notes sélectionnées' existe déjà.")
                return
        # Fonction intermédiaire pour capturer le browser
        def on_format_selected_notes():
            logger.info("Callback 'on_format_selected_notes' appelé !")
            try:
                format_selected_notes_in_browser(browser)
            except Exception as e:
                logger.error(f"Erreur dans le callback : {e}", exc_info=True)
                showInfo(f"Erreur : {e}")
        # Crée l'action
        new_action = QAction("Formater les notes sélectionnées", mw)
        new_action.triggered.connect(on_format_selected_notes)
        menu_notes.addAction(new_action)
        logger.info("Action 'Formater les notes sélectionnées' ajoutée avec succès.")
    except Exception as e:
        logger.error(f"Erreur dans add_format_menu_to_browser : {e}", exc_info=True)
