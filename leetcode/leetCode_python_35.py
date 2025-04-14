class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i = 0
        for index, _ in enumerate(nums):
            if nums[index] == target:
                return index
            elif nums[index] > target:
                return index
        return len(nums)


a = Solution()
print(a.searchInsert([1, 3, 5, 6], 7))
