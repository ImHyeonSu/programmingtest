class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        left, right = 0, len(nums) - 1
        return_list = []
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return_list.append(left if left < len(nums) and nums[left] == target else -1)

        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                left = middle + 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return_list.append(right if right >= 0 and nums[right] == target else -1)
        return return_list


# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

a = Solution()
print(a.searchRange([5, 7, 8, 8, 8, 10], 8))
