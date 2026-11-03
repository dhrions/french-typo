# tests/test_multiple_spaces.py
import pytest
from french_typo.core.rules.useless_spaces import remove_useless_spaces

def test_remove_useless_spaces():
    # Espaces normaux
    assert remove_useless_spaces("Hello   world") == "Hello world"
    assert remove_useless_spaces("  Hello   world  ") == "Hello world"
    # Mélange d'espaces normaux et &nbsp;
    assert remove_useless_spaces("Hello&nbsp; &nbsp;world") == "Hello world"
    # Texte sans espaces multiples
    assert remove_useless_spaces("Hello world") == "Hello world"
    # Texte vide
    assert remove_useless_spaces("") == ""
    # Tabulations
    assert remove_useless_spaces("Hello\t\tworld") == "Hello world"

def test_remove_space_before_dot():
    assert remove_useless_spaces("Bonjour .") == "Bonjour."
    assert remove_useless_spaces("Bonjour  .") == "Bonjour."
    assert remove_useless_spaces("Fin de phrase .\n") == "Fin de phrase.\n"
    assert remove_useless_spaces("A . B . C .") == "A. B. C."
    assert remove_useless_spaces("Attendez ...") == "Attendez..."


def test_keep_space_before_dotted_name():
    # Un point suivi d'un caractère de mot ouvre un nom (dossier ou fichier
    # caché), pas une fin de phrase : l'espace qui le précède reste.
    assert remove_useless_spaces("du dossier .claude/commands/ du coffre") == "du dossier .claude/commands/ du coffre"
    assert remove_useless_spaces("le fichier .gitignore et le dossier .venv") == "le fichier .gitignore et le dossier .venv"
    assert remove_useless_spaces("le chemin ./images") == "le chemin ./images"
