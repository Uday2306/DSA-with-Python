# Sum of subarray minimum
'''
Problem Statement: Given an array of integers arr of size n, calculate the sum of the minimum value in each (contiguous) subarray of arr. Since the result may be large, return the answer modulo 10⁹ +7.
'''
'''
Example 1:
Input:
 arr = [3, 1, 2, 5]
Output:
 18
Explanation:
 The minimum of subarrays: [3], [1], [2], [5], [3, 1], [1, 2], [2, 5], [3, 1, 2], [1, 2, 5], [3, 1, 2, 5] are 3, 1, 2, 5, 1, 1, 2, 1, 1, 1 respectively and their sum is 18.

Example 2:
Input:
 arr = [2, 3, 1]
Output:
 10
Explanation:
 The minimum of subarrays: [2], [3], [1], [2,3], [3,1], [2,3,1] are 2, 3, 1, 2, 1, 1 respectively and their sum is 10.
'''
# Brute Force Solution
'''
class Solution:
    def sumOfSubarrayMin(self, arr):
        n = len(arr)
        mod = int(1e9 + 7) 
        ans = 0
        for i in range(0,n):
            minVal = arr[i]
            for j in range(i,n):
                minVal = min(minVal,arr[j])

                ans = (ans + minVal) 
        return ans
obj = Solution()
arr = [2, 3, 1]
print(obj.sumOfSubarrayMin(arr))
'''
'''Time complexity: O(n**2)
Space complexity: O(1)'''

# Optimal Solution
class Solution:
    def sumSubarrayMins(self, arr):
        
        n = len(arr)
        stack = []
        left = [0] * n
        right = [0] * n 

        # For left side
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack[-1][1]
                stack.pop()
            stack.append((arr[i],count))
            left[i] = count
        stack.clear()

        # Right side
        for i in range(n-1,-1,-1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack[-1][1]
                stack.pop() 
            stack.append((arr[i],count))
            right[i] = count
        
        ans = 0
        # Calculate result
        mod = 10**9 + 7
        for i in range(n):
            ans += arr[i] * left[i] * right[i]
        
        return (ans % mod)
obj = Solution()
arr = [3, 1, 2, 5]
print(obj.sumSubarrayMins(arr))