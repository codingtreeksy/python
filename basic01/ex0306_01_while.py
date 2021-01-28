#반복문(while)
# while True: #무한 반복
#     print('python')

#1부터 10까지 출력
# a =0
# while a<10:
#     a=a+1
#     print(a)

# a = 0
# while True:
#     a += 1 #복합연산자 #a=a+1
#     if a>10: break
#     print(a)

#실습)사용자에게 입력받은 값을 더하는 프로그램
#사용자가 0을 입력하면 프로그램 종료
sum =0
while True:
    a = int(input('더할 숫자는?'))
    if a==0:
        print('합계는', sum)
        break
    sum += a


print('종료')





