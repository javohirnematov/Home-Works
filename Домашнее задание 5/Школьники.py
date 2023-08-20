ucheniki = {}
def add_uchenik(imya, klass):
    ucheniki[imya] = klass
    print(f'{imya} зарегистрирован(а) в базе школы и добавлен(а) в {klass}!')
    print(ucheniki)
def del_uchenik(imya):
    ucheniki.pop(imya)
    print(f'{imya} исключен(а) из школы!')
    print(ucheniki)

def izmenit_danniye_uchenika(imya, klass):
    ucheniki[imya] = klass
    print(f'{imya} переведен(а) в {klass}!')
    print(ucheniki)

while True:
    admin = int(input('1 - Регистрация ученика(цы), 2 - Удалить данные ученика(цы), 3 - Изменить данные ученика(цы): '))
    if admin == 1:
        imya = input('Добро пожаловать в школу! Введите имя ученика(цы): ')
        if imya in ucheniki.keys():
            print(f'{imya} уже есть в списке!')
        else:
            vibraniy_klass = int(input('Введите класс, в который нужно зарегистрировать ученика(цу): '))
            klass = f'{vibraniy_klass} класс'
            add_uchenik(imya, klass)

    elif admin == 2:
        imya = input('Введите имя ученика(цы) для исключения из школы: ')
        if imya in ucheniki.keys():
            del_uchenik(imya)
        else:
            print(f'Данные ученика(цы) {imya} не найдено в базе!')

    elif admin == 3:
        imya = input('Введите имя ученика(цы) для перевода в другой класс: ')
        if imya in ucheniki.keys():
            vibraniy_klass = int(input(f'В какой класс перевести ученика(цу) {imya}? '))
            izmenit_klass = f'{vibraniy_klass} класс'
            izmenit_danniye_uchenika(imya, izmenit_klass)
        else:
            print(f'Данные ученика(цы) {imya} не найдены в базе!')
    else:
        print('Не верно выбрано действие. Повторите пожалуйста снова!')