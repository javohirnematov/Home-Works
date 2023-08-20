import sqlite3
connection = sqlite3.connect('java_bank.db')
sql = connection.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS bank_clients'
            '(client_name TEXT, client_number TEXT, client_balance REAL);')
while True:
    choice_an_action = int(input('Что нужно сделать: '
                                 '1 - зарегистрировать нового клиента в базу данных банка, '
                                 '2 - найти клиента в базе данных банка: '))
    if choice_an_action == 1:
        client_name = input('Введите пожалуйста ФИО: ')
        client_number = input('Введите пожалуйста номер телефона: ')
        client_balance = float(input('Введите пожалуйста начальный баланс: '))
        sql.execute(f'INSERT INTO bank_clients (client_name, client_number, client_balance)'
                    f'VALUES("{client_name}", "{client_number}", "{client_balance}");')
        sql.connection.commit()
    elif choice_an_action == 2:
        search_client = int(input('Выберите по каким данным найти клиента: '
                                  '1 - Найти клиента по ФИО, '
                                  '2 - Найти клиента по номеру телефона: '))
        if search_client == 1:
            search_for_name = input('Введите ФИО: ')
            searching_client = sql.execute(f'SELECT * FROM bank_clients WHERE client_name="{search_for_name}";').fetchall()
            client_name = searching_client[0][0]
            client_number = searching_client[0][1]
            client_balance = searching_client[0][2]
        elif search_client == 2:
            search_for_number = input('Введите номер телефона: ')
            searching_client = sql.execute(f'SELECT * FROM bank_clients WHERE client_name="{search_for_number}";').fetchall()
            client_name = searching_client[0][0]
            client_number = searching_client[0][1]
            client_balance = searching_client[0][2]
        else:
            print('Запрос неверный')
            break
        work_with_balance = int(input('Действия с балансом клиента: '
                                      '1 - пополнить баланс, '
                                      '2 - снять деньги с баланса, '
                                      '3 - просмотр баланса, '
                                      '4 - банковские вклады, '
                                      '5 - личный кабинет клиента: '))
        if work_with_balance == 1:
            replenishment_amount = float(input('Введите сумму для пополнения баланса: '))
            client_balance = client_balance + replenishment_amount
            sql.execute(f'UPDATE bank_clients SET client_balance = {client_balance} WHERE client_name = "{client_name}";')
            connection.commit()
        elif work_with_balance == 2:
            decrease_the_balance = float(input('Введите сумму для снятия с баланса: '))
            client_balance = client_balance - decrease_the_balance
            sql.execute(f'UPDATE bank_clients SET client_balance = {client_balance} WHERE client_name = "{client_name}";')
            connection.commit()
        elif work_with_balance == 3:
            print(client_balance)
        elif work_with_balance == 4:
            contributions = int(input('JAVA BANK предоставляет вклады под 7% годовых, на период 12, 24 и 36 месяцев.'
                                      'Выберите количество месяцев: '))
            if contributions == 12\
                    or contributions == 24\
                    or contributions == 36:
                print(f'Cумма дохода по {contributions}-ти месячному вкладу под 7% составит ',
                      (0.07*client_balance*contributions/12))
            else:
                print('Запрос неверный')
        elif work_with_balance == 5:
            print(client_name, client_number, client_balance)
        else:
            print('Запрос неверный')
    else:
        print('Запрос неверный')