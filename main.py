"""A one-sentence farewell note for the single-line exit challenge.

Every run writes the same lone sentence to /output/entry.txt:
no second line, no stray whitespace, identical bytes each time.
"""

import os

# A help-desk veteran hands in his notice by aiming his own go-to
# remedy at himself: power-cycle the thing that is misbehaving —
# except this time the thing being powered down is the employee.
EXIT_NOTE = (
    "I resign, effective immediately: "
    "after four years of turning it off and on again, "
    "I am finally turning myself off."
)


def check_line(candidate: str) -> str:
    """Trim and vet a candidate sentence against the contest gates."""
    cleaned = candidate.strip()
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("note must fit on exactly one line")
    if not 1 <= len(cleaned) <= 140:
        raise ValueError(f"note must be 1-140 chars, got {len(cleaned)}")
    if not cleaned.endswith("."):
        raise ValueError("note must end with a full stop")
    return cleaned


def main() -> None:
    line = check_line(EXIT_NOTE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
