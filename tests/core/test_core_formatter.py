from french_typo.core.formatter import format_text


def test_format_text_applies_default_rules():
    assert format_text("Voir n°4 : 10 KM.") == "Voir n<sup>o</sup>4 : 10 km."


def test_format_text_removes_useless_spaces():
    assert format_text("Trop  d'espaces   ici.") == "Trop d'espaces ici."


def test_format_text_without_nbsp_by_default():
    result = format_text("Article 5 : oui.")
    assert "&nbsp;" not in result


def test_format_text_with_add_nbsp_enabled():
    result = format_text("Article 5 : oui.", add_nbsp_enabled=True)
    assert "&nbsp;" in result


def test_format_text_format_sup_numbers_enabled_by_default():
    assert "<sup>" in format_text("Voir n°4.")


def test_format_text_format_sup_numbers_disabled():
    result = format_text("Voir n°4 et le 1er jour.", format_sup_numbers_enabled=False)
    assert "<sup>" not in result
    assert "n°4" in result
    assert "1er" in result


def test_format_text_format_sup_numbers_disabled_other_rules_still_apply():
    """Désactiver les ordinaux ne doit pas désactiver les autres règles."""
    result = format_text("Trop  d'espaces avec 10 KM.", format_sup_numbers_enabled=False)
    assert result == "Trop d'espaces avec 10 km."
