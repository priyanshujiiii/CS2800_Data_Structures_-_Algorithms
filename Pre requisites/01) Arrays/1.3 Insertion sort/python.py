def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [5, 2, 8, 12, 1, 6, 3]
insertion_sort(arr)
print(arr)


#In the code above, the insertion_sort function takes an input list arr and performs the insertion sort algorithm on it. The outer loop iterates over each element starting from the second element (index 1). The variable key stores the current element being considered for insertion. The inner loop compares the key with the elements on its left and shifts them one position to the right if they are greater than the key. Finally, the key is inserted in its correct position.
#The example usage demonstrates how to use the insertion_sort function on a sample list arr. After sorting the list, it prints the sorted list to the console.
#Please note that the insertion_sort function modifies the input list in-place. If you want to keep the original list intact, you can make a copy before sorting by using sorted_arr = arr.copy() and sorting sorted_arr instead.
