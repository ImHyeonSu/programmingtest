class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        for i in range(0, len(s), 2 * k):
            revers_s = s[i : i + k]
            result += revers_s[::-1] + s[i + k : i + 2 * k]
        return result
