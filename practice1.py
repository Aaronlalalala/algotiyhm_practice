# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 10:17:17 2025

@author: YangAaron
"""

def test1(N1):
    result = 0  # 初始化 result 變數
    for N in range(1, N1 + 1):  # 注意這裡改為 N1 + 1，因為 range 不包含結束值
        if N % 2 != 0:  # 奇數
            result += N
        else:  # 偶數
            result -= N
    
    return result  # 將 return 移出循環外
    
def main():
    N1 = eval(input("Print the number you want to calculate: "))
    result = test1(N1)  # 保存返回值
    print("結果是:", result)  # 打印結果

# 調用 main 函數
main()