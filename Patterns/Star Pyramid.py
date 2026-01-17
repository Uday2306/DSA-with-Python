class Solution:
    def starPyramid(self,n):

        for i in range(n):

            for j in range(n - i -1):
                print(" ", end=" ")
            
            for j in range(2 * i - 1):
                print("*", end=" ")
            
            for j in range(n - i - 1):
                print(" ", end=" ")
            print()

obj = Solution()
n = 7
obj.starPyramid(n)