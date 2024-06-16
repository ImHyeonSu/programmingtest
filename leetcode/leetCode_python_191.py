class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 2
        test = 0
        firstFlag = False
        result = ""
        if n % bits != 0:
            n -= 1
            firstFlag = True
        while n > 0:
            if bits < n:
                bits * 2
                n +=1
            elif bits == n:
                result += "1"
                n = 0
            elif bits > n:
                bits /= 2

        return

# 11 2*e3 + 2*e1 + 1  17  2*e4 + 1


a = Solution()
print(a.reverseBits(00000010100101000001111010011100))