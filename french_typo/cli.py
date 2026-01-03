import click
from pathlib import Path
from french_typo.adapters.asciidoc.formatter import format_asciidoc_file

@click.command()
@click.argument("path", type=click.Path(exists=True))
def fix(path):
    """
    Corrige la typographie française des fichiers AsciiDoc.
    """
    p = Path(path)

    if p.is_file() and p.suffix == ".adoc":
        format_asciidoc_file(p)
    elif p.is_dir():
        for file in p.rglob("*.adoc"):
            format_asciidoc_file(file)
    else:
        raise click.BadParameter("Chemin invalide")

if __name__ == "__main__":
    fix()
