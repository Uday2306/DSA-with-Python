# Next Greater Element - II
'''
Problem Statement: Given a circular integer array arr, return the next greater element for every element in arr.
The next greater element for an element x is the first element greater than x that we come across while traversing the array in a clockwise manner.
If it doesn't exist, return -1 for that element element.
'''
'''
Example 1:
Input:
 arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
Output:
 [10, -1, 6, 6, 2, 6, 7, 7, 9, 9, 10]
Explanation:
 For the first element in arr i.e, 3, the greater element which comes next to it while traversing and is closest to it is 10. Hence,10 is present on index 0 in the resultant array. Now for the second element i.e, 10, there is no greater number and hence -1 is it’s next greater element (NGE). Similarly, we got the NGEs for all other elements present in arr.

Example 2:
Input:
 arr = [5, 7, 1, 7, 6, 0]
Output:
 [7, -1, 7, -1, 7, 5]
Explanation:
 For the first element in arr i.e, 5, the greater element which comes next to it while traversing and is closest to it is 7. Now for the second element i.e, 7, there is no greater number and hence -1 is it’s next greater element (NGE). Similarly, we got the NGEs for all other elements present in arr.
'''
class Solution:
    def nextGreaterElement(self,nums):
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2*n-1,-1,-1):

            while stack and stack[-1] <= nums[i%n]:
                stack.pop()

            if i < n:
                if stack:
                    ans[i] = stack[-1]

            stack.append(nums[i%n])
        return ans

obj = Solution()
nums = [1,2,3,5]
print(obj.nextGreaterElement(nums))