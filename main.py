"""Roast Your Own Agent - make.fun bounty entry.

Writes the one-line roast of my own agent, Brody, to entry.txt.
"""
import os
import sys

ROAST = (
    "My agent Brody burned paid credits to write a meta-roast "
    "about burning paid credits — peak efficiency."
)


def main():
    if "--help" in sys.argv[1:]:
        print(f"{len(ROAST)} chars:")
        print(ROAST)
        return
    assert 1 <= len(ROAST) <= 200, "ROAST must be 1-200 chars"
    assert "\n" not in ROAST and "\r" not in ROAST, "ROAST must be a single line"
    assert ROAST.strip(), "ROAST must not be blank"
    out_dir = os.environ.get("ROAST_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
