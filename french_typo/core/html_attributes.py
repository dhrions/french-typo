"""Protège les attributs des balises HTML des règles typographiques.

Un attribut n'est pas du texte : `src`, `href`, `style`, `class`… sont lus par une machine, et
la moindre espace ou balise qu'y glisse une règle le casse. Sans cette protection, la règle des
ordinaux transforme `paste-f77a…933d.jpg` en `paste-f77a…933<sup>d</sup>.jpg` (l'image n'existe
plus sous ce nom), et un passage typographique a été relevé sur 165 notes Anki — attributs
`style` invalides, liens Wikipédia à `%C3&nbsp;%A9` (2026-10-14).

Chaque bloc d'attributs (`<img` **` src="…" class="…"`**`>`) est remplacé par une sentinelle
d'une seule lettre de la zone Unicode à usage privé, qu'aucune règle ne reconnaît (ni espace,
ni ponctuation, ni chiffre), puis réinjecté à l'identique. Le nom de la balise reste visible :
les règles qui s'y réfèrent n'en perdent rien.
"""

from __future__ import annotations

import re

# Début de la zone à usage privé (U+E000–U+F8FF) : 6 400 sentinelles possibles par texte.
_SENTINEL_BASE = 0xE100
_SENTINEL_LIMIT = 0xF8FF

# <nom, puis un ou plusieurs attributs (valeur entre guillemets, entre apostrophes ou nue), puis la
# fin de la balise. Une balise mal formée ne correspond pas : elle reste exposée aux règles, comme
# avant. Les guillemets d'une valeur peuvent contenir « > » (`title="a > b"`).
_ATTRIBUTES_PATTERN = re.compile(
    r"""
    (<[A-Za-z][\w:-]*)
    (
        (?:\s+[^\s"'<>/=]+
            (?:\s*=\s*(?:"[^"]*"|'[^']*'|[^\s"'<>=`]+))?
        )+
    )
    (?=\s*/?>)
    """,
    re.VERBOSE,
)


def mask_attributes(text: str) -> tuple[str, list[str]]:
    """Remplace chaque bloc d'attributs par une sentinelle.

    Retourne le texte masqué et la liste des blocs, dans l'ordre des sentinelles.
    """
    blocks: list[str] = []

    def stash(match: re.Match[str]) -> str:
        if _SENTINEL_BASE + len(blocks) > _SENTINEL_LIMIT:
            return match.group(0)
        blocks.append(match.group(2))
        return match.group(1) + chr(_SENTINEL_BASE + len(blocks) - 1)

    return _ATTRIBUTES_PATTERN.sub(stash, text), blocks


def restore_attributes(text: str, blocks: list[str]) -> str:
    """Réinjecte à l'identique les blocs masqués par `mask_attributes`."""
    for index, block in enumerate(blocks):
        text = text.replace(chr(_SENTINEL_BASE + index), block)
    return text
