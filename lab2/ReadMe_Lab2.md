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
    letters - слово, буквы которого используются как алфавит
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
class NumberSystemConverter:
    def __init__(self, expression, base, condition):
        self.expression = expression
        self.base = base
        self.condition = condition
        self.result = eval(self.expression)

    def convert_to_base(self):
        digits = []
        num = self.result
        while num > 0:
            digits.append(num % self.base)
            num //= self.base
        return ''.join(str(digit) for digit in reversed(digits))

    def count_digits(self):
        converted_number = self.convert_to_base()
        return converted_number.count(str(self.condition))

    def get_value_in_base(self, new_base):
        digits = []
        num = self.result
        while num > 0:
            digits.append(num % new_base)
            num //= new_base
        return ''.join(str(digit) for digit in reversed(digits))


# Решение задачи из примера

converter = NumberSystemConverter(expression="5**36 + 5**24 - 25", base=5, condition=4)
print(converter.count_digits())
print(converter.get_value_in_base(new_base=5))
```
## Объяснение: 
Создаём класс NumberSystemConverter, внутри которого и будет решение задачи. На входе класс получает несколько обязательных значений. 
Обязательные: 
    expression - выражение в формате str; 
    base - система счисления, в которой будет записанно значение выражения;
    condition - цифра, количество которой надо посчитать
## Скриншот:
![image](https://github.com/user-attachments/assets/c7b21bfc-d284-4a38-b179-1173610ec3f4)

# 3 ЗАДАНИЕ 
Найдите 5 чисел больших 500000, таких, что среди их делителей есть число, оканчивающееся на 8, при этом этот делитель не равен 8 и самому числу. В качестве ответа приведите 5 наименьших чисел, соответствующих условию.

Формат вывода: для каждого из 5 таких найденных чисел в отдельной строке сначала выводится само число, затем минимальный делитель, оканчивающийся на 8, не равный 8 и самому числу.
## Решение: 
```
class NumberFinder:
    def __init__(self, n_numbers, comparison_type, target_number, conditions=None):
        self.n_numbers = n_numbers
        self.comparison_type = comparison_type
        self.target_number = target_number
        self.conditions = conditions or {}
        self.found_numbers = []

    def find_numbers(self):
        number = self.target_number
        while len(self.found_numbers) < self.n_numbers:
            if self.check_conditions(number):
                self.found_numbers.append(number)
            if self.comparison_type == 'bigger':
                number += 1
            elif self.comparison_type == 'smaller':
                number -= 1

    def check_conditions(self, number):
        for divisor in range(18, number // 2 + 1, 10):
            if number % divisor == 0 and divisor != number:
                if 'ends_with' in self.conditions:
                    if str(divisor)[-1] != self.conditions['ends_with']:
                        return False
                if 'not_equal_to' in self.conditions:
                    if divisor == self.conditions['not_equal_to']:
                        return False
                return True
        return False

    def print_results(self):
        for number in self.found_numbers:
            for divisor in range(18, number // 2 + 1, 10):
                if number % divisor == 0 and divisor != number:
                    print(f"{number} {divisor}")
                    break


# Решение задачи из примера

finder = NumberFinder(n_numbers=5, comparison_type='bigger', target_number=500000,
                      conditions={'ends_with': '8', 'not_equal_to': 8})
finder.find_numbers()
finder.print_results()
```
## Объяснение: 
Создаём класс NumberFinder, внутри которого и будет решение задачи. На входе класс получает несколько обязательных значений и одно необязательное. 
Обязательные: 
    n_numbers - количество чисел, которые нужно найти; 
    comparison_type - тип сравнения (bigger или smaller);
    target_number - число, относительно которого идет счет
Необязательное:
    conditions - условия для задачи(
        ends_with - на какую цифру заканчивается, пример - 'ends_with': '8'
        not_equal_to - не равен какому числу, пример - 'not_equal_to': 8)
## Скриншот:
![image](https://github.com/user-attachments/assets/409587e6-6b0d-4826-9730-af654cb8edd5)
