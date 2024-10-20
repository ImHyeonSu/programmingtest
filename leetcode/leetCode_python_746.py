class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        first = 0
        second = 0

        for i in range(n):
            current = cost[i] + min(first, second)
            first, second = second, current

        return min(first, second)


y = Solution()
print(y.minCostClimbingStairs([10, 15, 20]))
