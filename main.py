#!/usr/bin/env python3
"""Office Joke Open entry: one single-line office joke.

Writes the joke to /output/entry.txt, exactly one line, no trailing
newline. Standard library only.
"""

import os

JOKE = "Someone hit reply-all to say 'please stop hitting reply-all,' and now 400 people are replying-all to agree with him."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
