"""
Stack Data Structure
"""
class Stack():
    def __init__(self) -> None:
        self.items = []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self) -> any:
        return self.items.pop()

    def get_stack(self) -> list:
        return self.items
    
    def is_empty(self) -> bool:
        return self.items == []

    def peek(self) -> any:
        if not self.is_empty():
            return self.items[-1]

"""   
TESTING

myStack = Stack()
print(myStack.is_empty()) # True
myStack.push('Item A')
print(myStack.is_empty()) # False
myStack.push('Item B')
print(myStack.get_stack()) # A, B
myStack.pop()
print(myStack.get_stack()) # A
myStack.push('Item C')
print(myStack.peek()) # C
"""