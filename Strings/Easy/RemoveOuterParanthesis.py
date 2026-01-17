class Solution:
    def removeOuterParentheses(self, s) :
        result = ""
        count = 0

        for char in s:
            if char == '(':
                count += 1
                if count > 1:
                    result += char
            if char == ')':
                count -= 1
                if count > 0:
                    result += char

        return result

obj = Solution()
s = "(()())(())"
print(obj.removeOuterParentheses(s))



