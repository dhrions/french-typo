from format_anki_notes.main import remove_all_nbsp, add_nbsp, format_sup_numbers, normalize_units, format_text

def test_remove_all_nbsp():
    assert remove_all_nbsp('Hello&nbsp;world!') == 'Hello world!'
    assert remove_all_nbsp('No&nbsp;nbsp&nbsp;here') == 'No nbsp here'
    assert remove_all_nbsp('Already normal') == 'Already normal'
    assert remove_all_nbsp('') == ''

def test_format_sup_numbers():
    assert format_sup_numbers('Voir n°4 et n°58.') == 'Voir n<sup>o</sup>4 et n<sup>o</sup>58.'
    assert format_sup_numbers('Aucun numéro ici.') == 'Aucun numéro ici.'
    assert format_sup_numbers('') == ''

def test_normalize_units():
    assert normalize_units('10 KM, 5 Km, 20 kms, 30 KMS') == '10 km, 5 km, 20 km, 30 km'
    assert normalize_units('Aucune unité ici.') == 'Aucune unité ici.'
    assert normalize_units('') == ''

def test_add_nbsp():
    assert add_nbsp('Ceci est un exemple de "texte" avec des points d\'interrogation ?') == 'Ceci est un exemple de "texte" avec des points d\'interrogation&nbsp;?'
    assert add_nbsp('Mais aussi des points d\'exclamation ainsi que : des deux-points.') == 'Mais aussi des points d\'exclamation ainsi que&nbsp;: des deux-points.'
    assert add_nbsp('Mais aussi, des « guillemets ».') == 'Mais aussi, des «&nbsp;guillemets&nbsp;».'
    assert add_nbsp('Mais aussi des signes plus ou moins ± 10.') == 'Mais aussi des signes plus ou moins ±&nbsp;10.'
    assert add_nbsp('Mais aussi des signes égal = 10.') == 'Mais aussi des signes égal =&nbsp;10.'
    assert add_nbsp('Mais aussi des pourcentages 10 %.') == 'Mais aussi des pourcentages 10&nbsp;%.'
    assert add_nbsp('Mais aussi des nombres 10 cm') == 'Mais aussi des nombres 10&nbsp;cm'
    assert add_nbsp('') == ''
    assert add_nbsp('Voir article 4 et Article 58.') == 'Voir article&nbsp;4 et Article&nbsp;58.'
    assert add_nbsp('Durée : 27h ou 2h.') == 'Durée&nbsp;: 27&nbsp;h ou 2&nbsp;h.'
    assert add_nbsp('10 cm et 20 KM.') == '10&nbsp;cm et 20&nbsp;KM.'
    assert add_nbsp('Voir n<sup>o</sup>5 et n<sup>o</sup>10.') == 'Voir n<sup>o</sup>&nbsp;5 et n<sup>o</sup>&nbsp;10.'

def test_add_nbsp_dates():
    assert format_text('24 mai') == '24 mai'
    assert format_text('1er janvier') == '1<sup>er</sup>&nbsp;janvier'
    assert format_text('10 %') == '10&nbsp;%'


def test_format_text():
    # Cas avec unité en majuscule et numéro à formater
    text = 'Voir n°4 : 10 KM et article 5.'
    expected = 'Voir n<sup>o</sup>&nbsp;4&nbsp;: 10&nbsp;km et article&nbsp;5.'
    assert format_text(text) == expected

    # Cas avec guillemets et ponctuation
    text = '« Test » : 2h30 et 10% ?'
    expected = '«&nbsp;Test&nbsp;»&nbsp;: 2&nbsp;h30 et 10&nbsp;%&nbsp;?'
    assert format_text(text) == expected
