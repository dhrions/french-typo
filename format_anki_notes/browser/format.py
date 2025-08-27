# format_anki_notes/browser/format.py
from aqt import mw
from aqt.qt import QMessageBox
from aqt.utils import showInfo
from ..main import format_text
from ..logger import get_logger

def format_selected_notes_in_browser(browser):
    """Formate les notes sélectionnées dans le navigateur."""
    logger = get_logger()
    logger.info("format_selected_notes_in_browser appelé !")
    try:
        if not hasattr(browser, 'selectedNotes'):
            logger.warning("browser.selectedNotes non disponible.")
            showInfo("Veuillez sélectionner des notes dans le navigateur.")
            return
        selected_notes = browser.selectedNotes()
        logger.info(f"Notes sélectionnées : {selected_notes}")
        if not selected_notes:
            showInfo("Aucune note sélectionnée.")
            return
        confirm = QMessageBox.question(
            browser,
            "Formater les notes",
            f"Voulez-vous vraiment formater {len(selected_notes)} notes ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm != QMessageBox.StandardButton.Yes:
            logger.info("Formatage annulé par l'utilisateur.")
            return
        count = 0
        for note_id in selected_notes:
            try:
                note = mw.col.get_note(note_id)
                logger.info(f"Traitement de la note {note_id} (champs : {note.keys()})")
                modified = False
                for field_name in note.keys():
                    original_html = note[field_name]
                    formatted_html = format_text(original_html, is_anki=True)
                    if formatted_html != original_html:
                        note[field_name] = formatted_html
                        modified = True
                        logger.info(f"Champ '{field_name}' modifié.")
                if modified:
                    mw.col.update_note(note)
                    count += 1
                    logger.info(f"Note {note_id} formatée.")
            except Exception as e:
                logger.error(f"Erreur pour la note {note_id} : {e}", exc_info=True)
        showInfo(f"{count} notes formatées avec succès !")
        logger.info(f"{count} notes formatées avec succès.")
    except Exception as e:
        logger.error(f"Erreur inattendue : {e}", exc_info=True)
        showInfo(f"Erreur inattendue : {e}")
