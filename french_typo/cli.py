import click
from pathlib import Path
from french_typo.adapters.asciidoc.formatter import format_asciidoc_file


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option(
    "--nbsp",
    is_flag=True,
    help="Ajoute des espaces insécables (&nbsp;). Désactivé par défaut pour AsciiDoc.",
)
def fix(path, nbsp):
    """
    Corrige la typographie française des fichiers AsciiDoc.
    """
    p = Path(path)

    if p.is_file() and p.suffix == ".adoc":
        format_asciidoc_file(p, add_nbsp=nbsp)
    elif p.is_dir():
        for file in p.rglob("*.adoc"):
            format_asciidoc_file(file, add_nbsp=nbsp)
    else:
        raise click.BadParameter("Chemin invalide")


if __name__ == "__main__":
    fix()
