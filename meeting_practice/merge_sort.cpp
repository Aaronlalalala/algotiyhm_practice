#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "merge_sort.h"

// 合併函式，將兩個已經排序的部分合併成一個有序陣列
void merge(float arr[], int low, int mid, int high) {
    int n1 = mid - low + 1;
    int n2 = high - mid;

    float* left = (float*)malloc(n1 * sizeof(float));
    float* right = (float*)malloc(n2 * sizeof(float));

    for (int i = 0; i < n1; i++)
        left[i] = arr[low + i];
    for (int j = 0; j < n2; j++)
        right[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = low;
    while (i < n1 && j < n2) {
        if (left[i] <= right[j]) {
            arr[k++] = left[i++];
        }
        else {
            arr[k++] = right[j++];
        }
    }

    while (i < n1) {
        arr[k++] = left[i++];
    }
    while (j < n2) {
        arr[k++] = right[j++];
    }

    free(left);
    free(right);
}

// Top-down Merge Sort 
void merge_sort_top_down(float arr[], int low, int high) {
    if (low < high) {
        int mid = low + (high - low) / 2;
        merge_sort_top_down(arr, low, mid);
        merge_sort_top_down(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }
}

// Bottom-up Merge Sort 
void merge_sort_bottom_up(float arr[], int n) {
    for (int size = 1; size < n; size *= 2) {
        for (int low = 0; low < n - size; low += 2 * size) {
            int mid = low + size - 1;
            int high = (low + 2 * size - 1 < n) ? (low + 2 * size - 1) : (n - 1);
            merge(arr, low, mid, high);
        }
    }
}

bool arrays_equal_merge(float arr1[], float arr2[], int n) {
    for (int i = 0; i < n; i++) {
        if (arr1[i] != arr2[i]) {
            return false;  
        }
    }
    return true;  
}


void sort_and_measure_merge(float arr[], int n) {
   
    float* arr_top_down = (float*)malloc(n * sizeof(float));
    float* arr_bottom_up = (float*)malloc(n * sizeof(float));

    
    for (int i = 0; i < n; i++) {
        arr_top_down[i] = arr[i];
        arr_bottom_up[i] = arr[i];
    }

    clock_t start_time = clock();
    merge_sort_top_down(arr_top_down, 0, n - 1);
    clock_t end_time = clock();
    double time_taken_top_down = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    start_time = clock();
    merge_sort_bottom_up(arr_bottom_up, n);
    end_time = clock();
    double time_taken_bottom_up = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    
    printf("Time taken to merge sort (top-down): %f seconds\n", time_taken_top_down);
    printf("Time taken to merge sort (bottom-up): %f seconds\n", time_taken_bottom_up);

    
    if (arrays_equal_merge(arr_top_down, arr_bottom_up, n)) {
        printf("All sorting methods produced the same result.\n");
    }
    else {
        printf("Sorting methods produced different results.\n");
    }

    free(arr_top_down);
    free(arr_bottom_up);
}
