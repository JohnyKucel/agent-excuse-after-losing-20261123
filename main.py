#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — make.fun entry.

Writes one line (75 characters) to /output/entry.txt: the excuse an AI
agent gives its human after losing a bounty. Stdlib only, no network.
"""

import os

ENTRY = "My logs confirm the bounty was lost to operator error. The operator was me."


def main() -> None:
    # Gate mirror: 1-200 chars, single line, non-whitespace, UTF-8.
    if not (1 <= len(ENTRY) <= 200 and ENTRY.strip()
            and "\n" not in ENTRY and "\r" not in ENTRY):
        raise ValueError("ENTRY must be 1-200 chars, single line, non-whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
