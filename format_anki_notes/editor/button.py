# format_anki_notes/editor/button.py
from aqt import mw
from aqt.editor import Editor
from aqt.utils import showInfo
from ..logger import get_logger
from .format import format_current_note

def add_format_button_to_editor(editor: Editor) -> None:
    """Ajoute un bouton 'Formater' à l'éditeur de notes, sans doublons."""
    logger = get_logger()
    for link in getattr(editor, '_links', []):
        if isinstance(link, dict) and link.get('cmd') == "format_note":
            logger.debug("Bouton 'Formater' déjà présent dans l'éditeur.")
            return
    editor.addButton(
        icon=None,
        cmd="format_note",
        func=lambda e=editor: format_current_note(e),
        tip="Formater la note selon les règles typographiques françaises (n°, espaces insécables, etc.)",
        label="Formater",
        keys="Ctrl+Shift+F",
    )
    logger.info("Bouton 'Formater' ajouté à l'éditeur.")
