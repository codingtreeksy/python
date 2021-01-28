#무작위 위치에 도형 그리기
import random as r
import turtle
t = turtle.Pen() #펜만들기
t.speed(0)
def poly():
    x = r.randint(-300,300)
    y = r.randint(-200,200)
    l = r.randint(10,200) #한변의 길이
    #도형의내부색
    red = r.randint(0,255)/255
    green = r.randint(0,255)/255
    blue = r.randint(0,255)/255
    t.fillcolor(red,green,blue) #RGB칼라
    p = r.randint(3,10) #각형
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill() #칠하기 시작
    # for x in range(p):
    #     t.forward(l)
    #     t.right(360/p)
    t.circle(l, steps=p) #램덤 각형/길이
    t.end_fill() #칠하기 끝

for x in range(10):
    poly()

turtle.done()




