def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append the remaining elements
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Example usage:
arr = [5, 2, 8, 12, 1, 6, 3]
sorted_arr = merge_sort(arr)
print(sorted_arr)



#In the code above, the merge_sort function implements the Merge Sort algorithm. It recursively divides the input array into two halves until each subarray has only one element. Then, it merges the sorted subarrays back together using the merge function.
#The merge function takes two sorted arrays (left and right) and merges them into a single sorted array. It compares the elements from both arrays and appends them to the merged list in ascending order.
#The example usage demonstrates how to use the merge_sort function on a sample list arr. It assigns the sorted result to sorted_arr and prints it to the console.
#Note that the original arr is not modified, and a new sorted list is returned.
