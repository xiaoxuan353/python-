A=[[5,1,2,3,4],       #例如：
   [4,5,1,2,3],
   [3,4,5,1,2],
   [2,3,4,5,1],
   [1,2,3,4,5]]    
b=[45,40,40,45,55]
n=len(A)
# 定义函数
def Gauss(A,b,n):
    print('A=')
    for i in range(n):
        print('{}'.format(A[i]))
    print('b=')
    print('{}'.format(b))
    print('----------------')
    x=[0 for i in range(n)]
    # 判断
    for k in range(0,n-1):
        if abs(A[k][k])<10**(-10):
            print('a',kk,'在消元过程中为0,终止程序')
            break
    #选主元
        t=abs(A[k][k])
        s=k
        for i in range(k+1,n):
            if abs(A[i][k])>t:
                t=abs(A[i][k])
                s=i
    #换行
        if s!=k:
            for i in range(k,n):
                t=A[k][i]
                A[k][i]=A[s][i]
                A[s][i]=t
            t=b[k]
            b[k]=b[s]
            b[s]=t
        print('k={}'.format(k+1))
        print('A=')
        for i in range(n):
            print('{}'.format(A[i]))
        print('b={}'.format(b))
        print('----------------')         
        #消元
        for i in range(k+1,n):
            t=A[i][k]/A[k][k]
            print('t=',t)
            for j in range(k,n):
                A[i][j]=A[i][j]-t*A[k][j]
            b[i]=b[i]-t*b[k]
        print('k={}'.format(k+1))
        print('A=')
        for i in range(n):
            print('{}'.format(A[i]))
        print('b={}'.format(b))
        print('----------------')
        #回代解方程
    x[n-1]=b[n-1]/A[n-1][n-1]
    for k in range(n-1,-1,-1):
        sum=0
        for j in range(k+1,n):
            sum=sum+A[k][j]*x[j]
        x[k]=(b[k]-sum)/A[k][k]
    print('x={}'.format(x))
    print('----------------')
    return x
print(Gauss(A,b,n))
    

