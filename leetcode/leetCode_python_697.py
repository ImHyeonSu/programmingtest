from collections import Counter


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        # 最初カウンタ
        # かうんたでとったdegreeをしゅとく
        # そのdegreeとおりでつくれるやつをfor回す。
        num_counts = Counter(nums)
        degree = max(num_counts.values())
        first = {}
        last = {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
        min_length = len(nums)

        for num in num_counts:
            if num_counts[num] == degree:
                length = last[num] - first[num] + 1
                min_length = min(min_length, length)

        return min_length


y = Solution()
print(y.findShortestSubArray([1, 2, 2, 3, 1]))
