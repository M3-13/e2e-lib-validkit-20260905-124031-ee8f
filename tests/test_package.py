import inspect
import typing

import validkit

EXPECTED_FUNCTIONS = {
    "is_valid_email",
    "luhn_check",
    "is_valid_iban",
    "is_valid_isbn13",
    "normalize_phone",
    "strip_accents",
    "mask_secret",
    "slugify",
    "clamp",
}

EXPECTED_SIGNATURES = {
    "is_valid_email": {"params": ["text"], "return": bool},
    "luhn_check": {"params": ["digits"], "return": bool},
    "is_valid_iban": {"params": ["text"], "return": bool},
    "is_valid_isbn13": {"params": ["text"], "return": bool},
    "normalize_phone": {"params": ["text", "country_code"], "return": str},
    "strip_accents": {"params": ["text"], "return": str},
    "mask_secret": {"params": ["text", "keep"], "return": str, "defaults": {"keep": 4}},
    "slugify": {"params": ["text"], "return": str},
    "clamp": {"params": ["value", "low", "high"]},
}


def test_import_validkit():
    assert validkit is not None


def test_version():
    assert validkit.__version__ == "0.1.0"


def test_all_contains_exactly_nine_names():
    assert len(validkit.__all__) == 9
    assert set(validkit.__all__) == EXPECTED_FUNCTIONS


def test_every_function_is_an_attribute_with_correct_signature():
    for name, expected in EXPECTED_SIGNATURES.items():
        func = getattr(validkit, name)
        assert inspect.isfunction(func), f"{name} is not a function"
        sig = inspect.signature(func)
        assert list(sig.parameters) == expected["params"], f"{name} parameters"
        if "return" in expected:
            assert sig.return_annotation is expected["return"], f"{name} return annotation"
        for pname, default in expected.get("defaults", {}).items():
            assert sig.parameters[pname].default == default, f"{name} default for {pname}"


def test_clamp_return_annotation_is_typevar_constrained_to_int_and_float():
    sig = inspect.signature(validkit.clamp)
    ret = sig.return_annotation
    assert isinstance(ret, typing.TypeVar)
    assert set(ret.__constraints__) == {int, float}
