def insertion_sort(arr):
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        # The current element to be inserted in the sorted portion
        key = arr[i]
        # Prev
        j = i - 1
        
        # Shift elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key into its correct position
        arr[j + 1] = key
    return arr

# Time complexity: O(n^2) in the worst case, O(n) in the best case (when the array is already sorted)
# In practice, very good for nearly sorted arrays
# Space complexity: O(1) since it sorts the array in place
