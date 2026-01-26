
# Find the number that appears once, and the other numbers twice
'''
Docstring for Problem11_
Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

Examples
Example 1:
Input Format: arr[] = {2,2,1}
Result: 1
Explanation: In this array, only the element 1 appear once and so it is the answer.

'''
class Problem11_:
    def singleNumber(self,nums):
        xorr = 0
        for num in nums:
            xorr ^= num
        return xorr

obj = Problem11_()
print(obj.singleNumber([2,2,1])) 