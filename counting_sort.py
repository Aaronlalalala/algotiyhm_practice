# -*- coding: utf-8 -*-
"""
Created on Sat May  3 21:12:47 2025

@author: YangAaron
"""

# 匯入需要的套件
import numpy as np                 # 用來產生隨機整數陣列（比 random 快）
import random as rd                # 如果要用 random 模組也可以，但這裡用 numpy
import time                        # 用來計時排序的執行時間

# counting sort 可分為兩種 不穩定以及穩地的版本
def counting_sort_unstable(arr):
    if not arr:
        return []
    max_value = max(arr)
    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1

    return arr


def counting_sort_stable(arr):
    if not arr:
        return []  # 如果輸入是空的，直接回傳空陣列

    max_value = max(arr)  # 找到陣列裡的最大值
    count = [0] * (max_value + 1)  # 建立計數陣列，大小為最大值 + 1，全初始為 0

    # 第一步：計算每個數字出現的次數
    for num in arr:
        count[num] += 1

    # 第二步：轉換為「累計位置」
    # count[i] 變成「小於等於 i 的數字共有幾個」
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    # 例子：
    # 如果 count[2] == 5，表示數字 2 最後一個會放在 index 4
    # 因為 index 是從 0 開始算

    # 第三步：建立輸出陣列，準備放穩定排序結果
    output = [0] * len(arr)

    # 第四步：從右往左放回（為了保留相同元素的相對順序）
    for i in reversed(range(len(arr))):  # i 從 len(arr)-1 到 0
        num = arr[i]                     # 取出目前的數字
        count[num] -= 1                  # 找到它該放的位置（index = count[num] - 1）
        output[count[num]] = num         # 把它放進 output 陣列

    return output  # 回傳排序好的穩定結果




# 主程式
def main():
    # 產生隨機測試資料：0 ~ 1000 的整數，共 1000 個
    # 注意 numpy 產生的是 numpy array，要用 .tolist() 轉成 list 才能傳入 counting_sort
    counting_data = np.random.randint(0, 1001, size=100000).tolist()

    # 不穩定版
    start = time.time()
    unstable_result = counting_sort_unstable(counting_data.copy())
    unstable_time = time.time() - start
    print(f"Unstable counting sort time: {unstable_time:.6f} s")

    # 穩定版
    start = time.time()
    stable_result = counting_sort_stable(counting_data.copy())
    stable_time = time.time() - start
    print(f"Stable counting sort time: {stable_time:.6f} s")


    return 0


# 確保程式是直接執行（不是被匯入其他檔案時）才會跑 main()
if __name__ == "__main__":
    main()
