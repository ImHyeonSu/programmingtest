class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr == substr[::-1] and len(substr) > len(result):
                    result = substr
        return result if result else s[0]


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         result = ""
#         s_list = []
#         for idx, value in enumerate(s):
#             s_list.append(value)
#             if value in s_list:
#                 test_list = [i for i in range(len(s_list)) if s_list[i] == value]
#                 list_len = len(test_list)
#                 if list_len > 2:
#                     special_idx = test_list[list_len - 2]
#                     temp = s_list[special_idx : idx + 1]
#                 else:
#                     temp = s_list[s_list.index(value) : idx + 1]
#                 rev_list = temp[::-1]
#                 if temp == rev_list:
#                     if len(result) < len(rev_list):
#                         result = ""
#                         for v in rev_list:
#                             result += v
#         if result == "":
#             return s[0:1]
#         return result


y = Solution()
print(y.longestPalindrome("aacabdkacaa"))  # "babad" #cbbd # "a" "ac" "ccc" "aacabdkacaa"


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         result = ""
#         s_list = []
#         for idx, value in enumerate(s):
#             if value in s_list:
#                 s_list.append(value)
#                 rev_list = s_list[::-1]
#                 if s_list == rev_list:
#                     if len(result) < len(rev_list):
#                         result = ""
#                         for v in rev_list:
#                             result += v
#                         s_list = s_list[s_list.index(value)+1:]
#                 else:
#                     rev_list = s_list[s_list.index(value):idx+1]
#                     result = ""
#                     for v in rev_list:
#                         result += v
#             else:
#                 s_list.append(value)
#         if result == "":
#             return s[0:1]
#         return result
