#거북이 달리기 경주
import turtle, random, time
class CTurtle(turtle.Turtle): #컴퓨터 거북이
    def __init__(self, color):
        super().__init__()
        #글씨 쓰기
        self.penup()
        self.goto(0,200)
        self.pendown()
        self.write('거북이 경주',align='center', font=("Arial", 20, 'bold'))
        self.color(color)
        self.shape('turtle')
        self.penup()
        self.goto(-200, 100)
        self.pendown()

    def run(self): #달리기
        while True:
            time.sleep(0.5)
            self.forward(random.randint(10,50))
            if self.xcor()>200: break

class MyTurtle(turtle.Turtle): #나의 거북이
    def __init__(self, color):
        super().__init__()
        self.color(color)
        self.shape('turtle')
        self.penup()
        self.goto(-200, -100)
        self.pendown()
        #달리기

def rightMove():
    mT.forward(10)

cT = CTurtle('red')
mT = MyTurtle('blue')
s = turtle.Screen()
s.onkeypress(rightMove, 'Right')
s.listen()

cT.run()

turtle.done()


