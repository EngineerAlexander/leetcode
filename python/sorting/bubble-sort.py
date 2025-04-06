def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Track if any swap happens
        swapped = False
        # Last i elements are already in place, so ignore them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Time complexity: O(n^2) in the worst and average case, O(n) in the best case (already sorted)
# Space complexity: O(1) as it only uses a few variables
# Note: Bubble sort is not efficient for large datasets and is mainly used for educational purposes.