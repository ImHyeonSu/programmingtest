from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        for key, i in c.items():
            ans += int(i / 2) * 2
            if ans % 2 == 0 and i % 2 == 1:
                ans += 1
        return ans