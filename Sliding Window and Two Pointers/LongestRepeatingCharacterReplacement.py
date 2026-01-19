# Longest Repeating Character Replacement
'''
Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
'''
class Solution:
    def longestRepeatingChar(self,s,k):
        left = 0
        right = 0
        maxFrq = 0
        maxLength = 0
        n = len(s)
        frq_map = {}

        for right in range(n):
            frq_map[s[right]] = frq_map.get(s[right],0) + 1
            maxFrq = max(maxFrq,frq_map[s[right]])

            # When window is invalid
            while (right - left + 1) - maxFrq > k:
                frq_map[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, (right - left + 1))
        
        return maxLength
obj = Solution()
s = "ABAB"
k = 2
print(obj.longestRepeatingChar(s,k))
