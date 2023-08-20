tsifri = range(1, 11)
novaya_tsifra = int(input('Введите число: '))
chetniye_znacheniye = [i *novaya_tsifra for i in tsifri if i %2 ==0]
nechetniye_znacheniye = [i *novaya_tsifra for i in tsifri if i %2 !=0]
print(chetniye_znacheniye)
print(nechetniye_znacheniye)
