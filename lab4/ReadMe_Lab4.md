# 1 ЗАДАНИЕ 
Решить обе задачи своего варианта. Применить декоратор к замыканию. Реализовать декоратор классов вместо декоратора функций
1) Замыкание реализующее последовательность Фибоначчи.
2) Декоратор для кэширования результатов выполнения функций.
## Решение: 
``` python
from functools import wraps


def fib_class_decorator(cls):
    cache = {}
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.cache = cache

    cls.__init__ = new_init
    original_next_fib = cls.next_fib

    @wraps(original_next_fib)
    def wrapped_next_fib(self, index=None):
        if index is None:
            result = original_next_fib(self)
            self.cache[len(self.cache)] = result
            return result
        else:
            if index >= len(self.cache):
                while index >= len(self.cache):
                    original_next_fib(self)
            return self.cache[index]

    cls.next_fib = wrapped_next_fib
    return cls


@fib_class_decorator
class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def next_fib(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result
```
## Объяснение: 
Класс Fibonacci инициализирует два первых числа Фибоначчи: a=0 и b=1. Каждый последующий вызов метода next_fib() возвращает следующее число в последовательности, обновляя значения переменных a и b.
Декоратор fib_class_decorator сохраняет предыдущие результаты вызова метода next_fib(), что ускоряет последующие вызовы и позволяет вызывать число Фибоначчи по индексу.
## Скриншот:
![image](https://github.com/user-attachments/assets/dbe3b601-8beb-4712-af0d-2dc009bc472f)

# Источники:
[Нейросеть ГигаЧат](https://giga.chat/gigachat/)
