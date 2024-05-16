class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def __str__(self):
        return str(self.queue)


# Example usage:
cq = CircularQueue(5)

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq)  # [1, 2, 3, None, None]

print(cq.dequeue())  # 1
print(cq)  # [2, 3, None, None, None]

cq.enqueue(4)
cq.enqueue(5)
print(cq)  # [2, 3, 4, 5, None]

print(cq.dequeue())  # 2
print(cq)  # [3, 4, 5, None, None]
