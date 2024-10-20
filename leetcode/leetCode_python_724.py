# class Solution:
#     def pivotIndex(self, nums: list[int]) -> int:
#         for i in range(0, len(nums)):
#             # print(i, sum(nums[0:i]), sum(nums[i + 1 : len(nums)]))
#             if sum(nums[0:i]) == sum(nums[i + 1 : len(nums)]):
#                 return i
#         return -1


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1


y = Solution()
print(y.pivotIndex([-1, -1, 0, 1, 1, 0]))
