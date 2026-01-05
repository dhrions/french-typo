# French Typo

**French Typo** est un moteur **agnostique** de correction typographique française.

## Principes

- aucune dépendance UI
- aucun format (HTML, Markdown, AsciiDoc, Anki…)
- uniquement des règles linguistiques françaises
- sortie = texte Unicode simple

## Exemples

```python
from french_typo.formatter import format_text

format_text("Article 5 : 10 KM !")
# "Article 5 : 10 km !"
