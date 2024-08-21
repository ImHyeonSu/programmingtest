class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        minus_flag = num < 0
        num = abs(num)

        result = []
        while num > 0:
            result.append(str(num % 7))
            num //= 7

        base7 = "".join(result[::-1])

        return "-" + base7 if minus_flag else base7


y = Solution()
print(y.convertToBase7(-7))
