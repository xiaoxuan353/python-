from turtle import *

def setting():
    pensize(4)
    # hideturtle()
    colormode(255)
    color((255,155,192),"pink")
    setup(840,500)#用来设置绘图窗口的大小。具体来说，setup() 函数的参数表示窗口的宽度和高度
    speed(20)


def nose():
    penup()
    goto(-100,100)
    pendown()
    setheading(-30)
    begin_fill()
    a=0.4

    for i in range(120):
        if 0 <= i < 30 or 60 <= i <90:
            
            a += 0.08
            left(3)
            forward(a)
            
        else:
            
            a -=0.08
            left(3)
            forward(a)
        print('a=',a)
    end_fill()
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    pencolor(255,155,192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160,82,45)
    end_fill()
    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255,155,192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160,82,45)
    end_fill()




def head(x,y):
    color((255,155,192),"pink")
    penup()
    goto(x,y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300,-30)
    circle(100,-60)
    circle(80,-100)
    circle(150,-20)
    circle(60,-95)
    setheading(161)
    circle(-300,15)
    penup()
    goto(-100,100)
    pendown()
    setheading(-30)
    a=0.4
    for i in range(60):
        if 0<=i < 30 or 60 <= i < 90:
            a +=0.08
            lt(3)
            fd(a)
        else:
            a -=0.08
            lt(3)
            fd(a)
    end_fill()
    
def ears(x,y):
    color((255,155,192),"pink")
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50,50)
    circle(-10,120)
    circle(-50,54)
    end_fill()
    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    fd(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50,50)
    circle(-10,120)
    circle(-50,56)
    end_fill()
    
def eyes(x,y):
    color((255,155,192),"white")
    penup()
    setheading(90)
    fd(-20)
    seth(0)
    fd(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    fd(12)
    setheading(0)
    fd(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    color((255,155,192),"white")
    penup()
    seth(90)
    fd(-25)
    seth(0)
    
    fd(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    seth(90)
    fd(12)
    seth(0)
    fd(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    
def cheek(x,y):
    color((255,155,192))
    penup()
    goto(x,y)
    pendown()
    seth(0)
    begin_fill()
    circle(30)
    end_fill()
    
def mouth(x,y):
    color(239,69,19)
    penup()
    goto(x,y)
    pendown()
    seth(-80)
    circle(30,40)
    circle(40,80)
    
setting()
nose()
head(-69,167)
ears(0,160)
eyes(0,140)
cheek(80,10)
mouth(-20,30)
done()