class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        replace_s = s.replace("-", "")
        result = ""
        if len(replace_s) % k == 0:
            first_len = 0
        else:
            first_len = len(replace_s) % k
            result += replace_s[0:first_len]

        for i in range(first_len, len(replace_s), k):
            if i != 0:
                result += "-"
            result += replace_s[i : i + k]
        return result.upper()


y = Solution()
print(y.licenseKeyFormatting("5F3Z-2e-9-w", 4))
