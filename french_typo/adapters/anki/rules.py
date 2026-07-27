import re

from french_typo.core.rules.nbsps import add_ordinal_suffix_nbsp

_HTML_TAG_PUNCT_NO_SPACE_PATTERN = re.compile(r"(</[^>]+>)([:;!?])")
_NBSP_AFTER_TAG_PATTERN = re.compile(r"(</(?!sup\b)[^>]+>)&nbsp;(?![:;!?])")
_NBSP_AFTER_CLOZE_PATTERN = re.compile(r"(\}\})&nbsp;(?![:;!?%€$»])")


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


def nbsp_before_punctuation_after_tag(text: str) -> str:
    """
    Ajoute un espace insécable avant une ponctuation double collée à une balise
    HTML fermante sans espace (ex : `</b>:` -> `</b>&nbsp;:`).

    Le cas avec espace (`</b> :`) est déjà couvert par add_nbsp() côté core ;
    seul le cas sans espace est spécifique au HTML.
    """
    return _HTML_TAG_PUNCT_NO_SPACE_PATTERN.sub(r"\1&nbsp;\2", text)


def clean_nbsp_after_html_tags(text: str) -> str:
    """
    Supprime les espaces insécables mal placés après les balises HTML fermantes.

    Exceptions : ne touche pas aux nbsp après </sup> (placés intentionnellement
    par les suffixes ordinaux) ni aux nbsp suivis de ponctuation.
    """
    return _NBSP_AFTER_TAG_PATTERN.sub(r"\1 ", text)


def clean_nbsp_after_cloze(text: str) -> str:
    """
    Supprime les espaces insécables mal placés après les balises de cloze `}}`.

    Les nbsp après }} sont conservés uniquement s'ils précèdent une ponctuation.
    """
    return _NBSP_AFTER_CLOZE_PATTERN.sub(r"\1 ", text)


def remove_multiple_nbsps(text: str) -> str:
    """Réduit plusieurs &nbsp; consécutifs à un seul."""
    return re.sub(r'(&nbsp;)+', '&nbsp;', text)


def format_anki_specific_rules(text: str) -> str:
    """
    Applique toutes les règles spécifiques à Anki.
    """
    text = add_nbsp_with_anki_tags(text)
    text = nbsp_before_punctuation_after_tag(text)
    text = remove_multiple_nbsps(text)
    text = clean_nbsp_after_html_tags(text)
    text = clean_nbsp_after_cloze(text)
    return text
