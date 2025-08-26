# format_anki_notes/__init__.py
from aqt import mw, gui_hooks
from .logger import get_logger
from .format_anki_notes import initialize_addon

def initialize_all():
    """Initialise le logger et l'add-on."""
    try:
        mw.format_anki_notes_logger = get_logger()
        mw.format_anki_notes_logger.info("Logger initialisé avec succès.")
        initialize_addon()
    except Exception as e:
        print(f"[FormatAnkiNotes] Erreur lors de l'initialisation : {e}")

# Initialise après le chargement du profil
gui_hooks.profile_did_open.append(initialize_all)
