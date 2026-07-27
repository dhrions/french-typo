from french_typo.core.formatter import format_text


def test_format_text_applies_default_rules():
    assert format_text("Voir n°4 : 10 KM.") == "Voir n<sup>o</sup>4 : 10 km."


def test_format_text_removes_useless_spaces():
    assert format_text("Trop  d'espaces   ici.") == "Trop d'espaces ici."


def test_format_text_without_nbsp_by_default():
    result = format_text("Article 5 : oui.")
    assert "&nbsp;" not in result


def test_format_text_with_add_nbsp_enabled():
    result = format_text("Article 5 : oui.", add_nbsp_enabled=True)
    assert "&nbsp;" in result
