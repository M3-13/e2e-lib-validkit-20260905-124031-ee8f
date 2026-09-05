import pytest

from validkit import is_valid_isbn13
from validkit._common import MAX_INPUT_LENGTH


def test_valid_isbn13_with_separators():
    assert is_valid_isbn13("978-3-16-148410-0") is True


def test_valid_isbn13_without_separators():
    assert is_valid_isbn13("9783161484100") is True


def test_valid_isbn13_with_spaces():
    assert is_valid_isbn13("978 3 16 148410 0") is True


def test_wrong_check_digit_is_false():
    assert is_valid_isbn13("978-3-16-148410-1") is False


def test_wrong_check_digit_without_separators_is_false():
    assert is_valid_isbn13("9783161484101") is False


def test_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("")


def test_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_isbn13(9783161484100)  # type: ignore[arg-type]


def test_none_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_isbn13(None)  # type: ignore[arg-type]


def test_twelve_digits_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("978-3-16-148410")


def test_fourteen_digits_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("978-3-16-148410-00")


def test_non_digit_characters_raise_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("978-3-16-14841X-0")


def test_overlong_input_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("9" * (MAX_INPUT_LENGTH + 1))


def test_input_at_max_length_is_not_rejected_as_overlong():
    isbn = " " * (MAX_INPUT_LENGTH - 13) + "9783161484100"
    assert is_valid_isbn13(isbn) is True
