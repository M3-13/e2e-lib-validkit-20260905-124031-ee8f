import pytest

import validkit
from validkit._common import MAX_INPUT_LENGTH


def test_valid_german_iban_with_spaces():
    assert validkit.is_valid_iban("DE44 5001 0517 5407 3249 31") is True


def test_valid_iban_lowercase_and_no_spaces():
    assert validkit.is_valid_iban("de44500105175407324931") is True


def test_changed_digit_returns_false():
    assert validkit.is_valid_iban("DE45 5001 0517 5407 3249 31") is False


def test_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        validkit.is_valid_iban(12345)
    with pytest.raises(TypeError):
        validkit.is_valid_iban(None)


def test_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        validkit.is_valid_iban("")


def test_whitespace_only_raises_value_error():
    with pytest.raises(ValueError):
        validkit.is_valid_iban("   ")


def test_invalid_characters_raise_value_error():
    with pytest.raises(ValueError):
        validkit.is_valid_iban("DE44500105175407324931!")


def test_too_short_raises_value_error():
    with pytest.raises(ValueError):
        validkit.is_valid_iban("DE44")


def test_overlong_input_raises_value_error():
    with pytest.raises(ValueError):
        validkit.is_valid_iban("A" * (MAX_INPUT_LENGTH + 1))


def test_error_messages_are_static_and_do_not_echo_input():
    bad = "DE44500105175407324931!"
    with pytest.raises(ValueError) as exc_info:
        validkit.is_valid_iban(bad)
    assert bad not in str(exc_info.value)
