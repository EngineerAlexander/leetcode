# You are given an m x n binary matrix grid. 
# An island is a group of 1's (representing land) 
# connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        R = len(grid)
        C = len(grid[0])

        def bfs(r, c, R, C):
            visited.add((r, c))
            q = deque()
            q.append((r, c))
            area = 0
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                row, col = q.popleft()
                area += 1
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r >= 0) and (r < R) and (c >= 0) and (c < C) and (grid[r][c]==1) and ((r, c) not in visited):
                        visited.add((r, c))
                        q.append((r, c))
            return area

        for r in range(R):
            for c in range(C):
                if (grid[r][c] == 1) and ((r, c) not in visited):
                    max_area = max(max_area, bfs(r, c, R, C))
        
        return max_area