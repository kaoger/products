import os #載入作業系統檢查有沒有檔案用的
products =[]
if os.path.isfile('products.csv'):
    print('找到檔案了!')
    with open('products.csv','r',encoding='utf-8-sig') as f :
        for line in f:
            if '商品名稱,商品價格' in line:
                continue
            name, price  = line.strip().split(',')
            products.append([name , price])
        print(products)
else:
    print('檔案不存在')
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name,price])
print(products)
with open('products.csv','w',encoding='utf-8-sig') as f :
    f.write('商品名稱,商品價格'+'\n')
    for p in products:
         f.write(p[0]+','+p[1]+'\n')
