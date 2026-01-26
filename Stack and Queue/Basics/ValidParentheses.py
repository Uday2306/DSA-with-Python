# Valid Parentheses
'''
Problem Statement
Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

An input string is valid if:

Open brackets are closed by the same type of brackets.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket.
Example
Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false
'''
class Solution:
    def isValid(self,s):
        stack = []

        # Pushing the opening brackets onto the stack
        for brackets in s:
            if brackets == '(' or brackets == '{' or brackets == '[':
                stack.append(brackets)

            else:
                if len(stack) == 0:
                    return False
                ch = stack.pop()
                if(
                    (brackets == ')' and ch =='(')
                    or(brackets == ']' and ch =='[')
                    or(brackets == '}' and ch =='{')
                ):
                    continue
                else:
                    return False
        
        return len(stack) == 0
    
st = Solution()
s = "(]"
print(st.isValid(s))

'''
Time: O(n), where n is the length of the string. Each character is processed once.
Space: O(n), stack size can grow to at most n in worst case.
'''