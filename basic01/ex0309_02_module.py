#모듈 추가하기
# import time
# t = time.localtime()
# print(t)
# year =list(t)[0]
# print(year,'년')
# print(t.tm_year, '년') #객체의 필드를 이용한 값 추출

#sleep : 주어진 초만큼 멈추기
# print('시작')
# time.sleep(3)
# print('3초 지남')
# print(time.localtime())

#실습)타이머 출력하기
# import time
# sec = 5
# for x in range(1,sec+1):
#     time.sleep(1)
#     print(x,'초')

#실습)카운트 다운 출력해주는 사용자 함수
# import time
# def countDown(t):
#     for x in range(t,0,-1):
#         print(x,'초')
#         time.sleep(1)
#     print('발사!')
# a = int(input('카운트초?'))
# countDown(a)

#달력모듈
# import calendar
# # calendar.prcal(2020)
# calendar.prmonth(3000,3)

#무작위의 수 추출(random)
#알리아스 명 지정 : as
# import random as r
# print(r.randint(1,100))

#실습)주사위 게임
#A,B 의 1~6까지의 난수를 추출해서 숫자가 큰쪽이 이김
#A승 또는 B승 또는 비김
# import random as r
# scoreA = 0 #A의 점수
# scoreB = 0 #B의 점수
# while True:
#     a = r.randint(1,6)
#     b = r.randint(1,6)
#     print('A:', a, 'B:',b)
#     if a>b:
#         print('A승')
#         scoreA += 1
#     elif b>a:
#         print('B승')
#         scoreB += 1
#     else:
#         print('무승부')
#
#     #3승이 되면 종료
#     if scoreA>2:
#         print('A 3점 승 ')
#         break
#     elif scoreB>2:
#         print('B 3점 승 ')
#         break

#데이터를 섞는다
# import random as r
# data = ['a','b','c','d']
# r.shuffle(data)
# print(data)

#한개를 고르다
# import random as r
# print(r.choice(['가위','바위','보']))

#여러개를 고르다
# import random as r
# print(r.sample(range(1,46),6))

#실습)가위/바위/보
#from ~ import : 원하는 함수만
from random import choice
a = choice(['가위','바위','보'])
b = choice(['가위','바위','보'])
print(a,b)
#중첩 조건문
if a==b:
    print('무승부')
elif a=='가위':
    if b=='바위': print('B승')
    else: print('A승')
elif a=='바위':
    if b=='가위': print('A승')
    else: print('B승')
elif a=='보':
    if b=='가위': print('B승')
    else: print('A승')










