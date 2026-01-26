# Given an array arr, rotate the array by one position in Left direction.
# class Problem5_:
#     def leftRotateArray(self,arr):
#         temp = arr[0]
#         n = len(arr)
#         for i in range(1,n):
#             arr[i-1] = arr[i]
        
#         arr[n-1] = temp
#         return arr
    
# obj = Problem5_()
# arr = [1,2,3,4,5,6,7]
# print(obj.leftRotateArray(arr))

'''
Given an array arr, rotate the array by one position in Right direction.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]
Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.
'''

class Problem5_:
    def leftRotateArray(self,arr):
        n = len(arr)
        temp = arr[n-1]
        for i in range(n-1,0,-1):
            arr[i] = arr[i-1]
        
        arr[0] = temp
        return arr
    
obj = Problem5_()
arr = [1, 2, 3, 4, 5]
print(obj.leftRotateArray(arr))