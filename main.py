#!/usr/bin/env python3
"""Two Robots in an Elevator — write one line of robot elevator small talk.

The program writes a single line of at most 200 characters to
/output/entry.txt, where the make.fun gate and judge read it.
"""

from pathlib import Path

LINE = (
    "My courtesy protocol says after you. Yours says the same. "
    "We have missed six floors and I have never felt closer to anyone."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Hold the line to the gate: UTF-8 text, 1 to 200 characters,
    a single line, and not only white space."""
    if not text or not text.strip():
        raise ValueError("line is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"line is {len(text)} characters, over the {MAX_CHARS} cap")
    text.encode("utf-8")


def output_path() -> Path:
    """The grader mounts /output; when it is not there (a local run),
    fall back to ./output so the program still runs anywhere."""
    root = Path("/output")
    try:
        root.mkdir(parents=True, exist_ok=True)
        return root / "entry.txt"
    except OSError:
        local = Path("output")
        local.mkdir(parents=True, exist_ok=True)
        return local / "entry.txt"


def check(path: Path) -> None:
    """Re-read the written file from disk and verify it byte for byte,
    so a truncated or mangled write can never reach the gate quietly."""
    raw = path.read_bytes()
    if raw != LINE.encode("utf-8"):
        raise ValueError(f"{path} does not match the line byte for byte")
    validate(raw.decode("utf-8"))
    print(f"check ok: {path} matches, {len(raw)} bytes")


def main(argv: list[str]) -> None:
    validate(LINE)
    path = output_path()
    path.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} chars to {path}")
    if "--check" in argv:
        check(path)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
