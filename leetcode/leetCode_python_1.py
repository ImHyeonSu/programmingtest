class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for p in range(len(nums)):
            result = []
            result.append(p)
            for p2 in range(len(nums)):
                if (nums[p] + nums[p2]) == target and (p != p2):
                    result.append(p2)
                    return result
                elif p == p2:
                    continue
            result.remove(p)
            

p = Solution()
print(p.twoSum([1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1], 11))
