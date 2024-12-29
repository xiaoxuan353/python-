# 定义矩阵乘法函数
def matrix_multiply(A, B):
    # 获取矩阵的维度
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    # 检查矩阵乘法的条件：A的列数必须等于B的行数
    if cols_A != rows_B:
        raise ValueError("无法相乘！矩阵A的列数必须等于矩阵B的行数")
    
    # 初始化结果矩阵
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # 进行矩阵乘法
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# 示例矩阵
A = [[ 0.83333333,-0.,-0.        ],
 [ 0.92592593 ,0.11111111,-0.        ],
 [ 1.43518519  ,0.22222222 , 0.5       ]]

B = [[0,3.6,12],
     [0,0,-0.5],
     [0,0,0]]

# 计算并输出结果
result = matrix_multiply(A, B)
for row in result:
    print(row)
