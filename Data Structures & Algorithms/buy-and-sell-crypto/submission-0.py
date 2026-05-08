class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0,1
        n = len(prices)
        maxProfit = 0
        while sell < n:
            if prices[buy] <= prices[sell]:
                currProfit = prices[sell] - prices[buy]
                maxProfit = max(currProfit, maxProfit)
                sell += 1
            else:
                buy = sell
        return maxProfit