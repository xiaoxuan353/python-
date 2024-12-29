def 矩阵乘法(A,B):
    n=len(A)             #A矩阵行数
    l=len(A[0])          #A矩阵列数
    o=len(B)            #B矩阵行数
    m=len(B[0])           #B矩阵列数
    if l != o:
        print('不可相乘')
    else:
        result=[[0 for p in range(m)] for p in range(n)]
        for i in range(n):
            for j in range(m):
                for k in range(l):
                    result[i][j]+=A[i][k]*B[k][j]
        print(result)
        
A=[[1,0,2],
   [-1,3,1]]
B=[[2,1,3],
   [0,-1,4],
   [1,2,1]]
矩阵乘法(A,B)
