# -*- coding: utf-8 -*-
"""
Created on Sat May  3 22:19:37 2025

@author: YangAaron
"""

# average case : O(n log n) 但相對是最快的
# worst case : pivot挑選偏遠 導致左右切分不均 O(n ^2)
import numpy as np
import random as rd
import time

# 非 in-place 版本（你原本的）
def quick_sort_non_inplace(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[rd.randint(0, len(arr) - 1)]  # 隨機選 pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_non_inplace(left) + middle + quick_sort_non_inplace(right)

# In-place 版本
def quick_sort_inplace(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot_index = rd.randint(low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # 把 pivot 移到最後

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def main():
    data_size = 100000
    quick_sort_data = np.random.uniform(0, 1000, size=data_size).tolist()

    # 非 in-place 測試
    start = time.time()
    quick_sort_result_non_inplace = quick_sort_non_inplace(quick_sort_data.copy())
    non_inplace_time = time.time() - start
    print(f"Non-inplace quick sort time: {non_inplace_time:.6f} s")

    # In-place 測試
    inplace_data = quick_sort_data.copy()
    start = time.time()
    quick_sort_inplace(inplace_data, 0, len(inplace_data) - 1)
    inplace_time = time.time() - start
    print(f"Inplace quick sort time: {inplace_time:.6f} s")

    return 0

if __name__ == "__main__":
    main()

