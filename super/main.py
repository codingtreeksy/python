#슈퍼관리 프로그램
c = 17 #찍을갯수
import os

# 디렉토리 존재 여부 확인
if not os.path.isdir('data'):
    os.mkdir('data')

print('*' * c)
while True:
    print('슈퍼관리 프로그램')
    print('*' * c)
    print('1.상품관리')
    print('2.판매관리')
    print('3.재고관리')
    print('9.프로그램종료')
    print('*' * c)
    no=input('선택?')
    if no=='1':
        from base import item
        item.itemAdd()
    elif no == '2':
        from sales import sale
        sale.saleAdd()
    elif no == '3':
        from inven import inventory
        inventory.invenAdd()
    elif no =='9':
        print('프로그램을 종료합니다.')
        break


