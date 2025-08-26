# format_anki_notes/editor/format.py
from aqt import mw
from aqt.utils import showInfo
from ..main import format_text
from ..logger import get_logger
from aqt.editor import Editor

def format_current_note(editor: Editor) -> None:
    """Formate la note actuelle avec les règles typographiques françaises."""
    logger = get_logger()
    try:
        note = editor.note
        modified = False
        for field_name in note.keys():
            if field_name in note:
                original_text = note[field_name]
                formatted_text = format_text(original_text)
                if not isinstance(formatted_text, str):
                    formatted_text = original_text
                if formatted_text != original_text:
                    note[field_name] = formatted_text
                    modified = True
        if modified:
            mw.col.update_note(note)
            editor.loadNote()
            showInfo("Note formatée avec succès !")
            logger.info(f"Note {note.id} formatée avec succès.")
        else:
            showInfo("Aucune modification nécessaire.")
            logger.debug("Aucune modification nécessaire pour cette note.")
    except Exception as e:
        showInfo(f"Erreur lors du formatage : {str(e)}")
        logger.error(f"Erreur détaillée : {str(e)}", exc_info=True)
