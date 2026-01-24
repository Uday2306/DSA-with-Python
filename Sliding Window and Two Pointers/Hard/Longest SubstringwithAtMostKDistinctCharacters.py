# Longest Substring with At Most K Distinct Characters
'''
Problem Statement: Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters

Examples

Input :s = "aababbcaacc" , k = 2
Output :6
Explanation :The longest substring with at most two distinct characters is "aababb".
The length of the string 6


Input : s = "abcddefg" , k = 3
Output : 4
Explanation : The longest substring with at most three distinct characters is "bcdd".
The length of the string 4.
'''
# Brute Force Solution
'''class Solution:
    def lengthOfLongestSubstringKDistinct(self,s,k):
        max_length = 0

        for i in range(len(s)):
            frq = {}

            for j in range(i,len(s)):
                frq[s[j]] = frq.get(s[j],0) + 1

                if len(frq) > k:
                    break

                max_length = max(max_length,(j - i + 1))

        return max_length'''
'''
Time Complexity:O(n²) ,We are checking every possible substring which takes, and for each substring, we count distinct characters using a map/set which takes up to O(n) in the worst case. But since we break early when distinct characters exceed K, the inner loop doesn't always go to the end.Hence worst-case complexity remains O(n²).

Space Complexity:O(k) ,We use a hash map to store character frequencies for each substring, and in the worst case, it stores at most k distinct characters.
'''

# Optimal Solution
class Solution:
    def lengthOfLongestSubstringKDistinct(self,s,k):

        if k == 0 or not s:
            return 0

        left = 0
        max_length = 0

        frq = {}
        for right in range(len(s)):
            frq[s[right]] = frq.get(s[right],0) + 1

            while len(frq) > k:
                frq[s[left]] -= 1
                if frq[s[left]] == 0:
                    del frq[s[left]]
                left += 1
            
            max_length = max(max_length,(right - left + 1))
        
        return max_length
obj = Solution()
s = "aababbcaacc"
k = 2
print(obj.lengthOfLongestSubstringKDistinct(s,k))
'''
Time Complexity:O(n) ,We iterate through the string once, and each character is added and removed from the map at most once. So the overall time complexity is linear.

Space Complexity: O(k) ,We store at most k characters in the frequency map at any given time, so space used is proportional to k.
'''