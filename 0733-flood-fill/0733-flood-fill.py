class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        after_change_num = image[sr][sc]
        if color == after_change_num:
            return image

        def change(r, c):
            if (
                r < 0
                or r >= len(image)
                or c < 0
                or c >= len(image[0])
                or image[r][c] != after_change_num
            ):
                return
            if after_change_num == image[r][c]:
                image[r][c] = color
            change(r + 1, c)
            change(r - 1, c)
            change(r, c + 1)
            change(r, c - 1)

        change(sr, sc)

        return image