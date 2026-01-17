# Sum of Beauty of all substring
'''
Problem Statement: The beauty of a string is defined as the difference between the frequency of the most frequent character and the least frequent character (excluding characters that do not appear) in that string.

Given a string s, return the sum of beauty values of all possible substrings of s.
'''
'''
Example 1:
Input:
 s = "xyx"
Output:
 1
Explanation:
 The substrings with non-zero beauty are:
"xyx" → frequencies: x:2, y:1 → beauty = 2 - 1 = 1
"xy" → x:1, y:1 → beauty = 0
"yx" → y:1, x:1 → beauty = 0
"x" or "y" → beauty = 0
Total sum = 1 (from "xyx") = 1

Example 2:
Input:
 s = "aabcbaa"
Output:
 17
Explanation:
 Various substrings such as "aabc", "bcba", etc., have non-zero beauty values. Summing all gives 17.
'''

class Solution:
    def beautyString(self,s):
        n = len(s)
        total = 0


        for i in range(n):
            freq = {}
            for j in range(i,n):
                freq[s[j]] = freq.get(s[j],0) + 1

                values = freq.values()
                maxi = max(values)
                mini = min(values)

                total += (maxi - mini)
        
        return total

obj = Solution()
s = 'xyx'
print(obj.beautyString(s))