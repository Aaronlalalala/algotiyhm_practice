import numpy as np
import threading
import math
import time
import tkinter as tk
from tkinter import scrolledtext

def generate_matrices():
    row_a, col_a = 50, 80
    row_b, col_b = 80, 50
    a = np.zeros((row_a, col_a))
    b = np.zeros((row_b, col_b))
    for i in range(row_a):
        for j in range(col_a):
            a[i, j] = 10 * math.sin(i) - 0.6 * j
    for i in range(row_b):
        for j in range(col_b):
            b[i, j] = 7 - 12 * math.cos(5 * j) + 1.8 * i
    return a, b

def matmul_single_thread(a, b):
    result = np.zeros((a.shape[0], b.shape[1]))
    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            for k in range(a.shape[1]):
                result[i, j] += a[i, k] * b[k, j]
    return result

def matmul_thread_cell_based(a, b):
    result = np.zeros((a.shape[0], b.shape[1]))
    threads = []
    def compute_cell(i, j):
        for k in range(a.shape[1]):
            result[i, j] += a[i, k] * b[k, j]
    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            t = threading.Thread(target=compute_cell, args=(i, j))
            threads.append(t)
            t.start()
    for t in threads:
        t.join()
    return result

def matmul_thread_row_based(a, b):
    result = np.zeros((a.shape[0], b.shape[1]))
    threads = []
    def compute_row(i):
        for j in range(b.shape[1]):
            for k in range(a.shape[1]):
                result[i, j] += a[i, k] * b[k, j]
    for i in range(a.shape[0]):
        t = threading.Thread(target=compute_row, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return result

def matmul_thread_block_based(a, b, row_blocks=5, col_blocks=2):
    result = np.zeros((a.shape[0], b.shape[1]))
    threads = []
    row_step = a.shape[0] // row_blocks
    col_step = b.shape[1] // col_blocks
    def compute_block(row_start, row_end, col_start, col_end):
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                for k in range(a.shape[1]):
                    result[i, j] += a[i, k] * b[k, j]
    for i in range(row_blocks):
        for j in range(col_blocks):
            r_start = i * row_step
            r_end = (i + 1) * row_step if i != row_blocks - 1 else a.shape[0]
            c_start = j * col_step
            c_end = (j + 1) * col_step if j != col_blocks - 1 else b.shape[1]
            t = threading.Thread(target=compute_block, args=(r_start, r_end, c_start, c_end))
            threads.append(t)
            t.start()
    for t in threads:
        t.join()
    return result

def format_matrix(matrix, size=5):
    sub = matrix[:size, :size]
    return "\n".join(["\t".join([f"{v:.2f}" for v in row]) for row in sub])

def run_calculations(output_widget):
    a, b = generate_matrices()

    output_widget.delete(1.0, tk.END)

    start = time.time()
    r1 = matmul_single_thread(a, b)
    t1 = time.time() - start
    output_widget.insert(tk.END, f"🟩 單執行緒: {t1:.4f} 秒\n")

    start = time.time()
    r2 = matmul_thread_cell_based(a, b)
    t2 = time.time() - start
    match2 = np.allclose(r1, r2)
    output_widget.insert(tk.END, f"🟥 Cell-based (50x50 threads): {t2:.4f} 秒 | 一致：{match2}\n")

    start = time.time()
    r3 = matmul_thread_row_based(a, b)
    t3 = time.time() - start
    match3 = np.allclose(r1, r3)
    output_widget.insert(tk.END, f"🟨 Row-based (50 threads): {t3:.4f} 秒 | 一致：{match3}\n")

    start = time.time()
    r4 = matmul_thread_block_based(a, b, 5, 2)
    t4 = time.time() - start
    match4 = np.allclose(r1, r4)
    output_widget.insert(tk.END, f"🟦 Block-based (5x2 threads): {t4:.4f} 秒 | 一致：{match4}\n\n")

    output_widget.insert(tk.END, "前 5x5 結果矩陣 (單執行緒):\n")
    output_widget.insert(tk.END, format_matrix(r1))

def create_gui():
    window = tk.Tk()
    window.title("矩陣乘法計算比較")
    window.geometry("600x500")

    label = tk.Label(window, text="按下按鈕執行矩陣乘法並比較各種多執行緒時間")
    label.pack(pady=10)

    run_button = tk.Button(window, text="開始計算", command=lambda: run_calculations(output_area))
    run_button.pack(pady=10)

    output_area = scrolledtext.ScrolledText(window, width=70, height=20)
    output_area.pack(padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
