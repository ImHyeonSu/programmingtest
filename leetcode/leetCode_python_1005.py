class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()
        for _ in range(k):
            print("start", nums, k)
            nums[0] = -nums[0]
            nums.sort()
            print("end", nums, k)
        return sum(nums)


y = Solution()
print(y.largestSumAfterKNegations([2, -3, -1, 5, -4], 2))
