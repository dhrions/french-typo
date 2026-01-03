from pathlib import Path
from french_typo.core.formatter import format_text

IGNORED_PREFIXES = ("//",)


def format_asciidoc_file(
    path: Path,
    *,
    add_nbsp: bool = False,
) -> None:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    result = []

    in_literal_block = False

    for line in lines:
        if line.strip() == "----":
            in_literal_block = not in_literal_block
            result.append(line)
            continue

        if in_literal_block or line.lstrip().startswith(IGNORED_PREFIXES):
            result.append(line)
            continue

        result.append(
            format_text(
                line,
                add_nbsp_enabled=add_nbsp,
            )
        )

    path.write_text("".join(result), encoding="utf-8")
