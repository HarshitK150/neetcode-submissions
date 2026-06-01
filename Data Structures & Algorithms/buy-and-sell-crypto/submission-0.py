class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, output = 0, 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                output = max(output, prices[r] - prices[l])
        return output