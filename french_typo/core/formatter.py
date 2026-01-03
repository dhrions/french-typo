from .profiles import TypoProfile
from .rules import (
    remove_all_nbsp,
    remove_useless_spaces,
    normalize_units,
    format_sup_numbers,
    add_nbsp,
)


def format_text(
    text: str,
    *,
    add_nbsp_enabled: bool = False,
) -> str:
    """
    Applique les règles typographiques françaises.

    Paramètres :
    - add_nbsp_enabled : ajoute les espaces insécables (&nbsp;)
    """

    text = remove_all_nbsp(text)
    text = remove_useless_spaces(text)
    text = normalize_units(text)
    text = format_sup_numbers(text)

    if add_nbsp_enabled:
        text = add_nbsp(text)

    return text
