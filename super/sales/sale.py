name='판매관리'
c = 17
def saleAdd():
    while True:
        print('-' * c)
        print('판매관리')
        print('-' * c)
        print('1.판매등록')
        print('2.판매조회')
        print('9.메인으로')
        print('-' * c)
        no = input('선택?')
        if no=='1': #판매등록
            f = open('data/item.txt','r')
            data =f.readlines() #상품목록
            w = open('data/sale.txt', 'w')
            while True:
                print(data)
                name = input('판매상품명은?')
                if name=='': break
                qty = input('판매수량은?')
                w.write(name+' '+qty+'\n')
            f.close()
            w.close()
        elif no == '9': #메인으로
            break





