import random
import string
from concurrent.futures import ThreadPoolExecutor


def invert_case(c):
    return c.lower() if c.isupper() else c.upper()


def generate_random_char(num):
    if num <= 3:
        char = str(random.randint(0, 9))
        return char
    elif num <= 7:
        char = random.choice(string.ascii_letters)
        return char
    elif num == 8:
        special_chars = '!@#$%^&*()_+{}:"<>?|'
        char = random.choice(special_chars)
        return char
    else:
        punctuation_chars = ',.;:'
        char = random.choice(punctuation_chars)
        return char


def generate_password_thread(length):
    if length < 5:
        yield "Ошибка! Длина пароля слишком короткая"
    password_parts = []
    with ThreadPoolExecutor(max_workers=length) as executor:
        futures = [
            executor.submit(generate_random_char, random.randint(0, 9)) for _ in range(length)
        ]
        for future in futures:
            char = future.result()
            password_parts.append(char)
    password_str = ''.join(password_parts)
    inverted_password = ''.join(map(invert_case, password_str))
    yield inverted_password


if __name__ == "__main__":
    for i in range(5):
        password_generator = generate_password_thread(10)
        for result in password_generator:
            print(f"Сгенерированный пароль: {i}, {result}")
