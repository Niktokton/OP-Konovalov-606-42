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


def answer():
    print(distances)


distances = {}
for city1 in sites.keys():
    distances[city1] = {}
    for city2 in sites.keys():
        if city1 != city2:
            distance = calculate_distance(city1, city2)
            distances[city1][city2] = round(distance, 2)

if __name__ == "__main__":
    answer()
