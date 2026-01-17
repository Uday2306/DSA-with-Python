# Implement Atoi
'''
Problem Statement: Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:
1. Whitespace: Ignore any leading whitespace (" ").
2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
4. Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
'''
'''
Example 1:
Input:
 s = "1337c0d3"
Output:
 1337
Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)

Example 2:
Input:
 s = "words and 987"
Output:
 0
Explanation:
 Reading stops at the first non-digit character 'w'.
 '''

class Solution:
    def myAtoi(self, s):
        index = 0
        sign = 1
        result = 0

        # Skipping whitespaces
        while index < len(s) and s[index] == ' ':
            index += 1
        
        # If there are only white spaces so return 0
        if  index == len(s):
            return 0
        
        # Check for sign '-' or '+'
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        if s[index] == '+' and s[index + 1] == '-':
            return 0
        if s[index] == '-' and s[index + 1] == '+':
            return 0

        # Convert characters to Integers
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index]) 

            # If int is over or below 32-bit so to convert it down
            if sign * result > 2**31-1:
                return 2**31-1
            if sign * result < -2**31:
                return -2**31
            
            index += 1
        
        return sign*result

obj = Solution()
s ="  -+21"
print(obj.myAtoi(s))