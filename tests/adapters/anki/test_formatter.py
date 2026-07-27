from french_typo.adapters.anki.formatter import format_anki_html


def test_format_anki_html_end_to_end():
    assert format_anki_html("Voir n°4 : 10 KM") == "Voir n<sup>o</sup>&nbsp;4&nbsp;: 10&nbsp;km"


def test_format_anki_html_idempotent():
    texts = [
        "Voir n°4 : 10 KM",
        "« Bonjour » monde !",
        "1er janvier, 2e semaine",
        "{{c1::52}} kilomètres",
        "<b>Titre</b>: contenu",
    ]
    for text in texts:
        once = format_anki_html(text)
        assert format_anki_html(once) == once


def test_format_anki_html_cloze_guillemets_ordinal_composition():
    result = format_anki_html("«{{c1::1er}}» janvier")
    assert result == "«&nbsp;{{c1::1<sup>er</sup>}}&nbsp;» janvier"
    assert "&nbsp;&nbsp;" not in result
