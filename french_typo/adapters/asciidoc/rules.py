import re

BULLET_LINE = re.compile(r'^\*\s+.*')


def punctuate_bullet_line(
    line: str,
    *,
    is_last: bool,
) -> str:
    """
    Ajoute la ponctuation correcte à une ligne de liste AsciiDoc :
    - ' ;' si ce n'est PAS le dernier item
    - ' .' si c'est le dernier item

    La ponctuation existante est normalisée si nécessaire.
    """
    if not BULLET_LINE.match(line):
        return line

    # Supprimer toute ponctuation finale existante
    line = re.sub(r'[ \t]*[.;]\s*$', '', line)

    return line + ("." if is_last else " ;")
