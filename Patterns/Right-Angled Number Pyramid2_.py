class Solution:
    def numberPyramid(self,n):
        for i in range(n+1):
            for j in range(1,i+1):
                print(i,end=" ")
            print()

obj = Solution()
n = 7
obj.numberPyramid(n )