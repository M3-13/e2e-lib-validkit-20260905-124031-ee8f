from ._common import MAX_INPUT_LENGTH


def normalize_phone(text: str, country_code: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(country_code, str):
        raise TypeError("country_code must be a string")

    if len(text) > MAX_INPUT_LENGTH:
        raise ValueError("text exceeds maximum length")
    if len(country_code) > MAX_INPUT_LENGTH:
        raise ValueError("country_code exceeds maximum length")

    if not country_code.isdigit():
        raise ValueError("country_code must contain only digits")

    digits = "".join(ch for ch in text if ch.isdigit())
    if not digits:
        raise ValueError("text contains no digits")

    national = digits[len(country_code) :] if digits.startswith(country_code) else digits

    if national.startswith("0"):
        national = national[1:]

    if not national:
        raise ValueError("text contains no national number")

    return "+" + country_code + national
