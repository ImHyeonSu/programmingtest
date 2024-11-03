class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        i = 0

        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            groups.append(count)
            i += 1
        
        return sum(min(groups[j - 1], groups[j]) for j in range(1, len(groups)))
