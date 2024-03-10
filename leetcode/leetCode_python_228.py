class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        last_value = []
        if len(nums) == 1:
            result.append(str(nums[0]))
            return result
        for index, value in enumerate(nums):
            if index == 0:
                last_value.append(value)
                continue
            if last_value[-1] + 1 != value:
                if len(last_value) == 1:
                    result.append(str(last_value[0]))
                else:
                    result.append(str(last_value[0]) + "->" + str(last_value[-1]))
                last_value = []
                last_value.append(value)
            else:
                last_value.append(value)
            if index+1 == len(nums):
                if len(last_value) == 1:
                    result.append(str(last_value[0]))
                else:
                    result.append(str(last_value[0]) + "->" + str(last_value[-1]))
        return result

a = Solution();
print(a.summaryRanges( [1]));
