# Trapping Rainwater
'''''
Problem Statement: Given an array of non-negative integers representation elevation of ground. Your task is to find the water that can be trapped after rain .

Examples

Input : height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output : 6
Explanation : Water is trapped in the dips between bars. The total trapped water units add up to 6 (1+1+2+1+1).

Input : height = [4,2,0,3,2,5]
Output : 9
Explanation : The elevation map traps 9 units of water in total, as water fills the spaces between higher bars on both sides.
'''
# Brute Force Solution
''''
class Solution:
    def trappingRainwater(self,height):
        n = len(height)
        total_water = 0

        for i in range(n):
            max_left = 0
            max_right = 0

            for j in range(i + 1):
                if height[j] > max_left:
                    max_left = height[j]
            
            for j in range(i,n):
                if height[j] > max_right:
                    max_right = height[j]
            
            total_water += min(max_left,max_right) - height[i]

        return total_water

obj = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(obj.trappingRainwater(height))

Time Complexity: O(n²) because for each bar, we scan all bars to its left and right to find the maximum height, resulting in nested loops.

Space Complexity: O(1) as no additional data structures are used proportional to input size, only variables to track max heights and total water.
'''
# Optimal Solution

class Solution:
    def trappingRainwater(self,height):
        n = len(height)
        left = 0
        right = n-1
        maxLeft =0
        maxRight = 0
        totalWater = 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    totalWater += maxLeft - height[left]
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    totalWater += maxRight - height[right]
                right -= 1
            
        return totalWater
    
obj = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(obj.trappingRainwater(height))

'''
Time Complexity: O(n) because the two pointers traverse the array only once, each pointer moving inward and covering the entire array in total linear time.

Space Complexity: O(1) as only constant extra space is used for pointers and variables, regardless of input size.
'''