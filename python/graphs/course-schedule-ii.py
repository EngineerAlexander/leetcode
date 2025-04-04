# There are a total of numCourses courses you have to take, 
# labeled from 0 to numCourses - 1. You are given an array 
# prerequisites where prerequisites[i] = [ai, bi] indicates 
# that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you 
# have to first take course 1.
# Return the ordering of courses you should take to finish all courses. 
# If there are many valid answers, return any of them. If it is impossible 
# to finish all courses, return an empty array.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        order = []
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED]*numCourses

        def dfs(course):
            if states[course] == VISITED:
                return True
            elif states[course] == VISITING:
                return False
            
            states[course] = VISITING
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            states[course] = VISITED
            order.append(course)
            return True


        for course in range(numCourses):
            if not dfs(course):
                return []

        return order