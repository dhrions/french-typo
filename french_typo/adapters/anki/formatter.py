from french_typo.core.formatter import format_text
from french_typo.adapters.anki.rules import format_anki_specific_rules


def format_anki_html(text: str) -> str:
    """
    Formate du contenu HTML Anki (cloze + règles spécifiques).
    """
    text = format_text(
        text,
        add_nbsp_enabled=True,
    )
    text = format_anki_specific_rules(text)
    return text
