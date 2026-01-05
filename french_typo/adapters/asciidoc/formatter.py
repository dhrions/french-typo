from pathlib import Path
import re

from french_typo.core.formatter import format_text
from french_typo.adapters.asciidoc.rules import punctuate_bullet_line

IGNORED_PREFIXES = ("//",)
BULLET_START = re.compile(r'^\*\s+')
INTRO_LINE = re.compile(r'.+:\s*$')


def format_asciidoc_file(
    path: Path,
    *,
    add_nbsp: bool = False,
) -> None:
    """
    Formate un fichier AsciiDoc en appliquant :
    - les règles typographiques générales (core)
    - les règles spécifiques AsciiDoc :
      - ignore les blocs littéraux (----)
      - ignore les commentaires //
      - ponctue correctement les listes :
        * ';' pour les items intermédiaires
        * '.' pour le dernier item
      - insère une ligne vide après une phrase introductive
        se terminant par ':' avant une liste

    Préserve STRICTEMENT :
    - les lignes vides
    - la présence ou non du newline final
    """
    original_text = path.read_text(encoding="utf-8")

    # 🔒 Conserver l'information "newline final"
    has_trailing_newline = original_text.endswith("\n")

    lines = original_text.split("\n")
    result = []

    in_literal_block = False

    for i, line in enumerate(lines):
        # Ligne vide → conservée telle quelle
        if line == "":
            result.append(line)
            continue

        # Détection des blocs littéraux
        if line.strip() == "----":
            in_literal_block = not in_literal_block
            result.append(line)
            continue

        # Ignorer blocs littéraux et commentaires
        if in_literal_block or line.lstrip().startswith(IGNORED_PREFIXES):
            result.append(line)
            continue

        next_line = lines[i + 1] if i + 1 < len(lines) else ""

        # 🔹 Règle : ligne introductive avant une liste
        if INTRO_LINE.match(line) and BULLET_START.match(next_line):
            formatted = format_text(
                line,
                add_nbsp_enabled=add_nbsp,
            )
            result.append(formatted)
            result.append("")
            continue

        # 1. Typographie générale
        formatted = format_text(
            line,
            add_nbsp_enabled=add_nbsp,
        )

        # 2. Règles spécifiques aux listes AsciiDoc
        if BULLET_START.match(formatted):
            is_last = not BULLET_START.match(next_line.lstrip())

            formatted = punctuate_bullet_line(
                formatted,
                is_last=is_last,
            )

        result.append(formatted)

    output = "\n".join(result)

    # 🔒 Restaurer exactement le newline final
    if has_trailing_newline and not output.endswith("\n"):
        output += "\n"
    if not has_trailing_newline and output.endswith("\n"):
        output = output.rstrip("\n")

    path.write_text(output, encoding="utf-8")
