def cache_decorator(func):
    cache = {}
    counter = 0

    def cached_func(n=''):
        nonlocal counter
        if counter not in cache:
            cache[counter] = func()
        print(cache)
        if n:
            return cache[n]
        counter += 1
        return cache[counter - 1]

    return cached_func


def fibonacci():
    a, b = 0, 1

    @cache_decorator
    def next_fib():
        nonlocal a, b
        result = a
        a, b = b, a + b
        return result

    return next_fib


fib_gen = fibonacci()
for _ in range(10):
    print(fib_gen())
print(fib_gen(4))