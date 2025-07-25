# Очереди и сортировка слиянием

from collections import deque
import time
#01
class Queue:

    def __init__(self, size):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("Dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Peek from an empty queue")

#02
queue = Queue(10)
queue.enqueue(0)
queue.enqueue(1)
queue.enqueue(2)
print(f'Начало работы: {time.strftime("%H:%M:%S")}')
while not queue.is_empty():
    print(queue.peek())
    time.sleep(1)
    queue.dequeue()
    print(f'Конец задачи: {time.strftime("%H:%M:%S")}')






