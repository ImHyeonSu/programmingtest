class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        n = len(s)
        i = 0

        while i < n:
            count = 1
            while i + 1 < n and s[i] == s[i + 1]:
                count += 1
                i += 1
            groups.append(count)
            i += 1
        return_count = 0
        for j in range(1, len(groups)):
            return_count += min(groups[j - 1], groups[j])

        return return_count
