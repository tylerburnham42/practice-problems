# Best time to buy and sell stock #121
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 5-21-2022

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest = prices[0]
        best_profit = 0
        
        for price in prices: 
            #print(price, lowest, best_profit)
            if price < lowest:
                lowest = price
            elif price - lowest  > best_profit:
                best_profit = price - lowest
                
        return best_profit