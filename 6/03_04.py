# Очереди и сортировка слиянием

import numpy as np
import time

#03
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
#04
arr10 = np.random.randint(1,100, size=10)
arr100 = np.random.randint(1,100, size=100)
arr1000 = np.random.randint(1, 100, size=1000)


start = time.time()
time.sleep(1)
merge_sort(arr10)
end = time.time()-1
print('Время выполнения: {:.4f} секунд.'.format(end - start))

start = time.time()
time.sleep(1)
merge_sort(arr100)
end = time.time()-1
print('Время выполнения: {:.4f} секунд.'.format(end - start))

start = time.time()
time.sleep(1)
merge_sort(arr1000)
end = time.time()-1
print('Время выполнения: {:.4f} секунд.'.format(end - start))

