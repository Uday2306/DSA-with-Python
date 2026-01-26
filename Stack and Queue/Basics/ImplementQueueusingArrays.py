# Implement Queue using Arrays
'''
What is a Queue?
A queue is a simple data structure that works on FIFO (First In, First Out) principle.
That means: the first item that was added (pushed) is the first item to be removed (popped).
Think of a queue like a line of people waiting for a movie ticket: the first person in line (front) gets served first, and new people join at the end (rear).
'''

'''
Intuition
The simplest way is to use a Python list like a dynamic array. We add new elements to the end (using append, like the rear of the queue) and remove from the beginning (using pop(0), like the front). It’s like having a flexible line where people join at the back, but when someone leaves from the front, everyone else has to shift forward – which can be slow if the queue is long!

Detailed Approach
Initialization: Create an empty list self.arr.
Push(x): Append x to the end of the list (rear).
Pop(): If the list is empty, return -1. Otherwise, remove and return the first element (front) using pop(0).
Why Normal?: This is easy to code, but pop(0) shifts all elements, making it slow for large queues.
Edge Cases: Handle empty queue by checking len(self.arr) == 0.
'''
class Queue:
    # This will create an array which represents as an queue
    def __init__(self) -> None:
        self.arr = []

    def is_empty(self):
        return len(self.arr) == 0 

    # Method to add element in the queue
    def enqueue(self,x):
        self.arr.append(x)

    # Method to remove element from the queue
    def dequeue(self):
        if len(self.arr) == 0:
            return "Queue is underflow can't perform dequeue"
        x = self.arr.pop(0)
        return x
    
    def front(self):
        if len(self.arr) == 0:
            return "Queue is underflow can't have front element"
        return self.arr[0]
    
    def rear(self):
        if len(self.arr) == 0:
            return "Queue is underflow can't have rear element"
        
        return self.arr[-1]
    
    def size(self):
        return len(self.arr)

queue = Queue()
queue.enqueue(10)
queue.enqueue(11)
queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(14)
queue.enqueue(15)
queue.enqueue(16)
print("Dequeued element: ",queue.dequeue())
print("Dequeued element: ",queue.dequeue())
print("Dequeued element: ",queue.dequeue())
print("Is Queue empty: ",queue.is_empty())
print("Current Front element of the queue: ",queue.front())
print("Current Rear element of the queue: ",queue.rear())
print("Size of the queue: ",queue.size())

'''
Time and Space Complexity
push(): O(1) – Append is constant time
pop(): O(n) – pop(0) shifts n elements
Space: O(n) – For n elements in the list
'''
