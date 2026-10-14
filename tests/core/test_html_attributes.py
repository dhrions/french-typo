"""Les attributs HTML ne sont pas du texte : aucune règle typographique n'y touche.

Cas relevés sur la collection Anki le 2026-10-14 (165 notes) : un nom de fichier en hexadécimal
qui finit par `3d` devenait `3<sup>d</sup>`, un `style` perdait ses `:` et ses `;`, une URL
encodée gagnait un `&nbsp;` avant chaque `%`.
"""

import pytest

from french_typo.core.formatter import format_text
from french_typo.core.html_attributes import mask_attributes, restore_attributes

UNTOUCHED = [
    '<img src="paste-f77a809d29a3677a58f8b3adfe1b9671397f933d.jpg"/>',
    '<img src="paste-727ce12164d01006ba6567e5f6c52464eb6efa3e.jpg">',
    '<img src="hari singh.jpg" class="" style="height: 239px; width: 176px;">',
    '<span style="color: rgb(170, 0, 255);">mot</span>',
    '<span style=" font-style: normal; font-weight: normal; ">mot</span>',
    '<a href="https://fr.wikipedia.org/wiki/Heuristique_de_disponibilit%C3%A9">Wikipédia</a>',
    (
        '<a href="https://www.defense.gouv.fr/x/Strat%C3%A9gie%20%C3%A9nerg%C3%A9tique.pdf" '
        'title="Consulté le 2026-10-14">PDF</a>'
    ),
    '<a title="a > b" href="chapitre-2e.html">lien</a>',
    "<a href='https://exemple.org/3e'>lien</a>",
    "<font color=red size=2e>mot</font>",
    '<li class="x" data-note="1er : 2e ; 3d">mot</li>',
]


@pytest.mark.parametrize("html", UNTOUCHED)
@pytest.mark.parametrize("add_nbsp_enabled", [False, True])
def test_attributes_survive_every_rule(html, add_nbsp_enabled):
    assert format_text(html, add_nbsp_enabled=add_nbsp_enabled) == html


def test_text_around_the_tag_is_still_formatted():
    html = '<a href="https://exemple.org/p2e">le 2e étage</a>'

    assert (
        format_text(html)
        == '<a href="https://exemple.org/p2e">le 2<sup>e</sup> étage</a>'
    )


def test_text_next_to_an_image_is_still_formatted():
    html = 'Le 1er <img src="a3d.jpg" style="height: 2e;"> et le n°4'

    assert format_text(html) == (
        'Le 1<sup>er</sup> <img src="a3d.jpg" style="height: 2e;"> et le n<sup>o</sup>4'
    )


def test_formatting_is_idempotent_with_attributes():
    html = '<div>Le 2e <img src="a3d.jpg"/> : <a href="x%C3%A9">lien</a></div>'

    once = format_text(html, add_nbsp_enabled=True)

    assert format_text(once, add_nbsp_enabled=True) == once


def test_tag_name_stays_visible_to_the_rules():
    masked, _ = mask_attributes('<li class="x">a</li>')

    assert masked.startswith("<li")
    assert 'class="x"' not in masked


@pytest.mark.parametrize(
    "text",
    [
        "texte sans balise",
        "<b>gras</b> et <br>",
        '<img src="a.jpg" alt="un > deux">',
        '<img src="a.jpg',  # balise mal formée : laissée telle quelle
        'a < b et c > d, <a href="x">y</a>',
        "{{c1::<img src='a.png'>}}",
    ],
)
def test_masking_is_reversible(text):
    masked, blocks = mask_attributes(text)

    assert restore_attributes(masked, blocks) == text


def test_malformed_tag_is_left_exposed_not_swallowed():
    text = '<img src="a.jpg'

    masked, blocks = mask_attributes(text)

    assert masked == text
    assert blocks == []


def test_more_tags_than_sentinels_still_round_trips():
    text = "".join(f'<a href="x{i}">{i}</a>' for i in range(7000))

    masked, blocks = mask_attributes(text)

    assert len(blocks) < 7000
    assert restore_attributes(masked, blocks) == text
