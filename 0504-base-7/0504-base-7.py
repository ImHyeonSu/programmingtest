class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        plus_num = 0
        minus_flag = False
        result = ""
        if num < 0:
            minus_flag = True
            num *= -1
        while num > 0:
            plus_num = num % 7
            result += str(plus_num)
            num = num // 7
        result = result[::-1]
        if minus_flag:
            result = "-" + result
        return result