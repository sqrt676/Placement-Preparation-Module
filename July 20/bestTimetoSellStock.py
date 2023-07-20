class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''Practise=3 my approach failed for large case'''
        '''profit=0
        n=len(prices)
        for i in range(n-1):
            for j in range(i,n):
                curr_profit=prices[j]-prices[i]
                if curr_profit>profit:
                    profit=curr_profit
        return profit'''

        if len(prices) == 1:
            return 0
        buy,sell = prices[0],prices[0]
        profit = sell-buy
        profits = [0]
        if len(prices) == 2:
            return max(0,prices[1]-prices[0])
        for i in range(1,len(prices)):
            if buy > prices[i]:
                buy,sell = prices[i],prices[i]
                profits.append(profit)
                profit = sell - buy
            elif sell < prices[i]:
                sell = prices[i]
                profit = sell - buy
            
        profits.append(profit)   
    
        return max(profits)