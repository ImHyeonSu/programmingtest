# class Solution:
#     def maximumProduct(self, nums: list[int]) -> int:
#         nums.sort(reverse=True)
#         print(nums)
#         result = nums[0] * nums[1] * nums[2]
#         if nums[-1] < 0 and nums[-2] < 0:
#             if nums[0] > 0:
#                 max_num = (
#                     nums[1] * nums[2]
#                     if nums[1] * nums[2] > nums[-1] * nums[-2]
#                     else nums[-1] * nums[-2]
#                 )
#                 result = max_num * nums[0]
#         return result

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

y = Solution()
print(y.maximumProduct([-8, -7, -2, 10, 20]))
