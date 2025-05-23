from _00_distance import distances
from _01_circle import area, area_calc
from _02_operations import result
from _03_favorite_movies import my_favorite_movies
from _04_my_family import total_height
from _05_zoo import zoo
from _06_songs_list import time, time2
from _07_secret import secret_message
from _08_garden import garden_set, meadow_set
from _09_shopping import sweets
from _10_store import lamps_quantity, table_quantity, couch_quantity, chair_quantity


def main():
    print("Задача 0 -", distances)
    print("Задача 1 -", area)
    print("Задача 2 -", result)
    print("Задача 3 -", my_favorite_movies)
    print("Задача 4 -", total_height)
    print("Задача 5 -", zoo)
    print("Задача 6 -", time, time2)
    print("Задача 7 -", secret_message)
    print("Задача 8 -", garden_set, meadow_set)
    print("Задача 9 -", sweets)
    print("Задача 10 -", lamps_quantity, table_quantity, couch_quantity, chair_quantity)


def func(radius):
    return (area_calc(radius))


if __name__ == "__main__":
    main()
    print("-----------------------------------------")
    radius = 10
    print(func(radius))
