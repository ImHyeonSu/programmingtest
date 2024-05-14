class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        if len(nums) <= 1:
            return

        zero_idx = 0
        for idx, num in enumerate(nums):
            if num != 0:
                temp = nums[zero_idx]
                nums[zero_idx] = num
                nums[idx] = temp
                zero_idx += 1
            print(nums)

y = Solution()
print(y.moveZeroes([0,1,0,3,12]))
