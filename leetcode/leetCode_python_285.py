class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        if len(nums) == 1:
            return
        idx = 0
        zero_cnt = 0
        while zero_cnt < nums.count(0):
            if nums[idx] == 0 :
                if idx + 1 != len(nums):
                    last_value = nums[len(nums)-1]
                    if idx == 0:
                        for i in range(idx, len(nums)):
                            nums[i-1] = nums[i]
                    else:
                        for i in range(idx, len(nums)-1):
                            nums[i] = nums[i+1]
                        nums[len(nums)-1] = 0
                    nums[len(nums)-2] = last_value
                zero_cnt += 1
            else:
                idx += 1

y = Solution()
print(y.moveZeroes([1,0]))
