# Простые алгоритмы сортировки
from random import randint
import time

def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1)#Функция выполняется быстрее 1сек
        return_value = func(*args, **kwargs)
        end = time.time()-1

        print('Время выполнения: {:.4f} секунд.'.format(end - start))
        return return_value
    return wrapper

# Алгоритм сортировки пузырьком
@benchmark
def bubble_sorting(arr):
    n = len(arr)
    for i in range(n):
        swaped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaped = True
        if not swaped:
            break
    return arr

# Алгоритм сортировки выбором
@benchmark
def selection_sorting(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [42, 23, 16, 15, 8, 4]
print('Выборочная сортировка:')
selection_sorting_arr = selection_sorting(arr)
print('Пузырьковая сортировка:')
bubble_sorting_arr = bubble_sorting(arr)
print(selection_sorting_arr)
print(bubble_sorting_arr)
#Время выполнения обеих функций O(n²).
