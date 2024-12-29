import numpy as np

def sor(A, b, x0, omega=1.35, tol=1e-10, max_iterations=1000):
    """
    Successive Over-Relaxation (SOR) 迭代法求解 Ax = b

    参数:
    A : 系数矩阵
    b : 常数向量
    x0 : 初始猜测值向量
    omega : 松弛因子
    tol : 容差
    max_iterations : 最大迭代次数

    返回:
    x : 解向量
    iteration : 实际迭代次数
    """
    n = len(A)  # 提取矩阵的行数
    x = x0.copy()  # 初始化解向量
    
    for iteration in range(max_iterations):
        x_old = x.copy()  # 保存前一轮迭代的解向量
        
        # 遍历每一行进行更新
        for i in range(n):
            sum_Ax = np.dot(A[i, :], x) - A[i, i] * x[i]
            # SOR 更新公式
            x[i] = (1 - omega) * x[i] + omega * (b[i] - sum_Ax) / A[i, i]
        
        # 打印每次迭代的结果
        print(f"第 {iteration + 1} 次迭代的解向量: {x}")
        
        # 检查收敛条件
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            print(f"迭代在第 {iteration + 1} 次收敛")
            return x, iteration + 1
    
    print("达到最大迭代次数，未能收敛")
    return x, max_iterations

# 三阶矩阵 A 和 b
A = np.array([[1.2,-3.6,-12],
              [-10,9,0.5],
              [1,-4,2]])

b = np.array([1,2,3])
x0 = np.zeros(len(b))  # 初始猜测值

# 使用松弛因子 ω = 1.35
solution, iterations = sor(A, b, x0, omega=0.1)

print(f"最终解向量: {solution}")
print(f"迭代次数: {iterations}")
