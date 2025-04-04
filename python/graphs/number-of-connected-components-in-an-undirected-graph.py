# You have a graph of n nodes. You are given an integer 
# n and an array edges where edges[i] = [ai, bi] indicates 
# that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

# Constraints:
# There are no repeated edges.

# Solution with DFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            stack = [node]
            while stack:
                cur = stack.pop()
                visited.add(cur)
                for neighbor in reversed(graph[cur]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count
    
# Solution with Union Find
