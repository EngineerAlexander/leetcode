# You are given an m x n grid rooms initialized 
# with these three possible values.
# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 
# 231 - 1 = 2147483647 to represent INF as you may assume 
# that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. 
# If it is impossible to reach a gate, it should be filled with INF.

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []

        R = len(rooms)
        C = len(rooms[0])
        q = collections.deque()

        # Add all gates to FIFO queue
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    q.append((r,c))

        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        while q:
            x, y = q.popleft()
            # Since started at all gates
            distance = rooms[x][y]+1
            for dx, dy in dirs:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<R and 0<=new_y<C and rooms[new_x][new_y] == 2147483647:
                    rooms[new_x][new_y] = distance
                    q.append((new_x, new_y))

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        def bfs(r, c, R, C):
            visited = set()
            q = deque()
            q.append((r, c, 0))

            while q:
                r, c, l = q.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (0 <= row < R and 0 <= col < C and 
                        rooms[row][col] != -1 and rooms[row][col] != 0):
                        
                        if rooms[row][col] > l + 1:
                            rooms[row][col] = l + 1
                            q.append((row, col, l + 1))

        R = len(rooms)
        C = len(rooms[0])

        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    bfs(r, c, R, C)