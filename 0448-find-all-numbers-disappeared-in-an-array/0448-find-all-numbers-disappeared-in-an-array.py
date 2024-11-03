class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        result_list = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result_list.append(i + 1)

        return result_list