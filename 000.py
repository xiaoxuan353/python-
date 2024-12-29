for n in range(9):
    n=n + 1
    表 = list()
    for nn in range(n):
        nn = nn +1
        乘法=n*nn
        if len(str(乘法)) == 1:
            乘法 = ' '+str(乘法)
        Res = str(n) + str('X') + str(nn) + str('=') + str(乘法)
        表.append(Res)
        b=str(表)