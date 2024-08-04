class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = ""

        if num < 0:
            num += 2**32
        while num > 0:
            result = hex_chars[num % 16] + result
            num //= 16
        return result


y = Solution()
print(y.toHex(26))
