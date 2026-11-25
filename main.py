#!/usr/bin/env python3
"""Entry program for The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue (104 words, 546 chars, one line) to entry.txt in
MAKEFUN_OUTPUT_DIR. The Dark Lord's grand speech keeps getting derailed by
his own tower's machinery: a scrying mirror that demands a password reset
every third Tuesday, and a kettle that will not wait for the conquest.
"""

import os

ENTRY_TEXT = (
    "You want the grand speech? Fine. Stand there \u2014 no, left a bit, "
    "the brazier smokes. I have ruled these seven valleys for forty years, "
    "and no hero has ever \u2014 hold on. The mirror wants my password "
    "again. It wants a new one. Every third Tuesday. So. Where was I? "
    "The conquest. Yes. My legions march at dawn, my ravens carry the "
    "decree, and the \u2014 sorry, the kettle. The kettle's done. Look, "
    "the kingdom can wait until morning. It has waited forty years. It "
    "can wait one more night. Go home, hero. Tell the bards I was "
    "terrifying. Leave out the kettle."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: /output/entry.txt is UTF-8 text of 1 to 600 characters.
    assert 1 <= len(ENTRY_TEXT) <= 600, f"entry length {len(ENTRY_TEXT)}"
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
