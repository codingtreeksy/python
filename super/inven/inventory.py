#재고관리
name = '재고관리'
c = 17
def invenAdd():
    while True:
        print('-' * c)
        print('재고관리')
        print('-' * c)
        print('1.재고계산')
        print('2.재고조회')
        print('9.메인으로')
        print('-' * c)
        no = input('선택?')
        if no=='1': #재고계산
            # 상품목록을 딕셔너리로 만들기
            itemDic = {}
            f1 = open('data/item.txt','r')
            while True:
                item =f1.readline()
                if item=='': break
                itemname = item.split()[0]
                qty = int(item.split()[1][:-1])
                itemDic[itemname] = qty
            print(itemDic)
            #판매목록을 딕셔너리로 만들기
            f2 = open('data/sale.txt', 'r')
            sale =f2.readlines() #상품목록
            print(sale)
            f1.close()
            f2.close()
        elif no == '9': #메인으로
            break





