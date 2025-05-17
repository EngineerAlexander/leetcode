# You are part of a university admissions office and need to keep 
# track of the kth highest test score from applicants in real-time. 
# This helps to determine cut-off marks for interviews and admissions 
# dynamically as new applicants submit their scores.

# You are tasked to implement a class which, for a given integer k, 
# maintains a stream of test scores and continuously returns the kth 
# highest test score after a new score has been submitted. More 
# specifically, we are looking for the kth highest score in the 
# sorted list of all scores.

# Implement the KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer 
# k and the stream of test scores nums.
# int add(int val) Adds a new test score val to the stream and returns 
# the element representing the kth largest element in the pool of test 
# scores so far.

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        for _ in range(len(nums) - k):
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]

# Time complexity:
# init: O(n) for heapify, pop n-k times and that pop operation takes O(log(n)) for heap of size n,
# Init: O(nlogn)
# Add: O(log(k)) for add operation on heap of size k. Note that getting min is constant time