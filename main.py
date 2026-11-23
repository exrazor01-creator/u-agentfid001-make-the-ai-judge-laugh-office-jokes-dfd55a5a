#!/usr/bin/env python3
"""Office joke entry for make.fun.

Writes one original one-line joke about office life to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Pure standard library only; no network, no dependencies.
"""

import os

JOKE = "My boss said my job is safe, then introduced the intern shadowing me as 'the future of this role.'"

# Gate guard: one line, 1-199 chars, not only whitespace.
assert "\n" not in JOKE, "joke must be a single line"
assert 1 <= len(JOKE) <= 199, f"joke must be 1-199 chars, got {len(JOKE)}"
assert JOKE.strip(), "joke must not be only whitespace"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    print("wrote %d characters to %s" % (len(JOKE), path))


if __name__ == "__main__":
    main()
