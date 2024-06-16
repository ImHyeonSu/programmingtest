from typing import Optional


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        resultdic = {}
        for val in nums:
            if not val in resultdic:
                resultdic[val] = 1
            else:
                resultdic[val] = resultdic[val] + 1
        print(max(resultdic,key=resultdic.get));

a = Solution()
print(a.majorityElement([3, 2, 3]))
