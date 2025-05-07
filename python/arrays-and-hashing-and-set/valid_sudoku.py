# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
# need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the 
# digits 1-9 without repetition.
# Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # lhs to rhs then top down
        # CAN BE IMPROVED BY USING HASH SETS AS THEY HAVE CONSTANT LOOKUP
        sub_boxes = [set() for x in range(9)]

        row_values = [set() for x in range(9)]
        column_values = [set() for x in range(9)]

        # seperate everything out into proper group
        for row in range(9):
            for column in range(9):
                value = board[row][column]

                # no value
                if value == ".":
                    continue

                num = int(value)

                from_lhs = ((column) // 3)
                top_down_contribution = ((row) // 3)*3

                # duplicate break
                if (num in sub_boxes[from_lhs + top_down_contribution]) \
                    or (num in row_values[row]) \
                    or (num in column_values[column]):
                    return False

                sub_boxes[from_lhs + top_down_contribution].add(num)
                row_values[row].add(num)
                column_values[column].add(num)
        return True
    
# Time complexity: O(1), because we know the board is 9x9
# Space complexity: O(1), because we know the board is 9x9