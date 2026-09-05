from ._common import MAX_INPUT_LENGTH


def is_valid_iban(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if len(text) > MAX_INPUT_LENGTH:
        raise ValueError("input exceeds maximum allowed length")

    candidate = text.replace(" ", "")

    if not candidate:
        raise ValueError("IBAN must not be empty")

    if not (candidate.isascii() and candidate.isalnum()):
        raise ValueError("IBAN contains invalid characters")

    if not 15 <= len(candidate) <= 34:
        raise ValueError("IBAN has an invalid length")

    candidate = candidate.upper()
    rearranged = candidate[4:] + candidate[:4]
    digits = "".join(str(ord(ch) - 55) if "A" <= ch <= "Z" else ch for ch in rearranged)

    return int(digits) % 97 == 1
