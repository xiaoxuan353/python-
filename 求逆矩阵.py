import numpy as np

# 定义一个矩阵
A = np.array([[0,2.3,0.4],
             [0.6,0,0],
             [0,0.3,0]])

# 检查是否可以求逆矩阵（矩阵的行列式不为0）
if np.linalg.det(A) == 0:
    print("该矩阵没有逆矩阵")
else:
    # 计算逆矩阵
    inverse_A = np.linalg.inv(A)

 # 保留4位小数
    inverse_A_rounded = np.round(inverse_A, 4)
    
    print("原矩阵:\n", A)
    print("逆矩阵 (保留4位小数):\n", inverse_A_rounded)