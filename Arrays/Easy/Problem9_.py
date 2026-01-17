#Find Missing Number in an Array
# 

class Problem9_:
    def missing(self,nums):
        n = len(nums)
        original_total = (n*(n+1)//2)
        actual_total = sum(nums)

        return original_total-actual_total

obj = Problem9_()
nums = [0,1,2,4]
print(obj.missing(nums)) 