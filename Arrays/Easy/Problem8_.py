# Linear Search

class Problem8_():
    def linearSearch(self, nums, num):
        n = len(nums)
        for i in range(0,n-1):
            if nums[i] == num:
                return i
        return -1

obj = Problem8_()
nums = [89,98,76,13,23,4356,7]
print(obj.linearSearch(nums,13))