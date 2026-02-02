# Remove k Digits
'''
Problem Statement: Given a string nums representing a non-negative integer, and an integer k, find the smallest possible integer after removing k digits from num.

Examples
Example 1:
Input:
 nums = "541892", k = 2
Output:
 "1892"
Explanation:
 Removing the two digits 5 and 4 yields the smallest number, 1892.

Example 2:
Input:
 nums = "1002991", k = 3
Output:
 "21"
Explanation:
 Remove the three digits 1(leading one), 9, and 9 to form the new number 21(Note that the output must not contain leading zeroes) which is the smallest.
'''
class Solution:
    def removeKdigits(self,nums,k):
        stack = []

        # Traversing the array
        for digits in nums:
            # If smaller digit is found pop the top digit
            while stack and k > 0 and stack[-1] > digits:
                stack.pop()
                k -= 1
            # No smaller found so push onto the stack
            stack.append(digits)
        
        # If more digits can be popped
        while stack and k>0:
            stack.pop()
            k -= 1
        
        # If the length of k is same as nums so
        if not stack:
            return "0"
        
        # To store result
        res = ""

        # adding digits into a string var
        while stack:
            res += stack.pop()
        
        # Trimming zeros
        res = res.rstrip("0")

        # Reversing the result to get output
        res = res[::-1]
        
        # If there is no digit in res so return 0
        if not res:
            return "0"

        return res

obj = Solution()
nums = "10200"
k = 1
print(obj.removeKdigits(nums,k))

'''
Time Complexity: O(N), since traversing the given string takes O(N) time, each element is pushed onto and popped from the stack at most once in worst-case taking o(N) time, removing the remaining digits (if k > 0) takes O(k) time which can go upto O(N) in worst-case and forming the result, trimming the zeros and reversing the digits takes O(N) time.

Space Complexity: O(N), since we are using a stack to store the digits of the resulting number, in the worst case, the stack can contain all the digits of the input string.
'''