#딕셔너리
# dic = {'a':10, 'b':20,'c':30}
# print(dic['b'])
# a = list(dic.values())
# print(a[2])

# hei = {'홍길동':[165,'A'], '이순신':[170,'B']}
# print(hei['이순신'][1])
# hei['유관순'] = [160,'O']
# print(hei)
# print('유관순' in hei)
# print(hei.keys())

#사용자에게 RGB입력받기
# r = int(input('RED:'))
# g = int(input('GREEN:'))
# b = int(input('BLUE:'))
# # d = {'r':r, 'g':g, 'b':b}
# d={}
# d['r'] = r
# d['g'] = g
# d['b'] = b
# print(d)

#학생의 정보를 딕셔너리로
# name=input('이름?')
# age = int(input('나이?'))
# blood = input('혈액형?')
# std = {'이름':name, '나이':age, '혈액형':blood}
# print(std)
# print(std['이름'])
# print(list(std.values())[0])

#두명의 학생 정보 저장
#{'홍길동':[20,'A'],'이순신':[30,'B']}
dic={}
#첫번째
# name=input('이름?')
# age = int(input('나이?'))
# blood = input('혈액형?')
# dic[name] = [age, blood]
#두번째
name=input('이름?')
age = int(input('나이?'))
blood = input('혈액형?')
dic[name] = [age, blood]

print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
print(list(dic.keys()))
print(dic['kim'])






