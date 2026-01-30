# Sum of Subarray Ranges
'''
Problem Statement: Given an integer array nums, determine the range of a subarray, defined as the difference between the largest and smallest elements within the subarray. Calculate and return the sum of all subarray ranges of nums.

A subarray is defined as a contiguous, non-empty sequence of elements within the array.
Example 1:
Input:
 nums = [1, 2, 3]
Output:
 4
Explanation:
 The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

Example 2:
Input:
 nums = [1, 3, 3]
Output:
 4
Explanation:
 The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
'''

# Brute Force Solution
'''class Solution:
    def sumOfSubarrayRanges(self,nums):
        n = len(nums)
        left = 0
        totalSum = 0

        for i in range(0,n):
            smallest = nums[i]
            largest = nums[i]

            for j in range(i,n):
                smallest = min(smallest,nums[j])
                largest = max(largest,nums[j])

                totalSum += (largest - smallest)
        
        return totalSum

obj = Solution()
nums = [1, 3, 3]
print(obj.sumOfSubarrayRanges(nums))
        '''

class Solution:
    def sumSubarrayMinimums(self,nums):
        n = len(nums)
        stack = []
        left = [0]*n
        right = [0]*n

        for i in range(n):
            count = 1
            while stack and stack[-1][0] > nums[i]:
                count += stack[-1][1]
                stack.pop()
            stack.append((nums[i],count))
            left[i] = count
        stack = []

        for i in range(n-1,-1,-1):
            count = 1
            while stack and stack[-1][0] >= nums[i]:
                count += stack[-1][1]
                stack.pop()
            stack.append((nums[i],count))
            right[i] = count
        
        total = 0

        for i in range(n):
            total += nums[i] * left[i] * right[i]
        
        return total

    def sumSubarrayMaxs(self,nums):
        n = len(nums)
        stack = []
        left = [0]*n
        right = [0]*n

        for i in range(n):
            count = 1
            while stack and stack[-1][0] < nums[i]:
                count += stack[-1][1]
                stack.pop()
            stack.append((nums[i],count))
            left[i] = count
        stack = []

        for i in range(n-1,-1,-1):
            count = 1
            while stack and stack[-1][0] <= nums[i]:
                count += stack[-1][1]
                stack.pop()
            stack.append((nums[i],count))
            right[i] = count
        
        total = 0

        for i in range(n):
            total += nums[i] * left[i] * right[i]
        
        return total
    
    def subArrayRanges(self,nums):
        return self.sumSubarrayMaxs(nums) - self.sumSubarrayMinimums(nums)

obj = Solution()
nums = [1, 3, 3]

print(obj.subArrayRanges(nums))