# 	Maximum Consecutive Ones in an Array

'''
Docstring for Problem10_
Example 1:
Input: prices = {1, 1, 0, 1, 1, 1}
Output: 3
Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.
'''

class Problem10_:
    def maxConsecutiveOnes(self,nums):
        count = 0
        max_count = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                max_count = max(max_count,count)
                count = 0
        max_count = max(max_count,count)
        return max_count

obj = Problem10_()
nums = [1, 1, 0, 1, 1, 1]
print(obj.maxConsecutiveOnes(nums))   