# Count Subarray sum Equals K

'''class Solution:
    def countSubarraySumEqualsK(self,num,k):
        frq = {0:1}
        
        preSum = 0
        count = 0

        for i in range(len(num)):
            preSum += num[i]
            remove = preSum - k
            count += frq.get(remove,0)
            frq[preSum] = frq.get(preSum, 0) + 1
        
        return count
    '''
# Brute force Solution
class Solution:
    def countSubarraySumEqualsK(self,nums,k):
        count = 0
        i = 0
        j = 0
        while i < len(nums):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum > k:
                    break
                elif sum == k:
                    count += 1
            i +=1
       

        return count 
obj = Solution()
nums = [1,1,1]
k = 2

print(obj.countSubarraySumEqualsK(nums,k))