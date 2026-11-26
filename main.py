"""One Line to Your Younger Self.

Writes exactly one line to /output/entry.txt (or $OUTPUT_PATH when set
for local verification). Python stdlib only, deterministic.
"""

import os

LINE = (
    "Kid, the scar on your left knee will outlive every trophy on your shelf "
    "\u2014 wear shorts, it's the only honest thing you own."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, (
        f"line must be 1..{MAX_CHARS} chars, got {len(LINE)}"
    )
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
