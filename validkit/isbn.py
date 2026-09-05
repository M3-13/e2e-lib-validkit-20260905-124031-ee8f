from ._common import MAX_INPUT_LENGTH


def is_valid_isbn13(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if len(text) > MAX_INPUT_LENGTH:
        raise ValueError("input exceeds the maximum allowed length")

    digits = text.replace("-", "").replace(" ", "")

    if len(digits) != 13:
        raise ValueError("ISBN-13 must contain exactly 13 digits")

    if not digits.isascii() or not digits.isdigit():
        raise ValueError("ISBN-13 must contain only digits")

    total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits))
    return total % 10 == 0
