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


fib_gen = Fibonacci()
for _ in range(10):
    print(fib_gen.next_fib())
print(fib_gen.next_fib(7))
