numbers = range(1, 11)
kolichestvo = int(input('Введите количество: '))

while True:
    new_number = int(input('Введите число: '))
    print(f'Таблица умножения для числа: {new_number}')
    for number in numbers:
        print(f'{number} * {new_number} = {number * new_number}')