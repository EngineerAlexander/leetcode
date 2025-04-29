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