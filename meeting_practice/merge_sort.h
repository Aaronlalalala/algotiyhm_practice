
#pragma once
#ifndef MERGE_SORT_H
#define MERGE_SORT_H

// in_place quick sort 
// Top down & Bottom up 
// 主要都是使用left & right => 會需要swap 
void merge_sort_top_down(float arr[], int low, int high);

// Bottom-up Merge Sort (迭代法)
void merge_sort_bottom_up(float arr[], int n);

// 比較兩個排序結果
bool arrays_equal_merge(float arr1[], float arr2[], int n);

// 測量排序時間並比較
void sort_and_measure_merge(float arr[], int n);

#endif