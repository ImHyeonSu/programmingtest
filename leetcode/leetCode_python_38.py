class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        result = "1"
        for _ in range(2, n + 1):
            temp = ""
            count = 1
            current = result[0]

            for i in range(1, len(result)):
                if result[i] == current:
                    count += 1
                else:
                    temp += str(count) + current
                    current = result[i]
                    count = 1
            temp += str(count) + current
            result = temp

        return result


# class Solution:
#     def countAndSay(self, n: int) -> str:
#         if n == 1:
#             return str(1)
#         return_str = "1"
#         for i in range(2, n + 1, 1):
#             tmp_str = ""
#             last_str = return_str[0]
#             count = 0
#             for j in range(0, len(return_str)):
#                 if last_str == return_str[j]:
#                     count += 1
#                 if j != len(return_str) - 1 and last_str != return_str[j + 1]:
#                     tmp_str += str(count) + str(last_str)
#                     last_str = return_str[j + 1]
#                     count = 0
#                 if j == len(return_str) - 1:
#                     tmp_str += str(count) + str(last_str)
#             return_str = tmp_str
#         return return_str


a = Solution()
print(a.countAndSay(5))
