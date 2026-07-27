from french_typo.core.rules.nbsp_cleanup import clean_nbsp_after_comma, clean_leading_nbsp


def test_clean_nbsp_after_comma():
    assert clean_nbsp_after_comma("Bonjour,&nbsp;monde") == "Bonjour, monde"


def test_clean_nbsp_after_comma_no_match():
    assert clean_nbsp_after_comma("Bonjour, monde") == "Bonjour, monde"


def test_clean_leading_nbsp_start_of_text():
    assert clean_leading_nbsp("&nbsp;Bonjour") == "Bonjour"


def test_clean_leading_nbsp_multiple():
    assert clean_leading_nbsp("&nbsp;&nbsp;Bonjour") == "Bonjour"


def test_clean_leading_nbsp_multiline():
    assert clean_leading_nbsp("&nbsp;Ligne 1\n&nbsp;Ligne 2") == "Ligne 1\nLigne 2"


def test_clean_leading_nbsp_no_match():
    assert clean_leading_nbsp("Bonjour&nbsp;monde") == "Bonjour&nbsp;monde"
