"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

---------------------------------------------
zip wants a bunch of arguments to zip together, but what you have is a single argument (a list, whose elements are also lists).
The * in a function call "unpacks" a list (or other iterable), making each of its elements a separate argument.
So without the *, you're doing zip([[1,2,3], [4,5,6]]). With the *, you are doing zip([1,2,3], [4,5,6]).
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def checkUnit(unit):
            unit = [i for i in unit if i != '.']
            return len(set(unit)) == len(unit)

        def checkRow(board):
            for row in board:
                if not checkUnit(row):
                    return False
            return True

        def checkCol(board):
            for col in zip(*board):
                if not checkUnit(col):
                    return False
            return True

        def checkSquare(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                    if not checkUnit(square):
                        return False
            return True

        return (checkRow(board) and checkCol(board) and checkSquare(board))
