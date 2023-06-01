//Binary search

#include <iostream>
#include <vector>

int binarySearch(const std::vector<int>& array, int target) {
    int low = 0;
    int high = array.size() - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (array[mid] == target) {
            return mid;  // Return the index of the target element
        } else if (array[mid] < target) {
            low = mid + 1;  // Discard the left half of the array
        } else {
            high = mid - 1;  // Discard the right half of the array
        }
    }

    return -1;  // Return -1 if the target element is not found
}

int main() {
    std::vector<int> myArray = {1, 2, 3, 4, 5, 6};
    int targetElement = 4;

    int result = binarySearch(myArray, targetElement);

    if (result != -1) {
        std::cout << "Element " << targetElement << " found at index " << result << "." << std::endl;
    } else {
        std::cout << "Element " << targetElement << " not found in the array." << std::endl;
    }

    return 0;
}
