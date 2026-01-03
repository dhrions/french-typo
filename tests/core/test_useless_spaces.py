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
