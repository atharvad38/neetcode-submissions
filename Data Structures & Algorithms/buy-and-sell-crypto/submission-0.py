class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        min_buy = prices[0]
        for i in range(1,n):
            ans = max(ans,prices[i]-min_buy)
            min_buy = min(min_buy,prices[i])
        return ans

        