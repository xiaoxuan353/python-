# a=open('David.zx','w')
# for n in range(9):
#     n=n + 1
#     for nn in range(n):
#         nn = nn +1
#         乘法=n*nn
#         if len(str(乘法))<2:
#             乘法='{}'.format(乘法)
#         Res='{}X{}={}'.format(n,nn,乘法)        
#         a.write(Res)
#         a.write('  ')
#     a.write('\n')
# a.close()
#
# a=open('David.zx','r')
# b=a.read()
# c=b.split('/n')
# for n in c:
#     print(n)
# a.close()

a=open(r'C:\Users\hjw\Desktop\Job-1.inp','r',encoding='gbk')
b=a.read()
c=b.split('\n')
判断= False
e=[]
for n in c:
    e.append(n)
    if '*Node' in n:
        判断=True
        continue
        
    if 判断:
        if '*' in n:
            break
        else:
            n=replace(' ','').split(',')
            print('{}'.format(n))
            e.append(n)
    

a.close()