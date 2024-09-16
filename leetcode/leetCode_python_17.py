# class Solution:
#     def letterCombinations(self, digits: str) -> list[str]:
#         result_list = []
#         digits_dict = {
#             "1": "",
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz",
#         }
#         for i, v in enumerate(digits):
#             tmp_list = []
#             for digit_val in digits_dict[v]:
#                 if i == 0:
#                     result_list.append(digit_val)
#                     continue
#                 for result_val in result_list:
#                     tmp_list.append(result_val + digit_val)
#             if i != 0:
#                 result_list = tmp_list
#         return result_list


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        digits_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result_list = [""]

        for digit in digits:
            temp_list = []
            for combination in result_list:
                for letter in digits_dict[digit]:
                    temp_list.append(combination + letter)
            result_list = temp_list

        return result_list


y = Solution()
print(y.letterCombinations("23"))
