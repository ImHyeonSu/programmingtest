# class Solution:
#     def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
#         ans = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
#         for i in range(len(img)):
#             for j in range(len(img[0])):
#                 neighbors = []
#                 for x in range(max(0, i - 1), min(len(img), i + 2)):
#                     for y in range(max(0, j - 1), min(len(img[0]), j + 2)):
#                         neighbors.append(img[x][y])
#                 ans[i][j] = sum(neighbors) // len(neighbors)
#         return ans


import math
class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m, n = len(img), len(img[0])
        
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                total_sum = 0
                count = 0
                
                for r in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        if 0 <= r < m and 0 <= c < n:
                            total_sum += img[r][c]
                            count += 1
                
                result[i][j] = math.floor(total_sum / count)
        
        return result

y = Solution()
print(y.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
