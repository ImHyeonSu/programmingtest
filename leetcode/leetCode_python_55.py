class Solution:
    def canJump(self, nums: list[int]) -> bool:

        n = len(nums)
        if n <= 1:
            return True

        current_max_reach = 0
        next_max_reach = 0
        for idx in range(n - 1):
            next_max_reach = max(next_max_reach, nums[idx] + idx)
            if idx == current_max_reach:
                current_max_reach = next_max_reach
            if current_max_reach >= n - 1:
                return True

        return False


a = Solution()
print(a.canJump([3, 2, 1, 0, 4]))
