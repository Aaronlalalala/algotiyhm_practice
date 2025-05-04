
#pragma once
#ifndef MERGE_SORT_H
#define MERGE_SORT_H

// in_place quick sort 
// Top down & Bottom up 
// �D�n���O�ϥ�left & right => �|�ݭnswap 
void merge_sort_top_down(float arr[], int low, int high);

// Bottom-up Merge Sort (���N�k)
void merge_sort_bottom_up(float arr[], int n);

// �����ӱƧǵ��G
bool arrays_equal_merge(float arr1[], float arr2[], int n);

// ���q�ƧǮɶ��ä��
void sort_and_measure_merge(float arr[], int n);

#endif