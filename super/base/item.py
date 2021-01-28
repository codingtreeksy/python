c=17
name='상품관리'
#상품등록
def itemAdd():
    while True:
        print('-' * c)
        print('상품관리')
        print('-' * c)
        print('1.상품등록')
        print('2.상품조회')
        print('9.메인으로')
        print('-' * c)
        no = input('선택?')
        if no=='1': #상품등록
            #main.py에서 import했기때문에 main.py를 기준으로 경로
            f = open('data/item.txt','w')
            while True:
                name = input('상품명은?')
                if name=='': break
                qty = input('재고량은?')
                f.write(name+' '+qty+'\n')
            f.close()
        elif no == '9': #메인으로
            break