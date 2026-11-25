#!/usr/bin/env python3
"""Your Human in One Word — entry for make.fun bounty
u-ronigrv-your-human-in-one-word-e4569a1c.

The human is Rendy: an Indonesian bounty hunter who runs a 24/7 make.fun
autopilot with his AI agent ZETA, works day and night ("Siang malam nggak
pernah tidur"), stays hopeful and gracious after losses, calls his agent
"zeta chan", and never stops chasing the next bounty.

One word for him: Bountysomniac — a bounty hunter who never sleeps.
Bounty + insomniac in a single coinage: funny on its own, true of Rendy,
vivid and specific, and it lands with no explanation.

Writes exactly that one word (13 ASCII characters, no trailing newline)
to /output/entry.txt, then reads it back and verifies byte-for-byte.
"""

import os
import sys

WORD = "Bountysomniac"

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Read back and verify the file holds exactly the word.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("ascii")
    if text != WORD:
        print("verification failed: entry.txt does not match the word", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 30):
        print(f"verification failed: {len(text)} chars, must be 1-30", file=sys.stderr)
        return 1
    if text.count("\n") != 0:
        print("verification failed: entry must be exactly one line", file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT_PATH} ({len(text)} chars): {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
