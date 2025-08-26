import logging
import os
from aqt import mw

_LOGGER = None

def get_logger():
    global _LOGGER
    if _LOGGER is not None:
        return _LOGGER
    _LOGGER = logging.getLogger("FormatAnkiNotes")
    _LOGGER.setLevel(logging.DEBUG)
    try:
        if not hasattr(mw, 'pm') or mw.pm is None:
            print("[FormatAnkiNotes] Attention : mw.pm non disponible, logs dans la console.")
            handler = logging.StreamHandler()
        else:
            log_dir = os.path.join(mw.pm.profileFolder(), "addons", "format_anki_notes_logs")
            os.makedirs(log_dir, exist_ok=True)
            log_file = os.path.join(log_dir, "format_anki_notes.log")
            handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        _LOGGER.addHandler(handler)
    except Exception as e:
        print(f"[FormatAnkiNotes] Erreur lors de la configuration du logger : {e}")
        _LOGGER = logging.getLogger("FormatAnkiNotes")
        _LOGGER.addHandler(logging.StreamHandler())
    return _LOGGER
