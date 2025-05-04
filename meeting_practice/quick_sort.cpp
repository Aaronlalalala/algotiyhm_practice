#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "quick_sort.h"

void swap(float* a, float* b) {
    float temp = *a;
    *a = *b;
    *b = temp;
}

// partition 
int partition(float arr[], int low, int high) {
    float pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

// Recursive version of quicksort
void quick_sort_INPLACE(float arr[], int low, int high) {
    if (low < high) {
        int pivot_index = partition(arr, low, high);
        quick_sort_INPLACE(arr, low, pivot_index - 1);
        quick_sort_INPLACE(arr, pivot_index + 1, high);
    }
}

// Iterative (stack-based) version of quicksort
void quick_sort_STACK(float arr[], int low, int high) {
    int* stack = (int*)malloc((high - low + 1) * sizeof(int));  
    int top = -1;

    stack[++top] = low;
    stack[++top] = high;

    while (top >= 0) {
        high = stack[top--];
        low = stack[top--];

        int pivot_index = partition(arr, low, high);

        // 
        if (pivot_index - 1 > low) {
            stack[++top] = low;
            stack[++top] = pivot_index - 1;
        }
        if (pivot_index + 1 < high) {
            stack[++top] = pivot_index + 1;
            stack[++top] = high;
        }
    }
    free(stack);  
}

// result check 
bool arrays_equal(float arr1[], float arr2[], int n) {
    for (int i = 0; i < n; i++) {
        if (arr1[i] != arr2[i]) {
            return false;  
        }
    }
    return true;  
}

// 
void sort_and_measure_quick(float arr[], int n) {
    
    float* arr_inplace = (float*)malloc(n * sizeof(float));
    float* arr_stack = (float*)malloc(n * sizeof(float));

    for (int i = 0; i < n; i++) {
        arr_inplace[i] = arr[i];
        arr_stack[i] = arr[i];
    }

    clock_t start_time = clock();
    quick_sort_INPLACE(arr_inplace, 0, n - 1);
    clock_t end_time = clock();
    double time_taken_r = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    
    start_time = clock();
    quick_sort_STACK(arr_stack, 0, n - 1);
    end_time = clock();
    double time_taken_s = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    /*printf("Sorted array: \n");
    print_array(arr_stack, n);*/

    /*printf("Sorted array: \n");
    print_array(arr_inplace, n);*/

    // Display the sorting times
    printf("Time taken to quick sort (in-place): %f seconds\n", time_taken_r);
    printf("Time taken to quick sort (stack-based): %f seconds\n", time_taken_s);

    if (arrays_equal(arr_inplace, arr_stack, n)) {
        printf("Both sorting methods produced the same result.\n");
    }
    else {
        printf("Sorting methods produced different results.\n");
    }

    free(arr_inplace);
    free(arr_stack);
}
