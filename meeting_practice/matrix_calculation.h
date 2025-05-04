#pragma once
#ifndef MATRIX_CALCULATION_H 
#define MATRIX_CALCULATION_H 

void generate_matrices(float* a, float* b, int row_a, int col_a, int row_b, int col_b);
void matrix_multiply_single_thread(float* a, float* b, float* c, int row_a, int col_a, int row_b, int col_b);
void* matrix_multiply_thread(void* arg);
void matrix_multiply_multi_thread(float* a, float* b, float* c, int row_a, int col_a, int row_b, int col_b);
int matrices_equal(float* c1, float* c2, int rows, int cols);
void print_matrix(float* m, int rows, int cols);
#endif
