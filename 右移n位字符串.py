s=str(input('输入任意字符串'))
n=int(input('向右移动n位字符'))
while n>=len(s):
    n=n-len(s)
q=s[len(s)-1:len(s)-1-n:-1]
q=q[::-1]
ss=s[:len(s)-n:1]
print(q+ss)
