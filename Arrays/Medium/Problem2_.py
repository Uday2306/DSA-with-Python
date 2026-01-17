class Problem2_:
    def sortColors(self,nums):
        low = 0
        mid = 0
        high = len(nums) -1

        while mid <= high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid +=1
            elif nums[mid] == 2:
                nums[high],nums[mid] = nums[mid],nums[high]
                high -= 1
        return nums

obj = Problem2_()
nums = [2,0,2,1,1,0]
print(obj.sortColors(nums))