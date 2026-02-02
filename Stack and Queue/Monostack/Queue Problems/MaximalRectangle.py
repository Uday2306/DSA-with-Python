# Maximal Rectangle
'''Problem Statement: Given a m x n binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Examples
Example 1:
Input:
 matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
Output: 6
Explanation:
 The largest rectangle of only 1's has area 6, formed by the 2×3 block of 1's in rows 1 and 2, columns 2 to 4.

Example 2:
Input:
 matrix = [[1]] 
Output:
 1 
Explanation: In this case, there is only one rectangle with area 1.'''

class Solution:
    def maximalRectangle(self,matrix):
        if not matrix:
            return 0

        rows = len(matrix)
        columns =len(matrix[0])

        heights = [0] * columns
        maxArea = 0

        for r in range(rows):
            for c in range(columns):
                if  matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0

            maxArea = max(maxArea,self.largestRectangleHistogram(heights))

        return maxArea 

    def largestRectangleHistogram(self,heights):
        stack = []
        maxArea = 0
        n = len(heights)

        for i in range(n + 1):
            currentHeight = heights[i] if i < n else 0

            while stack and currentHeight < heights[stack[-1]]:
                h = heights[stack.pop()]

                if not stack:
                    width = i
                else: 
                    width = i - stack[-1] - 1

                maxArea = max(maxArea,(h * width))
            
            stack.append(i)
        
        return maxArea

obj = Solution()

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(obj.maximalRectangle(matrix))