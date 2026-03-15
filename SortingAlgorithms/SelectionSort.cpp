#include <vector>

using namespace std;

void selectionSort(vector<int>& arr) {
    int n = arr.size();
    int temp;
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        temp =  arr[minIndex];
        arr[minIndex] = arr[i];
        arr[i] = temp;
    }
}
