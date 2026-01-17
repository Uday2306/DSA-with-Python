class Solution:
    def numberPyramid(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end=" ")
            print()

obj = Solution()
n = 6
obj.numberPyramid(n)