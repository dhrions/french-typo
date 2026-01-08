from french_typo.rules.numbers import normalize_numbers


def test_preserve_french_ordinals():
    assert normalize_numbers("1er article") == "1er article"
    assert normalize_numbers("2e étage") == "2e étage"
    assert normalize_numbers("3d bataillon") == "3d bataillon"


def test_numbers_without_ordinals_are_unchanged():
    assert normalize_numbers("Article 10") == "Article 10"
