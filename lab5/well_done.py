import random
import string
from concurrent.futures import ThreadPoolExecutor


def invert_case(c):
    return c.lower() if c.isupper() else c.upper()


def generate_random_char(num):
    if num <= 3:
        char = str(random.randint(0, 9))
        return ('digit', char)
    elif num <= 7:
        char = random.choice(string.ascii_letters)
        if char.isupper():
            return ('uppercase_letter', char)
        else:
            return ('lowercase_letter', char)
    elif num == 8:
        special_chars = '!@#$%^&*()_+{}:"<>?|'
        char = random.choice(special_chars)
        return ('special_char', char)
    else:
        punctuation_chars = ',.;:'
        char = random.choice(punctuation_chars)
        return ('punctuation', char)


def generate_password_thread(length):
    if length < 5:
        return "Ошибка! Длина пароля слишком короткая"
    password_parts = []
    requirements_met = {
        'digit': False,
        'lowercase_letter': False,
        'uppercase_letter': False,
        'special_char': False,
        'punctuation': False
    }
    with ThreadPoolExecutor(max_workers=length) as executor:
        futures = [
            executor.submit(generate_random_char, random.randint(0, 9)) for _ in range(length)
        ]
        for future in futures:
            requirement_type, char = future.result()
            password_parts.append(char)
            requirements_met[requirement_type] = True
    if all(requirements_met.values()):
        password_str = ''.join(password_parts)
        inverted_password = ''.join(map(invert_case, password_str))
        return inverted_password
    else:
        return generate_password_thread(length)


if __name__ == "__main__":
    for i in range(5):
        print(f"Сгенерированный пароль: {generate_password_thread(10)}")
