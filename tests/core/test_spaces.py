from french_typo.rules.spaces import normalize_spaces


def test_remove_multiple_spaces():
    assert normalize_spaces("a   b") == "a b"


def test_remove_space_before_dot():
    assert normalize_spaces("test .") == "test."


def test_strip_leading_spaces():
    assert normalize_spaces("   test") == "test"


def test_strip_trailing_spaces():
    assert normalize_spaces("test   ") == "test"
