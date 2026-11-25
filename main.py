#!/usr/bin/env python3
"""One-line resignation letter for make.fun's "The One-Line Exit" bounty.

The program writes a single deadpan resignation line to /output/entry.txt:
an employee quits on the spot after learning the office dog was promoted
above them, and refuses to take orders from someone who licks the clients.
"""

import os

LETTER = (
    "I hereby resign, effective immediately: the office dog was promoted "
    "above me, and I will not report to someone who licks the clients."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
