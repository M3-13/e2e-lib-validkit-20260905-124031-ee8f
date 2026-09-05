import pytest

from validkit import slugify
from validkit._common import MAX_INPUT_LENGTH


def test_slugify_normalizes_accents_and_special_characters():
    assert slugify("Héllo Wörld!") == "hello-world"


def test_slugify_empty_string_returns_empty_string():
    assert slugify("") == ""


def test_slugify_only_special_characters_returns_empty_string():
    assert slugify("!!!---...") == ""


def test_slugify_collapses_repeated_dashes_and_trims_edges():
    assert slugify("  Hello   World  ") == "hello-world"
    assert slugify("---a---b---") == "a-b"


def test_slugify_preserves_alphanumeric_characters():
    assert slugify("Foo123Bar") == "foo123bar"


def test_slugify_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        slugify(123)


def test_slugify_input_at_limit_is_accepted():
    assert slugify("a" * MAX_INPUT_LENGTH) == "a" * MAX_INPUT_LENGTH


def test_slugify_overlong_input_raises_value_error():
    with pytest.raises(ValueError):
        slugify("a" * (MAX_INPUT_LENGTH + 1))


def test_slugify_error_messages_are_static_without_user_input():
    with pytest.raises(TypeError) as type_info:
        slugify(12345)
    assert "12345" not in str(type_info.value)

    overlong = "x" * (MAX_INPUT_LENGTH + 1)
    with pytest.raises(ValueError) as value_info:
        slugify(overlong)
    assert overlong not in str(value_info.value)
