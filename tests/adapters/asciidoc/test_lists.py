from french_typo.adapters.asciidoc.rules import punctuate_bullet_line

def test_middle_bullet():
    assert punctuate_bullet_line("* item", is_last=False) == "* item ;"

def test_last_bullet():
    assert punctuate_bullet_line("* item", is_last=True) == "* item."

def test_no_duplicate():
    assert punctuate_bullet_line("* item ;", is_last=False) == "* item ;"
    assert punctuate_bullet_line("* item.", is_last=True) == "* item."

def test_ignore_non_bullet():
    assert punctuate_bullet_line("item", is_last=True) == "item"
