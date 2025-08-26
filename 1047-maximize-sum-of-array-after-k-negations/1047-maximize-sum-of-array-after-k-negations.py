class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()
        for _ in range(k):
            nums[0] = -nums[0]
            nums.sort()
        return sum(nums)
