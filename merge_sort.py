# -*- coding: utf-8 -*-
"""
Created on Sat May  3 21:33:00 2025

@author: YangAaron
"""

# time complexity O(n log n)
# top-down (遞迴法) & bottom-up (迭代法)

import numpy as np
import time

# Top-down (遞迴) Merge Sort
def merge_sort_topDown(arr):
    if len(arr) <= 1:
        return arr  

    mid = len(arr) // 2
    left = merge_sort_topDown(arr[:mid])   # 遞迴排序左半邊
    right = merge_sort_topDown(arr[mid:])  # 遞迴排序右半邊

    return merge(left, right)  # 合併排序好的左右陣列

# Bottom-up (迭代) Merge Sort
def merge_sort_bottomUp(arr):
    width = 1
    n = len(arr)
    result = arr.copy()

    while width < n:
        for i in range(0, n, 2 * width):
            left = result[i:i + width]
            right = result[i + width:i + 2 * width]
            result[i:i + 2 * width] = merge(left, right)
        width *= 2

    return result

# 合併兩個已排序的陣列
def merge(left, right):
    result = []
    i = j = 0

    # 比較兩邊元素，較小的先放入 result
    while i < len(left) and j < len(right):
        # 
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 接回
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def main():
    merge_data = np.random.uniform(0, 1000, size=100000).tolist()

    # Top-down timing
    start_TD = time.time()
    sort_result_TD = merge_sort_topDown(merge_data.copy())
    merge_time_TD = time.time() - start_TD
    print(f"Merge sort time of top down: {merge_time_TD:.6f} s")

    # Bottom-up timing
    start_BU = time.time()
    sort_result_BU = merge_sort_bottomUp(merge_data.copy())
    merge_time_BU = time.time() - start_BU
    print(f"Merge sort time of bottom up: {merge_time_BU:.6f} s")

    return 0

if __name__ == "__main__":
    main()
