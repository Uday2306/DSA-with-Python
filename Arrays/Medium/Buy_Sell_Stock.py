# Best Time to Buy and Sell Stock
'''
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''
# Brute Force Solution
'''
class Buy_Sell_Stock:
    def buySell(self,prices):
        max_profit = 0
        for buy in range(0,len(prices)):
            for sell in range(buy+1,len(prices)):
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit,profit)

        if max_profit < 0:
            return 0
        else:
            return max_profit

obj = Buy_Sell_Stock()            
prices = [7,1,5,3,6,4]
print(obj.buySell(prices))
'''

# OPtimal Solution 
class Buy_Sell_Stock:
    def buySell(self,prices):
        max_profit = 0
        min_profit = float("inf")
        for i in range(0,len(prices)):
            min_profit = min(min_profit,prices[i])
            max_profit = max(max_profit,(prices[i]-min_profit))
        
        return max_profit

obj = Buy_Sell_Stock()            
prices = [7,1,5,3,6,4]
print(obj.buySell(prices))