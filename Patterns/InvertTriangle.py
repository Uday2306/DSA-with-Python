class Soltuion:
    def trianglePattern(self,n):

        for i in range(n,0,-1):
            for j in range(i,0,-1):
                print("*",end=" ")
            print()

obj = Soltuion()
n = 6
obj.trianglePattern(n)