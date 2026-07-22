from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for row in board:
            nums = []
            for x in row:
                if x != ".":
                    if x in nums:
                        return False
                    nums.append(x)

        # Check columns
        for col in range(9):
            nums = []
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] in nums:
                        return False
                    nums.append(board[row][col])

        # Check 3x3 boxes
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                nums = []
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] != ".":
                            if board[i][j] in nums:
                                return False
                            nums.append(board[i][j])

        return True