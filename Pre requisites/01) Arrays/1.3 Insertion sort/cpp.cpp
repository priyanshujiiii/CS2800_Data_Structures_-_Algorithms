#include <iostream>
#include <vector>

void insertionSort(std::vector<int>& arr) {
    for (int i = 1; i < arr.size(); i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
    std::vector<int> arr = {5, 2, 8, 12, 1, 6, 3};
    insertionSort(arr);

    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}

//In the code above, the insertionSort function takes a reference to a vector of integers (std::vector<int>& arr) and performs the insertion sort algorithm on it. The outer loop iterates over each element starting from the second element (index 1). The variable key stores the current element being considered for insertion. The inner loop compares the key with the elements on its left and shifts them one position to the right if they are greater than the key. Finally, the key is inserted in its correct position.

//The main function demonstrates how to use the insertionSort function on a sample vector arr. After sorting the vector, it prints the sorted elements to the console.
