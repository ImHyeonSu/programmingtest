# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         n = len(s)
#         return_count = 0
#         for i in range(0, len(s) - 1):
#             tmp_i = i
#             first_count = 1
#             while tmp_i + 1 < n and s[tmp_i] == s[tmp_i + 1]:
#                 first_count += 1
#                 tmp_i += 1
#             second_count = 1
#             while tmp_i + 2 < n and s[tmp_i + 1] == s[tmp_i + 2]:
#                 if first_count == second_count:
#                     break
#                 second_count += 1
#                 tmp_i += 1
#             if first_count == second_count:
#                 return_count += 1
#         return return_count
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


y = Solution()
print(y.countBinarySubstrings("00110011"))
