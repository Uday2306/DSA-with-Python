# Implement Queue using Stack
class StackQueue:
    def __init__(self) -> None:
        self.in_stack = []
        self.out_stack = []

    def push(self,x):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        self.in_stack.append(x)
        while self.out_stack:
            self.in_stack.append(self.out_stack.pop())
    
    def pop(self):
        if not self.in_stack:
            print("Stack is empty")
            return -1
        return self.in_stack.pop()
    
    def top(self):
        if not self.in_stack:
            print("Stack  is empty")
            return -1
        return self.in_stack[-1]

    def is_empty(self):
        return not self.in_stack

stack = StackQueue()
stack.push(10)
stack.push(11)
stack.push(12)
stack.push(13)
stack.push(14)
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.push(45)
print(f"Top of the  stack: {stack.top()}")
print(f"Is stack empty: {stack.is_empty()}")