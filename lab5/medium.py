import pytest
from rare import generate_password, invert_case


@pytest.mark.parametrize(
    "length, expected_len",
    [
        (5, 5),
        (10, 10),
        (15, 15),
        (20, 20),
    ],
)
def test_generate_password_length(length, expected_len):
    password = generate_password(length)
    assert len(password) == expected_len


@pytest.mark.parametrize(
    "char, expected",
    [
        ("A", "a"),
        ("b", "B"),
        ("1", "1"),
        ("!", "!"),
    ],
)
def test_invert_case_functionality(char, expected):
    result = invert_case(char)
    assert result == expected


@pytest.fixture
def generated_password():
    return generate_password(10)


def test_contains_upper_and_lower(generated_password):
    has_upper = any(c.isupper() for c in generated_password)
    has_lower = any(c.islower() for c in generated_password)
    assert has_upper and has_lower


def test_contains_digit(generated_password):
    has_digit = any(c.isdigit() for c in generated_password)
    assert has_digit


def test_contains_special_char(generated_password):
    special_chars = set(r"!@#$%^&*()_+{}:\"<>?|")
    has_special = any(c in special_chars for c in generated_password)
    assert has_special


def test_contains_punctuation(generated_password):
    punctuation_chars = set(",.;:")
    has_punctuation = any(c in punctuation_chars for c in generated_password)
    assert has_punctuation
