#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <windows.h>  

#define MAX_THREADS 4

void generate_matrices(float* a, float* b, int row_a, int col_a, int row_b, int col_b) {
    for (int i = 0; i < row_a; i++) {
        for (int j = 0; j < col_a; j++) {
            a[i * col_a + j] = 10 * sin(i) - 0.6 * j;
        }
    }

    for (int i = 0; i < row_b; i++) {
        for (int j = 0; j < col_b; j++) {
            b[i * col_b + j] = 7 - 12 * cos(5 * j) + 1.8 * i;
        }
    }
}

void matrix_multiply_single_thread(float* a, float* b, float* c, int row_a, int col_a, int row_b, int col_b) {
    for (int i = 0; i < row_a; i++) {
        for (int j = 0; j < col_b; j++) {
            c[i * col_b + j] = 0;
            for (int k = 0; k < col_a; k++) {
                c[i * col_b + j] += a[i * col_a + k] * b[k * col_b + j];
            }
        }
    }
}

// define data structure for matric calculation
typedef struct {
    int start_row;
    int end_row;
    float* a;
    float* b;
    float* c;
    int row_a;
    int col_a;
    int col_b;
} ThreadData;

// multi_thread 
DWORD WINAPI matrix_multiply_thread(LPVOID arg) {
    ThreadData* data = (ThreadData*)arg;
    for (int i = data->start_row; i < data->end_row; i++) {
        for (int j = 0; j < data->col_b; j++) {
            data->c[i * data->col_b + j] = 0;
            for (int k = 0; k < data->col_a; k++) {
                data->c[i * data->col_b + j] += data->a[i * data->col_a + k] * data->b[k * data->col_b + j];
            }
        }
    }
    return 0;
}

void matrix_multiply_multi_thread(float* a, float* b, float* c, int row_a, int col_a, int row_b, int col_b) {
    HANDLE threads[MAX_THREADS];
    ThreadData thread_data[MAX_THREADS];
    int rows_per_thread = row_a / MAX_THREADS;
    int extra_rows = row_a % MAX_THREADS;

    for (int i = 0; i < MAX_THREADS; i++) {
        thread_data[i].a = a;
        thread_data[i].b = b;
        thread_data[i].c = c;
        thread_data[i].row_a = row_a;
        thread_data[i].col_a = col_a;
        thread_data[i].col_b = col_b;
        thread_data[i].start_row = i * rows_per_thread;
        thread_data[i].end_row = (i + 1) * rows_per_thread;

        if (i == MAX_THREADS - 1) {
            thread_data[i].end_row += extra_rows;
        }

        threads[i] = CreateThread(NULL, 0, matrix_multiply_thread, (LPVOID)&thread_data[i], 0, NULL);
    }

    WaitForMultipleObjects(MAX_THREADS, threads, TRUE, INFINITE);

    for (int i = 0; i < MAX_THREADS; i++) {
        CloseHandle(threads[i]);
    }
}

int matrices_equal(float* c1, float* c2, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (c1[i * cols + j] != c2[i * cols + j]) {
                return 0;  
            }
        }
    }
    return 1;  
}

void print_matrix(float* m, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%.2f ", m[i * cols + j]);
        }
        printf("\n");
    }
}