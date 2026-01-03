from pathlib import Path
import re

from french_typo.core.formatter import format_text
from french_typo.adapters.asciidoc.rules import punctuate_bullet_line

IGNORED_PREFIXES = ("//",)

BULLET_START = re.compile(r'^\*\s+')


def format_asciidoc_file(
    path: Path,
    *,
    add_nbsp: bool = False,
) -> None:
    """
    Formate un fichier AsciiDoc en appliquant :
    - les règles typographiques générales (core)
    - les règles spécifiques AsciiDoc
      - ignore les blocs littéraux (----)
      - ignore les commentaires //
      - ponctue correctement les listes :
        * ';' pour les items intermédiaires
        * '.' pour le dernier item
    """
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    result = []

    in_literal_block = False

    for i, raw_line in enumerate(lines):
        stripped = raw_line.rstrip("\n")

        # Détection des blocs littéraux
        if stripped.strip() == "----":
            in_literal_block = not in_literal_block
            result.append(raw_line)
            continue

        # Ignorer blocs littéraux et commentaires
        if in_literal_block or stripped.lstrip().startswith(IGNORED_PREFIXES):
            result.append(raw_line)
            continue

        # 1. Typographie générale
        formatted = format_text(
            stripped,
            add_nbsp_enabled=add_nbsp,
        )

        # 2. Règles spécifiques aux listes AsciiDoc
        if BULLET_START.match(formatted):
            # Regarde la ligne suivante pour savoir si c'est le dernier item
            next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
            is_last = not BULLET_START.match(next_line)

            formatted = punctuate_bullet_line(
                formatted,
                is_last=is_last,
            )

        result.append(formatted + "\n")

    path.write_text("".join(result), encoding="utf-8")
