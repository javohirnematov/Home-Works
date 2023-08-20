class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def display_info(self):
        return (self.brand, self.year)
class Car(Vehicle):
    def __init__(self, brand, year, body):              # кузов
        super().__init__(brand, year)
        self.body = body
    def display_info(self):
        return (self.brand, self.year, self.body)
class Motorcycle(Vehicle):
    def __init__(self, brand, year, max_speed):        # максимальная скорость
        super().__init__(brand, year)
        self.max_speed = max_speed
    def display_info(self):
        return (self.brand, self.year, self.max_speed)

BMWX7 = Car('BMW X7', 2018, 'универсал')
SUZUKI_GSX1300R_HAYABUSA = Motorcycle('Suzuki Hayabusa', 1999, '303 км/ч')

print(BMWX7.display_info())
print(SUZUKI_GSX1300R_HAYABUSA.display_info())
