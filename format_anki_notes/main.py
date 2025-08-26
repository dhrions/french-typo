# format_anki_notes/main.py
from .rules import (
    remove_all_nbsp,
    remove_multiple_spaces,
    normalize_units,
    format_sup_numbers,
    add_nbsp
)

def format_text(text):
    """
    Applique toutes les transformations typographiques dans l'ordre :
    1. Supprime les &nbsp; existants
    2. Supprime les espaces sécables multiples
    3. Normalise les unités
    4. Formate les numéros
    5. Ajoute les espaces insécables
    """
    text = remove_all_nbsp(text)
    text = remove_multiple_spaces(text)
    text = normalize_units(text)
    text = format_sup_numbers(text)
    text = add_nbsp(text)
    return text
