# 1 ЗАДАНИЕ 
Ученица составляет 5-буквенные слова из букв ГЕПАРД. При этом в каждом слове ровно одна буква Г, слово не может начинаться на букву А и заканчиваться буквой Е. Какое количество слов может составить ученица?
## Решение: 
```
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
```
## Объяснение: 
C помощью функции calculate_distance вычисляем расстояние между городами и делаем так, чтобы не высчитывалось расстояние между одинаковыми городами, после чего это расстояние заносится в список. После всего этого список выводится.
## Скриншот:
![image](https://github.com/user-attachments/assets/edc90b73-f9bb-491a-87bd-c35df839b24f)
