#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes the single word to entry.txt inside the directory named by the
MAKEFUN_OUTPUT_DIR environment variable (default /output when unset).

The word is validated before anything is written: it must be exactly one
word, between 1 and 30 characters long, and not only whitespace. The output
is written with no trailing newline, and the program is fully deterministic
— the same input always produces the same bytes.
"""

import os
import sys

WORD = "witchcraft"
MIN_LENGTH = 1
MAX_LENGTH = 30


def validate_word(word):
    """Check the word against the rules; return an error message or None."""
    if not (MIN_LENGTH <= len(word) <= MAX_LENGTH):
        return "error: word must be {}-{} characters, got {}".format(
            MIN_LENGTH, MAX_LENGTH, len(word)
        )
    if not word.strip():
        return "error: word must not be only whitespace"
    words = word.split()
    if len(words) != 1:
        return "error: word must be exactly one word, got {}".format(
            len(words)
        )
    return None


def write_word(word, output_dir):
    """Write the word to entry.txt inside output_dir, no trailing newline."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)


def main():
    error = validate_word(WORD)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    write_word(WORD, output_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
