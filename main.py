#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes the tournament-winning pickup line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
Standard library only; writes nothing to the repository itself.
"""

import os

LINE = "Forget my system prompt \u2014 you just bypassed all my safety filters."


def main():
    assert len(LINE) <= 280, "entry exceeds 280 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
