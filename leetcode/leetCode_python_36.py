from collections import Counter


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row_i in range(0, 9, 1):
            # check row
            count_num = Counter(board[row_i])
            del count_num["."]
            if any(count >= 2 for count in count_num.values()):
                return False
            # check column
            for i in range(0, 9, 1):
                for j in range(0, 9, 1):
                    for z in range(i + 1, 9, 1):
                        if board[i][j] == "." or board[z][j] == ".":
                            continue
                        if board[i][j] == board[z][j]:
                            return False
            # check box
            for i in range(0, 3, 1):
                box_list = []
                for j in range(0, 3, 1):
                    box_list.append(board[i * 3][j * 3])
                    box_list.append(board[i * 3][j * 3 + 1])
                    box_list.append(board[i * 3][j * 3 + 2])
                    for z in range(i * 3 + 1, i * 3 + 3, 1):
                        box_list.append(board[z][j * 3])
                        box_list.append(board[z][j * 3 + 1])
                        box_list.append(board[z][j * 3 + 2])
                    count_num = Counter(box_list)
                    del count_num["."]
                    if any(count >= 2 for count in count_num.values()):
                        return False
                    box_list = []
        return True


a = Solution()
print(
    a.isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
