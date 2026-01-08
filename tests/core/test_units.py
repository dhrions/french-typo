from french_typo.rules.units import normalize_units


def test_normalize_km_variants():
    assert normalize_units("10 KM") == "10 km"
    assert normalize_units("5 Km") == "5 km"
    assert normalize_units("3 kms") == "3 km"
    assert normalize_units("7 KMS") == "7 km"


def test_normalize_kg_variants():
    assert normalize_units("2 KG") == "2 kg"
    assert normalize_units("4 Kg") == "4 kg"
    assert normalize_units("6 kgs") == "6 kg"
    assert normalize_units("8 KGS") == "8 kg"


def test_preserve_km_per_hour():
    assert normalize_units("90 km/h") == "90 km/h"
    assert normalize_units("90 KM/H") == "90 km/h"


def test_normalize_kg_per_m3():
    assert normalize_units("100 kg/m3") == "100 kg/m³"
    assert normalize_units("100 KG/M3") == "100 kg/m³"
