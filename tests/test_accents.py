import pytest

from validkit._common import MAX_INPUT_LENGTH
from validkit.accents import strip_accents


def test_strips_accents_and_german_specials():
    assert strip_accents("Grüße, José — déjà vu") == "Gruesse, Jose — deja vu"


def test_plain_ascii_is_unchanged():
    assert strip_accents("hello world 123") == "hello world 123"


def test_empty_string():
    assert strip_accents("") == ""


def test_punctuation_unchanged():
    assert strip_accents("— \u2013 … ! ? , .") == "— \u2013 … ! ? , ."


def test_uppercase_umlauts():
    assert strip_accents("ÄÖÜ") == "AeOeUe"


def test_single_german_special():
    assert strip_accents("ß") == "ss"


def test_already_decomposed_combining_characters():
    assert strip_accents("cafe\u0301") == "cafe"


def test_wrong_type_raises_type_error():
    for value in (123, None, 4.5, ["Grüße"], b"Gru\xc3\xbc\xc3\x9fe"):
        with pytest.raises(TypeError):
            strip_accents(value)


def test_overlong_input_raises_value_error():
    with pytest.raises(ValueError):
        strip_accents("x" * (MAX_INPUT_LENGTH + 1))


def test_exactly_max_length_is_accepted():
    assert strip_accents("a" * MAX_INPUT_LENGTH) == "a" * MAX_INPUT_LENGTH


def test_error_messages_are_static():
    for value in (123, None, 4.5, ["Grüße"], b"bytes"):
        with pytest.raises(TypeError) as exc:
            strip_accents(value)
        assert "Grüße" not in str(exc.value)
        assert "Gru" not in str(exc.value)
    with pytest.raises(ValueError) as exc:
        strip_accents("Grüße" * 2000)
    assert "Grüße" not in str(exc.value)
