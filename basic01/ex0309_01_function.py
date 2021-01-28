#함수
#함수의 도움말 보기
# help(print)
# print('a','b','c',sep='~',end='\n\n')
# print('hello')

#가장큰값/작은값
# print(max('abcdefg'))
# print(min('%&#324'))

#합계함수
# data = [3,4,5,6]
# print(sum(data))
# #평균구하기
# print(sum(data) / len(data))

#코드값/문자값 구하기
# print(ord('A'))
# print(ord('성'))
# print(chr(49457))

#사용자정의 함수
#두수를 인자로 받아서 합을 리턴하는 함수
# def add(a,b):
#     c = a+b
#     return c
#
# data = add(10,20)
# print(data)
#두수를 인자로 받아서 차을 리턴하는 함수
# def sub(a,b):
#     return a-b
#
# print(sub(20,5))
#
# #두수를 인자로 받아서 곱을 출력하는 함수
# def mul(a,b):
#     print(a*b)
#
# print(mul(30,2)) #None출력(리턴값 없다)

#실습)구구단 출력 함수
# def gugudan(dan):
#     for x in range(1,10):
#         print(dan , '*', x, '=', dan * x)
# dan = int(input('단수는?'))
# gugudan(dan)

#지역변수
# data = 100 #전역 변수를 사용
# def test():
#     global data #전역변수
#     local = 30  #지역변수
#     data = data + local
#     print(data)
# test()
# print(data)

#가변형 인자
#인자들의 합을 출력하는 함수
# def test(*args):
# #     s =0
# #     for x in args:
# #         s += x
# #     print('합계:', s)
# #
# # data = input('숫자들?')
# # data = data.split()
# # a,b,c = list(map(int, data))
# # test(a,b,c)

#디폴트(default)인자
# def test(a,b='easy'):
#     print(a)
#     print(b)
# #디폴트인자는 선택적으로 전달
# test('python','hard')

#딕셔너리로 전달
# def test(**args):
#     print(args)
# test(name='홍길동',score=90)

#함수의 리턴값이 여러개가 가능? 불가능
#여러개를 반환할 경우 리스트나 튜플 ...
# def test(a,b):
#     return a+b,a-b
#
# print(test(30,20))

#실습)팩토리얼
# def fac(n):
#     mul = 1 #초기값
#     for x in range(1,n+1):
#         mul = mul * x
#     return mul
# print(fac(30))





