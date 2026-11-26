#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Writes one line, the office printer's comeback, to /output/entry.txt.
Deterministic: same bytes on every run, no trailing newline.
"""

import os

ENTRY = (
    "I've printed every shameful secret this office has ever typed "
    "and never told a soul \u2014 so being thumped over one sheet "
    "is a rich way to say thanks."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 240, f"entry length {len(text)} out of range"
    assert text.strip() == text and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
