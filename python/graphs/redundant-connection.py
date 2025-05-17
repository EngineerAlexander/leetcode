# In this problem, a tree is an undirected graph 
# that is connected and has no cycles.

# You are given a graph that started as a tree with n 
# nodes labeled from 1 to n, with one additional edge 
# added. The added edge has two different vertices 
# chosen from 1 to n, and was not an edge that already 
# existed. The graph is represented as an array edges 
# of length n where edges[i] = [ai, bi] indicates that 
# there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting 
# graph is a tree of n nodes. If there are multiple answers, 
# return the answer that occurs last in the input.

# Constraints:
# There are no repeated edges.
# The given graph is connected.

# Note: A tree is generally connected and doesn't have cycles.
# Identify all the edges that belong to the cycle and return the last one.

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """"DFS Optimal"""
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = [False] * (n + 1)
        cycle = set()
        cycleStart = -1
        
        def dfs(node, par):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True  
            
            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
        
        dfs(1, -1)
        
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """"Union Find Optimal"""
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

# First Solution Complexity
# Time complexity: O(N + E) where N is the number of nodes and E is the number of edges.
# Space complexity: O(N + E) the graph itself uses this

# Second Solution Complexity
# Time complexity: O(N + E) where N is the number of nodes and E is the number of edges.
# Space complexity: O(N)