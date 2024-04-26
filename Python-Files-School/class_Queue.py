class Stack:
    
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


class Queue:

    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def sort(self):
        stack = self.to_stack()
        stack.items.sort()

        self.items = []

        while not stack.is_empty():
            self.enqueue(stack.pop())

    def to_stack(self):
        stack = Stack()
        while not self.is_empty():
            stack.push(self.dequeue())
        return stack

queue = Queue()
queue.enqueue(5)
queue.enqueue(2)
queue.enqueue(8)
queue.enqueue(1)

print("Unsorted Queue:", queue.items)

queue.sort()

print("Sorted Queue:", queue.items)
