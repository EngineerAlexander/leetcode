# There is an m x n rectangular island that borders both the 
# Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches 
# the island's left and top edges, and the Atlantic Ocean touches 
# the island's right and bottom edges.

# The island is partitioned into a grid of square cells. 
# You are given an m x n integer matrix heights where 
# heights[r][c] represents the height above sea level of 
# the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can 
# flow to neighboring cells directly north, south, east, and 
# west if the neighboring cell's height is less than or equal 
# to the current cell's height. Water can flow from any cell 
# adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where 
# result[i] = [ri, ci] denotes that rain water can flow 
# from cell (ri, ci) to both the Pacific and Atlantic oceans.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        # Create two matrices to mark reachability
        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]
        
        pacific_queue = deque()
        atlantic_queue = deque()
        
        # Initialize border cells for each ocean.
        # Pacific touches left and top edges.
        for i in range(m):
            pacific_reachable[i][0] = True
            pacific_queue.append((i, 0))
        for j in range(n):
            pacific_reachable[0][j] = True
            pacific_queue.append((0, j))
        
        # Atlantic touches right and bottom edges.
        for i in range(m):
            atlantic_reachable[i][n - 1] = True
            atlantic_queue.append((i, n - 1))
        for j in range(n):
            atlantic_reachable[m - 1][j] = True
            atlantic_queue.append((m - 1, j))
        
        def bfs(queue, reachable):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check boundaries, ensure we haven't visited this cell already,
                    # and only move if the neighbor's height is at least the current cell's height.
                    if 0 <= nr < m and 0 <= nc < n and not reachable[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        reachable[nr][nc] = True
                        queue.append((nr, nc))
        
        # Run BFS from both oceans
        bfs(pacific_queue, pacific_reachable)
        bfs(atlantic_queue, atlantic_reachable)
        
        # Collect cells that can reach both oceans.
        result = []
        for i in range(m):
            for j in range(n):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])
                    
        return result