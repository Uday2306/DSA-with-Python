# Minimum Window Substring
'''Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:'''
from collections import Counter

class Solution:
    def minimumWindowSubstring(self,s,k):
        if not k:
            return ""
        
        need = Counter(k)
        window = Counter()

        have = 0
        need_count = len(need)
        left = 0
        res_len = float("inf")
        res = [-1,-1]

        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0) + 1
            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1
            
            while have == need_count:
                if(right - left + 1) < res_len:
                    res = [left,right] 
                    res_len = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        l,r = res
        
        return s[l:r + 1] if res_len != float("inf") else ""

obj = Solution()
s = "ADOBECODEBANC"
k = "ABC"
print(obj.minimumWindowSubstring(s,k))

# Time complexity O(n)
# Space Complexity O(1)
