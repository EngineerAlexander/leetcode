# You have a graph of n nodes labeled from 0 to n - 1. 
# You are given an integer n and a list of edges where 
# edges[i] = [ai, bi] indicates that there is an undirected 
# edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid 
# tree, and false otherwise.

# Constraints:
# There are no self-loops or repeated edges.

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if we can reach all the nodes and there are no cycles in the graph then we are a valid tree
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
    
# Time complexity: O(N + E) where N is the number of nodes and E is the number of edges.
# We go through every node and then visit every edge only twice since we are keeping track of the visited nodes.
# and graph is undirected.
# Space complexity: O(N + E) the graph itself uses this