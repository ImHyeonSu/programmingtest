class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        pivot_idx, pivot_num = 0, 0
        don_pivot = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot_idx = i - 1
                pivot_num = nums[i - 1]
                break
            if i == 1:
                don_pivot = True
        if don_pivot:
            nums.sort()
        else:
            min_change_num_idx = len(nums) - 1
            while nums[min_change_num_idx] <= nums[pivot_idx]:
                min_change_num_idx -= 1
            nums[pivot_idx], nums[min_change_num_idx] = (
                nums[min_change_num_idx],
                pivot_num,
            )
            nums[pivot_idx + 1 :] = reversed(nums[pivot_idx + 1 :])