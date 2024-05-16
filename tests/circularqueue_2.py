class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Enqueue operation cannot be performed.")
            return
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        print(f"Enqueued {item} to the queue.")
        self.print_queue()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Dequeue operation cannot be performed.")
            return None
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
        print(f"Dequeued {item} from the queue.")
        self.print_queue()
        return item

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()


# Example usage:
queue = CircularQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
queue.enqueue(4)
queue.enqueue(5)
# This should print "Queue is full. Enqueue operation cannot be performed."
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()  # This should print "Queue is empty. Dequeue operation cannot be performed."
