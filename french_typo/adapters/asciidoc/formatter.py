from pathlib import Path
import re

from french_typo.core.formatter import format_text
from french_typo.adapters.asciidoc.protected import mask_protected, restore_protected
from french_typo.adapters.asciidoc.rules import punctuate_bullet_line

IGNORED_PREFIXES = ("//",)
BULLET_START = re.compile(r'^\*\s+')
INTRO_LINE = re.compile(r'.+:\s*$')
# Delimiters of blocks whose content is not prose: listing, literal, passthrough
# (a `[stem]` formula lives in a `++++` block).
VERBATIM_DELIMITERS = ("----", "....", "++++")
# The core engine writes superscripts as HTML, which Asciidoctor displays verbatim:
# AsciiDoc has its own syntax (`1^er^`).
HTML_SUP = re.compile(r'<sup>(.*?)</sup>')


def _format_prose(line: str, *, add_nbsp: bool) -> str:
    """Apply the core rules to a line, leaving formulas, URLs, macro targets and code alone."""
    masked, spans = mask_protected(line)
    formatted = format_text(masked, add_nbsp_enabled=add_nbsp)
    formatted = HTML_SUP.sub(r'^\1^', formatted)
    return restore_protected(formatted, spans)


def _format_lines(lines: list, *, add_nbsp: bool, punctuate_lists: bool = True) -> list:
    """
    Applique aux lignes d'un document AsciiDoc :
    - les règles typographiques générales (core)
    - les règles spécifiques AsciiDoc :
      - ignore les blocs littéraux (----)
      - ignore les commentaires //
      - ponctue correctement les listes :
        * ';' pour les items intermédiaires
        * '.' pour le dernier item
      - insère une ligne vide après une phrase introductive
        se terminant par ':' avant une liste
    """
    result = []
    in_literal_block = False
    open_delimiter = None

    for i, line in enumerate(lines):
        # Ligne vide → conservée telle quelle
        if line == "":
            result.append(line)
            continue

        # Détection des blocs littéraux (listing, littéral, passthrough)
        stripped = line.strip()
        if stripped in VERBATIM_DELIMITERS and open_delimiter in (None, stripped):
            in_literal_block = not in_literal_block
            open_delimiter = stripped if in_literal_block else None
            result.append(line)
            continue

        # Ignorer blocs littéraux et commentaires
        if in_literal_block or line.lstrip().startswith(IGNORED_PREFIXES):
            result.append(line)
            continue

        next_line = lines[i + 1] if i + 1 < len(lines) else ""

        # 🔹 Règle : ligne introductive avant une liste
        if INTRO_LINE.match(line) and BULLET_START.match(next_line):
            formatted = _format_prose(line, add_nbsp=add_nbsp)
            result.append(formatted)
            result.append("")
            continue

        # 1. Typographie générale
        formatted = _format_prose(line, add_nbsp=add_nbsp)

        # 2. Règles spécifiques aux listes AsciiDoc
        if punctuate_lists and BULLET_START.match(formatted):
            is_last = not BULLET_START.match(next_line.lstrip())

            formatted = punctuate_bullet_line(
                formatted,
                is_last=is_last,
                add_nbsp=add_nbsp,
            )

        result.append(formatted)

    return result


def format_asciidoc_file(
    path: Path,
    *,
    add_nbsp: bool = False,
    punctuate_lists: bool = True,
) -> None:
    """
    Formate un fichier AsciiDoc en place (cf. _format_lines pour les règles
    appliquées). Préserve STRICTEMENT les lignes vides et la présence ou non
    du newline final.
    """
    original_text = path.read_text(encoding="utf-8")

    # 🔤 Ramène toute espace insécable déjà présente en clair (U+00A0, écrite
    # par un run précédent) à la représentation textuelle '&nbsp;' utilisée en
    # interne par le moteur (remove_all_nbsp, lookarounds (?!&nbsp;)...) —
    # sans ça, un second passage sur un fichier déjà formaté ne la reconnaît
    # pas comme telle et perd l'idempotence.
    original_text = original_text.replace(" ", "&nbsp;")

    # 🔒 Conserver l'information "newline final"
    has_trailing_newline = original_text.endswith("\n")

    result = _format_lines(
        original_text.split("\n"),
        add_nbsp=add_nbsp,
        punctuate_lists=punctuate_lists,
    )

    output = "\n".join(result)

    # 🔤 AsciiDoc n'a pas besoin de l'entité HTML '&nbsp;' (pensée pour du
    # HTML, cf. l'adaptateur Anki) : le caractère Unicode insécable (U+00A0)
    # est un octet UTF-8 valide, rendu correctement par Asciidoctor tel quel,
    # et surtout lisible directement dans le texte source.
    output = output.replace("&nbsp;", " ")

    # 🔒 Restaurer exactement le newline final
    if has_trailing_newline and not output.endswith("\n"):
        output += "\n"
    if not has_trailing_newline and output.endswith("\n"):
        output = output.rstrip("\n")

    path.write_text(output, encoding="utf-8")
