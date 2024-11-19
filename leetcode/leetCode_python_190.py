class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            bits = n & 1
            output = output | bits << (31 - i)  # > output = bits << (31-i)
            n = n >> 1
        return output


a = Solution()
print(a.reverseBits(int("00000010100101000001111010011100", 2)))
