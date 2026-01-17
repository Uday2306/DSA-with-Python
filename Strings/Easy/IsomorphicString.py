# 	Isomorphic String
'''Example 1
Input:
 s = "paper", t = "title"
Output:
 true
Explanation:
 The characters in "s" can be mapped one-to-one to characters in "t": 
'p' → 't', 'a' → 'i', 'e' → 'l', 'r' → 'e'
Since the mapping is consistent and unique for each character, the strings are isomorphic.

Example 2
Input:
 s = "foo", t = "bar"
Output:
 false
Explanation:
 'f' → 'b' is fine, 'o' → 'a' for the first 'o', But the second 'o' in "s" would need to map to 'r' in "t", which conflicts with the earlier mapping of 'o' → 'a'
This inconsistency makes it impossible to convert "s" to "t" using a one-to-one character mapping.
'''

class Solution:
    def isIsomorphic(self,s,t):
        mapping_s_to_t = {}
        mapping_t_to_s = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            # Check if character of s is in the dictionary
            if char_s in mapping_s_to_t:
                if mapping_s_to_t[char_s] != char_t: 
                    return False
            else:
                mapping_s_to_t[char_s] = char_t

            if char_t in mapping_t_to_s:
                if mapping_t_to_s[char_t] != char_s:
                    return False
            else:
                mapping_t_to_s[char_t] = char_s
        return True

obj = Solution()
s = "paper"
t = "title"
print(obj.isIsomorphic(s,t))