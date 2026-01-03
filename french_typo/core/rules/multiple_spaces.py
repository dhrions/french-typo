# format_anki_notes/rules/multiple_spaces.py
import re

def remove_multiple_spaces(text):
    """
    Supprime les espaces sécables multiples dans le texte.
    Remplace deux ou plusieurs espaces consécutifs par un seul espace.
    Gère aussi les mélanges d'espaces normaux et d'espaces insécables (&nbsp;).

    Args:
        text (str): Le texte à nettoyer.

    Returns:
        str: Le texte avec les espaces multiples remplacés.
    """
    # Remplace les espaces insécables multiples
    text = re.sub(r'(&nbsp;\s*)+', ' ', text)
    # Remplace les espaces normaux multiples
    text = re.sub(r'[ \t]+', ' ', text)
    # Nettoie les espaces en début/fin de ligne
    text = text.strip()
    return text
