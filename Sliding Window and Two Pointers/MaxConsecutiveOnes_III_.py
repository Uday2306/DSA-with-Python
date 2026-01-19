
'''
Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''

# Brute Force Solution
'''class Solution:
    def maxConsecutiveOnes(self,nums,k):
        n = len(nums)
        maxi = 0
        for i in range(0,n):
            zeros = 0
            for j in range(i,n):
                if nums[j] == 0:
                    zeros += 1
                if zeros <= k:
                    lenght = j - i + k 
                else:
                    break
            maxi = max(maxi,lenght)
        
        return maxi

obj = Solution()
nums = [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
print(obj.maxConsecutiveOnes(nums,3))'''

# Time and Space Complexity
# Time: O(n^2)
# Space: O(1)

# Optimal Solution
class Solution:
    def maxConsecutiveOnes(self,nums,k):
        left = 0
        right = 0
        maxi = 0
        zeros = 0
        n = len(nums)

        while right < n:
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            if zeros <= k:
                length = (right - left + 1)
                maxi = max(maxi,length)

            right += 1
        return maxi
obj = Solution()
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(obj.maxConsecutiveOnes(nums,k))
'''
Time and Space Complexity
Time: O(n)
Space: O(1)
'''