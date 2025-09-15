class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        s_count = 0
        for v in s:
            if v == "R":
                s_count += 1
            elif v == "L":
                s_count -= 1
            if s_count == 0:
                count += 1
        return count


y = Solution()
print(y.balancedStringSplit("LLLLRRRR"))
