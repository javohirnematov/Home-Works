class Student:
    def __init__(self, name='Иван', age=18, group_number='10A'):
        self.name = name
        self.age = age
        self.group_number = group_number
    def get_name(self):
        return f'Имя студента: {self.name}'
    def get_age(self):
        return f'Bозраст студента: {self.age}'
    def get_group_number(self):
        return f'Группа студента: {self.group_number}'
    def set_name_age(self):
        name = input('Введите новое имя по умолчанию:')
        age = input('Введите новый возраст по умолчанию: ')
        self.name = name
        self.age = age
        return f'Новое имя по умолчанию: {self.name}, новый возраст по умолчанию: {self.age}'
    def set_group_number(self):
        group_number = input('Введите новую группу по умолчанию: ')
        self.group_number = group_number
        return f'Группа студента: {self.group_number}.'

Ivan = Student()
Lena = Student('Елена')
Java = Student('Жавохир', 32)
Ksyusha = Student('Ксения', 20, '85g')
Alex = Student('Александра', 16, "17AA")

print(Alex.get_name())
print(Lena.get_age())
print(Java.get_group_number())
print(Ksyusha.set_group_number())
print(Ivan.set_name_age())

print(Ivan.name, Ivan.age, Ivan.group_number)
print(Lena.name, Lena.age, Lena.group_number)
print(Java.name, Java.age, Java.group_number)
print(Ksyusha.name, Ksyusha.age, Ksyusha.group_number)
print(Alex.name, Alex.age, Alex.group_number)
