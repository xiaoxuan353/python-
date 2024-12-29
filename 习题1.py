a=int(input('输入任意非零自然数'))
c=0
for i in range(a):
    b=1
    for ii in range(i+1):
        b=b*(ii+1)
    c=c+b
if a>=3:
    print('1+2!+....+',a,'!=',c)
elif a==2:
    print('1+2!=',c)
else:
    print('1的阶乘为1')
