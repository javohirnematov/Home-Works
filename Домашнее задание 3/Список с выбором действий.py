clients = ['Мирон', 'Антон', 'Анастаcия', 'Кирилл', 'Олег', 'Никита', 'Света']
print(clients)
while True:
    turn_with_clients = input('Выберите действие со списком клиентов: добавить, заменить, удалить: ')
    if turn_with_clients == 'добавить':
        add_new_client = input('Введите имя нового контакта: ')
        if add_new_client in clients:
            print('Данное имя есть в списке контактов')
            break
        else:
            clients.append(add_new_client)
            print(clients)

    elif turn_with_clients == 'заменить':
        replace_client = input('Введите имя контакта для замены: ')
        replace_with_client = input('Введите имя контакта кем заменить: ')
        if replace_client in clients:
            clients_index = clients.index(replace_client)
            clients[clients_index] = (replace_with_client)
            print(clients)
        else:
            print('Данного имени нет в списке')
            break

    elif turn_with_clients == 'удалить':
        delete_client = input('Введите имя клиента для удаления из списка: ')
        if delete_client in clients:
            clients.remove(delete_client)
            print(clients)
        else:
            print('Данного имени нет в списке')
            break

    else:
        print('Выберите правильное действие со списком клие: добавить контакт, заменить контакт, удалить контакт: ')