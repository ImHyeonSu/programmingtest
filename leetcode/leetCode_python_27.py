class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if val == nums[i]:
                del nums[i]
                continue    
            i +=1
        return len(nums)
a = Solution()
print(a.removeElement([0,1,2,2,3,0,4,2], 2))