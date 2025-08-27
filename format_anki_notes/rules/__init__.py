# format_anki_notes/rules/__init__.py
from .nbsps import remove_all_nbsp, add_nbsp
from .units import normalize_units
from .numbers import format_sup_numbers
from .multiple_spaces import remove_multiple_spaces
from. anki_specific import format_anki_specific_rules 

__all__ = [
    'remove_all_nbsp',
    'add_nbsp',
    'normalize_units',
    'format_sup_numbers',
    'remove_multiple_spaces',
    'format_anki_specific_rules' 
]
