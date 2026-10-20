class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sell = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if(prices[j]>prices[i]):
                    sell_price = prices[j]-prices[i]
                    if (sell_price > max_sell):
                        max_sell = sell_price
        return max_sell

        