class CacheDecorator:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.counter = 0

    def __get__(self, instance, owner):
        def wrapped_method(n=''):
            if self.counter not in self.cache:
                self.cache[self.counter] = self.func(instance)
            self.counter += 1
            if n:
                return self.cache[n]
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


fib_gen = Fibonacci()
for _ in range(10):
    print(fib_gen.next_fib())
print(fib_gen.next_fib(7))
