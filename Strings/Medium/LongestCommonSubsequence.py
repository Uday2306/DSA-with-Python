# Longest Common Subsequence
'''
Example 1

Input:  text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The LCS is "ace" with length 3.
Example 2

Input:  text1 = "abc", text2 = "abc"
Output: 3
Explanation: The LCS is "abc" with length 3.
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

obj = Solution()
text1 = "abcde"
text2 = "ace"
print(obj.longestCommonSubstring(text1,text2))