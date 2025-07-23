# Быстрая сортировка

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

# 01
def fibonachy(n):
    '''
    Функция имеет временную сложность О(2ⁿ)
    Если базовый случай не выполняется
    происходит два рекурсивных вызова.
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachy(n - 1) + fibonachy(n - 2)


# 02
def get_max_element(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    element = arr[0]
    next_element = get_max_element(arr[1:])
    if element >= next_element:
        return element
    else:
        return next_element

# 03

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


arr_10 = [randint(1,50) for _ in range(10)]
arr_100 = [randint(1,50) for _ in range(100)]
arr_1000 = [randint(1,50) for _ in range(1000)]



start = time.time()
time.sleep(1)
quick_sort(arr_10)
end = time.time()-1
print('Время выполнения: {:.4f} секунд.'.format(end - start))

start = time.time()
time.sleep(1)
quick_sort(arr_100)
end = time.time()-1
print('Время выполнения: {:.4f} секунд.'.format(end - start))

start = time.time()
time.sleep(1)
quick_sort(arr_1000)
end = time.time()-1
print('Время выполнения: {:.4f} секунд.'.format(end - start))
