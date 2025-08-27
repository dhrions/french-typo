import re


def format_sup_numbers(text):
    """
    Transforme les suffixes ordinaux en exposant :
    - 1er → 1<sup>er</sup>
    - 2e → 2<sup>e</sup>
    - 2d → 2<sup>d</sup>
    - 3e → 3<sup>e</sup>
    - n° → n<sup>o</sup>
    """
    # Gestion des suffixes ordinaux (1er, 2e, 2d, 3e, etc.)
    text = re.sub(r'(\d+)(er|e|d)\b', r'\1<sup>\2</sup>', text)
    # Gestion de n° → n<sup>o</sup>
    text = re.sub(r'n°', r'n<sup>o</sup>', text)
    return text
