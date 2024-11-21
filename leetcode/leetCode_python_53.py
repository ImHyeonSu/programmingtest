# class Solution:
#     def __init__(self) -> None:
#         self.result = float("-inf")
#     def set_result(self, result):
#         self.result = result
#     def check_array(self, arr):
#         return sum(arr)
#     def maxSubArray(self, nums: list[int]) -> int:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums) + 1):
#                 sub = nums[i:j]
#                 current_sum = self.check_array(sub)
#                 if current_sum > self.result:
#                     self.set_result(current_sum)
# ->timemout...


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum


a = Solution()
print(a.maxSubArray([5, 4, -1, 7, 8]))
