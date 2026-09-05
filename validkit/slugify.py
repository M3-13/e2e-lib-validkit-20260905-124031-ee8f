import unicodedata

from ._common import MAX_INPUT_LENGTH


def slugify(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if len(text) > MAX_INPUT_LENGTH:
        raise ValueError("text exceeds the maximum allowed length")

    normalized = unicodedata.normalize("NFKD", text)
    without_accents = "".join(c for c in normalized if not unicodedata.combining(c))
    lowered = without_accents.lower()

    result = []
    for char in lowered:
        if char.isalnum():
            result.append(char)
        elif not result or result[-1] != "-":
            result.append("-")

    return "".join(result).strip("-")
