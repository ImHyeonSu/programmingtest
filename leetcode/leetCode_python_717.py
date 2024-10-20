class Solution:
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == len(bits) - 1


y = Solution()
print(y.isOneBitCharacter([1, 1, 1, 0]))
