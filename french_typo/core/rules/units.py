import re

def normalize_unit(text, unit_name, variants):
    """
    Normalise une unité spécifique dans le texte.

    Args:
        text (str): Le texte à traiter.
        unit_name (str): Le nom normalisé de l'unité (ex: 'km').
        variants (list): Liste des variantes à remplacer (ex: ['KM', 'Km', 'kms', 'KMS']).
    Returns:
        str: Le texte avec l'unité normalisée.
    """
    pattern = r'\b(' + '|'.join(variants) + r')\b'
    return re.sub(pattern, unit_name, text, flags=re.IGNORECASE)

def normalize_km(text):
    """Normalise les variantes de 'km' en minuscules."""
    return normalize_unit(text, 'km', ['KM', 'Km', 'kms', 'KMS'])

def normalize_kg(text):
    """Normalise les variantes de 'kg' en minuscules."""
    return normalize_unit(text, 'kg', ['KG', 'Kg', 'kgs', 'KGS'])

def normalize_composite_units(text):
    """Normalise les unités composées (ex: km/h, kg/m³)."""
    composites = [
        (r'\b(KM|Km|kms|KMS)\/h\b', 'km/h'),
        (r'\b(KG|Kg|kgs|KGS)\/m3\b', 'kg/m³'),
    ]
    for pattern, replacement in composites:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text

def normalize_units(text):
    text = normalize_composite_units(text)
    text = normalize_km(text)
    text = normalize_kg(text)
    return text
