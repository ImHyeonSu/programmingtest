from collections import Counter
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_duplicates(counter: Counter) -> bool:
            return any(count >= 2 for key, count in counter.items() if key != '.')

        def check_rows() -> bool:
            return all(not has_duplicates(Counter(row)) for row in board)

        def check_columns() -> bool:
            return all(not has_duplicates(Counter(row[i] for row in board)) 
                      for i in range(9))

        def check_boxes() -> bool:
            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    box = []
                    for i in range(3):
                        for j in range(3):
                            box.append(board[box_row + i][box_col + j])
                    if has_duplicates(Counter(box)):
                        return False
            return True

        return check_rows() and check_columns() and check_boxes()


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
