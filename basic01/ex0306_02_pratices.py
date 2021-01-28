#연습문제
#별찍기1)
# for x in range(1,7):
#     print('*' * x)
#별찍기2)
# for x in range(6,0,-1):
#     print('*' * x)

#참고
# print(' ' * 6, end='')
# print('*' * 3)

#별찍기3)
# for x in range(1,7):
#     print(' ' * (6-x),end='')
#     print('*' * x)

#실습)구구단
#2단 출력
# dan = int(input('몇단?'))
# for x in range(1,10):
#     print(dan,'*', x, '=', dan*x)
#2~9단 출력
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 2 * 6 = 12
# 2 * 7 = 14
# 2 * 8 = 16
# 2 * 9 = 18
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# 3 * 6 = 18
# 3 * 7 = 21
# 3 * 8 = 24
# 3 * 9 = 27

# for y in range(2,10):
#     print(y,'단')
#     for x in range(1,10):
#         print('%d * %d = %d'%(y,x,y*x))


#3단씩출력
# 2 * 1 = 2  3 * 1 = 3  4 * 1 = 4
# 2 * 2 = 4  3 * 2 = 6  4 * 2 = 9
# 2 * 3 = 6

# for x in range(2,10,3):
#     print(x,x+1,x+2)
#     for y in range(1,10):


#계산기
#수식이 q를 입력하면 종료
#첫번째방법
# while True:
#     a = input('수식?')
#     if a=='q': break
#     data = a.split() #문자열을 공백을 기분으로 분리
#     print(data)
#     a = int(data[0]) #첫번째수
#     b = int(data[2]) #두번째수
#     sign = data[1] #기호
#     if sign=='+':
#         print(a+b)
#     elif sign == '-':
#         print(a-b)
#     elif sign == '*':
#         print(a*b)
#     elif sign == '/':
#         print(a/b)
#     else:
#         print('기호가 올바르지 않습니다.')

#두번째 방법
# while True:
#     a = input('첫번째수?')
#     if a=='q' : break
#     a = int(a)
#     b = int(input('두번째수?'))
#     sign = input('기호는?')
#
#     if sign=='+':
#         print(a+b)
#     elif sign == '-':
#         print(a-b)
#     elif sign == '*':
#         print(a*b)
#     elif sign == '/':
#         print(a/b)
#     else:
#         print('기호가 올바르지 않습니다.')
#세번째 방법(딕셔너리이용)
# while True:
#     data = input('수식?')
#     if data =='q': break
#     listA = data.split()
#     a = int(listA[0])
#     b = int(listA[2])
#     sign = listA[1]
#     dic ={'+':a+b, '-':a-b, '*':a*b,'/':a/b}
#     print(dic[sign])
#네번째 방법
# while True:
#     data = input('수식?')
#     if data=='q' : break
#     print('결과값:', eval(data))

#90점 이상 출력
# dicA = {1:94, 2:87, 3:91, 4:75, 5:92}
# for k,v in dicA.items(): #튜플을 언패킹
#     if k >=90:
#         print(v,'번')

#일판매 히스토그램
# listA = ['홍길동','이순신','김순희','이철수']
# sale=[] #판매수량
# for x in listA:
#     a = input(x+' 판매수량?')
#     sale.append(int(a))
# print(sale)
#
# for x in range(len(listA)):
#     print(listA[x],':','*' * sale[x])

#실습)적정체중
name = input('이름?')
hei = int(input('키는?'))
wei = int(input('몸무게는?'))
nor = (hei-100) * 0.9 #적정체중
if wei < nor * 0.95:
    print(name ,': 체중미달')
elif wei > nor * 1.05:
    print(name, ': 과체중')
else:
    print(name, ': 적정체중')















