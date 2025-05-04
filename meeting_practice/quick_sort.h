#pragma once
#ifndef QUICK_SORT_H
#define QUICK_SORT_H

// in_place quick sort 
// stack ���� & ���j����
// �D�n���O�ϥ�left & right => �|�ݭnswap 

void quick_sort_INPLACE(float arr[], int low, int high);
void quick_sort_STACK(float arr[], int low, int high);
bool arrays_equal(float arr1[], float arr2[], int n);
void sort_and_measure_quick(float arr[], int n);
#endif