import re

from french_typo.core.rules.nbsps import add_ordinal_suffix_nbsp


def add_nbsp_with_anki_tags(text: str) -> str:
    """
    Ajoute des espaces insécables en tenant compte
    des spécificités Anki (HTML + cloze {{ }}).
    """

    # }} suivi d'un symbole
    text = re.sub(r'(}})\s*([:;!?%€$])', r'\1&nbsp;\2', text)
    text = re.sub(r'(}})\s*([°CkmgLhmin])', r'\1&nbsp;\2', text)

    # n<sup>o</sup> et suffixes ordinaux HTML suivis d'un chiffre ou d'une cloze
    text = add_ordinal_suffix_nbsp(text)

    return text


def remove_multiple_nbsps(text: str) -> str:
    """Réduit plusieurs &nbsp; consécutifs à un seul."""
    return re.sub(r'(&nbsp;)+', '&nbsp;', text)


def format_anki_specific_rules(text: str) -> str:
    """
    Applique toutes les règles spécifiques à Anki.
    """
    text = add_nbsp_with_anki_tags(text)
    text = remove_multiple_nbsps(text)
    return text
