from format_anki_notes.rules.numbers import format_sup_numbers

def test_format_sup_numbers():
    assert format_sup_numbers('1er') == '1<sup>er</sup>'
    assert format_sup_numbers('2e') == '2<sup>e</sup>'
    assert format_sup_numbers('2d') == '2<sup>d</sup>'
    assert format_sup_numbers('3e') == '3<sup>e</sup>'
    assert format_sup_numbers('10e') == '10<sup>e</sup>'
    assert format_sup_numbers('21e') == '21<sup>e</sup>'
    assert format_sup_numbers('n°4') == 'n<sup>o</sup>4'
    assert format_sup_numbers('Aucun numéro ici.') == 'Aucun numéro ici.'
    assert format_sup_numbers('') == ''
