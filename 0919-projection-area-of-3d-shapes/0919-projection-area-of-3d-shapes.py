class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        result = 0
        for tmp_grid in grid:
            # yx
            result += sum(1 for j in tmp_grid if j > 0)
            # zx
            result += max(tmp_grid)
        # yz
        result += sum(max(col) for col in zip(*grid))
        return result
