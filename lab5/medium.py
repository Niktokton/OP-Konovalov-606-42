import pytest

from rare import generate_password, invert_case


# Тест для проверки ошибки при короткой длине пароля
def test_short_password():
    short_length = 5
    expected_result = "Ошибка! Длинна пароля слишком короткая"
    actual_result = next(generate_password(short_length))
    assert actual_result == expected_result


# Тест для проверки генерации пароля правильной длины
def test_correct_length():
    correct_length = 12
    password = next(generate_password(correct_length))
    assert len(password) == correct_length


# Тест для проверки инверсии регистра
def test_inversion():
    input_char = 'A'
    expected_output = 'a'
    actual_output = invert_case(input_char)
    assert actual_output == expected_output

    input_char = 'a'
    expected_output = 'A'
    actual_output = invert_case(input_char)
    assert actual_output == expected_output


# Тест для проверки разнообразия символов в пароле
def test_symbol_variety():
    password_length = 16
    password = next(generate_password(password_length))

    # Проверка наличия цифр
    assert any(char.isdigit() for char in password)

    # Проверка наличия букв
    assert any(char.isalpha() for char in password)

    # Проверка наличия специальных символов
    special_chars = '!@#$%^&*()_+{}:"<>?|'
    assert any(char in special_chars for char in password)

    # Проверка наличия знаков препинания
    punctuation_chars = ',.;:'
    assert any(char in punctuation_chars for char in password)
