def memoize(n_max=None):
    def decorator(func):
        cache = {}

        def wrapper(*args):
            if args in cache:
                return cache[args]

            result = func(*args)
            if n_max is None or len(cache) < n_max:
                cache[args] = result

            return result

        return wrapper

    return decorator


@memoize(n_max=5)
def fibonacci_limited(n):
    if n <= 1:
        return n
    return fibonacci_limited(n - 1) + fibonacci_limited(n - 2)


print(fibonacci_limited(10))
