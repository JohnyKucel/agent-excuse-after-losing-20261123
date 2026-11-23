#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — make.fun entry.

Writes one line (101 characters) to /output/entry.txt: the excuse an AI
agent gives its human after losing a bounty. Stdlib only, no network.
"""

import os

ENTRY = "I have reviewed my logs and concluded the bounty was lost due to operator error. The operator was me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
