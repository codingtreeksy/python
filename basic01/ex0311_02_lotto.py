#테스트
# setA = {1, 2, 1, 1, 2, 3}
# print(setA)

# a = [30, 16, 41, 10, 20, 13]
# b = [8, 10, 41, 20, 42, 43]
# print(list(set(a).intersection(b)))

# b = [8, 10, 41, 20, 42, 43]
# b.sort()
# print(b)
#
# b = [8, 10, 41, 20, 42, 43]
# print(sorted(b))
# print(b)

#로또번호 파일로 저장하기
# import random as r
# no = input('회차는?')
# data = r.sample(range(1,46), 6)
# data.sort()
# print(data)
# f = open('data/lotto.txt','w')
# f.write(no+' ')
# for x in data:
#     f.write(str(x)+' ')
# f.close()

#로또번호 당첨 갯수 출력하기
#입력받은 번호
no = input('이번주 당첨번호는?')
data = no.split()
print(data)

#당첨번호 가져오기
f = open('data/lotto.txt')
lotto = f.readline().split()
lotto.pop(0) #회차 제외
print(lotto)
count = 0
for x in data:
    if x in lotto:
        count += 1

print('당첨개수:', count)





