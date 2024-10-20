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
