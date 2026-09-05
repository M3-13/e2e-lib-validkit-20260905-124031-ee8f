from typing import TypeVar

T = TypeVar("T", int, float)


def clamp(value: T, low: T, high: T) -> T:  # noqa: UP047 - PEP 695 needs 3.12+, pkg targets >=3.9
    raise NotImplementedError
