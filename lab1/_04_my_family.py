my_family = ['Отец', 'Мать', 'Сын', 'Дедушка', 'Бабушка']
my_family_height = [
    ['Отец', 187],
    ['Мать', 168],
    ['Сын', 174],
    ['Дедушка', 184],
    ['Бабушка', 159],
]
father_height = next(height for name, height in my_family_height if name == 'Отец')
total_height = sum(height for name, height in my_family_height)


def answer():
    print(f'Рост отца - {father_height} см')
    print(f'Общий рост моей семьи - {total_height} см')


if __name__ == "__main__":
    answer()
