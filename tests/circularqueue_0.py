class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.head = 0
        self.tail = 0
        self.size = size
        self.count = 0

    def enqueue(self, item):
        if self.count == self.size:
            print("Queue is full")
            return
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            print("Queue is empty")
            return
        item = self.queue[self.head]
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return item


# Example usage
queue = CircularQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)  # Output: "Queue is full"
print(queue.dequeue())  # Output: 3
print(queue.dequeue())  # Output: 4
print(queue.dequeue())  # Output: 5
print(queue.dequeue())  # Output: "Queue is empty"
