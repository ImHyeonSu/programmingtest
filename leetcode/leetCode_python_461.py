class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binary_x = format(x, "032b")
        binary_y = format(y, "032b")
        result = 0
        for i in range(len(binary_x)):
            if binary_x[i] != binary_y[i]:
                result += 1
        return result


y = Solution()
print(y.hammingDistance(3, 1))
