# tests/test_nbsps.py
import pytest
from format_anki_notes.rules.nbsps import remove_all_nbsp, add_nbsp

def test_remove_all_nbsp():
    """Teste la suppression de toutes les occurrences de &nbsp; dans le texte."""
    # Cas de base
    assert remove_all_nbsp("Hello&nbsp;world!") == "Hello world!"
    # Plusieurs &nbsp;
    assert remove_all_nbsp("No&nbsp;&nbsp;&nbsp;nbsp&nbsp;here") == "No   nbsp here"
    # Aucun &nbsp;
    assert remove_all_nbsp("Already normal") == "Already normal"
    # Texte vide
    assert remove_all_nbsp("") == ""
    # &nbsp; en début/fin de chaîne
    assert remove_all_nbsp("&nbsp;Hello&nbsp;") == " Hello "
    # Mélange avec des espaces normaux
    assert remove_all_nbsp("Hello&nbsp; world&nbsp;!") == "Hello  world !"

def test_add_nbsp():
    """Teste l'ajout d'espaces insécables selon les règles typographiques françaises."""
    # Espace insécable après guillemet ouvrant
    assert add_nbsp('« Hello') == '«&nbsp;Hello'
    # Espace insécable avant guillemet fermant
    assert add_nbsp('Hello »') == 'Hello&nbsp;»'
    # Espace insécable avant ponctuation double
    assert add_nbsp('Hello : world') == 'Hello&nbsp;: world'
    assert add_nbsp('Hello ; world') == 'Hello&nbsp;; world'
    assert add_nbsp('Hello ?') == 'Hello&nbsp;?'
    assert add_nbsp('Hello !') == 'Hello&nbsp;!'
    # Cas spéciaux "?!" et "? !" (doivent rester inchangés)
    assert add_nbsp('Hello?!') == 'Hello?!'
    assert add_nbsp('Hello? !') == 'Hello? !'
    # Espace insécable après ± et =
    assert add_nbsp('± 10') == '±&nbsp;10'
    assert add_nbsp('= 5') == '=&nbsp;5'
    # Espace insécable pour mots-clés suivis d'un chiffre
    assert add_nbsp('article 4') == 'article&nbsp;4'
    assert add_nbsp('Article 58') == 'Article&nbsp;58'
    assert add_nbsp('coef. 3') == 'coef.&nbsp;3'
    assert add_nbsp('partie 2') == 'partie&nbsp;2'
    # Espace insécable pour § suivi d'un chiffre
    assert add_nbsp('§ 5') == '§&nbsp;5'
    # Espace insécable pour les heures
    assert add_nbsp('2h 30') == '2&nbsp;h 30'
    assert add_nbsp('2h') == '2&nbsp;h'
    # Espace insécable entre chiffre et unité/symbole
    assert add_nbsp('10 cm') == '10&nbsp;cm'
    assert add_nbsp('20 km') == '20&nbsp;km'
    assert add_nbsp('5 kg') == '5&nbsp;kg'
    assert add_nbsp('30 °C') == '30&nbsp;°C'
    assert add_nbsp('100 %') == '100&nbsp;%'
    assert add_nbsp('50 €') == '50&nbsp;€'
    assert add_nbsp('10 $') == '10&nbsp;$'
    # Espace insécable après n<sup>o</sup> suivi d'un chiffre
    assert add_nbsp('n<sup>o</sup>5') == 'n<sup>o</sup>&nbsp;5'
    # Espace insécable avant %
    assert add_nbsp('100 %') == '100&nbsp;%'
    # Cas avec plusieurs règles combinées
    assert add_nbsp('« Test » : 2h30 et 10% ?') == '«&nbsp;Test&nbsp;»&nbsp;: 2&nbsp;h30 et 10&nbsp;%&nbsp;?'
    # Texte sans modification nécessaire
    assert add_nbsp('Hello world') == 'Hello world'
    # Texte vide
    assert add_nbsp('') == ''
    # Cas avec HTML (à tester après intégration avec format_html)
    assert add_nbsp('Voir <b>article 4</b>') == 'Voir <b>article&nbsp;4</b>'
    # Cas avec guillemets et ponctuation
    assert add_nbsp('« Test » : 2h30 et 10% ?') == '«&nbsp;Test&nbsp;»&nbsp;: 2&nbsp;h30 et 10&nbsp;%&nbsp;?'
