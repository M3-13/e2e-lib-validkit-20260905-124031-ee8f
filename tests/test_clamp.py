import pytest

from validkit.clamp import clamp


def test_clamp_value_within_range_returns_unchanged():
    assert clamp(5, 0, 10) == 5


def test_clamp_value_below_range_returns_low():
    assert clamp(-3, 0, 10) == 0


def test_clamp_value_above_range_returns_high():
    assert clamp(20, 0, 10) == 10


def test_clamp_value_equal_to_low():
    assert clamp(0, 0, 10) == 0


def test_clamp_value_equal_to_high():
    assert clamp(10, 0, 10) == 10


def test_clamp_preserves_int_type():
    result = clamp(-3, 0, 10)
    assert isinstance(result, int)


def test_clamp_preserves_float_type():
    assert clamp(2.5, 0.0, 10.0) == 2.5
    assert clamp(-3.5, 0.0, 10.0) == 0.0
    assert clamp(20.5, 0.0, 10.0) == 10.0


def test_clamp_low_greater_than_high_raises_value_error():
    with pytest.raises(ValueError):
        clamp(1, 5, 3)


def test_clamp_error_message_is_static_and_contains_no_input():
    with pytest.raises(ValueError) as excinfo:
        clamp(1, 5, 3)
    assert "5" not in str(excinfo.value)
    assert "3" not in str(excinfo.value)


def test_clamp_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        clamp("5", 0, 10)
    with pytest.raises(TypeError):
        clamp(5, "0", 10)
    with pytest.raises(TypeError):
        clamp(5, 0, "10")


def test_clamp_bool_is_rejected_as_wrong_type():
    with pytest.raises(TypeError):
        clamp(True, 0, 10)
