class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        result = ""
        str_num = str(num)
        for idx, value in enumerate(str_num):
            num_value = int(value)
            if num_value > 5:
                if num_value == 9:
                    result += dic[10 ** (len(str_num) - idx - 1)]
                    result += dic[10 ** (len(str_num) - idx)]
                else:
                    result += dic[10 ** (len(str_num) - idx) // 2]
                    num_value -= 5
                    for i in range(1, num_value + 1):
                        result += dic[10 ** (len(str_num) - idx - 1)]
            else:
                if num_value == 4:
                    result += dic[10 ** (len(str_num) - idx - 1)]
                    result += dic[10 ** (len(str_num) - idx - 1) * 5]
                elif num_value == 5:
                    result += dic[num_value * 10 ** (len(str_num) - idx - 1)]
                else:
                    for i in range(1, num_value + 1):
                        result += dic[10 ** (len(str_num) - idx - 1)]
        return result