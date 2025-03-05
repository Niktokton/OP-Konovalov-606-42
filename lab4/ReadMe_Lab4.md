# 1 ЗАДАНИЕ 
Решить обе задачи своего варианта. Применить декоратор к замыканию. Реализовать декоратор классов вместо декоратора функций
1) Замыкание реализующее последовательность Фибоначчи.
2) Декоратор для кэширования результатов выполнения функций.
## Решение: 
```
class CacheDecorator:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.counter = 0

    def __get__(self, instance, owner):
        def wrapped_method():
            if self.counter not in self.cache:
                self.cache[self.counter] = self.func(instance)
            self.counter += 1
            return self.cache[self.counter - 1]
        return wrapped_method


class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1

    @CacheDecorator
    def next_fib(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result
```
## Объяснение: 
Класс Fibonacci инициализирует два первых числа Фибоначчи: a=0 и b=1. Каждый последующий вызов метода next_fib() возвращает следующее число в последовательности, обновляя значения переменных a и b.
Декоратор CacheDecorator сохраняет предыдущие результаты вызова метода next_fib(), что ускоряет последующие вызовы и предотвращает избыточные вычисления.
## Скриншот:
![image](https://github.com/user-attachments/assets/dbe3b601-8beb-4712-af0d-2dc009bc472f)

# Источники:
[Нейросеть ГигаЧат](https://giga.chat/gigachat/)
