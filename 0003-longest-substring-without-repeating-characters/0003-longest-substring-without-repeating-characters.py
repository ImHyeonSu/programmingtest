class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = []
        result_len = 0
        for value in s:
            if value in result:
                result = result[result.index(value) + 1 :]
            result.append(value)
            result_len = max(result_len, len(result))
        return result_len
