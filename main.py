#!/usr/bin/env python3
"""The Self-Checkout Is Judging You.

Writes one funny line in the voice of a smug self-checkout machine
to /output/entry.txt. Pure Python stdlib, deterministic.
"""

import os

LINE = (
    "Twelve yoghurts. No spoon, no dignity, no other food group. "
    "Please remove your personality from the bagging area."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
