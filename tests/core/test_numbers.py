from french_typo.rules.numbers import normalize_numbers

def test_normalize_numbers():
    assert normalize_numbers("1er article") == "1er article"
    assert normalize_numbers("2e étage") == "2e étage"
