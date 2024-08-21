class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        result = 0
        tmp_count = 0
        for index, value in enumerate(nums):
            if value == 1:
                tmp_count += 1
                if index == len(nums) - 1 and result < tmp_count:
                    result = tmp_count
            else:
                if result < tmp_count:
                    result = tmp_count
                tmp_count = 0
        return result


y = Solution()
print(y.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
