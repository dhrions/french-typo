from french_typo.adapters.asciidoc.rules import punctuate_bullet_line
from french_typo.adapters.asciidoc.formatter import format_asciidoc_file

def test_middle_bullet():
    assert punctuate_bullet_line("* item", is_last=False) == "* item ;"

def test_last_bullet():
    assert punctuate_bullet_line("* item", is_last=True) == "* item."

def test_no_duplicate():
    assert punctuate_bullet_line("* item ;", is_last=False) == "* item ;"
    assert punctuate_bullet_line("* item.", is_last=True) == "* item."

def test_ignore_non_bullet():
    assert punctuate_bullet_line("item", is_last=True) == "item"

def test_intro_line_before_list_adds_blank_line(tmp_path):
    content = (
        "Il y a 3 catégories :\n"
        "* item 1\n"
        "* item 2\n"
    )

    path = tmp_path / "test.adoc"
    path.write_text(content, encoding="utf-8")

    format_asciidoc_file(path)

    result = path.read_text(encoding="utf-8")

    assert result == (
        "Il y a 3 catégories :\n"
        "\n"
        "* item 1 ;\n"
        "* item 2.\n"
    )
    
def test_intro_line_with_existing_blank_line_is_unchanged(tmp_path):
    content = (
        "Il y a 3 catégories :\n"
        "\n"
        "* item 1\n"
    )

    path = tmp_path / "test.adoc"
    path.write_text(content, encoding="utf-8")

    format_asciidoc_file(path)

    result = path.read_text(encoding="utf-8")

    assert result == (
        "Il y a 3 catégories :\n"
        "\n"
        "* item 1.\n"
    )

def test_no_intro_colon_does_not_add_blank_line(tmp_path):
    content = (
        "Il y a 3 catégories\n"
        "* item 1\n"
    )

    path = tmp_path / "test.adoc"
    path.write_text(content, encoding="utf-8")

    format_asciidoc_file(path)

    result = path.read_text(encoding="utf-8")

    assert result == (
        "Il y a 3 catégories\n"
        "* item 1.\n"
    )
