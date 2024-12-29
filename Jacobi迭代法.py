import numpy as np

def jacobi(A, b, x0, tol=1e-10, max_iterations=500):
    """
    Jacobi迭代法求解Ax = b，并打印每次迭代结果

    参数:
    A : 系数矩阵
    b : 常数向量
    x0 : 初始猜测值向量
    tol : 容差
    max_iterations : 最大迭代次数

    返回:
    x : 解向量
    iteration : 实际迭代次数
    """
    n = len(A)  # 提取矩阵的行数
    x = x0.copy()  # 初始化解向量
    
    for iteration in range(max_iterations):
        x_new = np.zeros_like(x)  # 创建一个新的解向量
        
        # 遍历每一行，进行Jacobi更新
        for i in range(n):
            sum_Ax = np.dot(A[i, :], x) - A[i, i] * x[i]
            x_new[i] = (b[i] - sum_Ax) / A[i, i]
        
        # 打印每次迭代后的解向量
        print(f"第 {iteration + 1} 次迭代的解向量: {x_new}")
        
        # 检查收敛条件
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"迭代在第 {iteration + 1} 次收敛")
            return x_new, iteration + 1
        
        x = x_new  # 更新解向量
    
    print("达到最大迭代次数，未能收敛")
    return x, max_iterations

# 测试
A = np.array([[1.2,-3.6,-12],
              [-10,9,0.5],
              [1,-4,2]])

b = np.array([1,2,3])
x0 = np.zeros(len(b))  # 初始猜测值

solution, iterations = jacobi(A, b, x0)
# A = np.array([[10,-1,-2],
#               [-1,10,-2],
#               [-1,-1,5]])
# 
# b = np.array([72,83,42])
# x0 = np.zeros(len(b))  # 初始猜测值
# 
# solution, iterations = jacobi(A, b, x0)


print(f"最终解向量: {solution}")
print(f"迭代次数: {iterations}")
