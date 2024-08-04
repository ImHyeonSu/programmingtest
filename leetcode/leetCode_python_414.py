class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        set_nums = set(nums)
        set_nums = sorted(set_nums, reverse=True)
        if len(set_nums) >= 3:
            return set_nums[2]
        else:
            return set_nums[0]


y = Solution()
print(y.thirdMax([1,2]))
