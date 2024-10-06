class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for v in moves:
            if v == "R":
                x += 1
            elif v == "L":
                x -= 1
            elif v == "U":
                y += 1
            elif v == "D":
                y -= 1
        return True if x == 0 and y == 0 else False


y = Solution()
print(y.judgeCircle("LL"))
