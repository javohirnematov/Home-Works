class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def start(self):
        return ('Автомобиль заведен')
    def stop(self):
        return ('Автомобиль заглушен')
    def set_year(self, year):
        self.year = year
    def set_type(self, type):
        self.type = type
    def set_color(self, color):
        self.color = color

lamborghini = Car(color='yellow', type='sportcar', year=2023)

while True:
    admin = int(input('Выберите действие с автомобилем:'
                  '1-запуск автомобиля, 2-отключение автомобиля,'
                  '3-присвоение автомобилю года выпуска,'
                  '4-присвоение автомобилю типа,'
                  '5-присвоение автомобилю цвета: ' ))
    if admin == 1:
        print(lamborghini.start())
    elif admin == 2:
        print(lamborghini.stop())
    elif admin == 3:
        Car.set_color = lamborghini.color
        print(Car.set_color)
    elif admin == 4:
        Car.set_type = lamborghini.type
        print(Car.set_type)
    elif admin == 5:
        Car.set_year = lamborghini.year
        print(Car.set_year)
    else:
        print('Неправильно выбрано дейсвтие!')