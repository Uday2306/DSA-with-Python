# Longest Palindromic Sunsequence
'''
Example 1:
Input:
 s = "babad"
Output:
 "3"
Explanation:
 It is the longest palindromic substring. "aba" is also a valid answer.

Example 2:
Input:
 s = "cbbd"
Output:
 "2"
Explanation:
 It is the longest palindromic substring.
 '''
class Solution:
    def longestCommonSubstring(self,text1,text2):
        # Getting lenths of both strings
        n , m = len(text1), len(text2)

        # Creating a dp table which store the LCS length
        dp = [[0]*(m+1) for _ in range(n+1)]

        # Filling dp table row by row
        for i in range(1,n+1):
            for j in range(1,m+1):

                # If characters are same 
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1] # add diagonal value + 1
                
                # If characters are different
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]) # It will take the maximum value of the top or left
        
        return dp[n][m]

    def longestPalindromicSubstring(self,s):
        s1 = s
        s2 = s[::-1]
        return self.longestCommonSubstring(s1,s2)
obj = Solution()
s = "babad"
print(obj.longestPalindromicSubstring(s))