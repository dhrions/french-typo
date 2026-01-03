import re


def remove_useless_spaces(text: str) -> str:
    """
    - Considère &nbsp; comme un espace sécable
    - Réduit les espaces sécables multiples à un seul
    - Supprime les espaces sécables en début et fin de ligne
    - Ne touche jamais aux retours à la ligne
    """

    # 0. Normalise tous les &nbsp; en espaces simples
    text = text.replace("&nbsp;", " ")

    # 1. Réduit les séquences d'espaces/tabs internes
    text = re.sub(r"[ \t]{2,}", " ", text)

    # 2. Supprime les espaces sécables en début de ligne
    text = re.sub(r"(?m)^[ \t]+", "", text)

    # 3. Supprime les espaces sécables en fin de ligne
    text = re.sub(r"[ \t]+(?=\r?\n|$)", "", text)

    return text
