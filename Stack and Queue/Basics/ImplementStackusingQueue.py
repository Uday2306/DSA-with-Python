#  Implement Stack using Queue
'''
Use just one queue and “rotate” it during push to bring the new element to the front. After adding the new element to the end, we remove and re-add the front elements (n-1 times) to move them behind the new one. This makes the new element the front (top of stack). It’s like spinning a line of people so the newest joins at the end but then we cycle the others to put the new one first!
'''
from collections import deque

class MyStack:
    def __init__(self) -> None:
        self.queue = deque()
    
    def is_empty(self):
        if len(self.queue) == 0:
            return "Queue is empty"
    
    def push(self,x):
        self.queue.append(x) #Append element at the end of the stack
        for _ in range(len(self.queue) - 1): # traverse through the queue by (n-1)
            self.queue.append(self.queue.popleft()) #pop leftmost element and add it to the end 
    
    def pop(self):
        return self.queue.popleft() 
    
    def top(self):
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
stack = MyStack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
print(f"Removed element: {stack.pop()}")    
print(f"Removed element: {stack.pop()}")    
print(f"Removed element: {stack.pop()}")
print(f"Top element of the current stack: {stack.top()}")    
print(f"Size of the stack: {stack.size()}")

'''
# Time complexity:
push() - O(n)
pop() - O(1)
top() - O(1)
size() - O(n)
'''