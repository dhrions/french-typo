from bs4 import BeautifulSoup

def strip_html_tags(html):
    """Supprime toutes les balises HTML et retourne le texte brut."""
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()

def escape_html(text):
    """Échappe les caractères spéciaux pour le HTML."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def unescape_html(text):
    """Déséchappe les entités HTML (ex: &nbsp; → espace)."""
    return text.replace("&nbsp;", " ")
