#클래스 : 객체를 만들기 위한 틀
# class Dog:
#     #필드(속성)
#     type ='강아지'
#     legs = 4
#     eyes = 2
#     #메소드(기능)
#     def walk(self):
#         print('걷는다')
#
# d1 = Dog()
# print(d1.type)
# d1.walk()
# d2 = Dog()
# print(d2.type)

#계산기 클래스
# class Cal:
#     maker = '국제계산기'
#     color = '그린'
#     #self : 객체 자기 자신
#     def add(self,a,b): #덧셈
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
# #객체생성
# c1 = Cal()
# print(c1.color)
# data = c1.add(20,15)
# print('덧셈:', data)
# print('뺄셈:', c1.sub(50,20))
# print('곱셈:', c1.mul(50,5))
# print('나눗셈:', c1.div(50,20))

#멤버 : 필드 + 메소드
#클래스멤버/인스턴스멤버
# class Dog:
#     #클래스멤버
#     type = '강아지'
#     def walk(self):
#         print('걸어간다')
# print(Dog.type)
#
# d1 = Dog()
# print(d1.type)
# d1.type = '고양이'
# print(Dog.type) #클래스멤버 참조
# print(d1.type) #객체(인스턴스멤버)를 먼저 참조

#self를 이용해서 인스턴스필드 생성
# class Cat:
#     #클래스 필드
#     type = '고양이'
#     def run(self,name):
#         #인스턴스 필드 생성
#         self.name = name
#         print(self.name +' 뛴다')
#
# c1 = Cat()
# #Cat.run(c1,'야옹이')#클래스명으로 메소드 호출
# c1.run('야옹이')
# print(c1.name)

#메소드에서 클래스필드 접근하기
# class Cat:
#     type ='고양이'
#     count =0 #고양이객체의 수
#     def countAdd(self): #고양이 수 카운터
#         Cat.count += 1
#
# c1 = Cat() ; c1.countAdd()
# c2 = Cat() ; c2.countAdd()
# print(Cat.count, '마리')

#실습)학생클래스 만들기
# class Student:
#     #클래스필드
#     schoolname = '국제'
#     count = 0
#     #초기화 메소드
#     def init(self,clname, name): #반,이름
#         Student.count += 1 #학생수
#         self.clname = clname
#         self.name = name
#     #점수의 합계 반환 메소드
#     def scoreSum(self,scoreList):
#         return sum(scoreList)
#
# print('학교명:', Student.schoolname)
# print('-' * 20)
# s1 = Student(); s1.init('파이쎤반', '홍길동')
# print('반:', s1.clname)
# print('이름:', s1.name)
# print('합계:', s1.scoreSum([80,77,78]))
# print('-' * 20)
# s2 = Student(); s2.init('자바반', '이순신')
# print('반:', s2.clname)
# print('이름:', s2.name)
# print('합계:', s2.scoreSum([68,79,90]))
# print('-' * 20)
# print('학생수 :', Student.count)


#자동차 클래스
#속성(클래스필드) : 모델
#속성(인스턴스필드) : 칼라
#기능 : 초기화메소드, 파워(on/off), 속도 업, 속도 다운
class Car:
    model ='람보르기니'
    def init(self,color):
        self.color = color
        self.pow = False #파워
        self.speed = 0 #속도

    def power(self): #파워를 토글
        self.pow = not self.pow
    # 속도를 1씩 증가 : 속도가 300초과되면 300
    def speedUp(self):
        if self.speed < 300: self.speed += 1
    # 속도를 1씩 감소 : 속도가 0미만이면 0
    def speedDown(self):
        if self.speed > 0: self.speed -= 1
c1 =Car() ; c1.init('빨강색')
print('c1 color :', c1.color, c1.pow)
c1.power(); print('c1의 시동:', c1.pow)
for x in range(400):
    c1.speedUp()
print('c1의 속도:', c1.speed)

for x in range(400):
    c1.speedDown()
print('c1의 속도:', c1.speed)









