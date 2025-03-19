# Rare
Написать генератор, создающий пароли по определённым правилам. Инвертировать регистр букв в выводе генератора.
## Решение: 
``` python
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
```
## Объяснение: 
Функция generate_password на входе получает число length - необходимую длинну пароля. Проводится проверка значения length, если оно меньше 6 то выводится ошибка. Создаётся массив password, в который будет записан получившийся пароль, и словарь requirements_met, в котором записанны условия правильности пароля.
Потом, в цикле длинной length мы сначало выбираем число от 0 до 9. 0-3 - элементом пароля станет случайное число, 4-7 - элементом пароля станет случайная буква, заглавная или строчная, 8 - случайные специальный символ, 9 - знаки препинания
После проводится проверка на соответствия критериям. Если пароль соответствует, то он собирается в строку, а регистр букв инвертируется, полученный пароль возвращается функцией. Иначе, пароль создаётся заново. 
## Скриншот:
![image](https://github.com/user-attachments/assets/fd02170d-1754-4360-95c7-e9d2bc16511e)


# Well Done
Реализовать многопоточную/параллельную версию генератора. Продемонстровать повышение производительности относительно исходной версии.
## Решение: 
``` python
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
```
## Объяснение: 
Принцпи работы сход с предидущей функцией, но отличается генерация элементов пароля. В функции generate_password_thread параллельно запускается генерация n элементов пароля в отдельной функции generate_random_char
## Скриншот:
![image](https://github.com/user-attachments/assets/113396c9-2ea5-4b7c-97a8-ce6cb079fe6d)


# Источники:
[Нейросеть ГигаЧат](https://giga.chat/gigachat/)
