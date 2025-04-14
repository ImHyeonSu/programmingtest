class Solution:
    # 2025_04_13確認
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index


p = Solution()
print(p.twoSum([1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1], 11))
