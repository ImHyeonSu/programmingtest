import random


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
y = Solution()
print(y.canWinNim(4))
