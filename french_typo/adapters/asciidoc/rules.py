import re

BULLET_LINE = re.compile(r'^\*\s+.*')


def punctuate_bullet_line(
    line: str,
    *,
    is_last: bool,
    add_nbsp: bool = False,
) -> str:
    """
    Ajoute la ponctuation correcte à une ligne de liste AsciiDoc :
    - ' ;' (ou '&nbsp;;' si add_nbsp) si ce n'est PAS le dernier item
    - '.' si c'est le dernier item

    La ponctuation existante est normalisée si nécessaire.
    """
    if not BULLET_LINE.match(line):
        return line

    # Supprimer toute ponctuation finale existante. Cette fonction tourne
    # après add_nbsp() : une espace déjà normalisée en '&nbsp;' doit être
    # reconnue au même titre qu'une espace normale, sinon elle survit au
    # nettoyage et se retrouve dupliquée par la ponctuation rajoutée plus bas
    # (ex: 'mot&nbsp;;' -> nettoyage incomplet -> 'mot&nbsp; ;').
    space_or_nbsp = r'(?:[ \t]|&nbsp;)'
    line = re.sub(rf'{space_or_nbsp}*[.;]{space_or_nbsp}*$', '', line)

    if is_last:
        return line + "."
    return line + ("&nbsp;;" if add_nbsp else " ;")
