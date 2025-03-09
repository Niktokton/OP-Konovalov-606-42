import random
import string


def invert_case(c):
    return c.lower() if c.isupper() else c.upper()


def generate_password(length):
    if length < 5:
        return "Ошибка! Длинна пароля слишком короткая"
    password = []
    requirements_met = {
        'digit': False,
        'lowercase_letter': False,
        'uppercase_letter': False,
        'special_char': False,
        'punctuation': False
    }
    for _ in range(length):
        num = random.randint(0, 9)
        if num <= 3:
            char = str(random.randint(0, 9))
            requirements_met['digit'] = True
        elif num <= 7:
            char = random.choice(string.ascii_letters)
            if char.isupper():
                requirements_met['uppercase_letter'] = True
            else:
                requirements_met['lowercase_letter'] = True
        elif num == 8:
            special_chars = '!@#$%^&*()_+{}:"<>?|'
            char = random.choice(special_chars)
            requirements_met['special_char'] = True
        else:
            punctuation_chars = ',.;:'
            char = random.choice(punctuation_chars)
            requirements_met['punctuation'] = True
        password.append(char)
    if all(requirements_met.values()):
        password_str = ''.join(password)
        inverted_password = ''.join(map(invert_case, password_str))
        return inverted_password
    else:
        return generate_password(length)


for i in range(5):
    print(f"Сгенерированный пароль: {generate_password(10)}")
