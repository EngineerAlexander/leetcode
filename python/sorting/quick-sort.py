# Functional (Not-in-place) QuickSort
def quicksort(arr):
    # Bases case
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

# Time complexity: O(n log n) on average, O(n^2) in the worst case
# Space complexity: O(log n) for the call stack
# Note: The worst case occurs when the pivot is always the smallest or largest element.
# This can be avoided by using a randomized pivot or the median of three method.