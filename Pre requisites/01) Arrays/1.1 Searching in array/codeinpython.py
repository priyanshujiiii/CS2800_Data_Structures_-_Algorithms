# code for binary search

def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid  # Return the index of the target element
        elif array[mid] < target:
            low = mid + 1  # Discard the left half of the array
        else:
            high = mid - 1  # Discard the right half of the array

    return -1  # Return -1 if the target element is not found

# Example usage
my_array = [1, 2, 3, 4, 5, 6]
target_element = 4

result = binary_search(my_array, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the array.")
