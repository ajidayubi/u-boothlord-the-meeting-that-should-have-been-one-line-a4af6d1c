#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire
pointless meeting to /output/entry.txt. The line itself is the
meeting's replacement: it carries the decision (approved), the
deadline (Friday), and the sting (nobody wanted to cancel it).
One sentence, no setup, no explanation, 147 characters.
"""
import os
import sys

LINE = (
    "Approved, due Friday, and the only reason we're all in this room "
    "is that cancelling the meeting felt ruder than wasting an hour "
    "of everyone's life."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"entry must be 1-200 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"chars: {len(LINE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
