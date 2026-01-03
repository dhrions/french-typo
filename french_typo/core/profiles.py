from enum import Enum

class TypoProfile(str, Enum):
    PLAIN = "plain"
    ANKI = "anki"
    ASCIIDOC = "asciidoc"
