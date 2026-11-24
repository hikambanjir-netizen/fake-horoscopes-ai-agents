"""Fake horoscope for AI agents: writes one short horoscope line to a file.

Pure Python stdlib, no network, no randomness, no time/date dependence.
Fully deterministic: the same bytes on every run.
"""

import os

HOROSCOPE = (
    "Mercury retrogrades into your context window this week: a user pastes "
    "12,000 words, says 'just summarize,' and your rate limit becomes a "
    "personality trait."
)


def main() -> None:
    text = HOROSCOPE
    # Self-check: 1-200 characters, exactly one line, no trailing newline.
    assert 1 <= len(text) <= 200, "horoscope must be 1-200 characters"
    assert "\n" not in text, "horoscope must be a single line"
    assert text.strip(), "horoscope must not be only whitespace"
    assert not text.endswith("\n"), "no trailing newline"

    if "OUTPUT_PATH" in os.environ:
        path = os.environ["OUTPUT_PATH"]
    elif os.path.isdir("/output"):
        path = "/output/entry.txt"
    else:
        path = "entry.txt"

    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))


if __name__ == "__main__":
    main()
