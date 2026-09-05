import pytest

from validkit import mask_secret
from validkit._common import MAX_INPUT_LENGTH


def test_mask_secret_keeps_last_n_visible():
    assert mask_secret("geheim1234", 4) == "******1234"


def test_mask_secret_default_keep_is_four():
    assert mask_secret("geheim1234") == "******1234"


def test_mask_secret_keep_zero_masks_everything():
    assert mask_secret("geheim1234", 0) == "**********"


def test_mask_secret_keep_greater_than_length_returns_original():
    assert mask_secret("geheim1234", 20) == "geheim1234"


def test_mask_secret_keep_equal_to_length_returns_original():
    assert mask_secret("geheim1234", 10) == "geheim1234"


def test_mask_secret_empty_text():
    assert mask_secret("", 4) == ""
    assert mask_secret("", 0) == ""


def test_mask_secret_keep_one():
    assert mask_secret("geheim1234", 1) == "*********4"


def test_mask_secret_negative_keep_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("geheim1234", -1)


def test_mask_secret_non_int_keep_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret("geheim1234", "4")  # type: ignore[arg-type]


def test_mask_secret_float_keep_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret("geheim1234", 4.0)  # type: ignore[arg-type]


def test_mask_secret_non_str_text_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret(1234, 4)  # type: ignore[arg-type]


def test_mask_secret_overlong_text_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("x" * (MAX_INPUT_LENGTH + 1), 4)


def test_mask_secret_max_length_text_is_accepted():
    assert mask_secret("x" * MAX_INPUT_LENGTH, 0) == "*" * MAX_INPUT_LENGTH


def test_mask_secret_error_messages_are_static():
    with pytest.raises(ValueError, match=r"input too long"):
        mask_secret("x" * (MAX_INPUT_LENGTH + 1), 4)
    with pytest.raises(ValueError, match=r"keep must be non-negative"):
        mask_secret("geheim1234", -1)
    with pytest.raises(TypeError, match=r"keep must be an integer"):
        mask_secret("geheim1234", "4")  # type: ignore[arg-type]
    with pytest.raises(TypeError, match=r"text must be a string"):
        mask_secret(1234, 4)  # type: ignore[arg-type]
