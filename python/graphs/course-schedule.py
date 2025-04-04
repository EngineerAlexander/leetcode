# There are a total of numCourses courses you have to take, 
# labeled from 0 to numCourses - 1. You are given an array 
# prerequisites where prerequisites[i] = [ai, bi] indicates 
# that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you 
# have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Turn into adjacency list, see if it is possible to take every node, keep history of which nodes are possible, if we see a node we are currently checking again, we are in a loop, return false.
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED]*numCourses

        def dfs(course):
            if states[course] == VISITED:
                return True
            if states[course] == VISITING:
                return False

            states[course] = VISITING

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            states[course] = VISITED
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
    
# Time complexity: O(N + E) where N is the number of nodes and E is the number of edges.
# We go through every node and then only visit every edge once since we are keeping track of the visited nodes.
# Space complexity: O(N + E) the adjacency list