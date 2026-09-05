from ._common import MAX_INPUT_LENGTH

_LOCAL_ALLOWED = frozenset(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'*+-/=?^_`{|}~."
)

_DOMAIN_ALLOWED = frozenset("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-")


def is_valid_email(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("input must be a string")
    if len(text) > MAX_INPUT_LENGTH:
        raise ValueError("input exceeds maximum allowed length")

    at = text.find("@")
    if at == -1 or text.find("@", at + 1) != -1:
        return False

    local = text[:at]
    domain = text[at + 1 :]

    if not local or not domain:
        return False

    for char in local:
        if char not in _LOCAL_ALLOWED:
            return False

    if "." not in domain:
        return False

    for label in domain.split("."):
        if not label or label[0] == "-" or label[-1] == "-":
            return False
        for char in label:
            if char not in _DOMAIN_ALLOWED:
                return False

    return True
