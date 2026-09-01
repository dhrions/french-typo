from french_typo.core.rules.nbsps import remove_all_nbsp, add_nbsp


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


def test_add_nbsp_guillemets_idempotent():
    once = add_nbsp("« Bonjour »")
    assert add_nbsp(once) == once


def test_add_abbreviation_nbsp_civilite():
    from french_typo.core.rules.nbsps import add_abbreviation_nbsp

    assert add_abbreviation_nbsp("M. Dupont") == "M.&nbsp;Dupont"
    assert add_abbreviation_nbsp("MM. Dupont et Durand") == "MM.&nbsp;Dupont et Durand"
    assert add_abbreviation_nbsp("Mme Martin") == "Mme&nbsp;Martin"
    assert add_abbreviation_nbsp("Mmes Martin et Durand") == "Mmes&nbsp;Martin et Durand"
    assert add_abbreviation_nbsp("Mlle Durand") == "Mlle&nbsp;Durand"
    assert add_abbreviation_nbsp("Dr Martin") == "Dr&nbsp;Martin"
    assert add_abbreviation_nbsp("Pr Curie") == "Pr&nbsp;Curie"


def test_add_abbreviation_nbsp_saint_et_raisons_sociales():
    from french_typo.core.rules.nbsps import add_abbreviation_nbsp

    assert add_abbreviation_nbsp("St Étienne") == "St&nbsp;Étienne"
    assert add_abbreviation_nbsp("Ste Anne") == "Ste&nbsp;Anne"
    assert add_abbreviation_nbsp("Cie Générale") == "Cie&nbsp;Générale"
    assert add_abbreviation_nbsp("Éts Dupont") == "Éts&nbsp;Dupont"


def test_add_abbreviation_nbsp_devant_nom_commun():
    """Le nbsp s'applique quelle que soit la casse du mot suivant."""
    from french_typo.core.rules.nbsps import add_abbreviation_nbsp

    assert add_abbreviation_nbsp("Mme la présidente") == "Mme&nbsp;la présidente"


def test_add_abbreviation_nbsp_idempotent():
    from french_typo.core.rules.nbsps import add_abbreviation_nbsp

    once = add_abbreviation_nbsp("M. Dupont et Dr Martin")
    assert add_abbreviation_nbsp(once) == once


def test_add_abbreviation_nbsp_ne_touche_pas_les_mots_englobants():
    """'Dr'/'St' à l'intérieur d'un mot ne doit pas être traité."""
    from french_typo.core.rules.nbsps import add_abbreviation_nbsp

    assert add_abbreviation_nbsp("Drancy est une ville") == "Drancy est une ville"
    assert add_abbreviation_nbsp("Stendhal a écrit") == "Stendhal a écrit"


def test_add_abbreviation_nbsp_sans_mot_suivant():
    """Une abréviation en fin de texte ou suivie d'une ponctuation est ignorée."""
    from french_typo.core.rules.nbsps import add_abbreviation_nbsp

    assert add_abbreviation_nbsp("Adressé à M.") == "Adressé à M."
    assert add_abbreviation_nbsp("le Dr .") == "le Dr ."
