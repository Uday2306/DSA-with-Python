# Longest Consecutive Sequence in an Array
'''
Example 1:
Input:
 nums = [100, 4, 200, 1, 3, 2]  
Output:
 4  
Explanation:
 The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which has a length of 4. This sequence can be formed regardless of the initial order of the elements in the array.
'''
# Brute-Force Solution

'''class LongestConsecutiveSequence:
    def longestSuccessiveElements(self,nums):
        n = len(nums)
        max_count = 0

        for i in range(0,n):
            num = nums[i]
            count = 1
            while num+1 in nums:
                count += 1
                num = num+1
            max_count = max(max_count,count)
        return max_count
    
obj = LongestConsecutiveSequence()
nums = [100, 4, 200, 1, 3, 2,] 
print(obj.longestSuccessiveElements(nums))
'''

# Optimal Solution
class LongestConsecutiveSequence:
    def longestSuccessiveElements(self,nums):
        my_set =set()
        n = len(nums)
        for i in range(0,n):
            my_set.add(nums[i])
        
        longest = 0
        for num in my_set:
            if num-1 not in my_set:
                x = num
                count = 1
                while x+1 in my_set:
                    count += 1
                    x += 1
        
                longest = max(longest,count)
        return longest    

obj = LongestConsecutiveSequence()
nums = [100, 4, 200, 1, 3, 2,] 
print(obj.longestSuccessiveElements(nums))