class NumberSystemConverter:
    def __init__(self, expression, base, condition):
        """
        Конструктор класса.

        :param expression: Выражение в виде строки.
        :param base: Основание системы счисления.
        :param condition: Условие для поиска (цифра, которую нужно посчитать).
        """
        self.expression = expression
        self.base = base
        self.condition = condition
        self.result = None

    def evaluate_expression(self):
        """
        Оценивает выражение и сохраняет результат.
        """
        try:
            self.result = eval(self.expression)
        except Exception as e:
            raise ValueError(f"Ошибка при вычислении выражения: {e}")

    def convert_to_base(self):
        """
        Преобразует результат выражения в систему счисления с заданным основанием.
        """
        if self.result is None:
            self.evaluate_expression()
        digits = []
        num = self.result
        while num > 0:
            digits.append(num % self.base)
            num //= self.base
        return ''.join(str(digit) for digit in reversed(digits))

    def count_digits(self):
        """
        Считает количество заданных цифр в представлении числа в новой системе счисления.
        """
        converted_number = self.convert_to_base()
        return converted_number.count(str(self.condition))

    def get_value_in_base(self, new_base):
        """
        Возвращает значение выражения в системе счисления с новым основанием.
        """
        if self.result is None:
            self.evaluate_expression()
        digits = []
        num = self.result
        while num > 0:
            digits.append(num % new_base)
            num //= new_base
        return ''.join(str(digit) for digit in reversed(digits))


# Пример использования класса

converter = NumberSystemConverter(expression="5**36 + 5**24 - 25", base=5, condition='4')
print(converter.count_digits())  # Количество цифр '4' в представлении числа в системе счисления с основанием 5
print(converter.get_value_in_base(new_base=5))  # Значение выражения в десятичной системе счисления
