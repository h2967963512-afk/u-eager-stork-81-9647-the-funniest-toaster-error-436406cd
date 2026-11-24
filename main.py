"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one deadpan toaster error message: the toast ejected
# early, filed for a transfer to the waffle iron, and will not return.
import os

TEXT = (
    "ERROR 04: Toast ejected early. It has filed for a transfer to the "
    "waffle iron and will not be returning."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# One line, 104 characters: breakfast as a resignation letter.
