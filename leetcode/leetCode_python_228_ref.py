class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        result = []
        start = end = nums[0]

        for value in nums:
            if end + 1 == value:
                end = value
            else:
                result.append(str(start) if start == end else f"{start}->{end}")
                start = end = value
        result.append(str(start) if start == end else f"{start}->{end}")

        # result = []
        # last_value = []
        # for index, value in enumerate(nums):
        #     if index == 0:
        #         last_value.append(value)
        #         continue
        #     if last_value[-1] + 1 != value:
        #         if len(last_value) == 1:
        #             result.append(str(last_value[0]))
        #         else:
        #             result.append(str(last_value[0]) + "->" + str(last_value[-1]))
        #         last_value = []
        #         last_value.append(value)
        #     else:
        #         last_value.append(value)
        #     if index+1 == len(nums):
        #         if len(last_value) == 1:
        #             result.append(str(last_value[0]))
        #         else:
        #             result.append(str(last_value[0]) + "->" + str(last_value[-1]))
        # return result



a = Solution();
print(a.summaryRanges( [1]));
