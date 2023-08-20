player1 = str(input('Введите имя пользователя 1: '))
turn1 = input('Что выберите? камень, ножницы, бумага ')
player2 = str(input('Введите имя пользователя 2: '))
turn2 = input('Что выберите? камень, ножницы, бумага: ')
if turn1 == 'камень' and turn2 == 'камень':
    print('НИЧЬЯ')
elif turn1 == 'камень' and turn2 == 'ножницы':
    print('Победил', player1)
elif turn1 == 'камень' and turn2 == 'бумага':
    print('Победил', player2)
elif turn1 == 'ножницы' and turn2 == 'камень':
    print('Победил', player2)
elif turn1 == 'ножницы' and turn2 == 'бумага':
    print('Победил', player1)
elif turn1 == 'бумага' and turn2 == 'камень':
    print('Победил', player1)
elif turn1 == 'бумага' and turn2 == 'ножницы':
    print('Победил', player2)
else:
    print('Выберите правильно: камень, ножницы, бумага')