# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent 
# to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has 
# a fresh orange. If this is impossible, return -1.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q_rotten = deque()
        fresh = 0
        
        # Find all rotten oranges and count fresh ones
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q_rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        
        # BFS level-order traversal
        # Note we do not need visited since we are changing grid
        while q_rotten and fresh:
            for _ in range(len(q_rotten)):
                r, c = q_rotten.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q_rotten.append((nr, nc))
            time += 1
        
        # If there are still fresh oranges, it's impossible
        return time if fresh == 0 else -1