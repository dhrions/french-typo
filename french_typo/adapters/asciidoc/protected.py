"""Protect the parts of an AsciiDoc line that are not prose from the typography rules.

A formula, a URL, a macro target or inline code is read by a machine, not by a reader: the
slightest space a rule slips in breaks it. Observed on 2026-11-01 on `notes-videos` with
`--nbsp`:

* the unit rule saw "6 h" in the YouTube id `xmNJ_ERe6hI` and turned the link into
  `xmNJ_ERe6 hI` (dead link);
* the non-breaking-space rule rewrote the LaTeX of `stem:[P(\\neg X) = 1 - P(X)]`.

Each protected span is replaced by a single character of the Unicode private use area, which no
rule recognises (neither space, punctuation nor digit), then restored verbatim. The base differs
from the one used by `french_typo.core.html_attributes`, so both maskings can be nested without
one restoring the other's sentinels.

Only the *target* of a macro is protected (`link:https://…`, `xref:page.adoc`): its bracketed
label is prose and is still corrected.
"""

from __future__ import annotations

import re

_SENTINEL_BASE = 0xF000
_SENTINEL_LIMIT = 0xF8FF

_PROTECTED_PATTERN = re.compile(
    r"""
      (?:stem|latexmath|asciimath|pass):\[(?:\\.|[^\]\\])*\]   # inline formula or passthrough
    | \+\+.+?\+\+                                              # ++passthrough++
    | `[^`\n]+`                                                # inline code
    | (?:xref|link|image|include|video|audio|kbd|btn|menu):{1,2}[^\s\[]*   # macro target
    | (?:https?|ftp|irc|mailto|file)://[^\s\[\]<>"]+         # bare URL
    | <<[^>\n]*>>                                              # cross reference
    """,
    re.VERBOSE,
)


def mask_protected(text: str) -> tuple[str, list[str]]:
    """Replace each protected span with a sentinel.

    Return the masked text and the list of spans, in sentinel order.
    """
    spans: list[str] = []

    def stash(match: re.Match[str]) -> str:
        if _SENTINEL_BASE + len(spans) > _SENTINEL_LIMIT:
            return match.group(0)
        spans.append(match.group(0))
        return chr(_SENTINEL_BASE + len(spans) - 1)

    return _PROTECTED_PATTERN.sub(stash, text), spans


def restore_protected(text: str, spans: list[str]) -> str:
    """Restore verbatim the spans masked by `mask_protected`."""
    for index, span in enumerate(spans):
        text = text.replace(chr(_SENTINEL_BASE + index), span)
    return text
