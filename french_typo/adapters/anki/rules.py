import re


def add_nbsp_with_anki_tags(text: str) -> str:
    """
    Ajoute des espaces insécables en tenant compte
    des spécificités Anki (HTML + cloze {{ }}).
    """

    # }} suivi d'un symbole
    text = re.sub(r'(}})\s*([:;!?%€$])', r'\1&nbsp;\2', text)
    text = re.sub(r'(}})\s*([°CkmgLhmin])', r'\1&nbsp;\2', text)

    # n<sup>o</sup> suivi d'un chiffre ou d'une cloze
    text = re.sub(r'(n<sup>o)&nbsp;</sup>(\{\{.*?\}\})', r'\1</sup>&nbsp;\2', text)
    text = re.sub(r'(n<sup>o</sup>)(\{\{.*?\}\})', r'\1&nbsp;\2', text)
    text = re.sub(r'(n<sup>o</sup>)\s*(\d+)', r'\1&nbsp;\2', text)

    # espace après suffixes ordinaux HTML
    text = re.sub(
        r'(<sup>er</sup>|<sup>o</sup>|<sup>e</sup>|<sup>d</sup>)\s+',
        r'\1&nbsp;',
        text,
    )

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
