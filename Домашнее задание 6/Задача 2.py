class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return (self.a + self.b)
    def multiplication(self):
        return (self.a * self.b)
    def division(self):
        return (self.a / self.b)
    def subtraction(self):
        return (self.a - self.b)

numbers = Math(10, 45)

while True:
    admin = int(input('Седалайте выбор действия: 1-сложение, 2-умножение, 3-деление, 4-вычитание: '))
    if admin == 1:
        print(numbers.addition())
    elif admin == 2:
        print(numbers.multiplication())
    elif admin == 3:
        print(numbers.division())
    elif admin == 4:
        print(numbers.subtraction())
    else:
        print('Непонятное действие')



