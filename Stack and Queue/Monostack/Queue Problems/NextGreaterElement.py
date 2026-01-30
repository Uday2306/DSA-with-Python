# Next Greater Element
'''
Problem Statement: Given an integer array A, return the next greater element for every element in A. The next greater element for an element x is the first element greater than x that we come across while traversing the array in a clockwise manner. If it doesn't exist, return -1 for this element.
'''
'''
Input: arr = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: In the array, the next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4 is -1, since it does not exist.
Input : arr = [6, 8, 0, 1, 3]
Output: [8, -1, 1, 3, -1]
Explanation : In the array, the next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1 , for 1 it is 3 and then for 3 there is no larger element on the right and hence -1.
'''
# Brute Force Approach (Naive Nested Loops)
# class Solution:
    # def nextGreaterElement(self,arr):
        # n = len(arr)
        # ans = [-1] * n
        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         if arr[j] > arr[i]:
        #             ans[i] = arr[j]
        #             break
        # return ans

# arr = [1,2,3,4,3]
# obj = Solution()
# print(obj.nextGreaterElement(arr))
'''##Time and Space Complexity
Time Complexity = O(n**2)
Space complexity = O(1)+O(n)'''
# Optimal Approach (Monotonic Stack)
class Solution:
    def nextGreaterElement(self,arr):
        n = len(arr)
        ans = [-1] * n
        stack = []
        for i in range(n-1,-1,-1):
            while len(stack) != 0 and stack[-1] <= arr[i]:
                stack.pop()
            
            if len(stack) != 0:
                ans[i] = stack[-1]
            
            stack.append(arr[i])
        return ans
obj = Solution()
arr = [1,2,3,4,3]
print(obj.nextGreaterElement(arr))
'''
Time: O(n) – each element is pushed and popped at most once, making it linear in total.
Space: O(n) – used for the stack and result array.
'''