# Given an m x n 2D binary grid grid which represents a map of 
# '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting 
# adjacent lands horizontally or vertically. You may assume all 
# four edges of the grid are all surrounded by water.

# Constraints:
# grid[i][j] is '0' or '1'.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Iterate over every node, if it is 1 and not visited yet, 
        increment island counter then bfs starting there to touch all nodes that are 1 
        and on same island. Return counter value.
        """
        def bfs(r, c, R, C):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r >= 0) and (r < R) and (c >= 0) and (c < C) and grid[r][c]=="1" and ((r, c) not in visited):
                        queue.append((r, c))
                        visited.add((r, c))
        visited = set()
        R = len(grid)
        C = len(grid[0])

        num_islands = 0
        for r in range(R):
            for c in range(C):
                if ((r,c) not in visited) and (grid[r][c]=="1"):
                    num_islands += 1
                    bfs(r, c, R, C)

        return num_islands

# Time complexity: O(n*m) to visit every node
# Space complexity: O(n*m) worst case for the queue