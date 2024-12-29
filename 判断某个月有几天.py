y=int(input('请输入任意年份'))
m=int(input('请输入任意月份'))
days={}
for i in range(1,8,2):
    days.update({i:31})
    days.update({i+1:30})
for i in range(8,13,2):
    days.update({i:31})
#     if i==12:
#         break
    days.update({i+1:30})
days.update({2:28})
del days[13]
if y%4==0:
    print(y,'年是闰年')
    days.update({2:29})
else:
    print(y,'年不是闰年')
print(y,'年',m,'月有',days[m],'天')
