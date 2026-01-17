# Check if two Strings are anagrams of each other
'''Example 1:
Input: CAT, ACT
Output: true
Explanation: Since the count of every letter of both strings are equal.

Example 2:
Input: RULES, LESRT 
Output: false
Explanation: Since the count of U and T  is not equal in both strings.
'''

class Solution:
    def isAnagram(self,str1,str2):
        # Check if both strings have same length
        if len(str1) != len(str2):
            return False
        
        frq = [0]*26 # Initialize an array of 26 length for(A to Z letters)
        # Iterate through each character in str1
        for char in str1:
            frq[ord(char) - ord('a')] += 1 #Iincrease count of that character in the frq[]

        # Now iterate through str2 to check that the same characters are present in str2
        for char in str2:
            frq[ord(char) - ord('a')] -= 1 # Now decrease the count by 1 for each character in the frq[]

        # Now iterate through the final frq[] and check if all the values are 0 or not if all are 0's then return True otherwise False
        for count in frq:
            if count != 0:
                return False
            
        return True
obj = Solution()
print(obj.isAnagram("cat", "act"))