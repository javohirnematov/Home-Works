ves_suvenira = int(75)
ves_bezdelushki = int(112)

suveniri_shtuk = int(input('Сколько закуплено сувениров: '))
x = ves_suvenira * suveniri_shtuk
print('Общий вес', suveniri_shtuk, 'сувениров составляет', x, 'гр')

bezdelushki_shtuk = int(input('Сколько закуплено безделушек: '))
y = ves_bezdelushki * bezdelushki_shtuk
print('Общий вес', bezdelushki_shtuk, 'безделушек составляет', y, 'гр')

z = x + y
print('Общий вес сувениров и безделушек составляет', z, 'гр')