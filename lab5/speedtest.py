import time
from rare import generate_password
from well_done import generate_password_thread


def measure_time(func, length, iterations):
    start_time = time.time()
    for _ in range(iterations):
        func(length)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


if __name__ == "__main__":
    LENGTH = 20
    ITERATIONS = 1000
    original_time = measure_time(generate_password, LENGTH, ITERATIONS)
    print(f"Время выполнения оригинальной функции: {original_time:.4f} секунд")
    threaded_time = measure_time(generate_password_thread, LENGTH, ITERATIONS)
    print(f"Время выполнения многопоточной функции: {threaded_time:.4f} секунд")
    speedup = original_time / threaded_time
    print(f"Ускорение: {speedup:.2f}x")
