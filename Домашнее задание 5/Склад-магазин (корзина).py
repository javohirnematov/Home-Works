all_products = {'Весь склад': {}}
korzina_pokupatelya = []
while True:
    admin = int(input('Что вы хотите сделать? 1 - добавить товар, 2 - склад, 3 - купить, 4 - корзина: '))
    if admin == 1:
        product_name = input('Введите название продукта: ')
        product_count = int(input('Введите количество: '))
        all_products['Весь склад'][product_name] = product_count
        print('Продукт добавлен')
        print(all_products)
    elif admin == 2:
        print(all_products)
    elif admin == 3:
        product_pokupki = input('Введите название продукта: ')
        if product_pokupki in all_products['Весь склад'].keys():
            kolichestvo = int(input('Введите количество: '))
            if all_products['Весь склад'][product_pokupki] >= kolichestvo:
                all_products['Весь склад'][product_pokupki] = all_products['Весь склад'][product_pokupki] - kolichestvo
                korzina_pokupatelya.append([product_pokupki, kolichestvo])
                print(korzina_pokupatelya)
                print(all_products)
            else:
                print('Такого продукта нет!')
    elif admin == 4:
        print(korzina_pokupatelya)
    else:
        print('Введите заново')