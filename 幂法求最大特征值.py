import numpy as np

def power_iteration(A, x0, tol=1e-10, max_iterations=1000):
    """
    幂迭代法求解矩阵的最大特征值及其对应特征向量

    参数:
    A : 矩阵
    x0 : 初始猜测向量
    tol : 容差
    max_iterations : 最大迭代次数

    返回:
    lambda_ : 最大特征值
    v : 对应的特征向量
    """
    x = x0 / np.linalg.norm(x0)  # 初始猜测向量的归一化
    lambda_old = 0  # 初始特征值
    
    for iteration in range(max_iterations):
        # 计算 Ax
        Ax = np.dot(A, x)
        print(Ax)
        
        # 计算新的特征值
        lambda_new = np.dot(x, Ax)
        
        # 打印当前迭代信息
        print(f"第 {iteration + 1} 次迭代的特征值: {lambda_new}")
        
        # 归一化特征向量
        x = Ax / np.linalg.norm(Ax)
        
        # 检查特征值的收敛
        if np.abs(lambda_new - lambda_old) < tol:
            print(f"特征值在第 {iteration + 1} 次迭代时收敛")
            return lambda_new, x
        
        lambda_old = lambda_new
    
    print("达到最大迭代次数，未能收敛")
    return lambda_new, x

# 测试矩阵 A
A = np.array([[1,2,3],
              [2,3,4],
              [3,4,5]])

# 初始猜测向量
x0 = np.array([1, 1, 1])

# 调用幂迭代法
eigenvalue, eigenvector = power_iteration(A, x0)

print(f"最大特征值: {eigenvalue}")
print(f"对应的特征向量: {eigenvector}")
