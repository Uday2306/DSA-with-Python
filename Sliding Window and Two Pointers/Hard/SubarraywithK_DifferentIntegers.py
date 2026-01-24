# Subarray with k different integers
'''
Problem Statement: You are given an integer array nums and an integer k. Return the number of good subarrays of nums.

A good subarray is defined as a contiguous subarray of nums that contains exactly k distinct integers. A subarray is a contiguous part of the array.

Examples
Input: nums = [1, 2, 1, 2, 3], k = 2  
Output: 7
Explanation: The 7 subarrays with exactly 2 different integers are:
[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]


Input: nums = [1, 2, 1, 3, 4], k = 3  
Output: 3
Explanation: The 3 subarrays with exactly 3 different integers are:  
[1,2,1,3], [2,1,3], [1,3,4] 
'''

# Brute Force
'''class Solution:
    def subarraysWithKDistinct(self,nums,k):
        count = 0

        for i in range(0,len(nums)):
            frq = {}
            for j in range(i,len(nums)):
                frq[nums[j]] = frq.get(nums[j],0) + 1

                if len(frq) == k:
                    count += 1
                if len(frq) > k :
                    break
        
        return count'''
'''
Time Complexity:O(N²*K) ,We check all possible subarrays by iterating over all start and end indices. For each subarray, we count the number of distinct integers using a HashSet or frequency map, which can take up to O(K) time per check. So overall it becomes O(N²*K) where N is the size of the array and K is the number of unique elements allowed.

Space Complexity:O(K) ,For each subarray, we maintain a HashSet or HashMap to store the distinct elements in it. In the worst case, this set can grow to size K.
'''
# Optimal Solution

class Solution:
    def atMostHelper(self,nums,k):
        count = 0
        left = 0
        n = len(nums)
        frq = {}

        for right in range(0,n):
            if nums[right] not in frq or frq[nums[right]] == 0:
                k -= 1
            frq[nums[right]] = frq.get(nums[right], 0) + 1

            while k < 0:
                frq[nums[left]] -= 1
                if frq[nums[left]] == 0:
                    k += 1
                left += 1
            count += (right - left + 1)
        return count
    def subarraysWithKDistinct(self,nums,k):
        return self.atMostHelper(nums,k) - self.atMostHelper(nums,k-1)

obj = Solution()
nums = [1, 2, 1, 3, 4]
k = 3
print(obj.subarraysWithKDistinct(nums,k))
'''
Time Complexity:O(N) ,where n is the length of the array. Both calls to atMostK() are linear.

Space Complexity:O(K) ,where k is the number of distinct elements in the current window. We use a hash map to store frequency counts, which in the worst case could grow to the number of unique elements in the array.
'''