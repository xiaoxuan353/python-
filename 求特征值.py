import numpy as np

# 定义矩阵 A
A = np.array([[0.0, 3, 10],
[0.0, 3.333333348, 11.055555605],
[0.0, 5.166666684000001, 17.11111117]])

# 使用 NumPy 的 eig 函数求解特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)

# 打印结果
print("特征值:")
print(eigenvalues)

print("\n对应的特征向量:")
print(eigenvectors)
