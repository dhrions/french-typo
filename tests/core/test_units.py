from french_typo.core.rules.units import normalize_simple_units, normalize_composite_units

# tests/test_units.py
def test_normalize_km():
    assert normalize_simple_units('10 KM') == '10 km'
    assert normalize_simple_units('5 Km et 20 kms') == '5 km et 20 km'

def test_normalize_kg():
    assert normalize_simple_units('5 KG') == '5 kg'
    assert normalize_simple_units('100 KGS') == '100 kg'

def test_normalize_composite_units():
    assert normalize_composite_units('100 KM/H') == '100 km/h'
    assert normalize_composite_units('50 KG/M3') == '50 kg/m³'
