class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # 2025_04_13確認
        if len(nums) == 1:
            return 1
        x = nums[0]
        i = 0
        while i < len(nums) - 1:
            if x == nums[1 + i]:
                del nums[1 + i]
            else:
                x = nums[1 + i]
                i += 1
        return i + 1


a = Solution()
print(a.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
