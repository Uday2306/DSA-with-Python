#  Reverse Words in a String
'''
Input: s = "welcome to the jungle"
Output: "jungle the to welcome"
Explanation: The words in the input string are "welcome", "to", "the", and "jungle". Reversing the order of these words gives "jungle", "the", "to", and "welcome". The output string should have exactly one space between each word.
'''

class Solution:
    def reverseWords(self,s):
        words = s.split()
        words.reverse()
        return " ".join(words)
        
        
obj = Solution()
s = "welcome to the jungle"
print(obj.reverseWords(s))


# Alternate Solution
"""""class Solution:
    def reverseWords(self,s):
        words = s.split()
        res = []

        for i in range(len(words)-1,-1,-1):
            res.append(words[i])
            # if i != 0:
            #     res.append(" ")
        return " ".join(res)
obj = Solution()
s = "welcome to the jungle"
print(obj.reverseWords(s))"""""