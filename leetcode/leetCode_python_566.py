class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        wid = 0
        result = []
        for i in mat:
            wid += len(i)
        if wid < r * c:
            return mat
        if r == 1 and c == 1 and wid > 1:
            return mat
        tmp_result = []
        for tmp_mat in mat:
            for val in tmp_mat:
                tmp_result.append(val)
                if len(tmp_result) == c:
                    result.append(tmp_result)
                    tmp_result = []
        return result


y = Solution()
print(y.matrixReshape([[1, 2], [3, 4]], 1, 4))
