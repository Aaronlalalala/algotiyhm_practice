import tkinter as tk
from tkinter import messagebox
import random as rd
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# -------- 排序演算法 --------
def counting_sort(arr):
    if not arr:
        return []
    max_value = max(arr)
    count = [0] * (max_value + 1)
    for num in arr:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    return output

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# -------- GUI 函數 --------
def run_sorts():
    # 資料生成
    counting_data = [rd.randint(0, 1000) for _ in range(1000)]
    merge_quick_data = [rd.uniform(-1000, 1000) for _ in range(1000)]
    
    # Counting Sort
    start = time.time()
    counting_result = counting_sort(counting_data.copy())
    counting_time = time.time() - start
    
    # Merge Sort
    start = time.time()
    merge_result = merge_sort(merge_quick_data.copy())
    merge_time = time.time() - start
    
    # Quick Sort
    start = time.time()
    quick_result = quick_sort(merge_quick_data.copy())
    quick_time = time.time() - start
    
    # 顯示前10筆
    messagebox.showinfo("排序結果 (前10筆)", 
        f"Counting Sort:\n{counting_result[:10]}\n\n"
        f"Merge Sort:\n{merge_result[:10]}\n\n"
        f"Quick Sort:\n{quick_result[:10]}"
    )
    
    # 畫圖
    draw_chart(counting_time, merge_time, quick_time)

def draw_chart(counting_time, merge_time, quick_time):
    fig, ax = plt.subplots(figsize=(6, 4))
    sorts = ['Counting Sort', 'Merge Sort', 'Quick Sort']
    times = [counting_time, merge_time, quick_time]
    ax.bar(sorts, times, color=['blue', 'green', 'orange'])
    ax.set_ylabel('Time (seconds)')
    ax.set_title('Sorting Algorithm Time Comparison')
    
    # 清空舊畫布
    for widget in chart_frame.winfo_children():
        widget.destroy()
    
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# -------- 主視窗 --------
root = tk.Tk()
root.title("排序算法時間比較")
root.geometry("700x500")

run_button = tk.Button(root, text="執行排序", command=run_sorts, font=("Arial", 16), bg="lightblue")
run_button.pack(pady=20)

chart_frame = tk.Frame(root)
chart_frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
