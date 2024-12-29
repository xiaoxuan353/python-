r=d=a=int(input('输入任意非零自然数'))
e=[]
for i in range(100):
    if 10**i<=a<10**(i+1):
        print(a,'是',i+1,'位数')
        c=i
for n in range(c,-1,-1):
    b=d//10**n
    e.append(b)
    d=d-b*10**n
print(e)
q=0
for nn in range(c+1):
    q=q+e[nn]**(c+1)
if a==q:
    print(r,'是自幂数')
else:
    print(r,'不是自幂数')