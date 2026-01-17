# Largest odd number in a string
'''
Example 1
Input:
 s = "5347"
Output:
 "5347"
Explanation:
 The odd numbers formed by the given string are → 5, 3, 53, 347, 5347. The largest odd number without leading zeroes is 5347.

Example 2
Input:
 s = "0214638"
Output:
 "21463"
Explanation:
 The odd numbers formed by the string are → 1, 3, 21, 63, 463, 1463, 21463. We can't use numbers starting with 0, so the largest valid odd number is 21463.
'''

class Solution:
    def largestOddNumber(self,num):
        n = len(num)
        for i in range(n-1,-1,-1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""
    
obj = Solution()
num = "021468"
print(obj.largestOddNumber(num))