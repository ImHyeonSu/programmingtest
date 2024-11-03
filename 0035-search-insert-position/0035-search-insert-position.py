class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i = 0
        for index, num in enumerate(nums):
            if nums[index] == target:
                return index
            elif nums[index] > target:
                return index
        return len(nums)