# Sort characters by frequency
'''Example 1:
Input:
 s = "tree"
Output:
 ['e', 'r', 't']
Explanation:

e → 2
r → 1
t → 1
Since 'r' and 't' have the same frequency, they are sorted alphabetically → 'r' comes before 't'.

Example 2:
Input:
 s = "raaaajj"
Output:
 ['a', 'j', 'r']
Explanation:

a → 4
j → 2
r → 1
Characters are sorted by decreasing frequency. In case of ties, alphabetically.
'''
class Solution:
    def sortCharacters(self,s):
        result = ""
        hash_map = {}

        for ch in s:
            hash_map[ch] =hash_map.get(ch,0)+1

        sorted_chars = sorted(hash_map.items(),key=lambda x:(-x[1] ,x[0]))

        for char,freq in sorted_chars:
            result = result+(char*freq)
        return result

obj  = Solution() 
s = "tree"
print(obj.sortCharacters(s))