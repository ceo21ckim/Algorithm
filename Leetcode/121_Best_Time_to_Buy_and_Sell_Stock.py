'''
You are given an array `prices` where `price[i]` is the price of a gvien stock on the `i-th` day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (Price = 1) and sell on day 5 (Price = 6), prifit = 6 - 1 = 5
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

# time out
prices = [7, 1, 5, 3, 6, 4]
# outs = [-1, 5, 1, 3, -2, 0]

def maxProfit(prices):
    if len(prices) == 1:
        return 0 
    
    results = [max(prices[i+1:]) - prices[i] for i in range(len(prices)) if i < len(prices)-1]
    outs = max(results)
    return outs if outs > 0 else 0

maxProfit(prices)


# solution 1
import sys 

# prices = [7, 1, 5, 3, 6, 4]
def maxProfit(prices):
    profit = 0 
    min_price = sys.maxsize # 9223372036854775807
    
    for price in prices:
        min_price = min(min_price, price) # 7, 1, 1
        profit = max(profit, price - min_price) # 0, 0, 4
    
    return profit 
