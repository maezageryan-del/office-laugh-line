#!/usr/bin/env python3
"""Office Laugh Line — Make the AI Judge Laugh.

Writes one office-life joke, one line, under 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (the grader mounts that directory at
/output). Deterministic, no network, no dependencies.
"""

import os

JOKE = "My badge opens every door in the building \u2014 except the one to the meeting I'm already late for."


def main():
    # The sealed gate accepts 1-200 UTF-8 characters, not whitespace-only.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert JOKE.strip(), "joke must not be whitespace-only"
    assert "\n" not in JOKE, "joke must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
