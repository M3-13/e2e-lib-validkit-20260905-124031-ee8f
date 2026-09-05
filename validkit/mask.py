from ._common import MAX_INPUT_LENGTH


def mask_secret(text: str, keep: int = 4) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if len(text) > MAX_INPUT_LENGTH:
        raise ValueError("input too long")
    if not isinstance(keep, int):
        raise TypeError("keep must be an integer")
    if keep < 0:
        raise ValueError("keep must be non-negative")
    if keep >= len(text):
        return text
    return "*" * (len(text) - keep) + text[len(text) - keep :]
