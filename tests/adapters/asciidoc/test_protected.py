"""Regressions seen on notes-videos (2026-11-01): spans that are not prose must survive intact."""

from french_typo.adapters.asciidoc.formatter import format_asciidoc_file
from french_typo.adapters.asciidoc.protected import mask_protected, restore_protected

NBSP = " "


def _format(tmp_path, content, **options):
    path = tmp_path / "page.adoc"
    path.write_text(content, encoding="utf-8")
    format_asciidoc_file(path, **options)
    return path.read_text(encoding="utf-8")


def test_url_target_is_not_split_by_unit_rule(tmp_path):
    # "6h" inside a YouTube id was read as "6 h" (hours).
    line = "Voir la link:https://www.youtube.com/watch?v=xmNJ_ERe6hI[vidéo].\n"
    assert "watch?v=xmNJ_ERe6hI[" in _format(tmp_path, line, add_nbsp=True)


def test_bare_url_is_untouched(tmp_path):
    line = "Source : https://example.org/a?x=10km&y=2e.\n"
    assert "https://example.org/a?x=10km&y=2e." in _format(tmp_path, line, add_nbsp=True)


def test_inline_formula_is_untouched(tmp_path):
    line = "La règle stem:[P(\\neg X) = 1 - P(X)] ; et latexmath:[a : b] aussi.\n"
    result = _format(tmp_path, line, add_nbsp=True)
    assert "stem:[P(\\neg X) = 1 - P(X)]" in result
    assert "latexmath:[a : b]" in result
    # The prose around the formula is still corrected.
    assert f"]{NBSP};" in result


def test_formula_block_is_untouched(tmp_path):
    content = "[stem]\n++++\nP(H \\mid D) : P(D)\n++++\n"
    assert _format(tmp_path, content, add_nbsp=True) == content


def test_inline_code_and_xref_target_are_untouched(tmp_path):
    line = "Lire `a : b` et xref:ROOT:page-2e.adoc[la page : suite].\n"
    result = _format(tmp_path, line, add_nbsp=True)
    assert "`a : b`" in result
    assert "xref:ROOT:page-2e.adoc[" in result
    assert f"[la page{NBSP}: suite]" in result


def test_ordinals_use_asciidoc_superscript(tmp_path):
    result = _format(tmp_path, "Le 1er cours, la 2e leçon, n° 3.\n")
    assert "1^er^" in result and "2^e^" in result and "n^o^" in result
    assert "<sup>" not in result


def test_mask_and_restore_round_trip():
    text = "a stem:[x : y] b https://x.org/c d `e : f`"
    masked, spans = mask_protected(text)
    assert "stem:" not in masked and "https" not in masked and "`" not in masked
    assert restore_protected(masked, spans) == text
