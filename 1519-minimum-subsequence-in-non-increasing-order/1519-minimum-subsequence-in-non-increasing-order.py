class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        for i in range(len(nums)):
            numbers = i
            if sum(nums[: i + 1]) > sum(nums[i + 1 :]):
                break

        return nums[: i + 1]
