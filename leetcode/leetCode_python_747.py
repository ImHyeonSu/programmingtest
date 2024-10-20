class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_num = max(nums)
        for i in nums:
            if i == max_num:
                continue
            if i * 2 > max_num:
                return -1
        return nums.index(max_num)


y = Solution()
print(y.dominantIndex([1, 2, 3, 4]))
