class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        for i in nums:
            if nums.count(i) == 2:
                pass
            else:
                return i


a = Solution()
print(a.singleNumber([1]))
