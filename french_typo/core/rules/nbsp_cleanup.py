import re

_COMMA_NBSP_PATTERN = re.compile(r",&nbsp;")
_LEADING_NBSP_PATTERN = re.compile(r"(?m)^(?:&nbsp;)+")


def clean_nbsp_after_comma(text):
    """
    Supprime les espaces insécables placés après une virgule.

    En typographie française, l'espace insécable ne se place jamais après une virgule.
    """
    return _COMMA_NBSP_PATTERN.sub(", ", text)


def clean_leading_nbsp(text):
    """
    Supprime les espaces insécables en début de ligne ou de texte.

    Le flag multiligne couvre à la fois le début du texte et le début de chaque ligne.
    """
    return _LEADING_NBSP_PATTERN.sub("", text)
