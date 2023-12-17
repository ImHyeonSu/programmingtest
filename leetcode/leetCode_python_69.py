class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0
        mulDate = 0
        while mulDate <= x:
            result += 1
            mulDate = result * result

        if mulDate > x:
            return result - 1
        elif mulDate == x:
            return result


a = Solution()
print(a.mySqrt(3))
