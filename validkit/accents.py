import unicodedata

from ._common import MAX_INPUT_LENGTH

_GERMAN_ASCII = str.maketrans(
    {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "ß": "ss",
        "Ä": "Ae",
        "Ö": "Oe",
        "Ü": "Ue",
        "ẞ": "SS",
    }
)


def strip_accents(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("strip_accents expects a str argument")
    if len(text) > MAX_INPUT_LENGTH:
        raise ValueError("input exceeds maximum length")

    transliterated = text.translate(_GERMAN_ASCII)
    decomposed = unicodedata.normalize("NFD", transliterated)
    return "".join(char for char in decomposed if unicodedata.category(char) != "Mn")
