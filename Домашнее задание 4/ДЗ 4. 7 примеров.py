numbers = [i for i in range(1, 15)]
print(numbers)


nums = [i*2 for i in range(1, 12)]
print(nums)


words = ['kniga', 'stol', 'vremya', 'metro', 'gazeta']
words_g = [word for word in words if 'g' in word]
print(words_g)
words_m = [word for word in words if 'm' in word]
print(words_m)


words = ['kniga', 'stol', 'vremya', 'metro', 'gazeta']
poslednaya_bukva = [bukva[-1] for bukva in words]
print(poslednaya_bukva)


spisok = ['Stanislav', 'Oleg', 'Misha', 'Javohir', 'Alina']
spisok2 = [i[1::3] for i in spisok]
print(spisok2)


spisok5 = ['Andrey', '17', 'Kirill', 'Evgeniy', '22']
spisok_new = [i+' student' for i in spisok5 if 'y' in i]
print(spisok_new)


tsifri = range(1, 11)
novaya_tsifra = int(input('Введите число: '))
chetniye_znacheniye = [i *novaya_tsifra for i in tsifri if i %2 ==0]
nechetniye_znacheniye = [i *novaya_tsifra for i in tsifri if i %2 !=0]
print(chetniye_znacheniye)
print(nechetniye_znacheniye)