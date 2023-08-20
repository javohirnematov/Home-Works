import random
number = random.randint (1, 50)
print(number)
attempt = 0
print('Загадано число от 1 до 51, угадай его')

while True:
    user_num = int(input('Введите число от 1 до 51: '))
    attempt += 1
    if user_num == number:
        print('Ты угадал число, поздравляю тебя!')
        print('Количество попыток:' + str(attempt))
        print('Спасибо за игру!')
        break
    elif user_num > number:
        print('Заданное число меньше твоего.')
    elif user_num < number:
        print('Заданное число больше твоего.')