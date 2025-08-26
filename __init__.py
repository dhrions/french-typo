# __init__.py (racine)
from aqt import mw
from anki.hooks import addHook

def load_addon():
    try:
        from .format_anki_notes import format_anki_notes  # Importe le module
        format_anki_notes.initialize_addon()  # Appelle la fonction
    except Exception as e:
        print(f"[FormatAnkiNotes] Erreur lors du chargement de l'add-on : {e}")

# Charge l'add-on après le chargement du profil
addHook("profileLoaded", load_addon)
