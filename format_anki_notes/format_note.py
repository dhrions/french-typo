# format_anki_notes/format_note.py
from french_typo.adapters.anki.formatter import format_anki_html


def format_note(note) -> bool:
    """Formate tous les champs d'une note Anki. Retourne True si un champ a été modifié."""
    modified = False

    for field_name in note.keys():
        original = note[field_name]
        formatted = format_anki_html(original)

        if formatted != original:
            note[field_name] = formatted
            modified = True

    return modified
