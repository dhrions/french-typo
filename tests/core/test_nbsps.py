from french_typo.core.rules.nbsps import remove_all_nbsp


def test_remove_all_nbsp_basic():
    assert remove_all_nbsp("Hello&nbsp;world!") == "Hello world!"


def test_remove_all_nbsp_multiple():
    assert remove_all_nbsp("No&nbsp;&nbsp;&nbsp;nbsp&nbsp;here") == "No   nbsp here"


def test_remove_all_nbsp_no_nbsp():
    assert remove_all_nbsp("Already normal") == "Already normal"


def test_remove_all_nbsp_empty():
    assert remove_all_nbsp("") == ""


def test_remove_all_nbsp_edges():
    assert remove_all_nbsp("&nbsp;Hello&nbsp;") == " Hello "


def test_remove_all_nbsp_mixed_spaces():
    assert remove_all_nbsp("Hello&nbsp; world&nbsp;!") == "Hello  world !"
