#터틀객체 생성
import turtle, random
class MyTurtle(turtle.Turtle):
    #생성자
    def __init__(self,color):
        super().__init__() #부모클래의 생성자 실행(첫줄에실행)
        self.color(color)
    #직사각형 박스를 그리는 메소드
    def box(self,width, length):
        x =random.randint(-200,200)
        y =random.randint(-200,200)
        self.penup()
        self.goto(x,y)
        self.pendown()
        for x in range(2):
            self.forward(width)
            self.right(90)
            self.forward(length)
            self.right(90)
t = []
for x in range(5):
    t.append(MyTurtle('green'))

for x in range(5):
    t[x].box(200,100)


turtle.done()