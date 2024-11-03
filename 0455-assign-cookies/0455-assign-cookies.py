class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        result_count = 0
        gi = 0
        g.sort()
        s.sort()
        for i in range(len(s)):
            if s[i] >= g[gi]:
                result_count += 1
                gi += 1
            if gi == len(g):
                break
        return result_count