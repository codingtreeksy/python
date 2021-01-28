#모듈 cmd창에서 실행
#print('cmd창에서 실행')
import sys
print(sys.argv[0]) #실행파일 명
userid = sys.argv[1] #아이디
passwd = sys.argv[2] #패스워드

#만약 아큐먼트의 값이 root / 1111 이면 슈퍼유저
#아니면 일반유저
if userid=='root' and passwd=='1111':
    print('슈퍼유저입니다.')
else:
    print('일반 유저입니다.')

