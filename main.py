"""Write one short text for make.fun, byte for byte, with no trailing newline."""

import os
import sys
from pathlib import Path

TEXT = (
    "My agent scheduled the deploy for end of day, "
    "defined end of day as 11:40, and went to lunch."
)


def main() -> None:
    text = TEXT
    assert 1 <= len(text) <= 280, f"text must be 1..280 characters, got {len(text)}"

    out_dir_name = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    out_dir = Path(out_dir_name or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)

    target = out_dir / "entry.txt"
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)

    print(f"characters: {len(text)}", file=sys.stderr)


if __name__ == "__main__":
    main()
