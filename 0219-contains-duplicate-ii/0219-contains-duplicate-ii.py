class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                if abs(i - dic[nums[i]]) <= k:
                    return True
                else:
                    dic[nums[i]] = i
            else:
                dic[nums[i]] = i
        return False