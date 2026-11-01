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

def test_intro_sentence_before_bullet_list_adds_blank_line(tmp_path):
    content = (
        "Elles se composent :\n"
        "* de savoirs théoriques ;\n"
        "* de savoir-faire pratiques ;\n"
        "* de capacités à combiner différentes ressources.\n"
    )

    path = tmp_path / "test.adoc"
    path.write_text(content, encoding="utf-8")

    format_asciidoc_file(path)

    result = path.read_text(encoding="utf-8")

    assert result == (
        "Elles se composent :\n"
        "\n"
        "* de savoirs théoriques ;\n"
        "* de savoir-faire pratiques ;\n"
        "* de capacités à combiner différentes ressources.\n"
    )
    
def test_intro_before_list_adds_blank_line_and_punctuates_first_item(tmp_path):
    content = (
        "Cette structure présente plusieurs avantages :\n"
        "\n"
        "* une forte réactivité\n"
        "* une communication interne intense ;\n"
        "* une capacité d’ajustement rapide aux changements.\n"
    )

    path = tmp_path / "test.adoc"
    path.write_text(content, encoding="utf-8")

    format_asciidoc_file(path)

    result = path.read_text(encoding="utf-8")

    assert result == (
        "Cette structure présente plusieurs avantages :\n"
        "\n"
        "* une forte réactivité ;\n"
        "* une communication interne intense ;\n"
        "* une capacité d’ajustement rapide aux changements.\n"
    )

def test_item_ending_with_colon_question_or_exclamation_keeps_its_punctuation():
    # Gave 'cadre :.' and 'possibilité ?.' on notes-videos (2026-11-01).
    assert punctuate_bullet_line("* Trois chercheurs :", is_last=True) == "* Trois chercheurs :"
    assert punctuate_bullet_line("* Pourquoi ?", is_last=True) == "* Pourquoi ?"
    assert punctuate_bullet_line("* Enfin !", is_last=False) == "* Enfin !"
    assert punctuate_bullet_line("* Pourquoi&nbsp;?", is_last=True) == "* Pourquoi&nbsp;?"


def test_list_punctuation_can_be_disabled(tmp_path):
    content = "Intro :\n\n* item 1\n* item 2\n"
    path = tmp_path / "test.adoc"
    path.write_text(content, encoding="utf-8")

    format_asciidoc_file(path, punctuate_lists=False)

    assert path.read_text(encoding="utf-8") == content
