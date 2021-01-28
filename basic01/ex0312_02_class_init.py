#클래스의 생성자
# class Dog:
#     type ='강아지'
#     count = 0 #강아지 수
#     #생성자 : 객체 생성시 자동 실행되는 메소드
#     def __init__(self,name,age):
#         Dog.count += 1
#         self.name = name
#         self.age = age
#     #소멸자 : 객체 삭제시 자동 실행되는 메소드
#     def __del__(self):
#         Dog.count -= 1
#
# d1 = Dog('발발이',5) #객체생성시 인자값 설정
# print('이름:', d1.name, '나이:', d1.age)
# print('강아지수:', Dog.count)
# del d1 #객체 삭제
# print('강아지수:', Dog.count)

#실습)영화 티켓 구입 클래스
#티켓구입(생성자),티켓삭제(소멸자)
#잔여좌석 출력 메소드
# class Ticket:
#     count = 20 #잔여좌석
#     def __init__(self): #생성자
#         Ticket.count -= 1
#     def __del__(self): #소멸자
#         Ticket.count += 1
#         print('취소되셨습니다.')
#
#     #어노테이션
#     @classmethod
#     def printCount(cls): #클래스 메소드
#        print('잔여좌석:',  cls.count)
#
# t1 = Ticket()
# t2 = Ticket()
# Ticket.printCount()
# del t1
# Ticket.printCount()

#로또클래스
#메소드 :
#1)당첨번호 자동 추출 메소드
#2)구매번호 저장 메소드
#3)당첨개수 반환 메소드
import random
class Lotto:
    name = '로또복권'
    def __init__(self):
        self.sel = {} #구매번호 딕셔너리
        self.autoNo()
    def autoNo(self): #자동추출번호
        lottoNo = random.sample(range(1, 46), 6)
        lottoNo.sort()
        self.lottoNo = lottoNo
    def saleNo(self,name, selno): #구매번호
        self.sel[name] = selno
    def rightCount(self,name): #당첨개수 반환
        rCount = 0
        for x in self.sel[name]:
            if x in self.lottoNo:
                rCount += 1
        return rCount
l1 = Lotto() #로또객체 생성
print('로또번호:', l1.lottoNo)
#구매정보 딕셔너리 인스턴스필드로 저장
#saleP = {'홍길동':[1,3,5,7,9,10],'이순신':[2,4,6,8,10,12]}
saleP = {}
while True:
    name = input('이름은?')
    if name=='': break
    selNo = input('선택번호는?').split()
    selNo = map(int, selNo)
    saleP[name] = list(selNo)
print(saleP)

for name, no in saleP.items():
    l1.saleNo(name,no)
print('구매내역:', l1.sel)
#
# #당첨내역 출력
for name in saleP.keys():
    print(name , '당첨갯수',l1.rightCount(name))



















