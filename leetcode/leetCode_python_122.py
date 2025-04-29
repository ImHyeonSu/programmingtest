class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


a = Solution()
print(a.maxProfit([1, 3, 4, 4, 5, 3, 2, 4, 5, 6, 4]))
