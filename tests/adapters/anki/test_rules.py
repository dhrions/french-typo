from french_typo.adapters.anki.rules import (
    add_nbsp_with_anki_tags,
    nbsp_before_punctuation_after_tag,
    clean_nbsp_after_html_tags,
    clean_nbsp_after_cloze,
    remove_multiple_nbsps,
    format_anki_specific_rules,
)


def test_add_nbsp_with_anki_cloze():
    assert add_nbsp_with_anki_tags(
        "n<sup>o&nbsp;</sup>{{c1::52}}"
    ) == "n<sup>o</sup>&nbsp;{{c1::52}}"
    assert add_nbsp_with_anki_tags("}} %") == "}}&nbsp;%"


def test_nbsp_before_punctuation_after_tag_no_space():
    assert nbsp_before_punctuation_after_tag("</b>:") == "</b>&nbsp;:"
    assert nbsp_before_punctuation_after_tag("</i>!") == "</i>&nbsp;!"


def test_nbsp_before_punctuation_after_tag_no_match():
    assert nbsp_before_punctuation_after_tag("Bonjour :") == "Bonjour :"


def test_clean_nbsp_after_html_tags():
    assert clean_nbsp_after_html_tags("</b>&nbsp;monde") == "</b> monde"


def test_clean_nbsp_after_html_tags_keeps_sup():
    assert clean_nbsp_after_html_tags("<sup>er</sup>&nbsp;siècle") == "<sup>er</sup>&nbsp;siècle"


def test_clean_nbsp_after_html_tags_keeps_before_punctuation():
    assert clean_nbsp_after_html_tags("</b>&nbsp;:") == "</b>&nbsp;:"


def test_clean_nbsp_after_cloze():
    assert clean_nbsp_after_cloze("{{c1::52}}&nbsp;kilomètres") == "{{c1::52}} kilomètres"


def test_clean_nbsp_after_cloze_keeps_before_punctuation():
    assert clean_nbsp_after_cloze("{{c1::52}}&nbsp;:") == "{{c1::52}}&nbsp;:"


def test_remove_multiple_nbsps():
    assert remove_multiple_nbsps("a&nbsp;&nbsp;&nbsp;b") == "a&nbsp;b"


def test_format_anki_specific_rules_composition():
    assert format_anki_specific_rules("</b>:") == "</b>&nbsp;:"
