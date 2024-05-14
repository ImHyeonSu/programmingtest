class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = []
        result_len = 0
        for value in s:
            if value in result:
                result = result[result.index(value) + 1:]
            result.append(value)
            result_len = max(result_len, len(result))
        return result_len

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         result = list()
#         result_len = 0
#         for value in s:
#             if value in result:
#                 if result_len < len(result):
#                     result_len = len(result)
#                 index = result.index(value)
#                 result = result[index+1:]
#             if not value in result:
#                 result.append(value)
#         if result_len < len(result):
#             result_len = len(result)
#         return result_len

y = Solution()
print(y.lengthOfLongestSubstring("bpfbhmipx")) #"pwwkew" #au # " " "abcabcbb" "bbbbb"
# bpfbhmipx, aabaab!bb
