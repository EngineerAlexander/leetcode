# You are given an m x n matrix board containing letters 'X' 
# and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells 
# horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells 
# if you can connect the region with 'X' cells and 
# none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 
# 'X's in-place within the original board. You do not 
# need to return anything.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        queue = deque()
        
        # Add all border cells that are 'O' to the queue.
        for r in range(rows):
            for c in (0, cols - 1):  # leftmost and rightmost columns.
                if board[r][c] == 'O':
                    queue.append((r, c))
        for c in range(cols):
            for r in (0, rows - 1):  # top and bottom rows.
                if board[r][c] == 'O':
                    queue.append((r, c))
        
        # Mark all cells that can reach the border as safe (S).
        while queue:
            r, c = queue.popleft()
            if board[r][c] != 'O':
                continue
            board[r][c] = 'S'
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    queue.append((nr, nc))
        
        # Flip all non-safe 'O's to 'X', and then revert safe 'S's back to 'O'.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'