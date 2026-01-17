class Solution:
    def squarePattern(self,n):

        for i in range(n):
            for j in range(n):
                print("*",end=" ")
            
            print()

obj = Solution()
n = 5
obj.squarePattern(n)