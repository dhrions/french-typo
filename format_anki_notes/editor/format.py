# format_anki_notes/editor/format.py
from aqt import mw
from aqt.utils import showInfo
from aqt.editor import Editor

from ..format_note import format_note
from ..logger import get_logger


def format_current_note(editor: Editor) -> None:
    """Formate la note actuellement ouverte dans l’éditeur."""
    logger = get_logger()

    try:
        note = editor.note
        modified = format_note(note)

        if modified:
            mw.col.update_note(note)
            editor.loadNote()
            showInfo("Note formatée avec succès.")
        else:
            showInfo("Aucune modification nécessaire.")

    except Exception as e:
        logger.error(
            f"Erreur lors du formatage de la note : {e}",
            exc_info=True,
        )
        showInfo(f"Erreur lors du formatage : {e}")
