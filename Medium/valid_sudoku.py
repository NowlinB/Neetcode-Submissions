"""You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

    Each row must contain the digits 1-9 without duplicates.
    Each column must contain the digits 1-9 without duplicates.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid. """

count1 = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        sol = Solution()
        rowsResult = sol.checkRows(board) #returns True if each row is unique and does not contain duplicates
        columnResult = sol.checkColumns(board) # returns True if each column does not contain duplicates
        subBoxResult = sol.checkSubBox(board) #returns True if all the values in a given 3x3 subbox have no duplicates
        if rowsResult and columnResult and subBoxResult:
            return True
        else:
            return False

    def checkRows(self, board: list[list[str]]) -> bool:
        i, j = 0, 0
        while i < len(board):
            j = 0
            count = {
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0,
                "7": 0,
                "8": 0,
                "9": 0,
            }
            while j < len(board):
                if board[i][j] != ".":  # we know we've found a number
                    count.update({board[i][j]: (count.get(board[i][j])) + 1})
                    if count.get(board[i][j]) > 1:
                        return False
                j += 1
            i += 1
        return True

    def checkColumns(self, board: list[list[str]]) -> bool:
        i, j = 0, 0
        while i < len(board):
            j = 0
            count = {
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0,
                "7": 0,
                "8": 0,
                "9": 0,
            }
            while j < len(board):
                if board[j][i] != ".":  # we know we've found a number
                    count.update({board[j][i]: (count.get(board[j][i])) + 1})
                    if count.get(board[j][i]) > 1:
                        return False
                j += 1
            i += 1
        return True

    def checkSubBox(self, board: list[list[str]]) -> bool:
        i, j = 0, 0
        x, y = 3, 0  # used to define the bounds of the current subbox
        while i < len(board):
            j = 0
            if y % 3 == 0:
                count = {
                    "1": 0,
                    "2": 0,
                    "3": 0,
                    "4": 0,
                    "5": 0,
                    "6": 0,
                    "7": 0,
                    "8": 0,
                    "9": 0,
                }
            while j < x:
                if board[i][j] != ".":  # we know we've found a number
                    count.update({board[i][j]: (count.get(board[i][j])) + 1})
                    if count.get(board[i][j]) > 1:
                        return False
                j += 1
            i += 1
            y += 1
        return True


sol = Solution()
board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", ".", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


testIsValid = sol.isValidSudoku(board)
print(testIsValid)
