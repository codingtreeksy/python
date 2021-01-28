#반복문(for)
# for x in [1,2,3,4,5]:
#     print(x)

# for x in ['java','python','c','basic']:
#     print(x)

# for x in 'python':
#     print(x)
# dic = {'1':100,'2':200,'3':300}
# for x in dic.keys():
#     print(x)
#
# for x in dic.values():
#     print(x)
#
# for x in dic.items():
#     print(x[0],x[1])
#
# for x,y in dic.items(): #튜플을 언패킹
#     print(x,y)

#순차적인 정수리스트
# print(list(range(5,101))) #start, stop
# print(list(range(0,11,2))) #start, stop, step

#1부터10까지 출력
# for x in range(1,11):
#     print(x)
# #홀수만 출력
# for x in range(1,11,2):
#     print(x)

#실습)1~30까지의 수중 3의 배수만 출력
# for x in range(3,31,3):
#     print(x)
# for x in range(3,31):
#     if x%3==0:
#         print(x)

#실습)1~30까지의 수중 3의 배수 또는 5의 배수 출력
# for x in range(3,31):
#     if x%3==0 or x%5==0:
#         print(x)

#1~10까지의 합계구하기
# sum = 0 #초기화
# for x in range(1,11):
#     sum = sum + x
# print(sum)

#실습)홀수,짝수 구하기
# for x in range(11):
#     if x%2 ==0: #짝수
#         print(x,':짝수')
#     else:
#         print(x, ':홀수')

#for ~ else
# for x in ['a','b','c','x','z','f']:
#     print(x)
#     if x=='z':
#         break #반복문의 수행 멈춤
# else: #for문이 정상수행
#     print('출력완료')

#1부터100까지의 수의 합계를 구할때
# 그합이 3000이 되면 반복문 종료
# 정수와 합계 출력
# sum =0
# for x in range(1,101):
#     sum = sum +x
#     if sum>6000:
#         print(x,sum)
#         break
# else:
#     print('합이 6000을 넘지 않습니다.')

#바른말 사용
# word = ['방가','굿','안녕','바보2','헬로우']
# bad=['못난이','바보','미워']
# for x in word:
#     if x in bad:
#         print('강퇴')
#         break
# else:
#     print('바른말사용')

#continue(계속)
# for x in [60,70,45,80,90]:
#     if x<60:
#         continue
#     print(x,'점 합격')

#실습) 모든 점수가 60점이 넘으면 합격
# score = [68,78,96,86,72]
# for x in score:
#     if x <60:
#         print('불합격')
#         break
# else: #break문을 실행되지 않았다
#     print('합격')

#실습) 300점이 넘으면 합격
#break
score = [68,15,15,86,72]
sum = 0
for x in score:
    sum = sum + x
    if sum >=300:
        print('합격')
        break
else:
    print(sum,'불합격')











