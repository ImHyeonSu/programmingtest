class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                repeat_str = s[:i]
                if repeat_str * (n // i) == s:
                    return True
        return False


y = Solution()
print(y.repeatedSubstringPattern("abcabcabcabc"))
