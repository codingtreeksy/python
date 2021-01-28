#예외처리
# while True:
#     try: #예외 가능 문장
#         a = int(input('숫자는?'))
#     except: #예외 발생시 실행
#         print('숫자를 입력해 주세요')
#     else: #예외가 발행하지 않았을때
#         print(a + 10)
#         break

#실습)나눗셈 예외처리
#나눌수를 입력을 받아서 100을 나누는 프로그램
# def div(a):
#     try:
#         a = int(a)
#         data = 100/a
#     except ZeroDivisionError as e:
#         print('0으로 나눌수 없습니다.')
#     except ValueError as e:
#         print(e)
#         print('숫자를 입력해 주세요')
#     else:
#         print(data)
#
# while True:
#     a = input('나눌수는?')
#     if a=='':break
#     div(a)

#finally 구문
# a =['hong'] #접속id
# try:
#     data = a[0]
# except IndexError as e:
#     print('잘못된 인덱스 접근')
# else:
#     print(data +'님 반갑습니다.')
# finally: #예외발생여부와 상관없이 실행
#     print('프로그램 로그인')

#실습)파일 오픈 (finally)
# try:
#     f = open('data/test.txt', 'r')
# except FileNotFoundError as e:
#     print('파일이 없습니다.')
# else:
#     #파일은 오픈 성공한후 close가능
#     try:
#         print(f.read())
#     except:
#         print('파일 읽기 예외')
#     finally:
#         f.close()
#         print('파일닫기')

#예외를 발생시키기
#raise Exception
#만약 자식클래스가 반드시 구현해야할 메소드가 있다면
class Parent:
    def setName(self, name):
        try:
            #사용자 예외발생
            raise Exception
        except:
            print('예외발생')

class Child(Parent):
    #오버라이딩
    def setName(self, name):
        self.name = name

c1 = Child()
c1.setName('홍길동')







