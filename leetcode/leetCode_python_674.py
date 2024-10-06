# class Solution:
#     def findLengthOfLCIS(self, nums: list[int]) -> int:
#         if len(nums) == 1:
#             return 1
#         data = 1
#         last_num = nums[0]
#         plus_value = nums[1] - nums[0]
#         tmp_list = []
#         for i in range(1, len(nums)):
#             if plus_value <= 0:
#                 continue
#             if (nums[i] - last_num) != plus_value:
#                 print(i, nums[i], nums[i] - last_num)
#                 if nums[i] - last_num > 0:
#                     plus_value = nums[i] - last_num
#                     print(plus_value)
#                 data = 1
#             elif (nums[i] - last_num) == plus_value:
#                 data += 1
#                 tmp_list.append(data)
#             last_num = nums[i]
#             print(i, nums[i], tmp_list)
#         return max(tmp_list) if len(tmp_list) > 0 else 1


# class Solution:
#     def findLengthOfLCIS(self, nums: list[int]) -> int:
#         if len(nums) == 1:
#             return 1
#         return_data = 1
#         return_set = set()
#         plus_value = nums[1] - nums[0] if nums[1] - nums[0] > 0 else 0
#         for i in range(0, len(nums) - 1):
#             if nums[i + 1] != nums[i] and plus_value == nums[i + 1] - nums[i]:
#                 return_data += 1
#                 if i == len(nums) - 2:
#                     return_data += 1
#             else:
#                 plus_value = nums[i + 1] - nums[i]
#                 return_data = 1
#             return_set.add(return_data)
#         return max(return_set) if max(return_set) < len(nums) else len(nums)
    

class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if not nums: 
            return 0
        
        max_len = 1  
        current_len = 1 
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  
                current_len += 1
            else:
                max_len = max(max_len, current_len)  
                current_len = 1  
        
        return max(max_len, current_len)


y = Solution()
print(y.findLengthOfLCIS([1,3,5,4,2,3,4,5]))
