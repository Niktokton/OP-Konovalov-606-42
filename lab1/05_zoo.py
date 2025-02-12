zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]


def answer(zoo):
    zoo.insert(2, 'bear')
    print(zoo)
    birds = ['rooster', 'ostrich', 'lark', ]
    zoo += birds
    print(zoo)
    zoo.remove('elephant')
    print(zoo)
    print("Лев - ", zoo.index('lion') + 1)
    print("Жаворонок - ", zoo.index('lark') + 1)


if __name__ == "__main__":
    answer(zoo)
