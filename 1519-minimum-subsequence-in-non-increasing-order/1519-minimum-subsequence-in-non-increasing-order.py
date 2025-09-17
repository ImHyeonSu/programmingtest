class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum > total - current_sum:
                return nums[: i + 1]
