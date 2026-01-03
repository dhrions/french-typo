import re

BULLET_LINE = re.compile(r'^\*\s+.*[A-Za-z0-9]$')

def punctuate_bullet_line(
    line: str,
    *,
    is_last: bool,
) -> str:
    """
    Ajoute la ponctuation correcte à une ligne de liste AsciiDoc :
    - ' ;' si ce n'est PAS le dernier item
    - ' .' si c'est le dernier item
    """
    if not BULLET_LINE.match(line):
        return line

    # Ne rien faire si déjà ponctué correctement
    if line.rstrip().endswith((" ;", " .")):
        return line

    return line + ("." if is_last else " ;")

