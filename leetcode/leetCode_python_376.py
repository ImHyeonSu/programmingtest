class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)


y = Solution()
print(y.wiggleMaxLength([1, 7, 4, 9, 2, 5]))
