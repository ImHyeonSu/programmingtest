class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        odd_count = 0
        even_count = 0
        for v in position:
            if v % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return min(odd_count, even_count)


y = Solution()
print(y.minCostToMoveChips([1, 2, 3]))
