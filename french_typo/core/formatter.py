from .html_attributes import mask_attributes, restore_attributes
from .rules import (
    remove_all_nbsp,
    remove_useless_spaces,
    normalize_units,
    format_sup_numbers,
    add_nbsp,
    clean_nbsp_after_comma,
    clean_leading_nbsp,
)


def format_text(
    text: str,
    *,
    add_nbsp_enabled: bool = False,
    format_sup_numbers_enabled: bool = True,
) -> str:
    """
    Applique les règles typographiques françaises.

    Paramètres :
    - add_nbsp_enabled : ajoute les espaces insécables (&nbsp;)
    - format_sup_numbers_enabled : formate les ordinaux et n° en exposant
      (1er, 2e, n°...). Activé par défaut pour ne pas changer le comportement
      des appelants existants ; un consommateur qui expose ce choix (ex. un
      panneau de préférences) passe explicitement False pour le désactiver.

    Les attributs des balises HTML (`src`, `href`, `style`…) ne sont jamais modifiés : ce ne
    sont pas du texte (cf. `html_attributes`).
    """

    text, attributes = mask_attributes(text)

    text = remove_all_nbsp(text)
    text = remove_useless_spaces(text)
    text = normalize_units(text)
    if format_sup_numbers_enabled:
        text = format_sup_numbers(text)

    if add_nbsp_enabled:
        text = add_nbsp(text)
        text = clean_nbsp_after_comma(text)
        text = clean_leading_nbsp(text)

    return restore_attributes(text, attributes)
