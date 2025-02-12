from math import sqrt

radius = 42
area = round(3.1415926 * radius ** 2, 4)


def answer():
    print(area)
    point_1 = (23, 34)
    print(sqrt(point_1[0] ** 2 + point_1[1] ** 2) <= radius)
    point_2 = (30, 30)
    print(sqrt(point_2[0] ** 2 + point_2[1] ** 2) <= radius)


if __name__ == "__main__":
    answer()
