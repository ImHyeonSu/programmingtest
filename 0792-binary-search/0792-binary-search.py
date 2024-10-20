class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1 if len(nums) > 1 else 1
        while left <= right:
            center = (left + right) // 2
            if center > len(nums) - 1:
                break
            if nums[center] > target:
                right = center - 1
            elif nums[center] < target:
                left = center + 1
            elif nums[center] == target:
                return center
        return -1