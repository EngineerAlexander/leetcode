# Heaps (ONLY IMPLEMENTED AS A MIN HEAP IN PYTHON)
# Note: To fake max heap, multipy everything by -1 first

import heapq

test = [1, 2, 3, 4]

# Time complexity O(n)
heapq.heapify([test])

# Time complexity O(log(n))
# pops minimum element
heapq.heappop(test)

# Time complexity O(log(n))
heapq.heappush(test, 5)

# Time complexity O(1)
# Get minimum element
test[-1]





# Default Dicts
from collections import defaultdict
test = defaultdict(int) # initializes to zero
# Note can also use list, set, str, lambda...





# Counters
from collections import Counter
test = Counter(['a', 'b', 'a', 'c'])
test = Counter("abac")
# Can also use on a dict

# functions in map
operator_map = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: int(a / b)
    }

# Getting out of dict with a default value
s1_count = {}
s1 = "abcde"
s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)

# Sorting by certain key
points = [[1, 2], [3, 4], [5, 6]]
points.sort(key = lambda x: x[1])