class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        unique_candies = set(candyType)
        return min(len(unique_candies), len(candyType) // 2)


y = Solution()
print(y.distributeCandies([1, 1, 2, 2, 3, 3]))
