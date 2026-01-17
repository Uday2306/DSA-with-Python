# Longest Palindromic Substring
'''Example 1:
Input:
 s = "babad"
Output:
 "bab"
Explanation:
 It is the longest palindromic substring. "aba" is also a valid answer.

Example 2:
Input:
 s = "cbbd"
Output:
 "bb"
Explanation:
 It is the longest palindromic substring.'''

class Solution:
    def longestPalindromicSubstring(self,s):
        longest = ""

        for i in range(len(s)):
            # For odd length substring
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Check if current palindrome length is greater than its previous one
                if right - left +1 > len(longest):
                    longest = s[left:right+1]
                
                left -= 1
                right += 1

            # For even length string
            left =  i 
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Check if current palindrome length is greater than its previous one
                if right - left +1 > len(longest):
                    longest = s[left:right+1]
                
                left -= 1
                right += 1
        
        return longest

obj = Solution()
s = "cbbd"
print(obj.longestPalindromicSubstring(s))