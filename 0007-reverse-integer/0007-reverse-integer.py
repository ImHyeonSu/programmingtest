class Solution:
    def reverse(self, x: int) -> int:

        result = ""
        str_x = str(x)
        result = str_x[::-1]
        if str_x[0] == "-":
            result = str_x[0] + str_x[1:][::-1]
        if int(result) < -(2**31) or int(result) > 2**31 - 1:
            return 0
        return int(result)