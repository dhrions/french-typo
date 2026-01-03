from .profiles import TypoProfile
from .rules import (
    remove_all_nbsp,
    remove_multiple_spaces,
    normalize_units,
    format_sup_numbers,
    add_nbsp,
)

def format_text(text: str, profile: TypoProfile = TypoProfile.PLAIN) -> str:
    """
    Applique les règles typographiques françaises.

    Profils :
    - PLAIN     : texte brut
    - ANKI      : HTML + cloze (géré par l'adapter)
    - ASCIIDOC  : texte AsciiDoc
    """

    text = remove_all_nbsp(text)
    text = remove_multiple_spaces(text)
    text = normalize_units(text)
    text = format_sup_numbers(text)
    text = add_nbsp(text)

    return text
