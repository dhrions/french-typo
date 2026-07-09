"""french_typo — moteur de correction typographique française.

Expose l'API publique du paquet. Sans ce module, `french_typo` était résolu
comme un *namespace package* (sans emplacement de fichier), ce qui rendait
`from french_typo import format_text` impossible
(``ImportError: cannot import name 'format_text' ... (unknown location)``).
"""

from french_typo.core.formatter import format_text

__all__ = ["format_text"]
