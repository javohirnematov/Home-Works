class User:
    def __init__(self, username, mail, age, number):
        self.username = username
        self.mail = mail
        self.age = age
        self.number = number
    def change_username(self, new_username):
        self.username = new_username
    def change_number(self, new_number):
        self.number = new_number
    def change_mail(self, new_mail):
        self.mail = new_mail
    def username_data(self):
        return self.username, self.mail, self.age, self.number

username = input('Введите свое имя: ')
mail = input(f'Введите e-mail {username}: ')
age = int(input(f'Введите возраст {username}: '))
number = input(f'Введите номер телефона {username}: ')
user1 = User(username, mail, age, number)

while True:
    choice = int(input('1-изменить имя, 2-изменить номер телефона, 3-изменить почту, 4-данные аккаунта: '))
    if choice == 1:
        change_name = input('Изменить имя, введите новое имя: ')
        user1.change_username(change_name)
    elif choice == 2:
        change_phone = input('Изменить номер телефона, введите новый номер телефона: ')
        user1.change_number(change_phone)
    elif choice == 3:
        change_new_mail = input('Изменить почту, введите новую почту: ')
        user1.change_mail(change_new_mail)
    elif choice == 4:
        print(user1.username_data())
    else:
        print('Не понял ваше действие')