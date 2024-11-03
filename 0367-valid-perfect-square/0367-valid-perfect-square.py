class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        mul_num = 1
        abs_num = 0
        while abs_num < num:
            abs_num = mul_num ** 2
            if abs_num == num:
                return True
            mul_num += 1
        return False