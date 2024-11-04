class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return_list = [[] for _ in matrix[0]]
        for tmp_mat in matrix:
            for idx, val in enumerate(tmp_mat):
                return_list[idx].append(val)
        return return_list