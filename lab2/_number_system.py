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
