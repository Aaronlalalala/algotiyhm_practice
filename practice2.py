import numpy as np

def matrix_multiply(A, B):
    try:
        return np.dot(A, B)
    except ValueError as e:
        print(f"矩陣相乘錯誤: {e}")
        return None

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("請輸入一個正整數！")
                continue
            return value
        except ValueError:
            print("無效的輸入！請輸入一個正整數。")

def get_matrix_row(row_num, cols, matrix_name):
    while True:
        try:
            row_input = input(f"輸入{matrix_name}第 {row_num} 行的 {cols} 個數字 (用空格分隔): ")
            values = list(map(float, row_input.split()))
            
            if len(values) != cols:
                print(f"錯誤：請輸入恰好 {cols} 個數字！")
                continue
                
            return values
        except ValueError:
            print("無效的輸入！請確保所有輸入都是數字。")

def main():
    print("=== 矩陣乘法計算器 ===")
    
    # 輸入矩陣維度（帶防呆）
    M = get_positive_integer("請輸入矩陣 A 的行數 M: ")
    N = get_positive_integer("請輸入矩陣 A 的列數 N (同時也是矩陣 B 的行數): ")
    P = get_positive_integer("請輸入矩陣 B 的列數 P: ")
    
    # 創建矩陣 A（帶防呆）
    print(f"\n請輸入矩陣 A ({M}x{N}) 的元素:")
    A = np.zeros((M, N))
    for i in range(M):
        A[i] = get_matrix_row(i+1, N, "矩陣A")
    
    # 創建矩陣 B（帶防呆）
    print(f"\n請輸入矩陣 B ({N}x{P}) 的元素:")
    B = np.zeros((N, P))
    for i in range(N):
        B[i] = get_matrix_row(i+1, P, "矩陣B")
    
    # 計算矩陣乘法
    print("\n正在計算矩陣乘法...")
    C = matrix_multiply(A, B)
    
    if C is not None:
        # 顯示結果
        print("\n矩陣 A:")
        print(A)
        
        print("\n矩陣 B:")
        print(B)
        
        print(f"\n結果矩陣 C ({M}x{P}):")
        print(C)
        
        # 可選：顯示更美觀的格式
        print("\n格式化的結果矩陣 C:")
        for row in C:
            print(" ".join([f"{x:.2f}" for x in row]))
    else:
        print("計算失敗！請檢查您的輸入。")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n程式被使用者中斷！")
    except Exception as e:
        print(f"\n發生未預期的錯誤: {e}")
    finally:
        print("\n謝謝使用矩陣乘法計算器！")