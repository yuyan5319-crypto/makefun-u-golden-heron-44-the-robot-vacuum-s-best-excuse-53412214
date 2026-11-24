#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

A robot vacuum's one-line excuse for missing a spot, written to
/output/entry.txt (the file the make.fun judge reads) and printed
to stdout. The line must be 1-140 characters.
"""

import os

LINE = (
    "My cliff sensor saw the rug fringe, panicked, and filed that "
    "corner as the edge of the world \u2014 I never argue with my own map."
)


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 140:
        raise SystemExit(f"entry must be 1-140 characters, got {len(line)}")
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
