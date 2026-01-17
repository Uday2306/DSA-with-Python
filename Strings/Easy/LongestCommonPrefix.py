# Longest Common Prefix
'''
Example 1
Input:
 str = ["flower", "flow", "flight"]
Output:
 "fl"
Explanation:
 All strings in the array begin with the common prefix "fl".
'''
class Solution:
    def longestPrefix(self,str):
        if len(str) == 0:
            return ""
        res = ""
        base = str[0]
        for i in range(0,len(base)):
            for word in str[1:]:
                if i == len(word) or word[i] != base[i]:
                    return res
            res += base[i]
        return res

obj = Solution()
str = ["flower", "flow", "flight"]
print(obj.longestPrefix(str))

