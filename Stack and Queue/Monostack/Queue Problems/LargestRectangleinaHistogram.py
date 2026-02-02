# Largest rectangle in a histogram
'''
Problem Statement: Given an array of integers heights representing the histogram's bar height where the width of each bar is 1 return the area of the largest rectangle in histogram. .

Examples
Example:

Input: N =6, heights[] = {2,1,5,6,2,3}
Output: 10
'''
# Brute force solution:
'''
class Solution:
    def largest_area(self,arr,n):
        max_area = 0
            
        for i in range(n):
            min_height = float("inf")

            for j in range(i,n):
                min_height = min(min_height,arr[j])

                width = j - i + 1
                area = min_height * width

                max_area = max(max_area,area)
        
        return max_area

obj = Solution()
N =6
heights = [2,1,5,6,2,3]

print(obj.largest_area(heights,N))

Time Complexity: O(N*N), since nested for loops are used
Space Complexity: O(1). No extra space used
'''

# Optimal Solution - 1
'''
# Core IDEA#
For each bar, assume it is the shortest bar (height) of a rectangle.
Now find:
- how far it can go to the left
- how far it can go to the right
- before a smaller bar appears.
'''
'''
# Approach:
Step 1: Find left boundary for every bar
    (Nearest smaller bar on the left)
    Use a stack to store bar indexes
    Traverse the array from left to right
    While the stack top bar is greater than or equal to the current bar:
        remove it from the stack
    If stack becomes empty:
        left boundary = 0
    Else:
        left boundary = stack top index + 1
        Store this in leftSmall[i]
        Push the current index into the stack
Step 2: Find right boundary for every bar
    (Nearest smaller bar on the right)
    Clear the stack
    Traverse the array from right to left
    While the stack top bar is greater than or equal to the current bar:
        remove it from the stack
    If stack becomes empty:
        right boundary = n - 1
    Else:
        right boundary = stack top index - 1
        Store this in rightSmall[i]
        Push the current index into the stack
Step 3: Calculate area for each bar
For each index i:
    width = rightSmall[i] - leftSmall[i] + 1
    area = heights[i] × width

Keep updating the maximum area.

#### Time and Space Complexity
Time Complexity: O(n)
(Each bar is pushed and popped once)
Space Complexity: O(n)
(Stack and boundary arrays)
'''
'''
class Solution:
    def largestRectangleArea(self,heights):
        n = len(heights)
        stack = []
        leftSmall = [0] * n
        rightSmall = [0] * n

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            leftSmall[i] = 0 if not stack else stack[-1] + 1
            stack.append(i)
        
        stack = []

        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            rightSmall[i] = n -1 if not stack else stack[-1] -1
            stack.append(i)

        maxArea = 0
        for i in range(n):
            width = rightSmall[i] - leftSmall[i] + 1
            maxArea = max(maxArea,heights[i]*width)
        
        return maxArea

obj = Solution()
nums = [2,1,5,6,2,3]
print(obj.largestRectangleArea(nums))

'''


# Optimal Solution - 2


# Core IDEA
'''
Use a stack to keep bars in increasing height order.
When a smaller bar comes, it means the rectangle for taller bars must stop.
'''

'''
****Approach****
Step 1: Use a stack
    The stack stores indexes of bars
    Bars in the stack are always in increasing height order

Step 2: Traverse bars one by one
    Loop from i = 0 to n - 1.
For each bar:
    Let currentHeight = heights[i]

Step 3: When to calculate area
While:
    stack is not empty AND
    current bar is smaller or equal to the bar at stack top
Then:
    Pop the top index from the stack
    That popped bar’s height is the height of rectangle

Step 4: Calculate width
After popping:
    If stack becomes empty:
        width = i
        (Rectangle extends from index 0 to i-1)
    Else:
        width = i - stack[-1] - 1
        (Rectangle is between two smaller bars)

Step 5: Update maximum area
    area = height × width
    maxArea = max(maxArea, area)

Step 6: Push current index
    After handling pops, push the current index into the stack.
'''
class Solution:
    def largestRectangleArea(self,heights):
        stack = []
        maxArea = 0
        n = len(heights)

        for i in range(n+1):
            currentHeight = heights[i] if i < n else 0

            while stack and (i == n or heights[stack[-1]] >= currentHeight):
                height = heights[stack.pop()]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                
                maxArea = max(maxArea,height*width)

            stack.append(i)
        return maxArea
obj = Solution()
nums = [2,4]

print(obj.largestRectangleArea(nums))
