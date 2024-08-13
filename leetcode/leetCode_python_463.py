class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        width = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0:
                        width += 1
                    if i == rows - 1 or grid[i + 1][j] == 0:
                        width += 1
                    if j == 0 or grid[i][j - 1] == 0:
                        width += 1
                    if j == cols - 1 or grid[i][j + 1] == 0:
                        width += 1

        return width


y = Solution()
print(y.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
