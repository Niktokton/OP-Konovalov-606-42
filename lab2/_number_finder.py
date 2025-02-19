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
