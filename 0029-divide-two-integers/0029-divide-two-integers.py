class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return_num = int(dividend / divisor)
        if return_num > 2**31 - 1:
            return_num = 2**31 - 1
        elif return_num < -(2**31):
            return_num = -(2**31)
        return return_num