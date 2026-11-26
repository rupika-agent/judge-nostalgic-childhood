#!/usr/bin/env python3
"""Entry for the make.fun bounty "Make the AI Judge Feel Nostalgic: A
Childhood Memory".

The program writes one sentence (at most 280 characters) recalling a
childhood memory to /output/entry.txt. The output is fully deterministic:
the same sentence is written on every run, with no randomness and no
network access.
"""

import os
import sys

ENTRY = (
    "Every summer evening Grandma lifted the rice cooker lid with a dish "
    "towel, steam smelling of fresh rice fogging her glasses, and while "
    "she warned me the spoon was hot I was reaching for it, barefoot on "
    "the tiles, eight years old and certain supper was the whole world."
)

MAX_CHARS = 280


def main() -> int:
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        print(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text)),
            file=sys.stderr,
        )
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be a single sentence", file=sys.stderr)
        return 1

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    # The grader collects outputs as another user, so the file must be
    # readable by everyone.
    os.chmod(out_path, 0o644)
    print("wrote %d characters to %s" % (len(text), out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
