'''
Docstring for Medium.MaxSum0fSubarray

###Kadane's Algorithm : Maximum Subarray Sum in an Array
Problem Statement: Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:
Input:
 nums = [2, 3, 5, -2, 7, -4]  
Output:
 15  
Explanation:
 The subarray from index 0 to index 4 has the largest sum = 15, which is the maximum sum of any contiguous subarray.
'''
# Brute Force Solution
'''
class MaxSumOfSubarray:
    def maxSum(self, nums):
        n = len(nums)
        total = 0
        maxi = float("-inf")
        for i in range(0,n):
            total = 0
            for j in range(i,n):
                total = total + nums[j]
                maxi = max(maxi,total)
                    
        return maxi

obj = MaxSumOfSubarray()
nums = [2, 3, 5, -2, 7, -4]
print(obj.maxSum(nums))
'''
# Optimal Solution
class MaxSumOfSubarray:
    def maxSum(self, nums):
        n = len(nums)
        total = 0
        maxi = float("-inf")
        for i in range(0,n):
            total += nums[i]
            maxi = max(maxi,total)
            if total < 0:
                total = 0                    
        return maxi

obj = MaxSumOfSubarray()
nums = [2, 3, 5, -2, 7, -4]
print(obj.maxSum(nums))