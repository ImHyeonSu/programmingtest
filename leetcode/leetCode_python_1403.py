# class Solution:
#     def minSubsequence(self, nums: list[int]) -> list[int]:
#         nums.sort(reverse=True)
#         for i in range(len(nums)):
#             numbers = i
#             if sum(nums[: i + 1]) > sum(nums[i + 1 :]):
#                 break

#         return nums[: i + 1]


class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum > total - current_sum:
                return nums[: i + 1]


y = Solution()
print(y.minSubsequence([4, 3, 10, 9, 8]))
