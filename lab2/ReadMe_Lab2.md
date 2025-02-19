# 1 ЗАДАНИЕ 
Ученица составляет 5-буквенные слова из букв ГЕПАРД. При этом в каждом слове ровно одна буква Г, слово не может начинаться на букву А и заканчиваться буквой Е. Какое количество слов может составить ученица?
## Решение: 
```
from itertools import product


class WordSolver:
    def __init__(self, n_letters, letters, printword=0, conditions=None):
        self.n_letters = n_letters
        self.letters = list(sorted(set(letters)))
        self.printword = printword
        self.conditions = conditions or {}
        self.value_dict = {letter: i for i, letter in enumerate(self.letters)}

    def value(self):
        return ', '.join(f'{letter} - {i}' for letter, i in self.value_dict.items())

    def count_words(self):
        total_count = 0
        for first_letter in self.letters:
            if 'first' in self.conditions and first_letter in self.conditions['first']:
                continue
            for last_letter in self.letters:
                if 'last' in self.conditions and last_letter in self.conditions['last']:
                    continue
                for inner_word in self.generate_inner_words():
                    word = first_letter + inner_word + last_letter
                    if self.is_valid(word):
                        total_count += 1
        return total_count

    def generate_inner_words(self):
        return (''.join(p) for p in product(self.letters, repeat=self.n_letters - 2))

    def is_valid(self, word):
        if 'positions' in self.conditions:
            for pos, banned_letters in self.conditions['positions'].items():
                if word[pos - 1] in banned_letters:
                    return False
        if 'occurrences' in self.conditions:
            for letter, required_occurrence in self.conditions['occurrences'].items():
                if word.count(letter) != required_occurrence:
                    return False
        return True


# Решение задачи из примера

solver = WordSolver(
    n_letters=5,
    letters="ГЕПАРД",
    conditions={
        'first': ['А'],
        'last': ['Е'],
        'occurrences': {'Г': 1}
    }
)

print(solver.value())
print(solver.count_words())
```
## Объяснение: 
Создаём класс WordSolver, внутри которого и будет решение задачи. На входе класс получает несколько обязательных и необязательных значений. 
Обязательные: 
    n_letters - количество букв в слове; 
    letters - слово, буквы которого используются как алфавит. 
Необязательные: 
    printword - выводить ли полученные слова (по умолчанию 0, не выводить); 
    conditions - условия для задачи (
        first - недопустимые первые буквы, пример - 'first': ['А']; 
        last - недопустимые последие буквы, пример - 'last': ['Е']; 
        positions - запрещённые буквы на конкретных позициях, пример - 'positions': {3: ['А']}, примечание - указывается не индекс, а номер буквы, то есть отсчёт идет с 1, а не с 0; 
        occurrences - требуемая частота появления, пример - 'occurrences': {'Г': 1})
## Скриншот:
![image](https://github.com/user-attachments/assets/108ce74a-5555-4a49-828a-704ed644a587)

# 2 ЗАДАНИЕ 
Значение выражения 5^36 + 5^24 − 25 записали в системе счисления с основанием 5. Сколько цифр 4 содержится в этой записи?
## Решение: 
```
```
## Объяснение: 
Создаём класс WordSolver, внутри которого и будет решение задачи. На входе класс получает несколько обязательных и необязательных значений. 
Обязательные: 
    n_letters - количество букв в слове; 
    letters - слово, буквы которого используются как алфавит. 
Необязательные: 
    printword - выводить ли полученные слова (по умолчанию 0, не выводить); 
    conditions - условия для задачи (
        first - недопустимые первые буквы, пример - 'first': ['А']; 
        last - недопустимые последие буквы, пример - 'last': ['Е']; 
        positions - запрещённые буквы на конкретных позициях, пример - 'positions': {3: ['А']}, примечание - указывается не индекс, а номер буквы, то есть отсчёт идет с 1, а не с 0; 
        occurrences - требуемая частота появления, пример - 'occurrences': {'Г': 1})
## Скриншот:
