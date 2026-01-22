# Number of Substrings Containing All Three Characters
'''
Problem Statement: Given a string s , consisting only of characters 'a' , 'b' , 'c'.Find the number of substrings that contain at least one occurrence of all these characters 'a' , 'b' , 'c'.
'''
'''
Input : s = "abcba"
Output :  5
Explanation : The substrings containing at least one occurrence of the characters 'a' , 'b' , 'c' are "abc" , "abcb" , "abcba" , "bcba" , "cba".


Input : s = "ccabcc"
Output : 8
Explanation : The substrings containing at least one occurrence of the characters 'a' , 'b' , 'c' are "ccab" , "ccabc" , "ccabcc" , "cab" , "cabc" , "cabcc" , "abc" , "abcc".
'''
# Brute Force Solution


'''        count = 0
        n = len(s)

        for i in range(0,n):
            freq = {'a':0 , 'b':0 , 'c':0}
            for j in range(i,n):
                freq[s[j]] += 1

                if freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                    count += 1
        
        return count
'''
'''
Time Complexity: O(n²), where n is the length of the input string.We iterate through all possible starting indices from 0 to n−1, and for each starting index, we traverse the substring until we find a valid one (containing at least one 'a', 'b', and 'c'). In the worst case, the inner loop can run up to n times for each outer loop iteration, leading to a total of O(n²) operations.

Space Complexity: O(1), constant space.We use a frequency map of fixed size (only for characters 'a', 'b', and 'c'). Regardless of input size, the space used remains constant. Hence, space complexity is O(1).
'''

class Solution:
    def numberOfSubstring(self,s):
        frq = [0,0,0]

        left = 0
        res = 0
        n = len(s)
        for right in range(0,n):
            frq[ord(s[right]) - ord('a')] += 1

            while frq[0] > 0 and frq[1] > 0 and frq[2] > 0:
                res += n - right

                frq[ord(s[left]) - ord('a')] -= 1
                left += 1
        
        return res
    
obj = Solution()
s = "ccabcc"
print(obj.numberOfSubstring(s))