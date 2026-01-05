from french_typo.formatter import format_text

def test_format_text():
    assert format_text("10  KM .") == "10 km."
