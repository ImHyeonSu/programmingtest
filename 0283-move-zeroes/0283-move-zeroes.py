class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        if len(nums) <= 1:
            return

        zero_idx = 0
        for idx, num in enumerate(nums):
            if num != 0:
                # 0
                temp = nums[zero_idx]
                # 1
                nums[zero_idx] = num
                # 0
                nums[idx] = temp
                zero_idx += 1