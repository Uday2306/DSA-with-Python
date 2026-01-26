class Problem7_():
    def moveZeros(self,nums):
        n = len(nums)
        if n == 1:
            return nums
        
        i = 0
        while i < n:
            if nums[i] == 0:
                break
            i += 1
        else:
            return
        j = i+1
        while j< n:
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
            j +=1
        return nums
obj = Problem7_()
nums = [0]
print(obj.moveZeros(nums))