"""Everyday Wonder entry for make.fun's "Everyday Wonder, Two Days to Find the Line" bounty.

The program writes one sentence (119 characters, a single sentence) to /output/entry.txt.

The sentence: a shadow on wet pavement walks half a step ahead of its owner
on an ordinary morning, as if it already knows the destination. The wonder
is not in something exotic happening, but in a thing seen every day behaving
as though it has intentions of its own — the familiar made strange by one
small impossibility, noticed on the walk to nowhere in particular. Every
word is doing work: the wet pavement grounds it, the half-step measures the
strangeness, and the final clause is the turn that makes the everyday new.
"""

import os
from pathlib import Path

LINE = (
    "My shadow on the wet pavement walked a half-step ahead of me "
    "this morning, like it knew where I was going before I did."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-200")
    if "\n" in LINE:
        raise SystemExit("line must be a single line")
    if LINE != LINE.strip():
        raise SystemExit("line must not start or end with whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
