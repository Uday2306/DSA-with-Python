# Longest Substring Without Repeating Characters 
'''
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# Brute Force Solution:

'''
class Solution:
    def longestString(self,s):
        maxi = 0
        n = len(s)
        for i in range(0,n):
            my_set =set()
            for j in range(i,n):
                if s[j] in my_set:
                    break
                maxi = max(maxi,(j - i + 1))

                my_set.add(s[j])
        return maxi

obj = Solution()
s = "abcabcbb"
print(obj.longestString(s))
'''

'''
Time and Space Complexity
Time: O(n^2)
Space: O(min(n, Σ)) for the set (Σ = character set size)
'''

# Optimal Solution
class Solution:
    def longestString(self,s):
        maxi = 0
        left = right = 0
        n = len(s)
        my_dict = {}

        while right < n:
            if s[right] in my_dict:
                left = max(left,my_dict[s[right]]+ 1)

            maxi = max(maxi,(right - left + 1))
            my_dict[s[right]] = right
            right += 1
        return maxi  
obj = Solution()
s = "abcabcbb"
print(obj.longestString(s))

'''
Time: O(n) – each index is visited at most twice (once by right, possibly once by left)
Space: O(min(n, Σ)) for the hash map
'''