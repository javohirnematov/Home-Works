price_small_bootle = float(0.10)
price_big_bootle = float(0.25)

small_bottle = int(input('Сколько бутылок с объемом 1 л и меньше: '))
x = price_small_bootle * small_bottle
print('Cумма за маленькие бутылки $%.2f.'% x)
big_bottle = int(input('Сколько бутылок с объемом 1 л и больше: '))
y = price_big_bootle * big_bottle
print('Cумма за большие бутылки $%.2f.'% y)
all_bootle = x + y
print('Выручка за все бутылки $%.2f.'% all_bootle)
