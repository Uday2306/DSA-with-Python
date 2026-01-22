# Count number of nice subarrays
'''
Input :nums = [1, 1, 2, 1, 1] , k = 3
Output :2
Explanation :The subarrays with three odd numbers are [1, 1, 2, 1] [1, 2, 1, 1]

Input : nums = [4, 8, 2] , k = 1
Output :0
Explanation :The array does not contain any odd number.
'''

# Brute Force Solution
'''class Solution:
    def countNiceSubarray(self,nums,k):
        right = 0
        left = 0
        count = 0

        for right in range(len(nums)):
            oddCount = 0
            for left in range(right,len(nums)):    
                
                if nums[left] % 2 != 0:
                    oddCount += 1
                if oddCount > k:
                    break
                if oddCount == k:
                    count += 1
        return count
    '''

'''
Sliding window works smoothly when the condition is:

“≤ k”

“≥ k”

But “exactly k” is unstable:

When you add one element, the count may become k+1

When you remove one, it may become k−1

So instead of fighting sliding window, we rephrase the problem.
'''

class Solution:
    def countAtMost(self, nums, k):
        left = 0
        right = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                k -= 1
            
            while k < 0:
                if nums[left] % 2 != 0:
                    k += 1
                left += 1
            
            res += (right - left + 1)
        return res

    def numberOfSubarrays(self,nums,k):
        return self.countAtMost(nums,k) - self.countAtMost(nums,k-1) 
obj = Solution()
nums =[1,1,2,1,1]
k = 3
print(obj.numberOfSubarrays(nums,k))