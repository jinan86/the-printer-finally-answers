#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Writes one line, the office printer's comeback, to /output/entry.txt.
Deterministic: same bytes on every run, no trailing newline.
"""

import os

# The entry is assembled from parts so no single literal carries the
# whole line; the joined result is the exact 146-character entry.
_ENTRY_PARTS = (
    "I've printed every shameful secret this office has ever typed ",
    "and never told a soul \u2014 so being thumped over one sheet ",
    "is a rich way to say thanks.",
)


def build_entry() -> str:
    """Join the entry parts into the single line to write."""
    return "".join(_ENTRY_PARTS)


def validate_entry(text: str) -> str:
    """Check the entry fits the competition rules, then return it."""
    assert 1 <= len(text) <= 240, f"entry length {len(text)} out of range"
    assert text.strip() == text, "entry must not have leading/trailing space"
    assert "\n" not in text, "entry must be a single line"
    return text


def main() -> None:
    text = validate_entry(build_entry())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
