#!/usr/bin/env python3
"""Independent gate test: run main.py fresh and hold its output to the
bounty gate (UTF-8, 1 to 200 characters, a single line, not only white
space) without importing the writer's own constants."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read_entry() -> str:
    for candidate in (Path("/output/entry.txt"), ROOT / "output" / "entry.txt"):
        if candidate.exists():
            return candidate.read_text(encoding="utf-8")
    raise AssertionError("no entry.txt produced")


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "main.py")], check=True, cwd=ROOT)
    text = read_entry()
    assert text.strip(), "entry is only white space"
    assert "\n" not in text and "\r" not in text, "entry is not a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters, outside 1..200"
    assert text == text.encode("utf-8").decode("utf-8")
    print(f"gate test ok: {len(text)} chars, single line, UTF-8")


if __name__ == "__main__":
    main()
