#조건문(if~else)
# python = 75
# if python >= 80:
#     print('잘했어!')
#     print('good')
# else:
#     print('노력해!')

#패스워드 확인하기
# mypw = '1234'
# pw = input('패스워드는?')
# if mypw == pw:
#     print('패스워드 일치')
# else:
#     #이스케이프 문자 : \n \t
#     print('불일치\n실패')

#실습)교제 8번
# data = ['a','b','c','d']
# if 'b' in data:
#     print('a포함')
# else:
#     print('a미포함')

#실습) 두수중 큰수 출력
# a = int(input('첫번째수?'))
# b = int(input('두번째수?'))
# if a>b:
#     print(a)
# else:
#     print(b)

#두수를 같이 입력
# data = input('두수를 입력?')
# data = data.split()
# a = int(data[0])
# b = int(data[1])
#data리스트를 int함수 작업하고 a와b에 언패킹
# a,b = map(int, data)
# if a>b:
#     print(a)
# else:
#     print(b)

#여러개의 조건
#if ~ elif ~ else문
# python = 55
# if python >=80:
#     print('very good')
# elif python >=70:
#     print('good')
# else:
#     print('try')

#학점 출력
# a = int(input('점수는?'))
# if a >=90:
#     print('A등급')
# elif a>=80:
#     print('B등급')
# elif a>=70:
#     print('C등급')
# elif a>=60:
#     print('D등급')
# else:
#     print('F등급')

#실습)거스름돈 계산하기
# money = int(input('현재돈?'))
# pay = int(input('물건값은?'))
# if money>pay:
#     print('거스름돈:', money-pay)
# elif pay > money:
#     print('부족금액:', pay-money)
# else:
#     print('계산완료')

#논리연산자(and)
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
# a=10; b = -10
# # print(a>0 and b>0)
# # print(a>0 and b<0)
# if a>0 and b>0:
#     print('둘다 양수')
# else:
#     print('둘중 하나이상 양수 아님')

#논리연산자 (or)
# print(True or False)
# print(False or False)
# a = -10; b = -10
# if a>0 or b>0:
#     print('둘중 하나이상은 양수')
# else:
#     print('둘 다 음수')

# 논리연산자(not)
# a = True
# print(not a)
# a = -10
# if not a>0: #a가 0보다 크지 않다면
#     print('음수입니다.')

#두수가 0보다 크면 '둘다 양수' 출력
#두수중 하나가 0보다 작으면 '둘중 하나 양수' 출력
#두수가 모두 음수이면 '둘다 음수'출력
#단 두수는 0이 아니다)
# a=-10; b=-20
# if a>0 and b>0:
#     print('둘다 양수')
# elif a>0 or b>0:
#     print('둘중 하나 양수')
# else:
#     print('둘다 음수')

#실습)메뉴고르기
# m = int(input('1.자장면,2.짬뽕,3.설렁탕,4.비빔밥:'))
# if m==1 or  m==2:
#     print('중식')
# elif m==3 or  m==4:
#     print('한식')

#예)자장면 , 중식, 5000원
menu={1:['자장면','중식',5000],
      2:['짬뽕','중식',6000],
      3:['설렁탕','한식',8000],
      4:['비빔밥','한식',9000]}
m = int(input('메뉴는?'))
print('선택메뉴:', menu[m][0])
print('코너:', menu[m][1])
print('가격:', menu[m][2])






