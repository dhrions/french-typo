import re

def remove_all_nbsp(text):
    """Supprime toutes les occurrences de &nbsp; dans le texte."""
    return text.replace('&nbsp;', ' ')

def add_nbsp(text):
    """
    Ajoute des espaces insécables selon les règles typographiques françaises.
    """
    # Espace insécable après les guillemets ouvrants
    text = re.sub(r'«\s+', '«&nbsp;', text)
    # Espace insécable avant les guillemets fermants
    text = re.sub(r'\s+»', '&nbsp;»', text)

    # On traite d'abord les cas spéciaux "?!" et "? !" en les marquant temporairement
    text = text.replace('?!', '___QUESTION_EXCLAMATION___')
    text = text.replace('? !', '___QUESTION_ESPACE_EXCLAMATION___')

    # Espace insécable avant les signes de ponctuation doubles
    text = re.sub(r'\s+\?', '&nbsp;?', text)
    text = re.sub(r'\s+!', '&nbsp;!', text)
    text = re.sub(r'\s+:', '&nbsp;:', text)
    text = re.sub(r'\s+;', '&nbsp;;', text)

    # On rétablit les cas spéciaux
    text = text.replace('___QUESTION_EXCLAMATION___', '?!')
    text = text.replace('___QUESTION_ESPACE_EXCLAMATION___', '? !')

    # Espace insécable après ± et =
    for sign in ['±', '=']:
        text = re.sub(rf'{re.escape(sign)}\s+', f'{sign}&nbsp;', text)

    # Espace insécable pour les mots clés suivis d'un chiffre
    keywords = r'article|coef\.|partie'
    text = re.sub(rf'\b({keywords})\s+(\d+)', r'\1&nbsp;\2', text, flags=re.IGNORECASE)

    # Espace insécable pour § suivi d'un chiffre
    text = re.sub(r'§\s*(\d+)', r'§&nbsp;\1', text)

    # Espace insécable pour les heures (ex: 2h, 2h30, 2h45min)
    text = re.sub(r'(\d+)\s*(h)(\d*)', r'\1&nbsp;\2\3', text)

    # Espace insécable entre un chiffre et une unité de mesure (ex: 10 cm, 20 km)
    units = r'cm|km|m|g|kg|L|h|min|s|°C'
    text = re.sub(rf'(\d)\s*({units})\b', r'\1&nbsp;\2', text, flags=re.IGNORECASE)

    # Espace insécable entre un chiffre et un symbole (ex: 10 %, 50 €, 10 $)
    symbols = r'%|€|\$'
    text = re.sub(rf'(\d)\s*({symbols})', r'\1&nbsp;\2', text)

    # Gestion spécifique de n<sup>o</sup> suivi d'un chiffre ou d'une balise Anki
    text = re.sub(r'(n<sup>o)&nbsp;<\/sup>(\{\{.*?\}\})', r'\1</sup>&nbsp;\2', text)
    text = re.sub(r'(n<sup>o<\/sup>)(\{\{.*?\}\})', r'\1&nbsp;\2', text)
    text = re.sub(r'(n<sup>o<\/sup>)(\s*)(\d+)', r'\1&nbsp;\3', text)
    
    # Espace insécable après les suffixes ordinaux au format HTML
    text = re.sub(r'(<sup>er<\/sup>|<sup>o<\/sup>|<sup>e<\/sup>|<sup>d<\/sup>)\s+', r'\1&nbsp;', text)


    return text

