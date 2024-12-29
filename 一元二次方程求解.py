a,b,c=input('依次输入ax**2+bx+c中a,b,c 用","分隔').split(',')
a=float(a)
b=float(b)
c=float(c)
# b=float(input('ax**2+bx+c中b'))
# c=float(input('ax**2+bx+c中c'))
E=D=-(b/(2*a))
if b**2-4*a*c<0:
    print('没有实数解')
else:
    A=-100000000
    B=100000000
    def F(x):
        return(float(a*(x**2)+b*x+c))
    
    while True:
        if F(A)*F(float(A+D)/2)<=0:
            D=(A+D)/2
        elif F(D)*F((A+D)/2)<=0:
            A=(A+D)/2
        if abs(D-A)<10**(-9):
            answer1=float((A+D)/2)
            break
        
    answer2=2*E-answer1
    if abs(answer1-answer2)<10**(-5):
        print(float((answer1+answer2)/2))
    else:
        print(answer1,answer2)
