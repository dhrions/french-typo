from importlib.metadata import version

__version__ = version("french-typo")

from .formatter import format_text

__all__ = ["format_text"]
