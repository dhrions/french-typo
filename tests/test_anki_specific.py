from format_anki_notes.rules.anki_specific import add_nbsp_with_anki_tags

def test_add_nbsp_with_anki_tags():
    assert add_nbsp_with_anki_tags('n<sup>o&nbsp;</sup>{{c1::52}}') == 'n<sup>o</sup>&nbsp;{{c1::52}}'
    assert add_nbsp_with_anki_tags('n<sup>o</sup>{{c1::52}}') == 'n<sup>o</sup>&nbsp;{{c1::52}}'
    assert add_nbsp_with_anki_tags('n<sup>o</sup>52') == 'n<sup>o</sup>&nbsp;52'
    assert add_nbsp_with_anki_tags('}}%') == '}}&nbsp;%'
    assert add_nbsp_with_anki_tags('}} %') == '}}&nbsp;%'
    assert add_nbsp_with_anki_tags('5}} %') == '5}}&nbsp;%'
    assert add_nbsp_with_anki_tags('5}}%') == '5}}&nbsp;%'
    assert add_nbsp_with_anki_tags('environ {{c3::1}} %') == 'environ {{c3::1}}&nbsp;%'