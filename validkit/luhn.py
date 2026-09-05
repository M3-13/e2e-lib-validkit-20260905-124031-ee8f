from ._common import MAX_INPUT_LENGTH


def luhn_check(digits: str) -> bool:
    if not isinstance(digits, str):
        raise TypeError("luhn_check expects a string")

    if len(digits) > MAX_INPUT_LENGTH:
        raise ValueError("input exceeds maximum allowed length")

    cleaned = digits.replace(" ", "")

    if cleaned == "":
        return False

    if not cleaned.isdigit():
        raise ValueError("input must contain only digits and spaces")

    total = 0
    for index, char in enumerate(reversed(cleaned)):
        value = int(char)
        if index % 2 == 1:
            value *= 2
            if value > 9:
                value -= 9
        total += value

    return total % 10 == 0
