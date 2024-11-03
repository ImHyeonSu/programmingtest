class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        var = 1
        while var <= n:
            var *= 3
            if var == n:
                return True
            elif var > n:
                return False