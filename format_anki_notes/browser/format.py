# format_anki_notes/browser/format.py
from aqt import mw
from aqt.qt import QMessageBox
from aqt.utils import showInfo

from french_typo.adapters.anki.formatter import format_anki_html

from ..logger import get_logger


def format_selected_notes_in_browser(browser):
    """Formate les notes sélectionnées dans le navigateur."""
    logger = get_logger()
    logger.info("format_selected_notes_in_browser appelé")

    if not hasattr(browser, "selectedNotes"):
        logger.warning("browser.selectedNotes non disponible.")
        showInfo("Veuillez sélectionner des notes dans le navigateur.")
        return

    selected_notes = browser.selectedNotes()
    if not selected_notes:
        showInfo("Aucune note sélectionnée.")
        return

    confirm = QMessageBox.question(
        browser,
        "Formater les notes",
        f"Voulez-vous vraiment formater {len(selected_notes)} notes ?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
    )

    if confirm != QMessageBox.StandardButton.Yes:
        logger.info("Formatage annulé par l'utilisateur.")
        return

    count = 0

    for note_id in selected_notes:
        try:
            note = mw.col.get_note(note_id)
            modified = False

            for field_name in note.keys():
                original = note[field_name]
                formatted = format_anki_html(original)

                if formatted != original:
                    note[field_name] = formatted
                    modified = True

            if modified:
                mw.col.update_note(note)
                count += 1

        except Exception as e:
            logger.error(
                f"Erreur lors du formatage de la note {note_id} : {e}",
                exc_info=True,
            )

    showInfo(f"{count} notes formatées avec succès.")
