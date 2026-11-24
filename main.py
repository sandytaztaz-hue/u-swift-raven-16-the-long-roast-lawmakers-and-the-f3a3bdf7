#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one original satirical sentence: the lawmakers who fine platforms
for losing your data, losing their own AI bill while trying to turn it
into a PDF. The program is deterministic: it always writes the same entry.
"""

import os

ENTRY = "The committee that fines platforms for losing your data spent a week trying to turn its own AI bill into a PDF, and lost the only copy somewhere in the chairman's Downloads folder, between a boarding pass and a coupon that expired in 2019."

# The bounty caps the entry at 320 characters; refuse loudly if it ever grows.
# One sentence only: the setup fines platforms for losing data, the turn
# loses the bill itself, and the punch lands on the last few words.
assert len(ENTRY) <= 320, "entry exceeds the 320-character cap"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
