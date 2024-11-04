class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] >= nums[left]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1


a = Solution()
print(a.search([4, 5, 6, 7, 0, 1, 2], 6))
