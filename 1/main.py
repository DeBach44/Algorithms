# Линейный поиск и сложности алгоритмов

'''
Временная сложность -  O(n):
n - количество элементов в списке
Алгоритму может понадобится проверить каждый элемент.

Пространственная сложность - O(1)
При итерации требуется память только для списка
и переменных для работы алгоритма (требуется
постоянное количество памяти).
'''

import time
import random

list_time=[]


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1)#Функция выполняется быстрее 1сек
        return_value = func(*args, **kwargs)
        end = time.time()-1
        list_time.append(round(end - start, 4))
        print('Время выполнения: {:.4f} секунд.'.format(end - start))
        return return_value
    return wrapper

@benchmark
def line_search(n, lst):
    for i in range(len(lst)):
        if lst[i] == n:
            return i
    return -1

list_numbers_10 = [random.randint(1,100) for _ in range(10)]
list_numbers_100 = [random.randint(1,100) for _ in range(100)]
list_numbers_1000 = [random.randint(1,100) for _ in range(1000)]

line_search(10, list_numbers_10)
line_search(10, list_numbers_100)
line_search(10, list_numbers_1000)

print(list_time)

