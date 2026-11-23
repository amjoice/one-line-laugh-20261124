#!/usr/bin/env python3
"""The One-Line Laugh — writes one funny line to /output/entry.txt.

One sentence, 118 characters, plain text. Deterministic: the line is a
literal, so every run writes byte-identical output.
"""

import os

LINE = "My alarm went off, I hit snooze, and my smart speaker said 'again?' in a tone I did not appreciate from a hockey puck."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
