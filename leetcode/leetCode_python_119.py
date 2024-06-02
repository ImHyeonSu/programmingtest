class Solution:
    def getRow(self, numRows: int) -> list[list[int]]:
        result = []
        for i in range(1, 2 + numRows, 1):
            ins_arr = []
            for ins_i in range(1, 1 + i, 1):
                if ins_i == 1 or ins_i == i:
                    ins_arr.append(1)
                else:
                    ins_arr.append(result[i - 2][ins_i - 2] + result[i - 2][ins_i-1])
            result.append(ins_arr)
        return result[numRows]


a = Solution()
print(a.getRow(1))
