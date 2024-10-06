# class Solution:
#     def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
#         nums.sort()
#         result = []
#         for i in range(len(nums) - 3):
#             for j in range(i + 1, len(nums) - 2):
#                 first_sum = nums[i] + nums[j]

#                 left, right = j + 1, len(nums) - 1
#                 while left < right:
#                     second_sum = nums[left] + nums[right]
#                     if first_sum + second_sum == target:
#                         result.append([nums[i], nums[j], nums[left], nums[right]])
#                         left += 1
#                         right -= 1
#                     elif first_sum + second_sum < target:
#                         left += 1
#                     elif first_sum + second_sum > target:
#                         right -= 1
#         result = list({tuple(row): row for row in result}.values())
#         return result


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, len(nums) - 1

                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if four_sum == target:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1

        return [list(quad) for quad in result]


y = Solution()
print(y.fourSum([-1, 0, 1, 2, -1, -4], -1))
