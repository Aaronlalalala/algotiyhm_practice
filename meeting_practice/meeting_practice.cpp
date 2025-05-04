
#include <iostream>
#include <stdio.h>
#include "merge_sort.h"
#include "quick_sort.h"
#include "counting_sort.h"
#include "matrix_calculation.h"
#include "polynomial_sum.h"

#include <stdlib.h>  // malloc 分配陣列
#include <math.h> // 矩陣運算
#include <time.h> // 計算排序演算法時間

using namespace std;
#define _CRT_SECURE_NO_WARNINGS

int main()
{
    // 執行各種程式碼
    // polynomial_sum 
    int N;
    int result;
    printf("Enter N: \n");
    while (scanf_s("%d", &N) != 1) {
        while (getchar() != '\n') {
            printf("Invalid input. Please enter integer again !\n");
        }
    }
    result = calculation_polynomail_sum(N);
    printf("Polynomial sum result : %d\n", result);
    
    // sorting algorithm  排序演算法
    printf("\n-------------------------------------\n");
    printf("\nSorting_algorithm:\n");
    
    int sort_number = 100000; 
    int min_value = -10000;  
    int max_value = 10000;    

    // counting sort  使用整數排列 => 允許負數
    int* arr = (int*)malloc(sort_number * sizeof(int));
    for (int i = 0; i < sort_number; i++) {
        arr[i] = int(rand() % (max_value - min_value + 1)) + min_value; 
    }
    sort_and_measure(arr, sort_number, min_value, max_value);
    free(arr);
    printf("\n-------------------------------------\n");

    // merge sort & quick sort 
    
    float* arr2 = (float*)malloc(sort_number * sizeof(float));
    for (int i = 0; i < sort_number; i++) {
        arr2[i] = float(rand() % (max_value - min_value + 1)) + min_value;
    }
    sort_and_measure_quick(arr2, sort_number);
    printf("\n-------------------------------------\n");
    sort_and_measure_merge(arr2, sort_number);
    free(arr2);

    // matrix calculation 
    printf("\n-------------------------------------\n");
    printf("\nMatrix calculation:\n");
    int row_a, col_a, row_b, col_b;
    printf("Enter the row of matrix A: ");
    scanf_s("%d", &row_a);
    printf("Enter the col of matrix A: ");
    scanf_s("%d", &col_a);
    printf("Enter the row of matrix B: ");
    scanf_s("%d", &row_b);
    printf("Enter the col of matrix B: ");
    scanf_s("%d", &col_b);
    // 如果row col of a & b不能進行乘法相乘 則重新輸入
    if (col_a != row_b) {
        printf("Matrix multiplication not possible. Number of columns of A must be equal to number of rows of B.\n");
        return -1;
    }
    // 生成矩陣
    float* a = (float*)malloc(row_a * col_a * sizeof(float));
    float* b = (float*)malloc(row_b * col_b * sizeof(float));
    float* c_single = (float*)malloc(row_a * col_b * sizeof(float));
    float* c_multi = (float*)malloc(row_a * col_b * sizeof(float));
    // 填充矩陣資訊
    generate_matrices(a, b, row_a, col_a, row_b, col_b);

    // Block thread => 看 a * b = c => 看matrix c 的row, col 找最大公因數 並實施該thread number 
    clock_t start_time = clock();
    matrix_multiply_single_thread(a, b, c_single, row_a, col_a, row_b, col_b);
    clock_t end_time = clock();
    double time_single = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    // multi thread
    start_time = clock();
    matrix_multiply_multi_thread(a, b, c_multi, row_a, col_a, row_b, col_b);
    end_time = clock();
    double time_multi = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    // 運算結果比較
    printf("\nSingle-threaded multiplication time: %f seconds\n", time_single);
    printf("Multi-threaded multiplication time: %f seconds\n", time_multi);

    if (matrices_equal(c_single, c_multi, row_a, col_b)) {
        printf("Both single-threaded and multi-threaded results are the same.\n");
    }
    else {
        printf("Results are different!\n");
    }

    // print_matrix(c_single, row_a, col_b);
    // print_matrix(c_multi, row_a, col_b);

    free(a);
    free(b);
    free(c_single);
    free(c_multi);

    
}

