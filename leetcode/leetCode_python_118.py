class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []
        print(result)
        for i in range(1, 1 + numRows, 1):
            ins_arr = []
            for ins_i in range(1, 1 + i, 1):
                if ins_i == 1 or ins_i == i:
                    ins_arr.append(1)
                else:
                    ins_arr.append(result[i - 2][ins_i - 2] + result[i - 2][ins_i-1])
            result.append(ins_arr)
        return result


a = Solution()
print(a.generate(5))


# class Solution:
#     def generate(self, numRows: int) -> list[list[int]]:
#         result = []
#         for i in range(numRows):
#             row = [1] * (i + 1)
#             for j in range(1, i):
#                 row[j] = result[i - 1][j - 1] + result[i - 1][j]
#             result.append(row)
#         return result