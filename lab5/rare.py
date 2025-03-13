import random
import string


def invert_case(c):
    return c.lower() if c.isupper() else c.upper()


def generate_password(length):
    if length < 10:
        yield "Ошибка! Длинна пароля слишком короткая"
    password = []
    while len(password) < length:
        num = random.randint(0, 9)
        if num <= 3:
            char = str(random.randint(0, 9))
        elif num <= 7:
            char = random.choice(string.ascii_letters)
        elif num == 8:
            special_chars = '!@#$%^&*()_+{}:"<>?|'
            char = random.choice(special_chars)
        else:
            punctuation_chars = ',.;:'
            char = random.choice(punctuation_chars)
        password.append(char)
    password_str = ''.join(password)
    yield password_str


if __name__ == "__main__":
    for i in range(5):
        password_generator = next(generate_password(10))
        print(f"Сгенерированный пароль: {i}, Изначальный пароль - {password_generator}, Инвертированный - {''.join(map(invert_case, password_generator))}")
