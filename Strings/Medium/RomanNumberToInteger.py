# Roman Number to Integer and vice versa
'''
Problem Statement: Roman numerals are represented by seven different symbols: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
For example: 2 is written as II, 12 is written as XII, 27 is written as XXVII.
Roman numerals are usually written largest to smallest from left to right. But in six special cases, subtraction is used instead of addition:
I before V or X → 4 and 9,
X before L or C → 40 and 90,
C before D or M → 400 and 900
Given a Roman numeral, convert it to an integer.
'''
'''
Example 1:
Input:
 s = "LVIII"
Output:
 58
Explanation:
 L = 50, V= 5, III = 3.

Example 2:
Input:
 s = "MCMXCIV"
Output:
 1994
Explanation:
 M = 1000, CM = 900, XC = 90 and IV = 4.
'''

class Solution:
    def romanToInteger(self,num):
        # Creating Dictionary for Roman Numbers and their values
        roman = {
            'I':1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D': 500, 'M':1000
        }
        res = 0

        for i in range(0,len(num)):
            if i < len(num)-1 and roman[num[i]] < roman[num[i+1]]:
                res -= roman[num[i]]
            else:
                res += roman[num[i]]
        
        return res 

obj = Solution()
num = "LVIII"
print(obj.romanToInteger(num))