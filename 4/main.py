# Рекурсия и стек

# 01 факториал числа
def factorial(n):
    #Базовый случай
    if n <= 1:
        return n
    else:
        return n * factorial(n - 1)

# 02 вычисления суммы всех элементов в списке
def sum_elements_list(arr):
    # Базовый случай
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_elements_list(arr[1:])


# 03 бинарный поиск
def binary_search(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, mid + 1, high, target)
        else:
            return binary_search(arr, low, mid - 1, target)
    else:
        return -1

# 04 класс Stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return self.stack == 0