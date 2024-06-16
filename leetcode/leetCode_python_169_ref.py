class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        for i in nums:
            if nums.count(i) > len(nums)//2:
                return i

a = Solution()
print(a.majorityElement([3, 2, 3]))
