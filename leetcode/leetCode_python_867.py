class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return_list = [[] for _ in matrix[0]]
        for tmp_mat in matrix:
            for idx, val in enumerate(tmp_mat):
                return_list[idx].append(val)
        return return_list


y = Solution()
print(y.transpose([[1, 2, 3], [4, 5, 6]]))
# Output: [[1,4,7],[2,5,8],[3,6,9]]

# [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
