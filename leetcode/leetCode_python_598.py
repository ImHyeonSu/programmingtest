# class Solution:
#     def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
#         matrix = [[0] * n for _ in range(m)]
#         for tmp_ops in ops:
#             for r in range(tmp_ops[0]):
#                 for c in range(tmp_ops[1]):
#                     matrix[r][c] += 1
#         max_value = max(max(row) for row in matrix)
#         max_count = sum(row.count(max_value) for row in matrix)
#         return max_count

# class Solution:
#     def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
#         if not ops:
#             return m * n
        
#         min_a = min(op[0] for op in ops)
#         min_b = min(op[1] for op in ops)
        
#         return min_a * min_b


class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        if not ops:
            return m * n
        
        min_a = m
        min_b = n
        
        for a, b in ops:
            min_a = min(min_a, a)
            min_b = min(min_b, b)
        
        return min_a * min_b


y = Solution()
print(y.maxCount(3, 3, [[2, 2], [3, 3]]))
