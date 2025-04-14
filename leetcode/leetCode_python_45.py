class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        jumps = 0
        current_max_reach = 0
        next_max_reach = 0
        for idx in range(n - 1):
            next_max_reach = max(next_max_reach, nums[idx] + idx)
            if idx == current_max_reach:
                jumps += 1
                current_max_reach = next_max_reach
            if current_max_reach >= n - 1:
                break

        return jumps


a = Solution()
print(a.jump([3, 4, 2, 1, 1, 3, 1, 2, 5, 1, 1, 1]))
