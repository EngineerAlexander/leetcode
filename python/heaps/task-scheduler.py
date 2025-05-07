# You are given an array of CPU tasks, each labeled with a letter 
# from A to Z, and a number n. Each CPU interval can be idle or 
# allow the completion of one task. Tasks can be completed in 
# any order, but there's a constraint: there has to be a gap of 
# at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        freqs = [-x for x in counts.values()]
        heapq.heapify(freqs)

        wait = deque()

        time = 0

        while freqs or wait:
            time += 1
            if freqs:
                count = 1 + heapq.heappop(freqs)
                if n > 0:
                    wait.append((count, time + n))
            if wait and wait[0][1] == time:
                heapq.heappush(freqs, wait.pop()[0])

        return time
    
# Time complexity: O(n log 26). Notice popping and pushing is a constant in this problem
# Space complexity: O(n) for the counts, freqs, and wait