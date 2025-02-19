from itertools import product


class WordSolver:
    def __init__(self, n_letters, letters, printword=0, conditions=None):
        """
        Конструктор класса.

        :param n_letters: Количество букв в словах.
        :param letters: Строка с уникальными буквами.
        :param conditions: Словарь с условиями. Возможные ключи:
            - 'first': недопустимые первые буквы.
            - 'last': недопустимые последние буквы.
            - 'positions': запрещённые буквы на конкретных позициях.
            - 'occurrences': требуемые частоты появления букв.
        """
        self.n_letters = n_letters
        self.letters = list(sorted(set(letters)))  # Список уникальных букв в алфавитном порядке
        self.printword = printword
        self.conditions = conditions or {}
        self.value_dict = {letter: i for i, letter in enumerate(self.letters)}

    def value(self):
        """Функция возвращает соответствие букв цифрам."""
        return ', '.join(f'{letter} - {i}' for letter, i in self.value_dict.items())

    def help(self):
        """Подсказка для решения задач."""
        print("Эта функция пока пустая. Заполните её вручную.")

    def count_words(self):
        """
        Подсчёт количества допустимых слов.

        Возвращает количество слов, удовлетворяющих заданным условиям.
        """
        total_count = 0
        for first_letter in self.letters:
            if 'first' in self.conditions and first_letter in self.conditions['first']:
                continue  # Пропускаем первую букву, если она недопустима
            for last_letter in self.letters:
                if 'last' in self.conditions and last_letter in self.conditions['last']:
                    continue  # Пропускаем последнюю букву, если она недопустима
                for inner_word in self._generate_inner_words():
                    word = first_letter + inner_word + last_letter
                    if self._is_valid(word):
                        total_count += 1
        return total_count

    def _generate_inner_words(self):
        """
        Генерация всех возможных внутренних комбинаций букв длиной n_letters - 2.

        Возвращает генератор всех возможных комбинаций внутренних букв.
        """
        return (''.join(p) for p in product(self.letters, repeat=self.n_letters - 2))

    def _is_valid(self, word):
        """
        Проверка валидности слова согласно дополнительным условиям.

        :param word: Слово для проверки.
        :return: True, если слово соответствует условиям, иначе False.
        """
        if 'positions' in self.conditions:
            for pos, banned_letters in self.conditions['positions'].items():
                if word[pos - 1] in banned_letters:
                    return False
        if 'occurrences' in self.conditions:
            for letter, required_occurrence in self.conditions['occurrences'].items():
                if word.count(letter) != required_occurrence:
                    return False
        return True


# Пример использования класса

solver = WordSolver(
    n_letters=5,
    letters="ГЕПАРД",
    printword=1,
    conditions={
        'first': ['А'],  # Слово не может начинаться на 'А'
        'last': ['Е'],  # Слово не может заканчиваться на 'Е'
        'occurrences': {'Г': 1}  # Буква 'Г' должна встречаться ровно 2 раза
    }
)

print(solver.value())  # Вывод соответствия букв цифрам
print(solver.count_words())  # Подсчет количества возможных слов
