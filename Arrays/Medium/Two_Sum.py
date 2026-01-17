class Two_Sum:
    def twoSum(self,nums,target):
        n = len(nums)
        hash_map = {}

        for i in range(n):
            remaining  = target - nums[i]
            if remaining in hash_map:
                res =  [hash_map[remaining],i]
                return res
            hash_map[nums[i]] = i

obj = Two_Sum()
nums = [2,7,11,15]
print(obj.twoSum(nums,9))