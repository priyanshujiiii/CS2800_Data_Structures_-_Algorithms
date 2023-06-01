// Selection sort

#include <iostream>
#include <vector>

void selectionSort(std::vector<int>& array) {
    int n = array.size();

    for (int i = 0; i < n - 1; ++i) {
        int min_index = i;

        // Find the minimum element in the unsorted part of the array
        for (int j = i + 1; j < n; ++j) {
            if (array[j] < array[min_index]) {
                min_index = j;
            }
        }

        // Swap the minimum element with the first unsorted element
        std::swap(array[i], array[min_index]);
    }
}

int main() {
    std::vector<int> myArray = {64, 25, 12, 22, 11};

    selectionSort(myArray);

    std::cout << "Sorted array: ";
    for (int num : myArray) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
