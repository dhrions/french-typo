"""Stub léger du module `aqt` (API Anki) quand l'add-on Anki n'est pas installé.

`aqt` n'est pas une dépendance pip légère (c'est le frontend Qt d'Anki, non
publié séparément sur PyPI pour un usage headless) : en CI, seul un stub est
disponible. En développement local avec un vrai environnement Anki (`env/`),
ce stub ne s'active pas — le vrai module est utilisé.

`mw = None` reproduit le comportement réel du module `aqt` avant
l'initialisation de l'application Anki (cf. `format_anki_notes/logger.py`).
"""

import sys
from unittest.mock import MagicMock

if "aqt" not in sys.modules:
    try:
        import aqt  # noqa: F401
    except ImportError:
        aqt_stub = MagicMock(name="aqt")
        aqt_stub.mw = None
        sys.modules["aqt"] = aqt_stub
        sys.modules["aqt.editor"] = MagicMock(name="aqt.editor")
        sys.modules["aqt.utils"] = MagicMock(name="aqt.utils")
        sys.modules["aqt.qt"] = MagicMock(name="aqt.qt")
        sys.modules["aqt.gui_hooks"] = MagicMock(name="aqt.gui_hooks")
