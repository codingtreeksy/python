#슈퍼마켓 재고 프로그램
import os
while True:
    os.system('cls') #화면을 지운다
    print('-' * 25)
    print('슈퍼마켓 관리 프로그램(v1.0)')
    print('-' * 25)
    print('1.상품등록')
    print('2.재고등록')
    print('3.재고조회')
    print('9.종료')
    print('-' * 25)
    no = input('메뉴를 선택?')
    if no=='1': #상품등록
        f = open('data/item.txt','a')
        while True:
            item = input('상품명?')
            if item=='': break
            f.write(item + '\n')
        f.close()
    elif no=='2': #재고등록
        f = open('data/item.txt','r')
        w = open('data/stock.txt', 'w')
        while True:
            item=f.readline()[:-1]
            if item =='': break
            qty = input(item+'의 입고수량?')
            w.write(item +' ' + qty + '\n')
        w.close()
    elif no=='3':
        f = open('data/stock.txt')
        print('-' * 20)
        print('재고현황')
        print('-' * 20)
        print(f.read())
        f.close()
        input('초기메뉴(엔터):')
    elif no=='9': break #종료
    else:
        print('잘못된 선택')
