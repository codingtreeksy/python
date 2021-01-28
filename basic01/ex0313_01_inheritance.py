#클래스상속
# class Life:
#     state = '생명체'
# class Animal(Life):
#     name = '동물'
# class Plants(Life):
#     name = '식물'
# a1 = Animal()
# print(a1.state); print(a1.name)
# p1 = Plants()
# print(p1.state); print(p1.name)

#클래스의 오버라이딩
#부모의 멤버를 자식클래스에서 재정의
# class Bird:
#     state = '날수있다'
#     legs = 2
# class Sparrow(Bird):
#     name = '참새'
# class Ostrich(Bird):
#     name = '타조'
#     state = '날수없다'
#
# s1 = Sparrow()
#
# print(s1.name, s1.state, s1.legs)
# o1 = Ostrich()
# print(o1.name, o1.state, o1.legs)

#클래스의 다중상속(부모가 두개이상)
#object : 가장 최상위의 부모
# class A(object):
#     name='A클래스'
#     a = 10
# class B:
#     name='B클래스'
#     b = 20
# class C(B,A): #B클래스 멤버 우선 사용
#     #name='C클래스'
#     c = 30
#
# c1 = C()
# print(c1.a, c1.b, c1.c)
# print(c1.name)

#참고)오버로딩
#메소드의 이름은 같고 매개변수가 다른경우
#파이쎤은 오버로딩이 지원되지 않는다
# class Test:
#     def testA(self):
#         print('테스트A')
#
#     def testA(self, a):
#         print('테스트A_매개변수 있음')
#
# t1 = Test()
# t1.testA()

#실습)계산기 클래스
#첫번째계산기 : +, -, *, / , %
#두번째계산기 : +, -, *, /, **
# class Cal: #부모
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
# class CalA(Cal): #자식
#     def mod(self,a,b):
#         return a%b
# class CalB(Cal): #자식
#     def squ(self,a,b):
#         return a**b
# a = CalA(); print(a.add(10, 20), a.mod(20,4))
# b = CalB(); print(b.add(10, 20), b.squ(20,2))

#실습)학교반 객체 생성
class Student:
    name='학생과'
    motto='예의범절'
class Subject:
    subject =['python','java','HTML']
class ClassRoom(Student, Subject):
    #생성자
    def __init__(self, cName,schdule,motto=Student.motto):
        self.cName = cName #반명
        self.schdule = schdule
        self.motto = motto
    #시간표 출력
    def schdulePrint(self):
        for x in self.schdule:
            print(Subject.subject[x], end=' ')
        print() #개행
c11 = ClassRoom('1-1반',[1,2,0], '건강하게')
print(c11.cName, c11.name, c11.schdule,c11.motto)
c11.schdulePrint()

c12 = ClassRoom('1-2반',[2,0,1])
print(c12.cName, c12.name, c12.schdule,c12.motto)
c12.schdulePrint()






