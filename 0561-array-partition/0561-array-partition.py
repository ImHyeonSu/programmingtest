class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result