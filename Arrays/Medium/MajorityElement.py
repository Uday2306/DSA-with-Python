'''
Docstring for Medium.MajorityElement
The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.

Example 1:
Input:
 nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]  
Output:
 7  
Explanation:
 The number 7 appears 5 times in the 9-sized array, making it the most frequent element.
############### Brute Force Solution#######################
count = 0
        n = len(nums)
        for i in range(0,n):
            for j in range(0,n):
                if nums[i] == nums[j]:
                    count += 1
            if count > (n/2):
                return nums[i]

'''
class MajorityElement:
    def majorityElement(self,nums):
        count = 0
        element = 0
        for num in nums:
            if count == 0:
                element = num
            if element == num:
                count += 1
            else:
                count -= 1
        return element

obj = MajorityElement()
nums = [3,2,3]  
print(obj.majorityElement(nums))