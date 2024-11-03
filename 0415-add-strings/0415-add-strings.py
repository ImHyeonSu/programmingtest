class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        min_len = len(num1)
        result = ""
        plus_num = 0
        min_num = num1[::-1]
        max_num = num2[::-1]
        if len(num1) > len(num2):
            min_len = len(num2)
            min_num = num2[::-1]
            max_num = num1[::-1]
        for i in range(0, min_len, 1):
            for_plus = 0
            if plus_num > 0:
                for_plus = int(min_num[i]) + int(max_num[i]) + plus_num
                plus_num = 0
            else:
                for_plus = int(min_num[i]) + int(max_num[i])
            if for_plus >= 10:
                result = str(for_plus)[1] + result
                plus_num = int(str(for_plus)[0])
            else:
                result = str(for_plus)[0] + result
        for i in range(min_len, len(max_num), 1):
            for_plus = 0
            if plus_num > 0:
                for_plus = int(max_num[i]) + plus_num
                plus_num = 0
            else:
                for_plus = int(max_num[i])
            if for_plus >= 10:
                result = str(for_plus)[1] + result
                plus_num = int(str(for_plus)[0])
            else:
                result = str(for_plus)[0] + result
        if plus_num > 0:
            result = str(plus_num) + result
        return str(result)