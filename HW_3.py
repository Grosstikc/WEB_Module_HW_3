import logging
from multiprocessing import Pool, cpu_count
import time

# Налаштування модуля logging для відображення часу та рівня логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Декоратор для вимірювання часу виконання функції
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"{func.__name__} виконано за {end_time - start_time} секунд")
        return result
    return wrapper

# Базова функція для пошуку дільників одного числа
def find_factors(number):
    factors = [i for i in range(1, number + 1) if number % i == 0]
    return factors

# Синхронна версія для обчислення дільників списку чисел
@timeit
def factorize_sync(numbers):
    return [find_factors(number) for number in numbers]

# Паралельна версія для обчислення дільників списку чисел
@timeit
def factorize_parallel(numbers):
    with Pool(cpu_count()) as pool:
        result = pool.map(find_factors, numbers)
    return result

# Тестування функцій
numbers = [128, 255, 99999, 10651060]
result_sync = factorize_sync(numbers)
result_parallel = factorize_parallel(numbers)

# Перевірка, що обидві функції повертають однакові результати
results_match = result_sync == result_parallel
results_match, result_sync, result_parallel
