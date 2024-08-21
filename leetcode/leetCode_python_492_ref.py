class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        if area == 1:
            return [1, 1]
        for i in range(int(area**0.5), 0, -1):
            if area % i == 0:
                return [area // i, i]


y = Solution()
print(y.constructRectangle(2))
