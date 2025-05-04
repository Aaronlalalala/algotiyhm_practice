#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "counting_sort.h"

// Counting Sort 實作，處理負數範圍
void counting_sort(int arr[], int n, int min, int max) {
    int range = max - min + 1;
    int* count = (int*)calloc(range, sizeof(int));
    int* output = (int*)malloc(n * sizeof(int));

    // 採用數值偏移 允許counting sort排序負整數
    for (int i = 0; i < n; i++) {
        count[arr[i] - min]++;
    }

    for (int i = 1; i < range; i++) {
        count[i] += count[i - 1];
    }

    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i] - min] - 1] = arr[i];
        count[arr[i] - min]--;
    }

    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }

    free(count);
    free(output);
}

void print_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void sort_and_measure(int arr[], int n, int min, int max) {
    clock_t start_time = clock();
    counting_sort(arr, n, min, max);
    clock_t end_time = clock();

    double time_taken = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    /*printf("Sorted array: \n");
    print_array(arr, n);*/

    printf("Time taken to sort: %f seconds\n", time_taken);
}
