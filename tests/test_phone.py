import pytest

from validkit import normalize_phone
from validkit._common import MAX_INPUT_LENGTH


def test_normalize_national_number_strips_trunk_zero():
    assert normalize_phone("030 1234567", "49") == "+49301234567"


def test_normalize_international_number_stays_e164():
    assert normalize_phone("+1 (415) 555-0132", "1") == "+14155550132"


def test_normalize_full_number_with_trunk_prefix_in_parens():
    assert normalize_phone("+49 (0) 30 1234567", "49") == "+49301234567"


def test_normalize_already_e164_is_idempotent():
    assert normalize_phone("+49301234567", "49") == "+49301234567"


def test_normalize_national_number_without_trunk_zero():
    assert normalize_phone("301234567", "49") == "+49301234567"


def test_normalize_embedded_country_code_without_plus():
    assert normalize_phone("49301234567", "49") == "+49301234567"


def test_empty_text_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("", "49")


def test_text_with_only_special_characters_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("---  ...", "49")


def test_non_string_text_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone(301234567, "49")


def test_none_text_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone(None, "49")


def test_non_string_country_code_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone("030 1234567", 49)


def test_overlong_text_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("1" * (MAX_INPUT_LENGTH + 1), "49")


def test_overlong_country_code_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "9" * (MAX_INPUT_LENGTH + 1))


def test_text_at_max_length_is_accepted():
    result = normalize_phone("1" * MAX_INPUT_LENGTH, "1")
    assert result == "+1" + "1" * (MAX_INPUT_LENGTH - 1)


def test_empty_country_code_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "")


def test_non_digit_country_code_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "DE")


def test_text_that_is_only_the_country_code_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("49", "49")


def test_error_messages_are_static():
    with pytest.raises(ValueError) as excinfo:
        normalize_phone("!!!###", "49")
    assert "!!!###" not in str(excinfo.value)

    with pytest.raises(TypeError) as excinfo:
        normalize_phone(123, "49")
    assert "123" not in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        normalize_phone("030 1234567", "DE")
    assert "030 1234567" not in str(excinfo.value)
