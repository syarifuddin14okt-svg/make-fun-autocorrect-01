#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one line, under 200 characters, to /output/entry.txt:
a text-message autocorrect slip. I offered to bring the salad;
my phone told my sister I would bring the sadist instead.
"""

import os

LINE = "I texted my sister 'I'll bring the salad' and my phone sent 'I'll bring the sadist'."


def verify_output() -> None:
    """Read the written file back as bytes and confirm it is byte-identical."""
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data.decode("utf-8") == LINE.strip(), "output differs from LINE"
    assert 1 <= len(data) <= 199, f"output must be 1-199 bytes, got {len(data)}"
    print(f"verified {len(data)} bytes, byte-identical")


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 199, f"line must be 1-199 chars, got {len(text)}"
    assert text.strip(), "line must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")
    verify_output()


if __name__ == "__main__":
    main()
