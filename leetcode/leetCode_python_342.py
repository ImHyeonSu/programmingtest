class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        var = 1
        while var <= n:
            var *= 4
            if var == n:
                return True
            elif var > n:
                return False
y = Solution()
print(y.isPowerOfFour(1))
