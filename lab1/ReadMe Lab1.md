![image](https://github.com/user-attachments/assets/080d6aa1-0ec0-432a-adfc-613f577a139b)# 1 ЗАДАНИЕ 
Вычислить расстояние между 3 городами с помощью данной в задании формуле.
## Решение: 
from math import sqrt

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}


def calculate_distance(city1, city2):
    x1, y1 = sites[city1]
    x2, y2 = sites[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


distances = {}
for city1 in sites.keys():
    distances[city1] = {}
    for city2 in sites.keys():
        if city1 != city2:
            distance = calculate_distance(city1, city2)
            distances[city1][city2] = round(distance, 2)
print(distances)
## Объяснение: 
C помощью функции calculate_distance вычисляем расстояние между городами и делаем так, чтобы не высчитывалось расстояние между одинаковыми городами, после чего это расстояние заносится в список. После всего этого список выводится.
## Скриншот:
![image](https://github.com/user-attachments/assets/edc90b73-f9bb-491a-87bd-c35df839b24f)


# 2 ЗАДАНИЕ 
Находиться ли точка в площади окружности.
## Решение: 
from math import sqrt

radius = 42
print(round(3.1415926 * radius**2, 4))
point_1 = (23, 34)
print(sqrt(point_1[0]**2 + point_1[1]** 2) <= radius)
point_2 = (30, 30)
print(sqrt(point_2[0]**2 + point_2[1]** 2) <= radius)
## Объяснение: 
Вычисляем площадь круга с помощью данного кода и выводим с тончость до 4 знака после запятой.
## Скриншот:
![image](https://github.com/user-attachments/assets/7a6e4641-ee52-4308-a438-daff357aece3)


# 3 ЗАДАНИЕ 
Расставить знаки +, -, * и скобки в выражении 1 ? 2 ? 3 ? 4 ? 5, так чтобы получилось 25.
## Решение:
result = ((1 + 2) * 3 - 4) * 5
print(result)
## Объяснение: 
Подбором находим нужное выражение
## Скриншот:
![image](https://github.com/user-attachments/assets/f1dd411e-b976-4b79-82f0-deaf815c944b)


# 4 ЗАДАНИЕ 
Выведите на консоль с помощью индексации строки, последовательно:
первый фильм
последний
второй 
второй с конца
## Решение: 
my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
print(my_favorite_movies[0:10])
print(my_favorite_movies[-15:])
print(my_favorite_movies[12:25])
print(my_favorite_movies[-22:-17])
## Объяснение: 
Используем срезы
## Скриншот:
![image](https://github.com/user-attachments/assets/86506494-1838-4008-82d3-2795f089d220)


# 5 ЗАДАНИЕ 
Выведите на консоль рост отца в формате. Выведите на консоль общий рост вашей семьи как сумму ростов всех членов.
## Решение: 
my_family = ['Отец', 'Мать', 'Сын', 'Дедушка', 'Бабушка']
my_family_height = [
    ['Отец', 187],
    ['Мать', 168],
    ['Сын', 174],
    ['Дедушка', 184],
    ['Бабушка', 159],
]

father_height = next(height for name, height in my_family_height if name == 'Отец')
print(f'Рост отца - {father_height} см')
total_height = sum(height for name, height in my_family_height)
print(f'Общий рост моей семьи - {total_height} см')
## Объяснение: 
Находим рост отца, потом считаем общий рост
## Скриншот:
![image](https://github.com/user-attachments/assets/3bfdbd37-569f-4e12-b180-e2b993f36be1)


# 6 ЗАДАНИЕ 
Удаление, добавление, изменение списков.
## Решение: 
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(2, 'bear')
print(zoo)
birds = ['rooster', 'ostrich', 'lark', ]
zoo += birds
print(zoo)
zoo.remove('elephant')
print(zoo)
print("Лев - ", zoo.index('lion') + 1)
print("Жаворонок - ", zoo.index('lark') + 1)
## Объяснение: 
Работаем с массивами, идем по ходу задачи
## Скриншот:
![image](https://github.com/user-attachments/assets/357cd758-b2b1-4007-8241-fa9c5a063f68)


# 7 ЗАДАНИЕ 
Посчитать продолжительность треков, до 2 знаков после запятой.
## Решение: 
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
time = 0
for song in violator_songs_list:
    if song[0] == 'Halo' or song[0] == 'Enjoy the Silence' or song[0] == 'Clean':
        time += song[1]
print(f'Три песни звучат {round(time, 2)} минут')
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
time = 0
for song in violator_songs_dict.keys():
    if song == 'Sweetest Perfection':
        time += violator_songs_dict['Sweetest Perfection']
    if song == 'Policy of Truth':
        time += violator_songs_dict['Policy of Truth']
    if song == 'Blue Dress':
        time += violator_songs_dict['Blue Dress']
print(f'А другие три песни звучат {round(time, 2)} минут')
## Объяснение: 
Используем циклы и ищем совпадения
## Скриншот:
![image](https://github.com/user-attachments/assets/018fb2d5-30aa-497e-ac97-6d55219f08a0)


# 8 ЗАДАНИЕ 
Расшифровать сообщение
## Решение: 
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
print(secret_message[0][3], end=' ')
print(secret_message[1][9:13], end=' ')
print(secret_message[2][5:15:2], end=' ')
print(secret_message[3][12:6:-1], end=' ')
print(secret_message[4][20:15:-1])
## Объяснение: 
Используем срезы как написанно в задании
## Скриншот:
![image](https://github.com/user-attachments/assets/a6dcb40c-b784-4873-9c97-e1da2f158674)


# 9 ЗАДАНИЕ 
Определить нужные цветы
## Решение: 
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
garden_set = set(garden)
meadow_set = set(meadow)
print(*garden_set)
print(*meadow_set)
print(*set(garden + meadow))
print(*garden_set & meadow_set)
print(*garden_set - meadow_set)
print(*meadow_set - garden_set)
## Объяснение: 
Работаем с множествами
## Скриншот:
![image](https://github.com/user-attachments/assets/d28233d7-a301-4447-ae7d-6b49a680551c)


# 10 ЗАДАНИЕ 
Создать словарь цен на продукты
## Решение: 
shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}
sweets = {
    'печенье': [
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'ашан', 'price': 10.99},
    ],
    'конфеты': [
        {'shop': 'магнит', 'price': 30.99},
        {'shop': 'пятерочка', 'price': 32.99},
    ],
    'карамель': [
        {'shop': 'магнит', 'price': 41.99},
        {'shop': 'ашан', 'price': 45.99},
    ],
    'пирожное': [
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ],
}
print(sweets)
## Объяснение: 
Смотрим на цены и выбираем самое дешевое
## Скриншот:
![image](https://github.com/user-attachments/assets/e8df5610-1ab4-43b7-80b5-27185f2a3566)


# 11 ЗАДАНИЕ 
Расчитать сумму товаров
## Решение: 
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

table_quantity = store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity']
table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price'] \
             + store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
print(f'Стол - {table_quantity}, стоимость {table_cost} руб')

couch_quantity = store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']
couch_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price'] \
             + store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
print(f'Диван - {couch_quantity}, стоимость {couch_cost} руб')

chair_quantity = store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] \
                 + store[goods['Стул']][2]['quantity']
chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price'] \
             + store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price'] \
             + store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
print(f'Стул - {chair_quantity}, стоимость {chair_cost} руб')
## Объяснение: 
Работаем по примеру
## Скриншот:
![image](https://github.com/user-attachments/assets/a00de930-f0bf-4931-8e28-2aef3ffb4047)


# Шпаргалка по работе с командами git:
Инициализация репозитория:
git init # Создает новый локальный репозиторий
Клонирование репозитория:
git clone <url_репозитория> # Клонирует удаленный репозиторий
Добавление файлов для отслеживания:
git add <имя_файла> # Добавляет файл под контроль версий
git add . # Добавляет все изменения в текущем каталоге
Фиксация изменений (коммит):
git commit -m "<сообщение>" # Фиксирует изменения с сообщением
Просмотр статуса репозитория:
git status # Показывает статус рабочего дерева
История коммитов:
git log # Просматривает историю коммитов
git log --oneline # Упрощенная версия истории
Создание ветки:
git branch <название_ветки> # Создает новую ветку
Переключение между ветками:
git checkout <название_ветки> # Переключает на указанную ветку
Объединение веток:
git merge <название_ветки> # Объединяет текущую ветку с указанной
Удаление ветки:
git branch -d <название_ветки> # Удаляет ветку после слияния
Добавление удаленного репозитория:
git remote add origin <url_удаленного_репозитория> # Связывание с удаленным репозиторием
Отправка изменений на сервер:
git push origin <название_ветки> # Отправляет изменения на удаленный репозиторий
Получение обновлений с сервера:
git pull origin <название_ветки> # Получает обновления с удаленного репозитория
Откат последних изменений:
git reset HEAD~1 # Отменяет последний коммит
Отмена всех изменений в рабочем дереве:
git checkout -- <имя_файла> # Возвращает файл к состоянию последнего коммита
