#파일 입출력
#절대경로

#파일읽기 모드
#open('D:/ksy/Dropbox/java2020/python/source/basic01/data')
#상대경로
# f = open('./data/sample.txt','r',encoding='utf-8') #파일 오픈모드를 읽기전용
# print(f.read())
# f.close()
# help(open)
#f.seek(0) #커서를 처음으로 옮기기

# data = f.readlines()
# print(data)
# for x in data:
#     print(x[:-1]) #마지막글자제외

# while True:
#     data = f.readline()
#     if data=='': break
#     print(data[:-1])
# f.close()

#파일쓰기(덮어쓰기)
# f=open('data/write.txt','w')
# f.write('자장면\n')
# f.write('피자\n')
# f.write('짬봉\n')
# f.close()

#파일쓰기(추가)
# f = open('data/write.txt','a')
# f.write('설렁탕\n')
# f.close()

#실습)메뉴판 파일 만들기
# f = open('data/menu.txt','w')
# # while True:
# #     data = input('메뉴명은?')
# #     if data=='': break
# #     f.write(data+'\n')
# # f.close()

#실습)메뉴파일 출력
# f= open('data/menu.txt',encoding='utf-8')
# no = 0
# while True:
#     data = f.readline()
#     if data=='':break
#     no += 1
#     print(no, data[:-1],sep='.', end=', ')
# f.close()

#실습)파일을 읽어와서 딕셔너리 만들기
#name.txt , score.txt
#{'홍길동':90, '이순신':88, '김말자':85}
# dic={}
# f1 = open('data/name.txt',encoding='utf-8')
# f2 = open('data/score.txt',encoding='utf-8')
# while True:
#     name = f1.readline()[:-1]
#     score = f2.readline()[:-1]
#     if name=='' or score =='': break
#     dic[name] = int(score)
# print(dic)

#교재137번
# f = open('data/stockcode.txt','r')
# data = f.read()
# print(data)
# f.close()

#실습)종목코드를 입력받고
# 파일에서 해당 종목명을 출력하기
# f = open('data/stockcode.txt','r')
# code = input('종목코드는?')
# while True:
#     data = f.readline()
#     if data=='':
#         # 데이타를 찾지 못했을때
#         print('데이타가 없습니다.')
#         break
#     listA = data[:-1].split()
#     if listA[0] == code:
#         print(code, listA[1])
#         break

#파일에 저장하고 읽기
# f = open('data/writeRead.txt','w+')
# f.write('파이쎤\n')
# f.write('자바\n')
#
# print(f.tell()) #포인터의 현재 위치
#
# f.seek(0) #파일의 포인터를 처음으로 바꾼다
# print('=' * 15)
# print('프로그래밍 언어')
# print('=' * 15)
# print(f.read())
# f.close()

#교재)142번
# f = open('data/name.txt','r', encoding='utf-8')
# w = open('data/nameCopy.txt','w')
# data = f.read()
# w.write(data)
# f.close()
# w.close()

#교재)143번
# f = open('data/fox.jpg','rb')
# w = open('data/foxCopy.jpg', 'wb')
# size = 1024 #1 kbyte
# while True:
#     data = f.read(size)
#     if not data : break #데이터가 없다면
#     w.write(data)
#
# f.close()
# w.close()

#자동으로 파일 닫기
# with open('data/write.txt') as f:
#     print(f.read())

#파일다루기
#파일삭제
# from os import remove
# remove('data/name.txt')
#파일이름변경
# from os import rename
# rename('data/menu.txt','data/rece.txt')
import os
#디렉토리 생성
if not os.path.isdir('data/sub') :
    os.mkdir('data/sub')
#디렉토리 삭제
if os.path.isdir('data/sub'):
    os.rmdir('data/sub')

