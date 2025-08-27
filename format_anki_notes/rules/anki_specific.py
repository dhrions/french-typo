# format_anki_notes/rules/anki_specific.py
import re
from ..logger import get_logger

logger = get_logger()

def add_nbsp_with_anki_tags(text):
    """
    Ajoute des espaces insécables selon les règles typographiques française
    en prenant en compte les balises d'Anki (balises HTML, {{ et }}).
    """

    # Remplace }} suivi d'un symbole par }}&nbsp;symbole (même sans espace entre les deux)
    text = re.sub(r'(}})\s?([:;!?%€$])', r'\1&nbsp;\2', text)
    text = re.sub(r'(}})\s?([°CkmgLhmin])', r'\1&nbsp;\2', text)
    # Remplace symbole ou chiffre suivi de {{ par symbole&nbsp;{{ (même sans espace)
    text = re.sub(r'([:;!?%€$])\s?(\{\{)', r'\1&nbsp;\2', text)

    # Gestion spécifique de n<sup>o</sup> suivi d'un chiffre ou d'une balise Anki
    text = re.sub(r'(n<sup>o)&nbsp;<\/sup>(\{\{.*?\}\})', r'\1</sup>&nbsp;\2', text)
    text = re.sub(r'(n<sup>o<\/sup>)(\{\{.*?\}\})', r'\1&nbsp;\2', text)
    text = re.sub(r'(n<sup>o<\/sup>)(\s*)(\d+)', r'\1&nbsp;\3', text)
    
    # Espace insécable après les suffixes ordinaux au format HTML
    text = re.sub(r'(<sup>er<\/sup>|<sup>o<\/sup>|<sup>e<\/sup>|<sup>d<\/sup>)\s+', r'\1&nbsp;', text)

    return text




def format_anki_specific_rules(text):
    """
    Applique toutes les règles spécifiques à Anki.
    """
    logger.debug("Application des règles spécifiques à Anki...")
    # text = format_cloze(text)
    text = add_nbsp_with_anki_tags(text)    
    return text
