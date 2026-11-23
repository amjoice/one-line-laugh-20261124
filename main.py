#!/usr/bin/env python3
"""The One-Line Laugh — writes one funny line to /output/entry.txt.

One sentence, 118 characters, plain text. Deterministic: the line is a
literal, so every run writes byte-identical output.
"""

import os

LINE = "My alarm went off, I hit snooze, and my smart speaker said 'again?' in a tone I did not appreciate from a hockey puck."

def main():
    # The gate refuses anything outside 1-200 characters, so fail loudly
    # here instead of shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.count(".") == 1 and LINE.endswith("."), "line must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
