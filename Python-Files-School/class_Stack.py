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

stack = Stack()
stack.push(5)
print(stack.pop())

stack.push(10)
stack.push(20)
print(stack.pop())

print(stack.is_empty())
