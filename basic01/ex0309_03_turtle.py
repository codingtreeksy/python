#그래픽 모듈
import turtle
t = turtle.Pen()
t.shape('turtle')
# t.color('red','blue')
turtle.colormode(255) #RGB칼라 최대값 255로 변경
t.pencolor(255,100,0) #펜칼라
t.fillcolor(0,150,170) #도형내부 칼라
t.shapesize(3)
t.pensize(3)
t.speed(0) #0최고속도, 1~10 : 숫자가 클수록 속도up
#사각형 그리기
t.penup() #펜올리기
t.goto(0,200) #x,y좌표 이동
t.pendown() #펜내리기
# t.begin_fill()
# for x in range(4):
#     t.forward(100)
#     t.right(90)
# t.end_fill()
# #삼각형그리기
# for x in range(3):
#     t.forward(100)
#     t.right(120)
# #오각형그리기
# for x in range(5):
#     t.forward(100)
#     t.right(72)

#다각형을 그리는 함수
def poly(n,l):
    t.begin_fill()
    for x in range(n):
        t.forward(l)
        t.right(360/n)
    t.end_fill()
n = int(input('각형은?')) #각형
l = int(input('한변의길이는?'))#한변의 길이 입력
poly(n,l)

#화면이 바로 닫히지 않게
turtle.done()