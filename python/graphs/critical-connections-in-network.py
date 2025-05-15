# There are n servers numbered from 0 to n - 1 connected by 
# undirected server-to-server connections forming a network 
# where connections[i] = [ai, bi] represents a connection 
# between servers ai and bi. Any server can reach other servers 
# directly or indirectly through the network.

# A critical connection is a connection that, if removed, 
# will make some servers unable to reach some other server.

# Return all critical connections in the network in any order.


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Step 1: Build the graph as an adjacency list
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        # Step 2: Initialize discovery and low-link arrays
        disc = [-1] * n  # Discovery time of each node
        low = [-1] * n   # Lowest discovery time reachable from subtree
        time = 0         # Global time counter (using list to pass by reference)
        res = []         # List to store the bridges (critical connections)

        def dfs(node: int, parent: int):
            nonlocal time
            # Set the discovery and low time
            disc[node] = time
            low[node] = time

            time += 1

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # Don't revisit the parent

                if disc[neighbor] == -1:
                    # If neighbor has not been visited, recurse on it
                    dfs(neighbor, node)
                    # After dfs, update low time
                    low[node] = min(low[node], low[neighbor])

                    # If the lowest reachable time from neighbor is greater than discovery time of current node,
                    # then this edge is a bridge (critical connection)
                    if low[neighbor] > disc[node]:
                        res.append([node, neighbor])
                else:
                    # If neighbor already visited, minimize low[node] using neighbor's discovery time
                    low[node] = min(low[node], disc[neighbor])

        # Start DFS from node 0 (or any node), assuming the graph is connected
        dfs(0, -1)
        return res
    
# Time complexity: O(V + E) where V is the number of vertices and E is the number of edges
# Space complexity: O(V + E) for the graph representation and O(V) for the discovery and low-link arrays