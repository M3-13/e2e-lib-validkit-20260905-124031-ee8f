import pytest

from validkit import luhn_check


def test_valid_card_number_with_spaces():
    assert luhn_check("4111 1111 1111 1111") is True


def test_valid_card_number_without_spaces():
    assert luhn_check("4111111111111111") is True


def test_known_valid_number():
    assert luhn_check("49927398716") is True


def test_one_digit_changed_returns_false():
    assert luhn_check("4111 1111 1111 1112") is False


def test_doubled_digit_changed_returns_false():
    assert luhn_check("5111 1111 1111 1111") is False


def test_empty_string_returns_false():
    assert luhn_check("") is False


def test_whitespace_only_returns_false():
    assert luhn_check("   ") is False


@pytest.mark.parametrize("value", [None, 4111111111111111, ["4111 1111 1111 1111"], 4.0, {}])
def test_wrong_type_raises_type_error(value):
    with pytest.raises(TypeError):
        luhn_check(value)


def test_non_digit_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("4111 1111 1111 111A")


def test_separator_chars_raise_value_error():
    with pytest.raises(ValueError):
        luhn_check("4111-1111-1111-1111")


def test_overlong_input_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("1" * (4096 + 1))


def test_max_length_input_is_not_rejected_on_length():
    assert luhn_check("1" * 4096) is False


def test_value_error_message_is_static():
    with pytest.raises(ValueError) as exc:
        luhn_check("4111 1111 1111 111Z")
    assert "4111" not in str(exc.value)
    assert "Z" not in str(exc.value)


def test_type_error_message_is_static():
    with pytest.raises(TypeError) as exc:
        luhn_check(123)
    assert "123" not in str(exc.value)
