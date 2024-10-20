class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary_n = format(n, "b")
        last_str = None
        for i in binary_n:
            if i == last_str:
                return False
            last_str = i
        return True

y = Solution()
print(y.hasAlternatingBits(10))
