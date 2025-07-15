# Бинарный поиск - реализация по индексам

from random import randint
import time
'''
Временная сложность - O(log n),
алгоритм проверяет только малую часть массива.

Пространственная сложность - O(1),
используется фиксированное количество памяти.
'''
def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1)#Функция выполняется быстрее 1сек
        return_value = func(*args, **kwargs)
        end = time.time()-1

        print('Время выполнения: {:.4f} секунд.'.format(end - start))
        return return_value
    return wrapper
@benchmark
def binary_search(arr, t):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
    return -1

list_numbers_100 = [randint(1,50) for _ in range(100)]
list_numbers_100.sort()

list_res = []

list_res.append(binary_search(list_numbers_100, 10))
list_res.append(binary_search(list_numbers_100, 20))
list_res.append(binary_search(list_numbers_100, 100))

print(list_res)