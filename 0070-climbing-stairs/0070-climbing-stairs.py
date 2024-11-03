class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        first = 1
        second = 2
        cur = 0
        for i in range(3,n+1,1):
            cur = first + second
            first = second
            second = cur
        return cur