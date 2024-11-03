class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        resultdic = {}
        for val in nums:
            if not val in resultdic:
                resultdic[val] = 1
            else:
                resultdic[val] = resultdic[val] + 1
        return max(resultdic,key=resultdic.get)