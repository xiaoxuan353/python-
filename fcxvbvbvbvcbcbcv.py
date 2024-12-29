import numpy as np

def normalized_power_iteration(A, x0, tol=1e-10, max_iterations=1000):
    """
    规范化幂法求解矩阵的最大特征值及其对应特征向量

    参数:
    A : 矩阵
    x0 : 初始猜测向量
    tol : 收敛容差
    max_iterations : 最大迭代次数

    返回:
    lambda_ : 最大特征值
    v : 对应的特征向量
    """
    # 归一化初始向量
    x = x0 / np.max(np.abs(x0))
    lambda_old = 0  # 上一轮特征值

    for iteration in range(max_iterations):
     
        
        x = x / np.max(np.abs(x))
        
        # 计算 Ax
        Ax = np.dot(A, x)
        print('Ax=',Ax)

        # 使用最大元素归一化特征向量
        max_elem = np.max(np.abs(Ax))
        print('max_elem=',max_elem)
        x = Ax / max_elem
        print('x=',x)

        # 计算新的特征值
        lambda_new = np.max(np.abs(Ax))

        # 打印归一化后的特征向量
        print(f"第 {iteration + 1} 次迭代后的特征向量: ")

        # 检查收敛性
        if np.abs(lambda_new - lambda_old) < tol:
            print(f"特征值在第 {iteration + 1} 次迭代时收敛")
            return lambda_new, x
        
        lambda_old = lambda_new
        print('____________')
    
    print("达到最大迭代次数，未能收敛")
    return lambda_new, x

# 测试矩阵 A
A = np.array([[1, 2, 3],
              [2, 3, 4],
              [3, 4, 5]])

# 初始猜测向量
x0 = np.array([1, 1, 1])

# 调用规范化幂法
eigenvalue, eigenvector = normalized_power_iteration(A, x0)

print(f"\n最大特征值: {eigenvalue}")
print(f"对应的特征向量: {eigenvector}")

