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
