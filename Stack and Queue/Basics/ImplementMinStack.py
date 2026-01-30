# Implement Min Stack
'''
Problem Statement
Design a stack that supports four operations, each in constant time (O(1)):

push(val): Pushes the integer val onto the stack.
pop(): Removes the element on the top of the stack.
top(): Retrieves the top element of the stack without removing it.
getMin(): Retrieves the minimum element in the entire stack at any point.
Your stack must efficiently keep track of the minimum element without the need to scan through the entire stack every time you call getMin().
'''

class Solution:
    def __init__(self) -> None:
        self.stack = []
    def push(self,x):
        if len(self.stack) == 0:
            self.stack.append([x,x])
        else:
            minn = self.stack[-1][1]
            new_min = min(minn,x)
            self.stack.append([x,new_min])
    def pop(self):
        if not self.stack:
            return 0
        return self.stack.pop()

    def top(self):
        if not self.stack:
            return 0
        return self.stack[-1][0]
    
    def getMin(self):
        if not self.stack:
            return 0
        return self.stack[-1][1]

minStack = Solution()
minStack.push(3)
minStack.push(5)
minStack.push(2)
minStack.push(1)
minStack.push(4)
print(minStack.getMin())
print(minStack.top())