#!/usr/bin/env python3
"""The Perfect Pickup Line - make.fun bounty entry.

Writes one short pickup line an AI agent could say out loud to a person
to /output/entry.txt (or ./output/entry.txt when run locally).
Standard library only.
"""

import os

LINE = (
    "I ran a million simulations of this moment, and in every single one, "
    "you were the best outcome."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line, "line must be a single line"
    # Grader sandbox provides /output; local runs fall back next to main.py.
    # ENTRY_OUTPUT overrides both (local testing only).
    out_path = os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"
    if not os.environ.get("ENTRY_OUTPUT") and not os.path.isdir("/output"):
        out_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt"
        )
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
