# Maximum Nesting Depth of Parenthesis
'''
Example 1:
Input:
 s = "(1+(2*3)+((8)/4))+1"
Output:
 3
Explanation:
 Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input:
 s = "(1)+((2))+(((3)))"
Output:
 3
Explanation:
 Digit 3 is inside of 3 nested parentheses in the string.
'''

class Solution:
    def maximumNesting(self,s):
        count = 0
        result = 0

        for ch in s:
            if ch == '(':
                count += 1
            elif ch == ')':
                count -=1
            result = max(result,count)
        return result

obj = Solution()
s  = "(1)+((2))+(((3)))"
print(obj.maximumNesting(s))