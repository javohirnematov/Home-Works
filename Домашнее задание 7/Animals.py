class Animals:
    def __init__(self, make_sound):
        self.make_sound = make_sound
class Dog(Animals):
    def __init__(self, make_sound, security):
        super().__init__(make_sound)
        self.security = security
class Cat(Animals):
    def __init__(self, make_sound, mousers):                      # мышеловы
        super().__init__(make_sound)
        self.mousers = mousers
class Cow(Animals):
    def __init__(self, make_sound, give_milk):
        super().__init__(make_sound)
        self.give_milk = give_milk


german_shepherd = Dog('лает ГАВ-ГАВ', 'охраняет дом')
print(f'Немецкая овчарка', german_shepherd.make_sound,'и', german_shepherd.security)

scottish_fold = Cat('мяучет МЯУ-МЯУ', 'ловит мышей')
print(f'Шотландская вислоухая кошка', scottish_fold.make_sound,'и', scottish_fold.mousers)

cow = Cow('мычит МУ-МУ', 'даёт молоко')
print(f'Домашняя корова', cow.make_sound,'и', cow.give_milk)