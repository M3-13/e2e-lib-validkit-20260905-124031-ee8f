from typing import TypeVar

T = TypeVar("T", int, float)


def clamp(value: T, low: T, high: T) -> T:  # noqa: UP047 - PEP 695 needs 3.12+, pkg targets >=3.9
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("clamp expects value, low and high to be int or float")
    if isinstance(low, bool) or not isinstance(low, (int, float)):
        raise TypeError("clamp expects value, low and high to be int or float")
    if isinstance(high, bool) or not isinstance(high, (int, float)):
        raise TypeError("clamp expects value, low and high to be int or float")

    if low > high:
        raise ValueError("low must not be greater than high")

    if value < low:
        return type(value)(low)
    if value > high:
        return type(value)(high)
    return value
