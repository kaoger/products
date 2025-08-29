products =[]
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append(['商品名稱: '+name,'商品價格: ' + price])
print(products)
for p in products:
    print(p[0])