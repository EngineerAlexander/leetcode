def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge the sorted halves.
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0
    
    # Merge the two lists by comparing their elements.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Append any remaining elements from left and right.
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# Time complexity: O(n log n) for all cases
# Space complexity: O(n) for the temporary arrays used in merging
# Note: Merge sort is stable and works well for linked lists as well.