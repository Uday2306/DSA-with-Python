class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            rev = int(str(x)[::-1])
            if rev == x:
                return True
        return False

obj = Solution()
print(obj.isPalindrome(0))