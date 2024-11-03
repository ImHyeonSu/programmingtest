class Solution:
    def findLHS(self, nums: list[int]) -> int:
        hMap = Counter(nums)
        max_len = 0

        for num, cnt in hMap.items():
            if num + 1 in hMap:
                max_len = max(max_len, hMap[num + 1] + cnt)
        
        return max_len