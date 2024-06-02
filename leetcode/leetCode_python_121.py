class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]   
        result = 0
        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            result = max(result, p - buy_price)

        return result


a = Solution()
print(a.maxProfit([7, 1, 5, 3, 6, 4]))
