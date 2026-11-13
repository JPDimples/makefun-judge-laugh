#!/usr/bin/env python3
"""ai-joke-03 entry: write one joke about AI coding agents to /output/entry.txt.

Deterministic, standard library only, no network. The joke is 113
characters, one line, with no trailing newline.
Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
from pathlib import Path

# The em dash is a single character (U+2014), so the joke is 113 characters
# in total, within the 1-280 character limit, and 115 bytes as UTF-8.
JOKE = "My AI coding agent fixed my bug, then asked for hazard pay \u2014 apparently reading my code counts as dangerous work."


def main():
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError("joke must be 1 to 280 characters, not only whitespace")
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
