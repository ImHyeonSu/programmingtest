class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        result = ""
        carry = 0

        for i in range(min(len(a), len(b))):
            bit_sum = int(a[i]) + int(b[i]) + carry
            result += str(bit_sum % 2)
            carry = bit_sum // 2

        for i in range(min(len(a), len(b)), max(len(a), len(b))):
            bit_sum = int(a[i]) + carry if len(a) > len(b) else int(b[i]) + carry
            result += str(bit_sum % 2)
            carry = bit_sum // 2

        if carry > 0:
            result += str(carry)

        return result[::-1]