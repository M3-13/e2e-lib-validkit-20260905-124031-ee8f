import pytest

from validkit._common import MAX_INPUT_LENGTH
from validkit.email import is_valid_email


def test_valid_plain_email():
    assert is_valid_email("user@example.com") is True


def test_valid_email_with_special_local_chars():
    assert is_valid_email("first.last+tag@sub.example.co.uk") is True


def test_valid_email_with_digits_and_hyphen():
    assert is_valid_email("user-123@ex-ample.com") is True


def test_email_without_at_is_false():
    assert is_valid_email("userexample.com") is False


def test_email_with_missing_domain_is_false():
    assert is_valid_email("user@") is False


def test_email_with_missing_local_part_is_false():
    assert is_valid_email("@example.com") is False


def test_email_with_multiple_at_is_false():
    assert is_valid_email("user@name@example.com") is False


def test_email_with_domain_without_dot_is_false():
    assert is_valid_email("user@localhost") is False


def test_empty_string_is_false():
    assert is_valid_email("") is False


def test_email_with_space_is_false():
    assert is_valid_email("user name@example.com") is False


def test_email_with_space_in_domain_is_false():
    assert is_valid_email("user@exam ple.com") is False


def test_email_with_invalid_local_char_is_false():
    assert is_valid_email("us()er@example.com") is False


def test_email_with_trailing_dot_in_domain_is_false():
    assert is_valid_email("user@example.com.") is False


def test_email_with_empty_label_is_false():
    assert is_valid_email("user@example..com") is False


def test_non_string_input_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_email(123)


def test_none_input_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_email(None)


def test_overlong_input_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_email("a" * (MAX_INPUT_LENGTH + 1) + "@example.com")


def test_input_exactly_at_max_length_does_not_raise():
    text = "a" * (MAX_INPUT_LENGTH - len("@example.com")) + "@example.com"
    assert isinstance(is_valid_email(text), bool)


def test_backtracking_suspect_input_is_handled_linearly():
    text = ("a" * 2000) + "@" + ("b" * 2000)
    assert is_valid_email(text) is False


def test_backtracking_suspect_domain_is_handled_linearly():
    text = "user@" + ".".join(["x" * 100] * 40)
    assert isinstance(is_valid_email(text), bool)
