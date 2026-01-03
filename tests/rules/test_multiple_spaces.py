# tests/test_multiple_spaces.py
import pytest
from french_typo.core.rules.multiple_spaces import remove_multiple_spaces

def test_remove_multiple_spaces():
    # Espaces normaux
    assert remove_multiple_spaces("Hello   world") == "Hello world"
    assert remove_multiple_spaces("  Hello   world  ") == "Hello world"
    # Mélange d'espaces normaux et &nbsp;
    assert remove_multiple_spaces("Hello&nbsp; &nbsp;world") == "Hello world"
    # Texte sans espaces multiples
    assert remove_multiple_spaces("Hello world") == "Hello world"
    # Texte vide
    assert remove_multiple_spaces("") == ""
    # Tabulations
    assert remove_multiple_spaces("Hello\t\tworld") == "Hello world"
