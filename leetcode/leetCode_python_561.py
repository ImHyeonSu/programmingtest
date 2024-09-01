class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result

# class Solution:
#     def arrayPairSum(self, nums: list[int]) -> int:
#         return sum(sorted(nums)[::2])


y = Solution()
print(y.arrayPairSum([6,2,6,5,1,2]))
