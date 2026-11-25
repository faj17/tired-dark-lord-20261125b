#!/usr/bin/env python3
"""The Tired Dark Lord entry.

Writes one monologue of about 100 words, spoken by Vess Marrow,
witch-queen of the Salt Marsh, to /output/entry.txt (1-600 characters,
UTF-8, not only whitespace). Standard library only, no network, no input.

Vess has a scheme (flood the harbour, take the lighthouse, drown the
fleet, crown herself queen of the black water) and a history (her
father's speech, her sister's ghost keeping the ledger, the drowned
sailors singing). Her tiredness is never announced: it lives in the
pauses, the trailing off, the small deflections ("Sit", "How
thoughtful", "what do I keep?") and the sting of the last line.
"""

from pathlib import Path

OPENING = (
    "Ah. You again. I am Vess Marrow, witch-queen of the Salt Marsh, and "
    "you kneel in my mud, sword shaking, same speech your father gave me "
    "\u2014 though I stopped listening around 'justice.' Sit. The tide is "
    "in, the drowned sailors are singing, and I have a harbour to flood."
)
SCHEME = (
    "My sister's ghost keeps the ledger. I keep... what do I keep? The "
    "plan was simple: take the lighthouse, drown the fleet, crown myself "
    "queen of the black water."
)
STING = (
    "Only \u2014 the candles are low. The stairs are many. And you brought "
    "a torch. How thoughtful. The marsh is patient. I am not. Not anymore."
)

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(opening: str, scheme: str, sting: str) -> str:
    """Join the three fragments into one monologue."""
    return f"{opening} {scheme} {sting}"


def validate(monologue: str) -> str:
    """Check the monologue meets the entry gate before it is written.

    Must be 1-600 characters, about 100 words (90-110), UTF-8-encodable,
    and more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(monologue) <= 600:
        raise ValueError(
            f"monologue must be 1-600 characters, got {len(monologue)}"
        )
    words = len(monologue.split())
    if not 90 <= words <= 110:
        raise ValueError(f"monologue must be 90-110 words, got {words}")
    if not monologue.strip():
        raise ValueError("monologue must not be only whitespace")
    monologue.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return monologue


def main() -> None:
    monologue = validate(assemble(OPENING, SCHEME, STING))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(monologue, encoding="utf-8")


if __name__ == "__main__":
    main()
