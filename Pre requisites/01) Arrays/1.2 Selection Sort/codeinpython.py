# Selection sort

def selection_sort(array):
    n = len(array)

    for i in range(n):
        min_index = i

        # Find the minimum element in the unsorted part of the array
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the minimum element with the first unsorted element
        array[i], array[min_index] = array[min_index], array[i]

    return array

# Example usage
my_array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(my_array)
print("Sorted array:", sorted_array)
