import re

def remove_all_nbsp(text):
    """Supprime toutes les occurrences de &nbsp; dans le texte."""
    return text.replace('&nbsp;', ' ')

def add_ordinal_suffix_nbsp(text):
    """
    Ajoute les espaces insécables autour des suffixes ordinaux au format HTML
    (n<sup>o</sup>, <sup>er</sup>, <sup>e</sup>, <sup>d</sup>), y compris
    lorsqu'ils sont suivis d'une balise cloze Anki ({{...}}).
    """
    # Gestion spécifique de n<sup>o</sup> suivi d'un chiffre ou d'une balise Anki
    text = re.sub(r'(n<sup>o)&nbsp;<\/sup>(\{\{.*?\}\})', r'\1</sup>&nbsp;\2', text)
    text = re.sub(r'(n<sup>o<\/sup>)(\{\{.*?\}\})', r'\1&nbsp;\2', text)
    text = re.sub(r'(n<sup>o<\/sup>)(\s*)(\d+)', r'\1&nbsp;\3', text)

    # Espace insécable après les suffixes ordinaux au format HTML
    text = re.sub(r'(<sup>er<\/sup>|<sup>o<\/sup>|<sup>e<\/sup>|<sup>d<\/sup>)\s+', r'\1&nbsp;', text)

    return text


def add_nbsp(text):
    """
    Ajoute des espaces insécables selon les règles typographiques françaises.
    """
    # Espace insécable après les guillemets ouvrants (idempotent : ne double pas
    # le nbsp si le texte a déjà été formaté)
    text = re.sub(r'«(?!&nbsp;)\s*', '«&nbsp;', text)
    # Espace insécable avant les guillemets fermants (idempotent)
    text = re.sub(r'(?<!&nbsp;)\s*»', '&nbsp;»', text)

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

    # Espace insécable après ± et = (signe mathématique isolé, ex: « x = 3 »).
    # Exclut le cas où le '=' est un marqueur de titre AsciiDoc (« = Titre »,
    # « == Sous-titre »...) : dans ce cas, tout ce qui précède le signe sur la
    # ligne courante n'est que d'autres '='. Un lookbehind à largeur fixe ne
    # suffit pas ici (1 à 6 niveaux de titre) ; on passe donc par un callback
    # qui inspecte le préfixe de la ligne au moment du match.
    def _replace_math_sign(match, *, sign, source):
        prefix = source[:match.start()]
        line_start = prefix.rfind('\n') + 1
        before_on_line = prefix[line_start:]
        if sign == '=' and re.fullmatch(r'=*', before_on_line):
            return match.group(0)
        return f'{sign}&nbsp;'

    for sign in ['±', '=']:
        pattern = re.compile(rf'{re.escape(sign)}\s+')
        text = pattern.sub(
            lambda m, sign=sign, source=text: _replace_math_sign(m, sign=sign, source=source),
            text,
        )

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

    # Espace insécable entre un chiffre et un symbole (ex: 10 %, 50 €, 10 $).
    # Le '%' est traité à part des deux autres : un '%' suivi de deux
    # caractères hexadécimaux (%5D, %C3...) est la signature d'un octet
    # d'URL-encoding, jamais un pourcentage français — quel que soit ce qui
    # précède le chiffre (un %XX isolé comme dans un paramètre de requête,
    # ou un %XX%YY chaîné comme dans un caractère accentué encodé).
    text = re.sub(r'(\d)\s*(%)(?![0-9A-Fa-f]{2})', r'\1&nbsp;\2', text)
    text = re.sub(r'(\d)\s*(€|\$)', r'\1&nbsp;\2', text)

    text = add_ordinal_suffix_nbsp(text)

    return text

