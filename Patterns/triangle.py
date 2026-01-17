class Soltuion:
    def trianglePattern(self,n):

        for i in range(n):
            for j in range(0,i):
                print("*",end=" ")
            print()

obj = Soltuion()
n = 6
obj.trianglePattern(n)