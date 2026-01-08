from french_typo.formatter import format_text


def test_format_text_basic():
    assert format_text("10  KM .") == "10 km."


def test_format_text_order():
    text = "  5  KGS ."
    assert format_text(text) == "5 kg."
