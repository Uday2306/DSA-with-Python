# Minimum number of coins
'''
You are given a value N. Your task is to represent this value using the minimum number of coins and notes available in the Indian currency system.

The available denominations are:

[2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
You need to output the coins/notes used in making the change for the given amount.

Example 1:

Input: N = 43
Output: [20, 20, 2, 1]
Explanation: 
- 20 + 20 + 2 + 1 = 43 using 4 coins/notes.
Example 2:

Input: N = 1000
Output: [500, 500]
Explanation:
- The amount 1000 can be formed using only two 500 rupee notes.
'''

class Solution:
    def minimumNumberOfCoins(self,coins,target):
        result = []
        n = len(coins)

        for i in range(n-1,-1,-1):
            while target >= coins[i]:
                result.append(coins[i])
                target -= coins[i] 
        
        return result

obj = Solution()
# coins = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
coins = [1,2,5,10,20,50,100,200,500,2000]
n = 1000
print(obj.minimumNumberOfCoins(coins,n))