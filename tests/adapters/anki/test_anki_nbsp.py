from french_typo.core.rules.nbsps import add_nbsp
from french_typo.adapters.anki.rules import add_nbsp_with_anki_tags


def test_add_nbsp_basic_typography():
    assert add_nbsp("10 %") == "10&nbsp;%"
    assert add_nbsp("article 4") == "article&nbsp;4"
    assert add_nbsp("§ 5") == "§&nbsp;5"


def test_add_nbsp_punctuation():
    assert add_nbsp("Hello : world") == "Hello&nbsp;: world"
    assert add_nbsp("Hello ?") == "Hello&nbsp;?"
    assert add_nbsp("Hello !") == "Hello&nbsp;!"


def test_add_nbsp_quotes():
    assert add_nbsp("« Hello »") == "«&nbsp;Hello&nbsp;»"


def test_add_nbsp_units():
    assert add_nbsp("10 km") == "10&nbsp;km"
    assert add_nbsp("30 °C") == "30&nbsp;°C"


def test_add_nbsp_ordinal_html():
    assert add_nbsp("n<sup>o</sup>5") == "n<sup>o</sup>&nbsp;5"


def test_add_nbsp_with_anki_cloze():
    assert add_nbsp_with_anki_tags(
        "n<sup>o&nbsp;</sup>{{c1::52}}"
    ) == "n<sup>o</sup>&nbsp;{{c1::52}}"

    assert add_nbsp_with_anki_tags(
        "n<sup>o</sup>{{c1::52}}"
    ) == "n<sup>o</sup>&nbsp;{{c1::52}}"

    assert add_nbsp_with_anki_tags(
        "n<sup>o</sup>52"
    ) == "n<sup>o</sup>&nbsp;52"

    assert add_nbsp_with_anki_tags("}} %") == "}}&nbsp;%"
    assert add_nbsp_with_anki_tags("5}}%") == "5}}&nbsp;%"
    assert add_nbsp_with_anki_tags(
        "environ {{c3::1}} %"
    ) == "environ {{c3::1}}&nbsp;%"
