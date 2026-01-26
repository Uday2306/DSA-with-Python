# class Solution:
#     def largestElement(self, nums):
#         max = nums[0]
#         for i in nums:
#             if i > max:
#                 max = i
#         return max
    
# obj = Solution()
# print(obj.largestElement([3, 3, 6, 1]))
class Solution:
    def isSorted(self, arr) -> bool:
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True

obj = Solution()
arr = [10, 20, 30, 40, 50]
print(str(obj.isSorted(arr)).lower())
