class Solution:
    def binaryGap(self, n: int) -> int:

        binary_n = format(n, "b")
        if str(binary_n).count("1") < 2:
            return 0
        indices = [i for i in range(len(binary_n)) if binary_n[i] == "1"]
        result = 0
        for i in range(len(indices) - 1, -1, -1):
            if i != 0 and indices[i] - indices[i - 1] > result:
                result = indices[i] - indices[i - 1]
        return result


y = Solution()
print(y.binaryGap(5))
