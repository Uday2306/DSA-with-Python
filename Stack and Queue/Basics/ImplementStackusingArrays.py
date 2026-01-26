# Implement Stack using Arrays
'''
What is a Stack?
A stack is a simple data structure that works on LIFO (Last In, First Out) principle.
That means: the last item that was added (pushed) is the first item to be removed (popped).
Think of a stack like a pile of books: you add (push) books on top and remove (pop) books from the top only.

Approach and Intuition
We’ll use a Python list (self.arr) as the internal storage for the stack.
push(data):
Add the given data at the end of the list (top of the stack).
pop():
Remove and return the last element from the list (top of the stack).
If the list (our stack) is empty, return -1 (as per the problem!).
Why use list’s .append() and .pop()?
append() adds element at the end → top of stack.
pop() removes and returns the last element → top of stack.
'''
class Stack:
    def __init__(self) -> None:
        # Create an empty list/array to represent stack
        self.items = []

    # Method to check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0
    
    # Method to push data elements onto the stack
    def push(self,item):
        # Append is used to add data element at the end.
        self.items.append(item)

    # Method to pop data items from the stack
    def pop(self):
        # Check if stack is empty or not
        if not self.items:
            return "Cannot pop item cuz stack is empty!"
            # pop() is used to remove last element of the stack or any data structure
        x = self.items.pop()
        return x
    # Method to return the top element of stack
    def top(self):
        if not self.items:
            return "Cannot found top, stack is empty"
        return self.items[-1]
    
    # Method to return the size of the stack
    def size(self):
        return len(self.items)
    
stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)
print(f"Stack contains: {stack}")
print(f"Popped item:: {stack.pop()}")
print(f"Stack contains: {stack}")
print(f"Top item of the current stack: {stack.top()}")
print(f"Is stack empty: {stack.is_empty()}")

'''
Time and Space Complexity
push(): O(1) per operation
pop(): O(1) per operation
Space: O(n) where n is the number of elements in the stack
'''