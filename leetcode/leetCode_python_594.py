from collections import defaultdict

# class Solution:
#     def findLHS(self, nums: list[int]) -> int:
#         count_num = 0
#         for i, v in enumerate(nums):
#             tmp_count = 0
#             if nums[i + 1 :].count(v + 1) != 0:
#                 tmp_count = nums[i + 1 :].count(v + 1) + 1 + nums[i + 1 :].count(v)
#             if count_num < tmp_count:
#                 count_num = tmp_count
#             tmp_count = 0
#             if nums[i + 1 :].count(v - 1) != 0:
#                 tmp_count =nums[i + 1 :].count(v - 1) + 1 + nums[i + 1 :].count(v)
#             if count_num < tmp_count:
#                 count_num = tmp_count
#         return count_num

from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        count = Counter(nums)
        max_length = 0
        
        for num in count:
            if num + 1 in count:  
                max_length = max(max_length, count[num] + count[num + 1])
        
        return max_length


y = Solution()
print(y.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
