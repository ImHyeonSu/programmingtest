class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def isNice(sub):
            chars = set(sub)
            for c in chars:
                if c.isupper() and c.lower() not in chars:
                    return False
                if c.islower() and c.upper() not in chars:
                    return False
            return True

        result = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if isNice(sub) and len(sub) > len(result):
                    result = sub

        return result
